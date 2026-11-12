#!/usr/bin/env python3
"""Tao file am thanh VOICEVOX cho moi cau trong index.html, cho tung giong trong VOICES.

Can mo app VOICEVOX truoc (engine chay o localhost:50021).
    python3 tools/gen_audio.py      # chi tao cau moi / cau da sua

Moi cau luu thanh audio/<hash>.m4a, hash lay tu speaker id + noi dung cau, nen sua cau
thi chi cau do duoc tao lai. File khong con dung se bi xoa.
audio/manifest.js liet ke cac giong va anh xa cau -> file cho trang dung.
Them / bot giong: sua danh sach VOICES (id lay tu `curl localhost:50021/speakers`).
"""
import hashlib, json, os, re, subprocess, sys, tempfile, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO = os.path.join(ROOT, "audio")
ENGINE = "http://127.0.0.1:50021"

# Giong dau tien la giong mac dinh tren trang.
VOICES = [
    {"id": 14, "name": "冥鳴ひまり", "style": "ノーマル"},
    {"id": 1, "name": "ずんだもん", "style": "あまあま"},
]


def post(path, params, body=None):
    url = f"{ENGINE}{path}?{urllib.parse.urlencode(params)}"
    data = json.dumps(body).encode() if body is not None else b""
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def synth(text, speaker, out):
    query = json.loads(post("/audio_query", {"text": text, "speaker": speaker}))
    query["prePhonemeLength"] = 0.05
    query["postPhonemeLength"] = 0.1
    wav = post("/synthesis", {"speaker": speaker}, query)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(wav)
        tmp = f.name
    subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "64000", tmp, out], check=True)
    os.unlink(tmp)


def main():
    html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    texts = list(dict.fromkeys(json.loads(f'"{t}"') for t in
                               re.findall(r'"?\bja"?\s*:\s*"((?:[^"\\]|\\.)*)"', html)))
    os.makedirs(AUDIO, exist_ok=True)

    voices, used, made = [], set(), 0
    for v in VOICES:
        files = {}
        for i, text in enumerate(texts, 1):
            fname = hashlib.sha1(f"{v['id']}:{text}".encode()).hexdigest()[:12] + ".m4a"
            files[text] = fname
            used.add(fname)
            out = os.path.join(AUDIO, fname)
            if not os.path.exists(out):
                synth(text, v["id"], out)
                made += 1
                print(f"{v['name']} [{i}/{len(texts)}] {text}")
        voices.append({"key": str(v["id"]), "name": v["name"], "style": v["style"], "files": files})

    for f in os.listdir(AUDIO):
        if f.endswith(".m4a") and f not in used:
            os.unlink(os.path.join(AUDIO, f))

    with open(os.path.join(AUDIO, "manifest.js"), "w", encoding="utf-8") as f:
        f.write("window.VOICE_FILES=" + json.dumps({"voices": voices}, ensure_ascii=False, indent=0) + ";\n")
    print(f"Xong: {len(texts)} câu × {len(VOICES)} giọng, tạo mới {made}.", file=sys.stderr)


if __name__ == "__main__":
    main()
