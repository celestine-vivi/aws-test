# Khuôn chung cho bài học tuần (bai-hoc/tuan-XX.html)

Nguồn sự thật về nội dung tuần: AWS-SAA-checklist.md (đọc đúng phần tuần đó). Quy trình học và quy cách quiz: CLAUDE.md.
Mẫu chuẩn: bai-hoc/tuan-01.html. ĐỌC TOÀN BỘ file này trước khi viết (dùng Read, file 66KB).

## Phải giữ y nguyên từ tuan-01.html
- Mở đầu bằng <title>SAA Tuần N ...</title> (2 đến 4 từ, không doctype, không <html>/<head>/<body>, Artifact sẽ bọc).
- Dòng <meta name="claude:viewport-fit-sides" content="cover"> và <link> Google Fonts y nguyên.
- Toàn bộ khối <style> copy nguyên văn (token màu :root, dark mode, .card .block .grid2 .kw .note .tbl .check .q .steps .flow .diag .sv-*). Được thêm vài class nhỏ nếu cần nhưng không sửa cái cũ.
- Cấu trúc: <header class="hero"> (eyebrow "AWS SAA-C03 · Lộ trình 12 tuần · Tuần N", h1, p.lead, div.meta với nhịp học / domain liên quan / chi phí lab ước tính, div.progress với #bar #pct) → <div class="wrap"> gồm <nav class="toc"> và <main>.
- Thứ tự section trong <main>: #ke-hoach (bảng 7 ngày) → từng mục Lý thuyết (mỗi mục một <section id="..."> với eyebrow "Lý thuyết i / n", h2, một .card) → #handson → #moc → #tukhoa → #checklist.
- Mỗi mục lý thuyết trong .card có các .block theo thứ tự: "Giải thích ngắn" → (tùy chọn "Hình dung" bằng SVG inline class .diag dùng class sv-region/sv-az/sv-edge/sv-t/sv-m/sv-line, hoặc bảng/grid2) → "Khi nào dùng" → "Dễ nhầm" (bảng Đề bài muốn / Chọn / Không phải, hoặc Cặp / Khác nhau ở chỗ) → "Từ khóa trong đề" (div.kw với <span>từ khóa tiếng Anh <b>→ đáp án</b></span>) → "Kiểm tra nhanh" (2 đến 4 div.q, đánh số liên tục cả bài, nút data-reveal, p.ans hidden có <b>đáp án</b> rồi giải thích vì sao đáp án sai hay bị chọn).
- Hands-on: mỗi lab một .card với h3 "Lab k. ..." và <ol class="steps">, bước nào có lệnh thì <pre><code>. Cuối lab có resource tốn tiền phải có div.note nhắc xóa (NAT Gateway, ALB, RDS, EKS, Elastic IP, EC2). Lab cuối luôn là dọn dẹp và kiểm tra Billing.
- #moc: grid2 các .card, mỗi mốc kiểm tra một card với "Gợi ý khung trả lời" dạng ul.
- #tukhoa: bảng "Đề bài có chữ" / "Nghĩ ngay tới", 20 đến 30 dòng, từ khóa in nghiêng <em>.
- #checklist: label.check với input id c1..cN data-ck, chia h4 Lý thuyết / Hands-on / Mốc kiểm tra / Khác; mục cuối là "Quiz tuần N đạt từ 80%". Số mục phải khớp #pct "0/N" trong hero.
- Khối <script> copy nguyên, chỉ đổi KEY='saa-tuan-XX' (XX là số tuần hai chữ số).
- TOC phải có link tới mọi section, nhóm bằng <span class="grp eyebrow">.

## Văn phong
- Tiếng Việt, giữ tên dịch vụ và từ khóa AWS bằng tiếng Anh. Từ khóa đề thi in nghiêng (<em>least operational overhead</em>, <em>most cost-effective</em>...).
- Mỗi mục lý thuyết viết SÂU như tuan-01: không chỉ định nghĩa mà có số liệu, giới hạn, bẫy đề thi, so sánh với dịch vụ dễ nhầm. Độ dài file đích 55 đến 80 KB.
- KHÔNG bịa tính năng AWS. Con số giới hạn hay giá không chắc thì ghi "(cần kiểm tra lại trên tài liệu AWS)". Không dùng em-dash.
- Bảng kế hoạch 7 ngày: ngày 6 đến 7 là ôn + quiz, ghi đúng tên file quiz của tuần (xem PROMPT-session-tuan.md).
- Hands-on viết cho Windows + AWS CLI v2 profile "saa", Region ap-northeast-1, theo đúng các lab trong checklist của tuần đó.

## Sau khi viết
1. Ghi file vào bai-hoc/tuan-XX.html (Write).
2. Kiểm tra: grep đếm <section, số input data-ck khớp #pct, có đúng một <script>, KEY đúng.
3. Publish bằng tool Artifact: file_path tuyệt đối tới file vừa viết, icon "book", description một câu. Không truyền url.
4. Báo cáo: URL artifact, kích thước file, danh sách id section, số mục checklist. Không dán nội dung file vào báo cáo.
