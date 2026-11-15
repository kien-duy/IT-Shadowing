# Nội dung IT-Shadowing

Sửa trực tiếp trong file này rồi gửi lại cho Claude để cập nhật trang luyện, âm thanh và mau-cau.html.

**Cách viết**

- Mỗi `# ...` là một mục (tab). Dòng `id:` giữ nguyên, mục mới thì đặt id mới (p9, p10…).
- Các trường trên một dòng ngăn bằng ` | `. Chỉ cần sửa chữ, giữ nguyên dấu `|`.
- **Romaji** để trống cũng được, Claude sẽ tự điền.
- Trong **Kịch bản**: `### Tên tình huống` là dòng ngăn nhóm (không đọc thành tiếng).
  Mỗi câu: `- [vai] câu tiếng Nhật | romaji | nghĩa Việt | câu cô hỏi`. Vai 上司 / 先生 / 新人 là câu của người kia.
  Cột cuối **câu cô hỏi** (không bắt buộc) là câu cô hoặc cấp trên nói ngay trước câu này, dùng cho chế độ "Cô hỏi".
  Nếu câu ngay trước đã là câu của người kia thì không cần viết.
- Số và từ viết tắt nên viết cách đọc bằng chữ để máy đọc đúng: `十五分`, `デブワン`, `エヌジー`.
- Muốn ghi chú cho Claude thì viết dòng bắt đầu bằng `> ` ở bất cứ đâu, ví dụ `> câu này nói tự nhiên hơn giúp tôi`.

---

# ① 自己紹介 | Phần 1 · Tự giới thiệu

id: p1

## Giới thiệu

Nói liền 8 ý theo đề cương, mỗi ý một câu ngắn. Cô hỏi sâu ý nào thì lấy mẫu câu và từ vựng bên dưới để nói thêm.

## Dùng khi

Đầu bài thi, khi cô nói 自己紹介をお願いします.

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 名前・理由 | namae・riyū | tên, lý do | Tên, quê, vì sao chọn IT Nhật.
- 担当 | tantō | công việc | Vị trí và dự án đang làm.
- 仕事の流れ | shigoto no nagare | quy trình | まず → 次に → それから → 最後に.
- 大切なこと | taisetsu na koto | điều quan trọng | Một điều + lý do.
- 困ること | komaru koto | khó khăn, lưu ý | Khó gì + mình làm gì.
- 目標 | mokuhyō | mục tiêu | Một câu.
- チーム | chīmu | nhóm hay cá nhân | Số người + cách chia việc.
- 一番難しいこと | ichiban muzukashii koto | điều khó nhất | Khó gì + đang cố thế nào. Kết bằng 以上です.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- 〇〇と申します。〇〇出身です。 | ... to mōshimasu. ... shusshin desu. | Tôi tên là… Tôi quê ở…
- 〜が好きで、〜を選びました。 | ... ga suki de, ... o erabimashita. | Vì thích… nên tôi đã chọn…
- 趣味は〜ことです。 | Shumi wa ... koto desu. | Sở thích của tôi là…
- 今は〜を担当しています。 | Ima wa ... o tantō shite imasu. | Hiện tôi phụ trách…
- まず〜。次に〜。それから〜。最後に〜。 | Mazu… Tsugi ni… Sorekara… Saigo ni… | Đầu tiên… Tiếp theo… Sau đó… Cuối cùng…
- 一番大切なのは〜ことです。〜からです。 | Ichiban taisetsu na no wa ... koto desu. ... kara desu. | Quan trọng nhất là… Vì…
- 困ることは〜です。 | Komaru koto wa ... desu. | Điều tôi gặp khó là…
- 分からないことはメモして、あとで〜に聞きます。 | Wakaranai koto wa memo shite, ato de ... ni kikimasu. | Điều không hiểu tôi ghi lại rồi hỏi … sau.
- 〜ようにしています。 | ... yō ni shite imasu. | Tôi luôn cố gắng…
- 目標は〜ことです。 | Mokuhyō wa ... koto desu. | Mục tiêu là…
- 以上です。 | Ijō desu. | Tôi xin hết.

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- 出身 | shusshin | quê
- 担当 | tantō | phụ trách
- 予約システム | yoyaku shisutemu | hệ thống đặt lịch
- 機能 | kinō | chức năng
- 医師 | ishi | bác sĩ
- タスク | tasuku | task
- 仕様 | shiyō | spec
- 実装 | jissō | implement, viết code
- テスト | tesuto | test
- レビュー | rebyū | review
- 結果 | kekka | kết quả
- 日報 | nippō | báo cáo ngày
- 会議 | kaigi | cuộc họp
- 目標 | mokuhyō | mục tiêu
- 同僚 | dōryō | đồng nghiệp
- 趣味 | shumi | sở thích
- 上司 | jōshi | cấp trên
- 考え方 | kangaekata | cách suy nghĩ
- 品質管理 | hinshitsu kanri | quản lý chất lượng

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 選ぶ | erabu | chọn
- 担当する | tantō suru | phụ trách
- 作る | tsukuru | làm, tạo
- 確認する | kakunin suru | xác nhận, hỏi lại
- 実装する | jissō suru | implement
- 理解する | rikai suru | hiểu
- 質問する | shitsumon suru | hỏi
- 報告する | hōkoku suru | báo cáo
- 手伝う | tetsudau | giúp
- 練習する | renshū suru | luyện tập
- メモする | memo suru | ghi chú
- チャレンジする | charenji suru | thử thách, thử sức

## Kịch bản

### Tự giới thiệu (mỗi ý một câu)

- [名前] グエン・ズイ・キエンと申します。ハノイ出身です。 | Guen Zui Kien to mōshimasu. Hanoi shusshin desu. | Tôi là Nguyễn Duy Kiên, quê Hà Nội. | では、自己紹介をお願いします。
- [理由] パソコンが好きで、ITの仕事を選びました。趣味はバドミントンと、友達や同僚とカフェに行くことです。 | Pasokon ga suki de, aitī no shigoto o erabimashita. Shumi wa badominton to, tomodachi ya dōryō to kafe ni iku koto desu. | Vì thích máy tính nên tôi chọn nghề IT. Sở thích là cầu lông và đi cà phê với bạn bè, đồng nghiệp. | どうしてITの仕事を選びましたか。
- [担当] フルスタックエンジニアで、病院の予約システムを作っています。 | Furusutakku enjinia de, byōin no yoyaku shisutemu o tsukutte imasu. | Tôi là Fullstack Developer, đang làm hệ thống đặt lịch của bệnh viện. | 今、どんな仕事をしていますか。
- [仕事の流れ] タスクを確認して、実装、テスト、レビューの順に進めます。 | Tasuku o kakunin shite, jissō, tesuto, rebyū no jun ni susumemasu. | Tôi xác nhận task rồi làm theo thứ tự: code, test, review. | 仕事は、どんな流れで進めますか。
- [大切なこと] 一番大切なのは、タスクを正しく理解することです。 | Ichiban taisetsu na no wa, tasuku o tadashiku rikai suru koto desu. | Quan trọng nhất là hiểu đúng task. | 仕事で一番大切なことは何ですか。
- [困ること] 日本語の会議は難しいので、分からないことはメモして、あとでベトナム人の上司に聞きます。 | Nihongo no kaigi wa muzukashii node, wakaranai koto wa memo shite, ato de Betonamujin no jōshi ni kikimasu. | Họp bằng tiếng Nhật khó nên điều không hiểu tôi ghi lại, rồi hỏi cấp trên người Việt. | 仕事で困ることはありますか。
- [目標] 目標は、ビジネスの考え方を勉強して、品質管理の仕事にもチャレンジすることです。以上です。 | Mokuhyō wa, bijinesu no kangaekata o benkyō shite, hinshitsu kanri no shigoto ni mo charenji suru koto desu. Ijō desu. | Mục tiêu là học cách tư duy business và thử sức cả với công việc quản lý chất lượng. Tôi xin hết. | これからの目標は何ですか。

---

# ② 納期の相談 | Tình huống 1 · Sắp trễ hạn

id: p2

## Giới thiệu

Đề: đang làm thì có việc gấp chen vào, sắp trễ hạn. Giải thích với cấp trên, xin lùi sang đợt release sau. Khung: 問題 → 原因 → 影響 → 提案.

## Dùng khi

Roleplay với cấp trên (ミンさん).

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 問題 | mondai | vấn đề | Nói kết luận ngay.
- 原因 | gen'in | nguyên nhân | Vì sao trễ.
- 影響 | eikyō | ảnh hưởng | Trễ bao nhiêu.
- 提案 | teian | đề xuất | Gia hạn, hoặc nhờ người.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- 〇〇さん、今よろしいでしょうか。 | ... san, ima yoroshii deshō ka. | Anh/chị …, giờ có tiện không ạ?
- 〜に間に合わないかもしれません。 | ... ni maniawanai kamo shiremasen. | Có thể không kịp…
- 〜の対応が多くて、〜はまだ〜しか終わっていません。 | ... no taiō ga ōkute, ... wa mada ... shika owatte imasen. | Vì phải xử lý nhiều … nên … mới xong được …
- 〜を次のリリースに延ばしてもよろしいでしょうか。 | ... o tsugi no rirīsu ni nobashite mo yoroshii deshō ka. | Em lùi … sang đợt release sau có được không ạ?
- 〜までに〜を報告します。 | ... made ni ... o hōkoku shimasu. | Trước … em sẽ báo cáo …

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- 納期 | nōki | hạn bàn giao
- 期限 | kigen | thời hạn
- 延長 | enchō | gia hạn
- 担当 | tantō | người phụ trách
- スケジュール | sukejūru | lịch
- 急ぎのタスク | isogi no tasuku | việc gấp
- バグ修正 | bagu shūsei | sửa bug
- リリース | rirīsu | release
- 本番環境 | honban kankyō | production
- デブワン | debuwan | môi trường dev1
- セキュリティのバグ | sekyuriti no bagu | lỗi bảo mật
- 次のリリース | tsugi no rirīsu | đợt release sau
- パーセント | pāsento | phần trăm

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 間に合う | maniau | kịp
- 遅れる | okureru | trễ
- 延ばす | nobasu | lùi, kéo dài
- 相談する | sōdan suru | trao đổi, xin ý kiến
- 手伝う | tetsudau | giúp
- 分ける | wakeru | chia
- 進める | susumeru | tiến hành
- デプロイする | depuroi suru | deploy

## Kịch bản

### Lỗi bảo mật nhiều, test mới xong 70%

- [問題] ミンさん、今よろしいでしょうか。このタスクは、金曜日のリリースに間に合わないかもしれません。 | Min-san, ima yoroshii deshō ka. Kono tasuku wa, kin'yōbi no rirīsu ni maniawanai kamo shiremasen. | Anh Minh, giờ có tiện không ạ? Task này có thể không kịp release thứ Sáu. | はい、どうしましたか。
- [原因] セキュリティのバグの対応が多くて、テストはまだ七十パーセントしか終わっていません。 | Sekyuriti no bagu no taiō ga ōkute, tesuto wa mada nanajuppāsento shika owatte imasen. | Vì phải xử lý nhiều lỗi bảo mật nên test mới xong được 70%. | どうして間に合わないんですか。
- [提案] このタスクを、次のリリースに延ばしてもよろしいでしょうか。 | Kono tasuku o, tsugi no rirīsu ni nobashite mo yoroshii deshō ka. | Em lùi task này sang đợt release sau có được không ạ? | じゃあ、どうしたいですか。
- [上司] 分かりました。次のリリースにしましょう。 | Wakarimashita. Tsugi no rirīsu ni shimashō. | (Cấp trên) Được, để đợt release sau nhé.
- [自分] ありがとうございます。今日中に、新しいスケジュールを報告します。 | Arigatō gozaimasu. Kyōjū ni, atarashii sukejūru o hōkoku shimasu. | Cảm ơn anh. Trong hôm nay em sẽ báo lịch mới.

---

# ③ 仕様の確認 | Tình huống 2 · Spec chưa rõ

id: p3

## Giới thiệu

Đề: spec có chỗ không rõ. Dừng lại để hỏi, rồi đề xuất cách làm tiếp. Khung: 確認 → 問題 → 提案.

## Dùng khi

Roleplay với cấp trên. Ngoài đời: đọc task thấy chỗ mơ hồ thì hỏi trước khi code.

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 確認 | kakunin | xin hỏi | Nói đang hỏi về chức năng nào.
- 問題 | mondai | chỗ chưa rõ | Spec không ghi điều gì.
- 提案 | teian | đề xuất | Cách của mình.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- 〜について、確認したいことがあります。 | ... ni tsuite, kakunin shitai koto ga arimasu. | Em có điều muốn hỏi lại về…
- 仕様書に、〜場合が書かれていません。 | Shiyōsho ni, ... baai ga kakarete imasen. | Spec không ghi trường hợp…
- 〜のは、どうでしょうか。 | ... no wa, dō deshō ka. | … thì thế nào ạ?

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- 仕様書 | shiyōsho | tài liệu spec
- 指示書 | shijisho | tài liệu chỉ thị
- 不明な点 | fumei na ten | điểm chưa rõ
- 画面 | gamen | màn hình
- 処理 | shori | xử lý
- 個人情報 | kojin jōhō | thông tin cá nhân
- 進め方 | susumekata | cách tiến hành
- 案 | an | phương án
- 場合 | baai | trường hợp
- パスワード | pasuwādo | mật khẩu
- アカウント | akaunto | tài khoản
- ログイン | roguin | đăng nhập

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 確認する | kakunin suru | xác nhận
- 止める | tomeru | dừng
- 決まる | kimaru | được quyết định
- 決める | kimeru | quyết định
- 提案する | teian suru | đề xuất
- 表示する | hyōji suru | hiển thị
- 間違える | machigaeru | nhập sai, làm sai
- ロックする | rokku suru | khóa

## Kịch bản

### Spec không ghi khi nhập sai mật khẩu 5 lần

- [確認] ミンさん、ログイン機能について、確認したいことがあります。 | Min-san, roguin kinō ni tsuite, kakunin shitai koto ga arimasu. | Anh Minh, em có điều muốn hỏi lại về chức năng đăng nhập. | はい、どうしましたか。
- [問題] 仕様書に、パスワードを五回間違えた場合が書かれていません。 | Shiyōsho ni, pasuwādo o gokai machigaeta baai ga kakarete imasen. | Spec không ghi trường hợp nhập sai mật khẩu 5 lần. | 何が分からないんですか。
- [提案] アカウントを三十分ロックするのは、どうでしょうか。 | Akaunto o sanjuppun rokku suru no wa, dō deshō ka. | Khóa tài khoản 30 phút thì thế nào ạ? | キエンさんは、どうしたらいいと思いますか。

---

# ④ 事故報告 | Tình huống 3 · Báo lỗi do mình

id: p4

## Giới thiệu

Đề: gửi nhầm do kiểm tra không kỹ (ở đây: không đọc lại tin nhắn AI soạn). Báo ngay cho cấp trên, nói nguyên nhân và cách xử lý. Khung: 謝罪 → 原因 → 対応 → 対策.

## Dùng khi

Roleplay với cấp trên.

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 謝罪 | shazai | xin lỗi | Câu đầu tiên.
- 原因 | gen'in | nguyên nhân | Mình đã bỏ sót gì.
- 対応 | taiō | đã xử lý | Đã sửa gì.
- 対策 | taisaku | phòng ngừa | Lần sau làm khác thế nào.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- 申し訳ありません。〜に間違いがありました。 | Mōshiwake arimasen. ... ni machigai ga arimashita. | Em xin lỗi. … bị sai.
- 〜のが原因です。 | ... no ga gen'in desu. | Nguyên nhân là…
- 〜を直しました。 | ... o naoshimashita. | Em đã sửa…
- 今後は、〜ようにします。 | Kongo wa, ... yō ni shimasu. | Từ nay em sẽ…
- 〜までに〜して、〜で報告します。 | ... made ni ... shite, ... de hōkoku shimasu. | Trước … em sẽ … và báo qua…

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- 間違い | machigai | chỗ sai
- 確認不足 | kakunin busoku | kiểm tra không kỹ
- 操作ミス | sōsa misu | thao tác sai
- 原因 | gen'in | nguyên nhân
- 対策 | taisaku | biện pháp
- データ | dēta | dữ liệu
- 件数 | kensū | số bản ghi
- チェックリスト | chekku risuto | checklist
- 手順書 | tejunsho | tài liệu quy trình
- メッセージ | messēji | tin nhắn
- 文章 | bunshō | văn bản
- チャット | chatto | chat

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 間違える | machigaeru | làm sai
- 直す | naosu | sửa
- 作り直す | tsukurinaosu | làm lại
- 送り直す | okurinaosu | gửi lại
- 削除する | sakujo suru | xóa
- チェックする | chekku suru | kiểm tra
- 連絡する | renraku suru | liên lạc

## Kịch bản

### Không kiểm tra tin nhắn AI soạn trước khi gửi

- [謝罪] 申し訳ありません。AIが作ったメッセージに、間違いがありました。 | Mōshiwake arimasen. Ēai ga tsukutta messēji ni, machigai ga arimashita. | Em xin lỗi. Tin nhắn AI soạn bị sai. | どうしましたか。
- [原因] 送る前に、自分で読んで確認しなかったのが原因です。 | Okuru mae ni, jibun de yonde kakunin shinakatta no ga gen'in desu. | Nguyên nhân là em không tự đọc lại trước khi gửi. | 原因は何ですか。
- [対応] 正しいメッセージを送り直して、三時までにチャットで報告します。 | Tadashii messēji o okurinaoshite, sanji made ni chatto de hōkoku shimasu. | Em sẽ gửi lại tin đúng và báo qua chat trước 3 giờ. | これから、どう対応しますか。
- [対策] 今後は、AIの文章も、送る前に必ずチェックします。 | Kongo wa, ēai no bunshō mo, okuru mae ni kanarazu chekku shimasu. | Từ nay văn bản AI soạn em cũng sẽ kiểm tra trước khi gửi. | 今後は、どうしますか。

---

# ⑤ 意見 | Chủ đề A · Nêu ý kiến

id: p5

## Giới thiệu

Đề: họp và liên lạc nhiều quá, mất thời gian làm việc. Nên cải thiện thế nào, vì sao? Khung: 意見 → 理由 → 改善案 → まとめ.

## Dùng khi

Phần cuối bài thi. Cô hay hỏi vặn lại, có sẵn câu đáp ở cuối.

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 意見 | iken | ý kiến | Kết luận trước.
- 理由 | riyū | lý do | 〜からです.
- 改善案 | kaizen'an | cách cải thiện | 1–2 cách.
- まとめ | matome | chốt lại | そうすれば〜.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- 私は、〜べきだと思います。 | Watashi wa, ... beki da to omoimasu. | Em nghĩ nên…
- 〜からです。 | ... kara desu. | Vì…
- 例えば、〜。 | Tatoeba, ... | Ví dụ…
- 〜たらいいと思います。 | ... tara ii to omoimasu. | Em nghĩ … thì tốt.
- そうすれば、〜と思います。 | Sō sureba, ... to omoimasu. | Làm vậy thì em nghĩ…
- 確かにそうですね。ですから、〜。 | Tashika ni sō desu ne. Desukara, ... | Đúng vậy ạ. Vì thế…

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- 作業時間 | sagyō jikan | thời gian làm việc
- 効率 | kōritsu | hiệu suất
- 改善 | kaizen | cải thiện
- 集中 | shūchū | tập trung
- 朝会 | asakai | họp sáng
- ルール | rūru | quy tắc
- 連絡 | renraku | liên lạc
- 返事 | henji | trả lời

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 減らす | herasu | giảm
- 増える | fueru | tăng
- まとめる | matomeru | gom lại
- 決める | kimeru | quyết định
- 集中する | shūchū suru | tập trung
- 改善する | kaizen suru | cải thiện
- 守る | mamoru | giữ

## Kịch bản
- [先生] 会議や連絡が多くて、作業時間が足りないとき、どう改善しますか。 | Kaigi ya renraku ga ōkute, sagyō jikan ga tarinai toki, dō kaizen shimasu ka. | (Cô) Họp và liên lạc nhiều làm thiếu thời gian làm việc, em cải thiện thế nào?
- [意見] 会議を減らすべきだと思います。 | Kaigi o herasu beki da to omoimasu. | Em nghĩ nên giảm số cuộc họp.
- [理由] 作業が止まると、集中できないからです。 | Sagyō ga tomaru to, shūchū dekinai kara desu. | Vì công việc bị ngắt thì không tập trung được. | どうしてですか。
- [改善案] 朝会は十五分にして、連絡はチャットにまとめます。 | Asakai wa jūgofun ni shite, renraku wa chatto ni matomemasu. | Họp sáng 15 phút, liên lạc thì gom vào chat. | では、どう改善しますか。
- [まとめ] そうすれば、作業時間が増えると思います。 | Sō sureba, sagyō jikan ga fueru to omoimasu. | Làm vậy thì thời gian làm việc sẽ tăng. | そうすると、どうなりますか。

---

# ⑥ 新人のサポート | Chủ đề · Hỗ trợ người mới

id: p6

## Giới thiệu

Tình huống thêm: có bạn người Việt mới vào, ra trường được một năm, bạn là mentor. (a) trả lời câu cô hỏi, khả năng ra thi cao; (b) roleplay nói với người mới.

## Dùng khi

Khi cô hỏi 新しいメンバーが入ったら、何をしますか.

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 意見 | iken | sẽ làm gì | Vai trò mentor.
- 理由 | riyū | lý do | Trải nghiệm của mình.
- 具体例 | gutairei | việc cụ thể | Công cụ → tài liệu → task nhỏ → review → small talk.
- 自分 ↔ 新人 | jibun ↔ shinjin | roleplay | Nói thân thiện, thêm ね, よ.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- メンターとして、〜ように手伝います。 | Mentā to shite, ... yō ni tetsudaimasu. | Với vai trò mentor, em giúp để…
- 私も最初は〜だったからです。 | Watashi mo saisho wa ... datta kara desu. | Vì lúc đầu em cũng…
- 〜を任せます。 | ... o makasemasu. | Em giao … cho bạn ấy.
- 〜てくださいね。 | ... te kudasai ne. | Bạn hãy … nhé.
- 〜ておくといいですよ。 | ... te oku to ii desu yo. | Bạn nên … trước nhé.
- 〜のような人です。 | ... no yō na hito desu. | Là người giống như…

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- メンター | mentā | mentor
- 新人 | shinjin | người mới
- ツール | tsūru | công cụ
- 資料 | shiryō | tài liệu
- 小さいタスク | chiisai tasuku | task nhỏ
- 趣味 | shumi | sở thích
- 食べ物 | tabemono | đồ ăn
- 定例会議 | teirei kaigi | họp định kỳ
- 日報 | nippō | báo cáo ngày

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 慣れる | nareru | quen
- 教える | oshieru | dạy
- 渡す | watasu | đưa
- 任せる | makaseru | giao phó
- 準備する | junbi suru | chuẩn bị
- メモする | memo suru | ghi chú
- 緊張する | kinchō suru | hồi hộp

## Kịch bản

### (a) Trả lời câu hỏi của cô

- [先生] 新しいメンバーが入ったら、何をしますか。 | Atarashii menbā ga haittara, nani o shimasu ka. | (Cô) Khi có thành viên mới, em sẽ làm gì?
- [意見] メンターとして、早く慣れるように手伝います。 | Mentā to shite, hayaku nareru yō ni tetsudaimasu. | Với vai trò mentor, em giúp bạn ấy sớm quen việc.
- [具体例] まず、ツールの準備と資料の説明をします。 | Mazu, tsūru no junbi to shiryō no setsumei o shimasu. | Đầu tiên em chuẩn bị công cụ và giải thích tài liệu. | 具体的に、何をしますか。
- [具体例] 次に、小さいタスクを任せて、レビューします。 | Tsugi ni, chiisai tasuku o makasete, rebyū shimasu. | Tiếp theo em giao task nhỏ rồi review. | それから、何をしますか。
- [具体例] お昼には、食べ物や趣味の話もします。 | O-hiru ni wa, tabemono ya shumi no hanashi mo shimasu. | Giờ trưa em cũng nói chuyện đồ ăn, sở thích. | 仕事のほかに、何かしますか。

### (b) Nói với người mới

- [自分] 分からないことは、何でも聞いてくださいね。 | Wakaranai koto wa, nan demo kiite kudasai ne. | Có gì không hiểu cứ hỏi mình nhé. | 新人に、最初に何と言いますか。
- [自分] 会議の前に、話すことをメモしておくといいですよ。 | Kaigi no mae ni, hanasu koto o memo shite oku to ii desu yo. | Trước họp bạn nên ghi sẵn điều sẽ nói. | 会議が苦手な新人には、何と言いますか。

---

# ⑦ 用語の説明 | Giải thích thuật ngữ IT

id: p7

## Giới thiệu

Cô không làm IT, nên có thể hỏi lại 「〇〇って何ですか」. Trả lời một câu theo mẫu 〇〇は、〜ことです.

## Dùng khi

Bất cứ lúc nào cô hỏi lại một từ.

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 説明 | setsumei | giải thích | 〇〇は、〜ことです.
- たとえ | tatoe | so sánh | 〜と同じです.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- すみません、簡単に説明しますね。 | Sumimasen, kantan ni setsumei shimasu ne. | Xin lỗi, em giải thích đơn giản nhé.
- 〇〇は、〜ことです。 | ... wa, ... koto desu. | … là việc…
- 〇〇は、〜という意味です。 | ... wa, ... to iu imi desu. | … nghĩa là…
- 〜と同じです。 | ... to onaji desu. | Giống như…
- 簡単に言うと、〜。 | Kantan ni iu to, ... | Nói đơn giản thì…

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- 専門用語 | senmon yōgo | thuật ngữ chuyên môn
- 説明書 | setsumeisho | bản hướng dẫn
- 土台 | dodai | nền móng
- テスト用 | tesuto-yō | dùng để test
- プログラム | puroguramu | chương trình
- サービス | sābisu | dịch vụ

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 説明する | setsumei suru | giải thích
- 置く | oku | đặt
- 公開する | kōkai suru | công bố
- まとめる | matomeru | gộp lại
- 動く | ugoku | chạy, hoạt động
- 使う | tsukau | dùng

## Kịch bản
- [説明] すみません、簡単に説明しますね。 | Sumimasen, kantan ni setsumei shimasu ne. | Xin lỗi, em giải thích đơn giản nhé. | すみません、専門用語はよく分かりません。
- [デプロイ] デプロイは、作ったものを、テスターやお客様が使える場所に置くことです。 | Depuroi wa, tsukutta mono o, tesutā ya okyakusama ga tsukaeru basho ni oku koto desu. | Deploy là đặt thứ mình làm vào nơi tester và khách hàng dùng được. | デプロイって何ですか。
- [リリース] リリースは、新しい機能や、バグを直したものを公開することです。 | Rirīsu wa, atarashii kinō ya, bagu o naoshita mono o kōkai suru koto desu. | Release là công bố chức năng mới hoặc bản đã sửa lỗi. | リリースって何ですか。
- [本番環境] 本番環境は、お客様が使っているシステムです。 | Honban kankyō wa, okyakusama ga tsukatte iru shisutemu desu. | Production là hệ thống khách hàng đang dùng. | 本番環境って何ですか。
- [レビュー] レビューは、新しいバグが出ないように、ほかの人にチェックしてもらうことです。 | Rebyū wa, atarashii bagu ga denai yō ni, hoka no hito ni chekku shite morau koto desu. | Review là nhờ người khác kiểm tra để không sinh ra lỗi mới. | レビューって何ですか。
- [仕様書] 仕様書は、作るものの説明書です。 | Shiyōsho wa, tsukuru mono no setsumeisho desu. | Spec là bản hướng dẫn về thứ sẽ làm. | 仕様書って何ですか。
- [フルスタック] フルスタックは、全部を担当できるエンジニアです。 | Furusutakku wa, zenbu o tantō dekiru enjinia desu. | Fullstack là kỹ sư làm được mọi phần. | フルスタックって何ですか。

---

# ⑧ つなぎ・困った時 | Câu nối và gỡ bí

id: p8

## Giới thiệu

Câu ngắn để xin nhắc lại, xin thời gian, chuyển ý. Nói một câu trong số này vẫn tốt hơn im lặng.

## Dùng khi

Bất cứ lúc nào trong bài thi.

## Khung câu

<!-- tên bước | romaji | nghĩa Việt | giải thích -->
- 聞き返し | kikikaeshi | xin nhắc lại | Đừng gật đại.
- 時間 | jikan | xin vài giây | Khi chưa nghĩ ra.
- つなぎ | tsunagi | chuyển ý | Nối câu thành mạch.

## Mẫu câu

<!-- mẫu câu | romaji | nghĩa Việt -->
- もう一度お願いします。 | Mō ichido onegai shimasu. | Xin nói lại một lần nữa.
- 〜ということですか。 | ... to iu koto desu ka. | Ý cô là… phải không ạ?
- 少し考えてもいいですか。 | Sukoshi kangaete mo ii desu ka. | Cho em nghĩ một chút được không ạ?
- 簡単に言うと、〜。 | Kantan ni iu to, ... | Nói đơn giản thì…
- 結論から言うと、〜。 | Ketsuron kara iu to, ... | Nói kết luận trước thì…
- 確認して、あとで連絡します。 | Kakunin shite, ato de renraku shimasu. | Em kiểm tra rồi báo lại sau.

## Danh từ

<!-- từ | romaji | nghĩa Việt -->
- 結論 | ketsuron | kết luận
- 意味 | imi | ý nghĩa
- 質問 | shitsumon | câu hỏi

## Động từ

<!-- từ | romaji | nghĩa Việt -->
- 言う | iu | nói
- 考える | kangaeru | suy nghĩ
- 聞く | kiku | nghe, hỏi

## Kịch bản
- [聞き返し] すみません、もう一度お願いします。 | Sumimasen, mō ichido onegai shimasu. | Xin lỗi, cô nói lại giúp em ạ.
- [聞き返し] もう少し、ゆっくりお願いします。 | Mō sukoshi, yukkuri onegai shimasu. | Cô nói chậm hơn chút giúp em ạ.
- [時間] 少し考えてもいいですか。 | Sukoshi kangaete mo ii desu ka. | Cho em nghĩ một chút được không ạ? | AIについて、どう思いますか。
- [つなぎ] 簡単に言うと、テストが足りません。 | Kantan ni iu to, tesuto ga tarimasen. | Nói đơn giản là test chưa đủ. | それは、どういう意味ですか。
- [保留] 確認して、あとで連絡します。 | Kakunin shite, ato de renraku shimasu. | Em kiểm tra rồi báo lại sau. | それは、いつできますか。
