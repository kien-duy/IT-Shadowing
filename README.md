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

## Học thuộc kịch bản

Thanh chế độ phía trên có ba nút:

- **Nghe & nhại**: chế độ shadowing ở trên.
- **Nhớ lại**: trang chỉ hiện nghĩa tiếng Việt và nhãn vai. Bạn nói câu tiếng Nhật, rồi bấm
  **Xem đáp án** để xem câu và nghe máy đọc, sau đó tự chấm **Nhớ** hoặc **Quên**. Câu bị Quên
  quay lại sau 2–3 thẻ, cho đến khi nhớ. Bấm **Gợi ý** để hiện hai chữ đầu của mỗi cụm; câu đã
  dùng gợi ý được tính là Quên.
- **Cô hỏi**: máy đọc câu cô hoặc cấp trên hỏi (bằng giọng còn lại), bạn có 4/6/9 giây để trả
  lời, rồi trang tự hiện đáp án để chấm. Gợi ý lần một hiện câu hỏi và nghĩa, lần hai hiện chữ đầu.

Ô **Phạm vi**: mục đang chọn, tất cả mục, hoặc chỉ câu chưa thuộc. Kết quả Nhớ / Quên được lưu
trong trình duyệt nên buổi sau chọn "Chỉ câu chưa thuộc" để ôn tiếp.
Phím tắt: `Space` xem đáp án · `H` gợi ý · `1` nhớ · `2` quên · `R` nghe lại.

**Nghe trên điện thoại**: cuối trang có các file `audio/nghe/*.m4a`, mỗi tab một file và một
file gộp tất cả. Mỗi câu là nghĩa tiếng Việt → khoảng lặng để tự nói → câu tiếng Nhật →
khoảng lặng để nhại theo.

## Nội dung

Xếp theo đề thi nói cuối kỳ: nói chuyện liền mạch với thầy 10–15 phút. Mọi câu nằm trong phạm vi
ngữ pháp N3, từ vựng IT và văn phòng; bối cảnh là dự án hệ thống đặt lịch khám. Trang có hai tab:

| Tab | Nội dung |
| --- | --- |
| ① 自己紹介 | Tự giới thiệu, mỗi ý một câu: tên, lý do và sở thích, công việc, quy trình, điều quan trọng, khó khăn, mục tiêu |
| ② シナリオ | Hội thoại hỏi đáp với thầy, theo thứ tự luyện bên dưới |

Các tình huống trong tab ② シナリオ:

1. **納期の相談**: báo senpai là sắp trễ hạn release vì lỗi bảo mật, xin lùi sang đợt sau.
2. **トラブル対応**: báo sự cố gấp cho senpai: hệ thống dừng, AI trả lời sai, lỡ xóa dữ liệu, bị hỏi điều chưa biết.
3. **仕様の確認**: spec chưa rõ, hỏi lại và đề xuất cách làm.
4. **意見**: nêu ý kiến về họp và liên lạc quá nhiều, trả lời câu hỏi vặn.
5. **新人のサポート**: (a) thầy hỏi có người mới thì làm gì, (b) thầy đóng vai người mới.

Thầy đóng vai senpai (ミンさん) nên câu của mình ở mức です・ます; chỉ câu xin lỗi dùng
申し訳ございません. Dòng `上司` / `先生` / `新人` là câu thầy nói, kèm câu đáp của mình ngay sau.
Câu đầu mỗi tình huống có câu thầy giao đề (trường `q`) để luyện ở chế độ Cô hỏi.

Mỗi tab có **bộ học thuộc**: mẫu câu có chỗ trống `〜` để tự điền, danh từ và động từ hay dùng
(mảng `patterns`, `nouns`, `verbs` trong `SETS`). `mau-cau.html` là bản in của toàn bộ nội dung,
kèm bảng tổng hợp từ vựng.

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

Script tạo âm thanh cho cả câu kịch bản (`ja`) và câu cô hỏi (`q`). Nó chỉ tạo lại câu mới hoặc câu đã sửa, xóa file thừa và ghi lại `audio/manifest.js`.
Muốn thêm hoặc bớt giọng thì sửa danh sách `VOICES` đầu script
(id của từng giọng: `curl localhost:50021/speakers`). Câu nào chưa có file âm thanh thì trang bỏ qua.

Sau đó tạo lại file nghe cho điện thoại (dùng giọng tiếng Việt Linh có sẵn trên macOS và `afconvert`):

```
python3 tools/gen_listen.py
```

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

Cách dễ nhất là sửa `noi-dung.md` (toàn bộ nội dung, mỗi câu một dòng
`- [vai] tiếng Nhật | romaji | nghĩa Việt | câu cô hỏi`), rồi nạp lại vào trang:

```
node tools/md_to_sets.js noi-dung.md --write index.html
```

Chiều ngược lại, xuất `SETS` ra md: `node tools/sets_to_md.js index.html noi-dung.md`.

Nội dung nằm trong mảng `SETS` ở cuối `index.html`:

```js
{r:"結論", ja:"...", ro:"...", vi:"...", q:"..."}   // một câu; q là câu cô hỏi, không bắt buộc
{g:"Tên tình huống"}                                 // dòng ngăn nhóm, không đọc
```

Nếu câu ngay trước là câu của `上司` / `先生` / `新人` thì chế độ Cô hỏi dùng luôn câu đó, không cần `q`.

Với số và từ viết tắt, viết cách đọc bằng katakana (`シーアイ・シーディー`, `五百エラー`)
để máy đọc đúng, rồi ghi romaji theo đúng cách đọc đó.
