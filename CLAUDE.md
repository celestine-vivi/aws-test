# Thư mục học AWS SAA (Solutions Architect – Associate)

Đây là thư mục tự học để thi AWS SAA-C03. Mỗi tuần trong lộ trình được học trong một session Claude riêng. Trả lời bằng tiếng Việt, giữ nguyên tên dịch vụ và từ khóa AWS bằng tiếng Anh.

## File trong thư mục

- `AWS-SAA-checklist.md`: lộ trình 12 tuần, mỗi tuần có Lý thuyết, Hands-on, Mốc kiểm tra. Đây là nguồn sự thật về nội dung từng tuần. Tick `[x]` khi user xác nhận đã xong một mục.
- `AWS-SAA-quiz-01.md`: đề tổng hợp 40 câu, dùng ở tuần 10 trở đi làm bài kiểm tra chung. Không sửa file này.
- `PROMPT-session-tuan.md`: prompt mẫu user dán vào đầu mỗi session tuần.
- `quiz/tuan-XX.md`: quiz cuối tuần do Claude sinh ra, một file mỗi tuần (XX là số tuần, ví dụ `tuan-01.md`, `tuan-02-03.md`).
- `bai-hoc/`: bài học chi tiết mỗi tuần (`tuan-XX.html` tiếng Việt, `tuan-XX.ja.html` tiếng Nhật) và dashboard `index.html`, publish gộp thành một artifact có link ở `bai-hoc/README.md`. Sửa bài thì sửa file nguồn (cả bản Việt và bản Nhật), chạy `python bai-hoc/_build.py` rồi publish lại artifact từ `bai-hoc/dist/`. Repo dùng GitHub Pages qua `.github/workflows/pages.yml` (build bằng `_build.py --pages` ra `site/`), nên push lên `main` là trang tự cập nhật. Khuôn tạo bài mới: `_BRIEF-template.md`, khuôn dịch: `_BRIEF-ja.md`. Khi user bắt đầu một tuần, đưa link dashboard và trang tuần đó trước khi giảng.
- `so-ghi-cau-sai.md`: sổ ghi câu sai gộp của mọi tuần, mỗi dòng gồm ngày, tuần, dịch vụ, mình chọn, đáp án đúng, vì sao sai, từ khóa.

## Quy trình một session tuần

1. User nói đang học tuần nào. Đọc phần tuần đó trong `AWS-SAA-checklist.md` trước khi giảng.
2. Giảng lý thuyết theo đúng thứ tự các mục Lý thuyết của tuần đó. Mỗi mục: giải thích ngắn, khi nào dùng, so sánh với dịch vụ dễ nhầm, và từ khóa hay gặp trong đề thi. Hỏi lại user 1 đến 2 câu nhanh sau mỗi mục để chắc đã hiểu.
3. Hướng dẫn Hands-on từng bước trên AWS Console hoặc CLI. Sau mỗi lab nhắc user xóa resource tốn tiền (NAT Gateway, ALB, RDS, EKS, Elastic IP).
4. Khi user nói "xong tuần" hoặc "cho quiz": sinh quiz cuối tuần và lưu vào `quiz/tuan-XX.md`. Nếu file đã có thì tạo `quiz/tuan-XX-lan2.md`.
5. User làm quiz rồi gửi đáp án. Chấm điểm, giải thích từng câu sai, ghi câu sai vào `so-ghi-cau-sai.md`, và tick các mục Mốc kiểm tra trong checklist nếu đạt.
6. Dưới 80%: đề xuất ôn lại đúng mục yếu rồi làm quiz lần 2. Từ 80% trở lên: xác nhận xong tuần, nói tuần tiếp theo học gì.

## Quy cách quiz cuối tuần

- 30 câu cho tuần một khối, 40 câu cho khối hai tuần (tuần 2 đến 3, tuần 4 đến 5, tuần 10 đến 12).
- Chỉ ra đề trong phạm vi dịch vụ của tuần đó, cộng tối đa 5 câu ôn lại các tuần trước.
- Dạng tình huống giống đề thật: mô tả bài toán, 4 lựa chọn A B C D, một đáp án đúng. Khoảng 20% câu dạng "chọn 2 đáp án".
- Từ khóa quan trọng trong đề in nghiêng bằng tiếng Anh, ví dụ *least operational overhead*, *most cost-effective*, *decouple*.
- Cấu trúc file theo đúng `AWS-SAA-quiz-01.md`: bảng điểm ở đầu, phần câu hỏi, phần đáp án và giải thích ở cuối có gắn domain (SEC, RES, PERF, COST), bảng thống kê theo domain.
- Đáp án và giải thích để cuối file, không viết cạnh câu hỏi.
- Giải thích phải nói vì sao đáp án đúng và vì sao ít nhất một đáp án sai hay bị chọn nhầm.

## Lưu ý

- Không bịa tính năng AWS. Chỗ nào không chắc (giới hạn số, giá) thì nói rõ là cần kiểm tra lại trên tài liệu AWS.
- Không tạo resource AWS thay user, chỉ hướng dẫn.
- Nếu user dán lỗi từ console hoặc CLI, giúp debug trước rồi mới học tiếp.
