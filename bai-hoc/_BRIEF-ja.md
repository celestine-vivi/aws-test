# Khuôn dịch bài tuần sang tiếng Nhật (bai-hoc/tuan-XX.ja.html)

Nguồn: `bai-hoc/tuan-XX.html` (tiếng Việt, headless: bắt đầu bằng `<title>`, có `<style>`, `<header class="hero">`, `<div class="wrap">`, `<script>`).
Đích: `bai-hoc/tuan-XX.ja.html`, cùng cấu trúc HTML y hệt, chỉ khác phần chữ.

## Giữ nguyên tuyệt đối
- Mọi thẻ HTML, thuộc tính, `id`, `class`, `href`, `data-*`, thứ tự section, số lượng section, số `<input data-ck>`, số nút `data-reveal`, số `<p class="ans">`.
- Toàn bộ khối `<style>` (copy nguyên văn) và `<link>` Google Fonts.
- Khối `<script>`: copy nguyên, giữ `KEY='saa-tuan-XX'` KHÔNG đổi (để tiến độ checklist dùng chung hai ngôn ngữ). Chỉ dịch hai chuỗi hiển thị `'Xem đáp án'` → `'答えを見る'` và `'Ẩn đáp án'` → `'答えを隠す'` (cả trong HTML nút và trong script).
- Tên dịch vụ AWS, từ khóa đề thi tiếng Anh trong `<em>` và `.kw`, tên instance type, CLI command, JSON, đường dẫn file, URL, số liệu, đơn vị. Nội dung trong `<pre><code>` giữ nguyên, chỉ dịch dòng chú thích tiếng Việt (sau `#` hoặc `//`) nếu có.
- Tên file quiz (`quiz/tuan-XX.md`), tên file trong thư mục (`AWS-SAA-checklist.md`, `so-ghi-cau-sai.md`, `PROMPT-session-tuan.md`).

## Dịch
- `<title>`: dạng `SAA 第N週 <chủ đề ngắn>` (ví dụ `SAA 第3週 S3 Storage`). Với tuần 2-3: `SAA 第2〜3週 Compute Storage`.
- Eyebrow hero: `AWS SAA-C03 · 12週間ロードマップ · 第N週`.
- Dịch mọi chữ hiển thị còn lại: h1, p.lead, meta, nhãn tiến độ, TOC, tiêu đề section, bảng, bullet, note, câu hỏi và đáp án kiểm tra nhanh, các bước lab, mốc kiểm tra, bảng từ khóa (cột "Đề bài có chữ" giữ từ khóa tiếng Anh, chỉ dịch phần giải thích tiếng Việt), nhãn checklist, chữ trong SVG `<text>`.
- Văn phong: tiếng Nhật tự nhiên cho tài liệu tự học kỹ thuật, です・ます調, ngắn gọn, thuật ngữ IT theo cách dùng phổ biến ở Nhật (可用性, 冗長化, 暗号化, 権限, 障害, 復旧...). Dấu câu tiếng Nhật (、。), không dùng em-dash.
- Các nhãn cố định: "Giải thích ngắn" → "概要", "Hình dung" → "イメージ", "Khi nào dùng" → "使いどころ", "Dễ nhầm" → "混同しやすい点", "Từ khóa trong đề" → "試験キーワード", "Kiểm tra nhanh" → "確認クイズ", "Lý thuyết i / n" → "理論 i / n", "Thực hành" → "ハンズオン", "Mốc kiểm tra" → "確認ポイント", "Ôn nhanh" → "クイックレビュー", "Theo dõi" → "進捗", "Kế hoạch 7 ngày" → "7日間の計画", "Lab k." → "Lab k.", "Checklist tuần N" → "第N週チェックリスト", "Tiến độ checklist" → "チェックリスト進捗", cột bảng "Đề bài muốn / Chọn / Không phải" → "設問の要求 / 選ぶ / 選ばない".
- Chỗ ghi "(cần kiểm tra lại trên tài liệu AWS)" → "（AWSドキュメントで要確認）".

## Cách làm
1. Đọc toàn bộ file nguồn (Read, file 100 đến 175 KB).
2. Viết file đích theo nhiều phần nhỏ vào thư mục nháp riêng trong scratchpad (ví dụ `ja-XX/p1.html`...), rồi ghép lại thành `bai-hoc/tuan-XX.ja.html`. Không ghi đè file nguồn.
3. Kiểm tra bằng lệnh (so với file nguồn): số `<section`, số `data-ck`, số `data-reveal`, số `class="ans"`, có đúng một `<script>` và một `<style>`, `KEY=` giống hệt, không còn chuỗi tiếng Việt có dấu ngoài `<pre>` (grep thử vài từ hay gặp: "của", "được", "không", "với", "trong").
4. KHÔNG publish artifact. Chỉ báo lại: đường dẫn file, kích thước, kết quả các số đếm so với nguồn, và chỗ nào còn phân vân về thuật ngữ.

## Quy ước đã chốt khi dịch lần đầu
- Dịch `aria-label` (chữ cho trình đọc màn hình). Dịch placeholder có chữ tiếng Việt trong lệnh, ví dụ `<bạn>` → `<ユーザー名>`.
- Số theo kiểu Nhật: `256.000` → `256,000`, `0,5` → `0.5`; khoảng "X đến Y" → `X〜Y`.
- Comment HTML/CSS/JS tiếng Việt không hiển thị thì có thể giữ.
- Câu lệnh user gõ trong session ("cho quiz") hoặc prompt mẫu trong `<pre>` giữ tiếng Việt hoặc dịch đều được, Claude trong session hiểu cả hai.
- Nhãn ngoài bảng cố định: "Mục lục" → 目次, "Checklist tuần" (TOC) → 週のチェックリスト, "nhận diện" → 見分け方.
