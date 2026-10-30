# AWS SAA-C03: lộ trình tự học 12 tuần

Bộ tài liệu tự học cho kỳ thi AWS Certified Solutions Architect – Associate (SAA-C03), gồm lộ trình 12 tuần, bài học chi tiết từng tuần bằng tiếng Việt và tiếng Nhật, quiz và sổ ghi câu sai.

**Xem online:** `https://<tên-github>.github.io/<tên-repo>/` (sau khi bật GitHub Pages, xem bên dưới)

## Nội dung

| Đường dẫn | Là gì |
|---|---|
| `bai-hoc/index.html` | Dashboard 12 tuần: tiến độ checklist, thông tin kỳ thi, bảng từ khóa, nút chuyển Tiếng Việt / 日本語 |
| `bai-hoc/tuan-XX.html` | Bài học chi tiết từng tuần (tiếng Việt): lý thuyết, hands-on, mốc kiểm tra, từ khóa, checklist |
| `bai-hoc/tuan-XX.ja.html` | Bản tiếng Nhật của từng tuần, cùng cấu trúc và dùng chung tiến độ với bản Việt |
| `bai-hoc/_build.py` | Script build: `--pages` tạo `site/` cho GitHub Pages, không có cờ thì tạo `bai-hoc/dist/` cho artifact claude.ai |
| `bai-hoc/_check.sh` | Kiểm tra nhanh cấu trúc các trang tuần |
| `bai-hoc/_BRIEF-template.md`, `_BRIEF-ja.md` | Khuôn để Claude sinh bài tuần mới và dịch sang tiếng Nhật |
| `AWS-SAA-checklist.md` | Lộ trình 12 tuần, nguồn sự thật về nội dung từng tuần |
| `AWS-SAA-quiz-01.md` | Đề tổng hợp 40 câu |
| `PROMPT-session-tuan.md` | Prompt mẫu dán vào đầu mỗi session học với Claude |
| `so-ghi-cau-sai.md` | Sổ ghi câu sai |
| `CLAUDE.md` | Hướng dẫn cho Claude Code khi học trong thư mục này |

## Xem trên máy

```bash
python bai-hoc/_build.py --pages
python -m http.server 8000 --directory site
```

Mở http://localhost:8000. Tiến độ checklist lưu trong localStorage của trình duyệt, mỗi máy và mỗi domain riêng.

## Đưa lên GitHub Pages

1. Tạo repo trên GitHub, push nhánh `main`.
2. Vào **Settings → Pages → Build and deployment → Source**, chọn **GitHub Actions**.
3. Mỗi lần push lên `main`, workflow `.github/workflows/pages.yml` tự chạy `_build.py --pages` và deploy thư mục `site/`. Xem tiến trình ở tab **Actions**.

Thư mục `site/` và `bai-hoc/dist/` là output build nên không commit (đã có trong `.gitignore`).

## Sửa nội dung

- Sửa file nguồn trong `bai-hoc/`. Nếu sửa một tuần thì sửa cả bản Việt và bản Nhật cho khớp.
- Chạy `sh bai-hoc/_check.sh` để kiểm tra cấu trúc, rồi commit và push. Pages tự cập nhật.
