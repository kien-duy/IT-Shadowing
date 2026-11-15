#!/usr/bin/env python3
"""Tao file nghe cho dien thoai: moi muc mot file m4a, them mot file gop tat ca.

Moi cau cua minh:  nghia tieng Viet (giong Linh cua macOS) -> lang de tu noi
                   -> cau tieng Nhat (giong mac dinh) -> lang de nhai theo.
Cau cua co / cap tren (上司, 先生, 新人): chi doc tieng Nhat bang giong thu hai.

Can chay tools/gen_audio.py truoc (lay file tieng Nhat tu audio/manifest.js).
    python3 tools/gen_listen.py
Ket qua: audio/nghe/<id>.m4a, audio/nghe/tat-ca.m4a, audio/nghe/list.js
"""
import json, os, re, subprocess, sys, tempfile, wave

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO = os.path.join(ROOT, "audio")
OUT = os.path.join(AUDIO, "nghe")
RATE = 24000
OTHER = {"上司", "先生", "新人"}
VI_VOICE = "Linh"


def load_sets():
    html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    a = html.index("const SETS = [")
    b = html.index("\n];", a) + 3
    js = html[a + 12:b]
    out = subprocess.run(["node", "-e", "process.stdout.write(JSON.stringify(eval(require('fs').readFileSync(0,'utf8'))))"],
                         input=js, capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def load_manifest():
    txt = open(os.path.join(AUDIO, "manifest.js"), encoding="utf-8").read()
    return json.loads(txt[txt.index("=") + 1:].rstrip().rstrip(";"))["voices"]


def pcm(path):
    with wave.open(path) as w:
        assert w.getframerate() == RATE and w.getnchannels() == 1 and w.getsampwidth() == 2, path
        return w.readframes(w.getnframes())


def decode(m4a, tmp):
    out = os.path.join(tmp, os.path.basename(m4a) + ".wav")
    if not os.path.exists(out):
        subprocess.run(["afconvert", "-f", "WAVE", "-d", f"LEI16@{RATE}", "-c", "1", m4a, out], check=True)
    return pcm(out)


def say_vi(text, tmp, cache={}):
    if text not in cache:
        out = os.path.join(tmp, f"vi{len(cache)}.wav")
        subprocess.run(["say", "-v", VI_VOICE, "-r", "185", "-o", out, f"--data-format=LEI16@{RATE}", text], check=True)
        cache[text] = pcm(out)
    return cache[text]


def silence(sec):
    return b"\x00\x00" * int(RATE * sec)


def secs(data):
    return len(data) / 2 / RATE


def build_set(s, main, other, tmp):
    parts = [say_vi(s["title"].replace("·", ","), tmp), silence(1.2)]
    for l in s["lines"]:
        if "g" in l:
            parts += [say_vi(l["g"], tmp), silence(0.8)]
            continue
        if l["r"] in OTHER:
            parts += [decode(os.path.join(AUDIO, other[l["ja"]]), tmp), silence(1.0)]
            continue
        ja = decode(os.path.join(AUDIO, main[l["ja"]]), tmp)
        d = secs(ja)
        parts += [say_vi(l["vi"], tmp), silence(max(3.0, d * 1.1)), ja, silence(max(2.0, d)), ]
    return b"".join(parts)


def write_m4a(data, path, tmp):
    wav = os.path.join(tmp, "out.wav")
    with wave.open(wav, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(data)
    subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "48000", wav, path], check=True)


def main():
    sets = load_sets()
    voices = load_manifest()
    main_v, other_v = voices[0]["files"], voices[-1]["files"]
    os.makedirs(OUT, exist_ok=True)
    listing, everything = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for s in sets:
            data = build_set(s, main_v, other_v, tmp)
            everything += [data, silence(2.0)]
            write_m4a(data, os.path.join(OUT, s["id"] + ".m4a"), tmp)
            listing.append({"file": s["id"] + ".m4a", "label": s["tab"], "min": round(secs(data) / 60, 1)})
            print(f"{s['id']}  {secs(data):.0f}s", file=sys.stderr)
        data = b"".join(everything)
        write_m4a(data, os.path.join(OUT, "tat-ca.m4a"), tmp)
        listing.insert(0, {"file": "tat-ca.m4a", "label": "Tất cả mục", "min": round(secs(data) / 60, 1), "all": True})
    keep = {f["file"] for f in listing} | {"list.js"}
    for f in os.listdir(OUT):
        if f not in keep:
            os.unlink(os.path.join(OUT, f))
    with open(os.path.join(OUT, "list.js"), "w", encoding="utf-8") as f:
        f.write("window.LISTEN_FILES=" + json.dumps(listing, ensure_ascii=False) + ";\n")
    print(f"Xong: {len(listing)} file, tổng {listing[0]['min']} phút.", file=sys.stderr)


if __name__ == "__main__":
    main()
