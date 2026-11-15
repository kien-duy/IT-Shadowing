#!/usr/bin/env node
// Doc noi-dung.md (dinh dang do tools/sets_to_md.js xuat ra) thanh mang SETS.
//   node tools/md_to_sets.js noi-dung.md                    -> in JSON ra stdout
//   node tools/md_to_sets.js noi-dung.md --notes            -> chi in cac dong ghi chu "> ..."
//   node tools/md_to_sets.js noi-dung.md --write index.html -> ghi SETS vao index.html
const fs = require("fs");

function parse(md) {
  const sets = [], notes = [];
  let s = null, sec = null;
  const cells = t => t.replace(/^-\s*/, "").split(/\s+\|\s+|\s+\|$|^\|\s+/).map(x => x.trim());
  for (const raw of md.split("\n")) {
    const line = raw.replace(/\s+$/, "");
    if (/^>\s?/.test(line)) { notes.push({ set: s && s.id, section: sec, text: line.replace(/^>\s?/, "") }); continue; }
    if (/^<!--.*-->$/.test(line) || line === "---") continue;
    let m;
    if ((m = line.match(/^# (.+?) \| (.+)$/))) {
      s = { id: "", tab: m[1].trim(), title: m[2].trim(), lead: "", terms: [], patterns: [], nouns: [], verbs: [], when: "", lines: [] };
      sets.push(s); sec = null; continue;
    }
    if (!s) continue;
    if ((m = line.match(/^id:\s*(\S+)/))) { s.id = m[1]; continue; }
    if ((m = line.match(/^## (.+)$/))) { sec = m[1].trim(); continue; }
    if (sec === "Kịch bản") {
      if ((m = line.match(/^### (.+)$/))) { s.lines.push({ g: m[1].trim() }); continue; }
      if ((m = line.match(/^- \[([^\]]*)\]\s*(.+)$/))) {
        const [ja, ro = "", vi = "", q = ""] = cells(m[2]);
        const l = { r: m[1].trim(), ja, ro, vi };
        if (q) l.q = q;
        s.lines.push(l);
      }
      continue;
    }
    const key = { "Khung câu": "terms", "Mẫu câu": "patterns", "Danh từ": "nouns", "Động từ": "verbs" }[sec];
    if (key && line.startsWith("- ")) { s[key].push(cells(line)); continue; }
    if ((sec === "Giới thiệu" || sec === "Dùng khi") && line.trim()) {
      const f = sec === "Giới thiệu" ? "lead" : "when";
      s[f] = s[f] ? s[f] + " " + line.trim() : line.trim();
    }
  }
  return { sets, notes };
}

// Ghi SETS vao index.html, dung dinh dang moi dong mot ban ghi nhu hien tai.
function serialize(sets) {
  const J = JSON.stringify, arr = (k, a) => `  ${k}:[\n` + a.map(r => "    " + J(r)).join(",\n") + "\n  ]";
  const one = s => ["{", `  id:${J(s.id)},`, `  tab:${J(s.tab)},`, `  title:${J(s.title)},`, `  lead:${J(s.lead)},`,
    arr("terms", s.terms) + ",", arr("patterns", s.patterns) + ",", arr("nouns", s.nouns) + ",", arr("verbs", s.verbs) + ",",
    `  when:${J(s.when)},`, arr("lines", s.lines), "}"].join("\n");
  return "const SETS = [\n" + sets.map(one).join(",\n\n") + "\n];";
}
function writeHtml(htmlPath, sets) {
  const h = fs.readFileSync(htmlPath, "utf8");
  const a = h.indexOf("const SETS = ["), b = h.indexOf("\n];", a) + 3;
  fs.writeFileSync(htmlPath, h.slice(0, a) + serialize(sets) + h.slice(b));
}

if (require.main === module) {
  const { sets, notes } = parse(fs.readFileSync(process.argv[2], "utf8"));
  const w = process.argv.indexOf("--write");
  if (w > 0) { writeHtml(process.argv[w + 1], sets); console.error(`Đã ghi ${sets.length} mục vào ${process.argv[w + 1]}`); }
  else console.log(JSON.stringify(process.argv.includes("--notes") ? notes : sets, null, 1));
}
module.exports = { parse, serialize, writeHtml };
