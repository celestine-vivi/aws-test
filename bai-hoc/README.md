# Bài học chi tiết từng tuần (artifact)

## Dashboard (dùng cái này)

**https://claude.ai/artifact/WvybvQguVnMeFJrnVgpTeM**: một artifact gộp gồm trang tổng quan 12 tuần (tiến độ checklist từng tuần, thông tin kỳ thi, bảng từ khóa) và 12 trang bài học. Góc trên mỗi trang có nút chuyển Tiếng Việt / 日本語, lựa chọn được nhớ cho các trang sau.

- Nguồn: `index.html` (dashboard), `tuan-XX.html` (tiếng Việt), `tuan-XX.ja.html` (tiếng Nhật, đủ 12 trang). Sửa nội dung một tuần thì sửa cả hai file cho khớp.
- Build: `python bai-hoc/_build.py` tạo thư mục `dist/` (bọc doctype, chèn thanh điều hướng và script ngôn ngữ). Publish lại artifact từ `dist/index.html` với `files` là các `dist/tuan-*.html`.
- Tiến độ checklist lưu trong localStorage theo key `saa-tuan-XX`, dùng chung cho bản Việt và Nhật của cùng tuần.
- GitHub Pages: `python bai-hoc/_build.py --pages` tạo `site/` ở gốc repo. Khi push lên `main`, workflow `.github/workflows/pages.yml` tự build và deploy (xem README ở gốc repo).

## Artifact riêng từng tuần (bản cũ, vẫn mở được)

Mỗi tuần một trang HTML, đã publish làm artifact riêng tư trên claude.ai. File nguồn nằm ngay thư mục này, muốn sửa thì sửa file rồi publish lại cùng URL.

| Tuần | File | Artifact |
|---|---|---|
| 1 | `tuan-01.html` | https://claude.ai/artifact/PHGF4XzJhj9oc9esBPo1Cs |
| 2 đến 3 (khối gộp, tạo ở session tuần 2) | `tuan-02-03.html` | https://claude.ai/artifact/NDwEWMtKZLMqpKuGJLinso |
| 3 (S3, Storage Gateway, Snow, DataSync, Backup) | `tuan-03.html` | https://claude.ai/artifact/BKjGFvavmjWHy4iGJsBj6j |
| 4 (VPC, NAT, SG/NACL, endpoint, peering/TGW, VPN/DX) | `tuan-04.html` | https://claude.ai/artifact/U817c4D6DD2sTfNaEkhQkP |
| 5 (ELB, ASG, Route 53, CloudFront, Global Accelerator) | `tuan-05.html` | https://claude.ai/artifact/NdgYNRkKMgMaQBFMH8Jad3 |
| 6 (RDS, Aurora, DynamoDB, ElastiCache, Redshift, DMS) | `tuan-06.html` | https://claude.ai/artifact/HBKsJgHhxemMrb9fd7b9cW |
| 7 (Lambda, API Gateway, Step Functions, SQS/SNS, EventBridge, Kinesis, container) | `tuan-07.html` | https://claude.ai/artifact/9Bsr5bzdMcM7Aam8yxQNtc |
| 8 (KMS, Secrets Manager, WAF/Shield, GuardDuty/Inspector/Macie, Cognito, Organizations, CloudTrail/CloudWatch/SSM, IaC, chi phí) | `tuan-08.html` | https://claude.ai/artifact/KCEXfAFw2E8SE12XJ15Qnq |
| 9 (Well-Architected, DR, migration, analytics, ML) | `tuan-09.html` | https://claude.ai/artifact/BsYXqTiQFZBQoLn9Ghotnz |
| 10 (ôn tổng hợp, bảng so sánh dịch vụ, 3 đề đầu) | `tuan-10.html` | https://claude.ai/artifact/6U4NJhP67hyBxCXaK6DQ3h |
| 11 (luyện đề theo domain, TD đề 2 đến 5, phân tích câu sai) | `tuan-11.html` | https://claude.ai/artifact/9Chur7WZSVLo481uFx6Kv9 |
| 12 (đặt lịch, cheat sheet con số và từ khóa, chiến thuật ngày thi) | `tuan-12.html` | https://claude.ai/artifact/UNk4XsKw5nUi3AyMFAehkL |

Lưu ý: `tuan-02-03.html` và `tuan-03.html` trùng phần S3. Khi học tuần 3 dùng `tuan-03.html` (chi tiết hơn), `tuan-02-03.html` dùng cho phần EC2, EBS, EFS, FSx của tuần 2.

## Khuôn và kiểm tra

- `_BRIEF-template.md`: khuôn bắt buộc (cấu trúc, style, script, văn phong) để sinh bài tuần mới giống `tuan-01.html`.
- `_check.sh`: chạy `sh bai-hoc/_check.sh` để kiểm tra nhanh cấu trúc mọi file (số section, checklist khớp thanh tiến độ, script, KEY).
- Muốn làm lại một tuần (ví dụ bản lần 2), nói "tạo lại bài học tuần N theo bai-hoc/_BRIEF-template.md" rồi publish lại cùng URL.
