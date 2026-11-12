# IT-shadowing

Trang luyện shadowing tiếng Nhật IT theo đề thi nói cuối kỳ, bối cảnh dự án hệ thống đặt lịch khám
bệnh viện (診察予約システム). Một file HTML tĩnh, chạy offline, không cần cài gì.

**Bản deploy:** https://kien-duy.github.io/IT-Shadowing/

## Cách luyện

1. Bấm một câu bất kỳ để nghe riêng câu đó.
2. Bấm **Chạy shadowing**: máy đọc từng câu, rồi chừa một khoảng lặng đúng bằng độ dài câu —
   bạn nói đè lên khoảng lặng đó.
3. Vòng 1 nghe không nói, vòng 2 nói nhỏ theo cùng lúc, vòng 3 tắt romaji và nghĩa tiếng Việt
   rồi nói lại từ trí nhớ.

Mỗi câu có ba dòng: tiếng Nhật, **romaji**, nghĩa tiếng Việt. Hai nút `Romaji` và `Nghĩa Việt`
bật/tắt độc lập; lựa chọn được nhớ trong trình duyệt.

Phím tắt: `Space` chạy/dừng · `R` nghe lại câu hiện tại · `B` bật tắt romaji · `V` bật tắt nghĩa.

## Nội dung

Xếp theo đề thi nói cuối kỳ: nói chuyện liền mạch với thầy 10–15 phút. Mọi câu nằm trong phạm vi
ngữ pháp N3, từ vựng IT và văn phòng; bối cảnh là dự án hệ thống đặt lịch khám.

| Mục | Phần thi | Khung câu |
| --- | --- | --- |
| ① 自己紹介 | Tự giới thiệu (8 ý theo đề cương) | 名前・理由 → 担当 → 仕事の流れ → 大切なこと → 困ること・注意すること → 目標 → チーム・個人 → 一番難しいこと |
| ② 納期の相談 | Roleplay テーマ1: việc gấp chen vào / dev1 NG trước ngày release | 問題 → 原因 → 影響 → 対応 → 提案 → 連絡 |
| ③ 仕様の確認 | Roleplay テーマ2: spec AI assistant có chỗ chưa rõ | 問題 → 原因 → 影響 → 対応 → 提案 |
| ④ 事故報告 | Roleplay テーマ3: gửi dữ liệu sai | 謝罪 → 状況説明 → 原因 → 対応 → 今後の対策 → 連絡 |
| ⑤ 意見 | Part 3 テーマA: họp và liên lạc quá nhiều | 意見 → 理由 → 具体例 → 改善案 → まとめ |
| ⑥ 新人のサポート | Làm mentor cho người mới: trả lời câu hỏi của cô + roleplay | 意見 → 理由 → 具体例 → 注意 → まとめ |
| ⑦ 用語の説明 | Giải thích thuật ngữ IT cho người không làm IT | 〇〇というのは、〜のことです + so sánh đời thường |
| ⑧ つなぎ・困った時 | Câu nối và gỡ bí khi đang thi | 聞き返し・確認・時間・つなぎ・保留 |

Câu mẫu ngắn, mỗi câu một ý. Mỗi mục có thêm **bộ học thuộc**: mẫu câu có chỗ trống `〜` để tự điền,
danh từ và động từ hay dùng (mảng `patterns`, `nouns`, `verbs` trong `SETS`), để lúc thi tự ghép câu.
`mau-cau.html` là bản in của toàn bộ nội dung, kèm bảng tổng hợp từ vựng.

Các mục roleplay có dòng `上司` / `先生` / `新人` là câu người kia có thể nói, kèm câu đáp của mình.
Nội dung dùng ngữ cảnh thật: Fullstack Developer, dự án quản lý lịch khám, chức năng AI assistant dùng
Amazon Bedrock, cấp trên ミンさん, đồng nghiệp 桑原さん・井原さん.

Mỗi mục có một thẻ giải nghĩa ngay dưới thanh tab: từ tiếng Nhật đặt tên cho mục nghĩa là gì,
từng thành phần trong khung câu đảm nhiệm việc gì, và ngữ cảnh nào thì mang khung đó ra dùng.

## Giọng đọc

Trang chỉ dùng hai giọng VOICEVOX, có sẵn dưới dạng file âm thanh trong `audio/`, nên máy nào
mở trang cũng nghe giống nhau, không phụ thuộc giọng cài trong máy:

- **冥鳴ひまり（ノーマル）**: giọng mặc định
- **ずんだもん（あまあま）**

Đổi giọng ở ô `Giọng`; lựa chọn được nhớ trong trình duyệt.

Sau khi sửa hoặc thêm câu, mở app [VOICEVOX](https://voicevox.hiroshiba.jp/) rồi chạy:

```
python3 tools/gen_audio.py
```

Script chỉ tạo lại câu mới hoặc câu đã sửa, xóa file thừa và ghi lại `audio/manifest.js`.
Muốn thêm hoặc bớt giọng thì sửa danh sách `VOICES` đầu script
(id của từng giọng: `curl localhost:50021/speakers`). Câu nào chưa có file âm thanh thì trang bỏ qua.

## Chạy tại máy

Mở thẳng `index.html` bằng trình duyệt, hoặc:

```
python3 -m http.server 8000
```

## Deploy

GitHub Pages lấy thẳng từ nhánh: Settings → Pages → Source **Deploy from a branch**, chọn `main`
và thư mục `/ (root)`. Mỗi lần push vào `main` là GitHub tự build lại, không cần Actions.
File `.nojekyll` để Jekyll khỏi đụng vào nội dung.

## Thêm hoặc sửa câu

Toàn bộ nội dung nằm trong mảng `SETS` ở cuối `index.html`:

```js
{r:"結論", ja:"...", ro:"...", vi:"..."}   // một câu
{g:"Tên tình huống"}                        // dòng ngăn nhóm, không đọc
```

Với số và từ viết tắt, viết cách đọc bằng katakana (`シーアイ・シーディー`, `五百エラー`)
để máy đọc đúng, rồi ghi romaji theo đúng cách đọc đó.
