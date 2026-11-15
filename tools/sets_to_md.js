// Xuat SETS trong index.html ra noi-dung.md de nguoi dung sua tay.
const fs = require("fs");
const [, , htmlPath, outPath] = process.argv;
const h = fs.readFileSync(htmlPath, "utf8");
const a = h.indexOf("const SETS = ["), b = h.indexOf("\n];", a) + 3;
const SETS = eval(h.slice(a + 12, b));

const row = arr => "- " + arr.map(x => (x ?? "").trim()).join(" | ");
const out = [];
out.push(`# Nội dung IT-Shadowing

Sửa trực tiếp trong file này rồi gửi lại cho Claude để cập nhật trang luyện, âm thanh và mau-cau.html.

**Cách viết**

- Mỗi \`# ...\` là một mục (tab). Dòng \`id:\` giữ nguyên, mục mới thì đặt id mới (p9, p10…).
- Các trường trên một dòng ngăn bằng \` | \`. Chỉ cần sửa chữ, giữ nguyên dấu \`|\`.
- **Romaji** để trống cũng được, Claude sẽ tự điền.
- Trong **Kịch bản**: \`### Tên tình huống\` là dòng ngăn nhóm (không đọc thành tiếng).
  Mỗi câu: \`- [vai] câu tiếng Nhật | romaji | nghĩa Việt | câu cô hỏi\`. Vai 上司 / 先生 / 新人 là câu của người kia.
  Cột cuối **câu cô hỏi** (không bắt buộc) là câu cô hoặc cấp trên nói ngay trước câu này, dùng cho chế độ "Cô hỏi".
  Nếu câu ngay trước đã là câu của người kia thì không cần viết.
- Số và từ viết tắt nên viết cách đọc bằng chữ để máy đọc đúng: \`十五分\`, \`デブワン\`, \`エヌジー\`.
- Muốn ghi chú cho Claude thì viết dòng bắt đầu bằng \`> \` ở bất cứ đâu, ví dụ \`> câu này nói tự nhiên hơn giúp tôi\`.
`);

for (const s of SETS) {
  out.push(`\n---\n\n# ${s.tab} | ${s.title}\n\nid: ${s.id}\n`);
  out.push(`## Giới thiệu\n\n${s.lead}\n`);
  out.push(`## Dùng khi\n\n${s.when}\n`);
  out.push(`## Khung câu\n\n<!-- tên bước | romaji | nghĩa Việt | giải thích -->\n` + s.terms.map(row).join("\n") + "\n");
  out.push(`## Mẫu câu\n\n<!-- mẫu câu | romaji | nghĩa Việt -->\n` + (s.patterns || []).map(row).join("\n") + "\n");
  out.push(`## Danh từ\n\n<!-- từ | romaji | nghĩa Việt -->\n` + (s.nouns || []).map(row).join("\n") + "\n");
  out.push(`## Động từ\n\n<!-- từ | romaji | nghĩa Việt -->\n` + (s.verbs || []).map(row).join("\n") + "\n");
  const lines = [];
  for (const l of s.lines) {
    if (l.g) lines.push(`\n### ${l.g}\n`);
    else lines.push(`- [${l.r}] ${l.ja} | ${l.ro} | ${l.vi}` + (l.q ? ` | ${l.q}` : ""));
  }
  out.push(`## Kịch bản\n` + lines.join("\n") + "\n");
}
fs.writeFileSync(outPath, out.join("\n").replace(/\n{3,}/g, "\n\n"));
console.log(outPath, SETS.length, "mục");
