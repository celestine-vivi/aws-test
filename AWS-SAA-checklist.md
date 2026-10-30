# Lộ trình học AWS SAA (Solutions Architect – Associate) kết hợp hands-on

> Bắt đầu: ____/____/2026  Ngày thi dự kiến: ____/____/2026
> Nhịp học: 1,5 đến 2 giờ mỗi ngày trong tuần, cuối tuần làm lab tổng hợp.
> Nguyên tắc: học lý thuyết một dịch vụ xong thì dựng ngay, dựng xong thì xóa ngay để không tốn tiền.
> Cách học: mỗi tuần mở một session Claude mới trong thư mục này, dán prompt trong `PROMPT-session-tuan.md`. Cuối tuần Claude sinh quiz vào `quiz/tuan-XX.md`, đạt từ 80% mới sang tuần sau. Câu sai ghi vào `so-ghi-cau-sai.md`.

## Thông tin kỳ thi

| Mục | Giá trị |
|---|---|
| Mã đề | SAA-C03 (kiểm tra lại trang AWS trước khi đăng ký xem có bản mới không) |
| Số câu / thời gian | 65 câu / 130 phút (50 câu tính điểm, 15 câu thử nghiệm) |
| Điểm đỗ | 720 / 1000 |
| Lệ phí | 150 USD |
| Ngôn ngữ | Tiếng Anh hoặc tiếng Nhật |
| Domain 1: Design Secure Architectures | 30% |
| Domain 2: Design Resilient Architectures | 26% |
| Domain 3: Design High-Performing Architectures | 24% |
| Domain 4: Design Cost-Optimized Architectures | 20% |

- [ ] Nếu thi tiếng Anh: xin accommodation "ESL +30 minutes" trước khi đặt lịch.

## Tài nguyên (chọn và chốt ở tuần 1)

- [ ] Khóa học chính (chọn một): Stephane Maarek (Udemy, ~27h, gọn) hoặc Adrian Cantrill (~70h, sâu, nhiều lab)
- [ ] Bộ đề: Tutorials Dojo (Jon Bonso) 6 bộ đề
- [ ] Bộ đề: AWS Skill Builder Official Practice Question Set (miễn phí)
- [ ] Khóa miễn phí: AWS Skill Builder "Exam Prep Standard Course: SAA-C03"
- [ ] Lab có hướng dẫn: workshops.aws, Well-Architected Labs
- [ ] Cheat sheet: Tutorials Dojo cheat sheets và bài so sánh dịch vụ (đọc ở tuần 10)

---

## Tuần 1: Nền tảng và dựng môi trường

### Lý thuyết
- [ ] Region, Availability Zone, Edge location
- [ ] Shared responsibility model
- [ ] IAM: user, group, role, policy
- [ ] IAM: thứ tự đánh giá policy (explicit deny > allow > implicit deny)
- [ ] Cách tính tiền cơ bản, Free Tier hiện hành

### Hands-on
- [ ] Tạo tài khoản AWS, bật MFA cho root
- [ ] Tạo IAM user admin, từ đây chỉ dùng user này, không dùng root
- [ ] Tạo AWS Budget 10 USD có email cảnh báo
- [ ] Cài AWS CLI, cấu hình profile, chạy `aws sts get-caller-identity`
- [ ] Tự viết IAM policy chỉ cho đọc một bucket, kiểm tra bằng IAM Policy Simulator

### Mốc kiểm tra
- [ ] Giải thích được khi nào dùng role thay vì user
- [ ] Giải thích được vì sao explicit deny thắng allow

---

## Tuần 2 đến 3: Compute và Storage

### Lý thuyết
- [ ] EC2: instance family, user data, metadata
- [ ] EC2 pricing: On-Demand, Spot, Reserved, Savings Plans, Dedicated Host
- [ ] EC2: placement group (cluster, spread, partition)
- [ ] EBS: gp3, io2, st1, sc1, snapshot, encryption, multi-attach
- [ ] AMI, instance store
- [ ] EFS: performance mode, throughput mode, storage class
- [ ] FSx for Windows, FSx for Lustre, FSx for NetApp ONTAP
- [ ] S3: storage class (Standard, IA, One Zone-IA, Intelligent-Tiering, Glacier Instant / Flexible / Deep Archive)
- [ ] S3: lifecycle, versioning, replication (CRR, SRR), Object Lock
- [ ] S3: bucket policy, ACL, Block Public Access, encryption SSE-S3 / SSE-KMS / SSE-C
- [ ] S3: presigned URL, Transfer Acceleration, multipart upload, event notification
- [ ] Storage Gateway (File, Volume, Tape), Snow family, AWS Backup, DataSync

### Hands-on
- [ ] Chạy EC2 với user data cài web server, truy cập qua public IP
- [ ] Gắn thêm EBS, format, mount, chụp snapshot
- [ ] Tạo AMI từ EC2, launch lại ở AZ khác
- [ ] Tạo S3 static website, bật versioning, upload đè và khôi phục bản cũ
- [ ] Lifecycle rule chuyển sang Glacier sau 30 ngày
- [ ] Mount một EFS vào hai EC2, xem file dùng chung
- [ ] Tạo presigned URL bằng CLI và mở trên trình duyệt

### Mốc kiểm tra
- [ ] Phân biệt EBS, EFS, instance store, S3 dùng trong tình huống nào
- [ ] Chọn được storage class S3 theo từ khóa đề bài

---

## Tuần 4 đến 5: Networking (trọng tâm nhất)

### Lý thuyết
- [ ] VPC, CIDR, subnet, route table
- [ ] Internet Gateway, NAT Gateway, NAT Instance, Egress-only IGW
- [ ] Security Group với NACL (stateful và stateless)
- [ ] VPC endpoint: gateway (S3, DynamoDB) và interface (PrivateLink)
- [ ] VPC peering, Transit Gateway
- [ ] Site-to-Site VPN, Client VPN, Direct Connect
- [ ] ELB: ALB, NLB, Gateway Load Balancer, sticky session, cross-zone
- [ ] Auto Scaling: scaling policy, cooldown, lifecycle hook, warm pool
- [ ] Route 53: routing policy (simple, weighted, latency, failover, geolocation, geoproximity, multi-value), health check, alias
- [ ] CloudFront: origin, OAC, signed URL / cookie, cache policy
- [ ] Global Accelerator so với CloudFront

### Hands-on
- [ ] Dựng VPC hai AZ với public và private subnet, Internet Gateway, route table
- [ ] NAT Gateway cho private subnet, bastion host ở public subnet
- [ ] EC2 private truy cập S3 qua gateway endpoint, bỏ NAT vẫn chạy
- [ ] ALB trước Auto Scaling Group, target tracking theo CPU
- [ ] Stress test (stress-ng) để xem ASG scale out rồi scale in
- [ ] Route 53 failover với health check, tắt instance chính xem DNS chuyển
- [ ] CloudFront trước S3 private bằng OAC, truy cập thẳng S3 phải bị chặn
- [ ] Xóa NAT Gateway, ALB ngay sau khi xong

### Mốc kiểm tra
- [ ] Vẽ lại VPC vừa dựng trên giấy không nhìn console
- [ ] Giải thích gói tin từ private EC2 ra Internet đi qua những gì
- [ ] Phân biệt Security Group với NACL bằng ví dụ cụ thể

---

## Tuần 6: Database

### Lý thuyết
- [ ] RDS: Multi-AZ khác Read Replica, backup, snapshot, encryption, RDS Proxy
- [ ] Aurora: cluster endpoint, reader endpoint, Global Database, Serverless
- [ ] DynamoDB: on-demand và provisioned, GSI với LSI, DAX, Streams, TTL, Global Table
- [ ] ElastiCache: Redis với Memcached, cache-aside và write-through
- [ ] Redshift, Redshift Spectrum
- [ ] DMS, Schema Conversion Tool
- [ ] Neptune, DocumentDB, Keyspaces, Timestream, QLDB (chỉ cần nhận diện)

### Hands-on
- [ ] Tạo RDS Multi-AZ, ép failover, xem endpoint không đổi
- [ ] Tạo read replica, kết nối và thử ghi để thấy bị từ chối
- [ ] Tạo bảng DynamoDB, dùng Lambda ghi và đọc
- [ ] Bật DynamoDB TTL và Streams, xem item hết hạn bị xóa
- [ ] Xóa RDS trong ngày

### Mốc kiểm tra
- [ ] Chọn được RDS, Aurora, DynamoDB, ElastiCache theo yêu cầu đề bài
- [ ] Giải thích Multi-AZ phục vụ HA còn Read Replica phục vụ scale read

---

## Tuần 7: Serverless, tích hợp, container

### Lý thuyết
- [ ] Lambda: limit, concurrency, layer, chạy trong VPC, event source
- [ ] API Gateway: REST với HTTP API, throttling, cache, authorizer
- [ ] Step Functions
- [ ] SQS: standard với FIFO, DLQ, visibility timeout, long polling
- [ ] SNS: topic, fan-out, filter policy
- [ ] EventBridge
- [ ] Kinesis: Data Streams, Firehose, Data Analytics, Video Streams
- [ ] ECS, EKS, Fargate, ECR, App Runner
- [ ] Amazon MQ, AppSync (nhận diện)

### Hands-on
- [ ] API Gateway + Lambda + DynamoDB thành CRUD API
- [ ] SNS fan-out ra hai SQS queue, bật DLQ cho một queue
- [ ] Build container, đẩy lên ECR, chạy bằng Fargate sau ALB
- [ ] Làm lại CRUD API bằng CDK để đối chiếu với lần làm trên console

### Mốc kiểm tra
- [ ] Giải thích khi nào dùng SQS, SNS, EventBridge, Kinesis
- [ ] Giải thích ECS trên EC2 khác Fargate ở đâu

---

## Tuần 8: Bảo mật, giám sát, quản trị

### Lý thuyết
- [ ] KMS: customer managed key, envelope encryption, rotation, multi-Region key
- [ ] Secrets Manager với Parameter Store
- [ ] ACM, CloudHSM
- [ ] WAF, Shield Standard / Advanced, Firewall Manager, Network Firewall
- [ ] GuardDuty, Inspector, Macie, Security Hub, Detective
- [ ] Cognito: User Pool với Identity Pool
- [ ] Organizations, SCP, Control Tower, consolidated billing
- [ ] STS, cross-account role, IAM Identity Center
- [ ] CloudTrail, CloudWatch (metric, log, alarm, dashboard), Config, Trusted Advisor
- [ ] Systems Manager: Session Manager, Parameter Store, Patch Manager
- [ ] CloudFormation, Elastic Beanstalk, CDK
- [ ] Cost Explorer, Cost Allocation Tag, Compute Optimizer, Budgets

### Hands-on
- [ ] CloudWatch alarm CPU gửi SNS email
- [ ] Bật CloudTrail ghi vào S3, tìm lại một hành động vừa làm
- [ ] Tạo KMS key, mã hóa EBS và S3 bằng key đó
- [ ] Secrets Manager lưu mật khẩu RDS, bật rotation
- [ ] SSM Session Manager vào EC2 không mở cổng SSH
- [ ] Nếu có Organizations: tạo SCP chặn một region

### Mốc kiểm tra
- [ ] Phân biệt Secrets Manager với Parameter Store
- [ ] Phân biệt WAF, Shield, GuardDuty, Inspector, Macie theo mục đích

---

## Tuần 9: Kiến trúc tổng hợp và Well-Architected

### Lý thuyết
- [ ] Well-Architected Framework: 6 trụ cột
- [ ] Disaster recovery: backup and restore, pilot light, warm standby, multi-site theo RPO và RTO
- [ ] Migration 7R, Migration Hub, Application Migration Service
- [ ] Analytics nhận diện: Athena, Glue, QuickSight, EMR, OpenSearch, Lake Formation
- [ ] ML services nhận diện: Rekognition, Comprehend, Transcribe, Polly, SageMaker

### Hands-on
- [ ] Dựng kiến trúc 3-tier bằng CDK hoặc CloudFormation: CloudFront, ALB, ASG ở private subnet, RDS Multi-AZ, S3, CloudWatch alarm
- [ ] Vẽ diagram kiến trúc vừa dựng
- [ ] Tự viết 3 cách tối ưu chi phí cho kiến trúc đó
- [ ] Tự viết 3 điểm cần sửa để tăng tính chịu lỗi
- [ ] Xóa toàn bộ stack

### Mốc kiểm tra
- [ ] Giải thích 4 chiến lược DR và chi phí tương ứng
- [ ] Nhìn một kiến trúc, chỉ ra single point of failure

---

## Tuần 10 đến 12: Luyện đề và thi

### Luyện đề
- [ ] Tutorials Dojo đề 1: ____% 
- [ ] Tutorials Dojo đề 2: ____% 
- [ ] Tutorials Dojo đề 3: ____% 
- [ ] Tutorials Dojo đề 4: ____% 
- [ ] Tutorials Dojo đề 5: ____% 
- [ ] Tutorials Dojo đề 6: ____% 
- [ ] AWS Official Practice Question Set: ____% 
- [ ] Đề của khóa học chính: ____% 
- [ ] Làm lại các đề dưới 80% sau 1 tuần
- [ ] Mỗi câu sai ghi vào sổ: dịch vụ, lý do sai, từ khóa trong đề
- [ ] Đọc giải thích cả câu làm đúng
- [ ] Đọc Tutorials Dojo cheat sheets và bài so sánh dịch vụ

### Bảng từ khóa cần thuộc
- [ ] "least operational overhead" → managed / serverless
- [ ] "decouple" → SQS
- [ ] "real-time streaming" → Kinesis
- [ ] "single-digit millisecond key-value" → DynamoDB
- [ ] "microsecond latency" → DAX / ElastiCache
- [ ] "shared file system Linux" → EFS
- [ ] "Windows file share" → FSx for Windows
- [ ] "HPC / high throughput file" → FSx for Lustre
- [ ] "global users low latency" → CloudFront / Global Accelerator
- [ ] "static IP, TCP/UDP, failover nhanh" → Global Accelerator
- [ ] "hybrid storage on-premises" → Storage Gateway
- [ ] "infrequent but instant access" → S3 Standard-IA
- [ ] "archive, retrieve in hours" → Glacier Flexible / Deep Archive
- [ ] "cost-effective compute, interruption OK" → Spot
- [ ] "steady workload 1-3 năm" → Reserved / Savings Plans
- [ ] "DNS failover" → Route 53 failover + health check
- [ ] "private access to AWS service" → VPC endpoint
- [ ] "rotate credentials" → Secrets Manager
- [ ] "audit API calls" → CloudTrail
- [ ] "compliance config drift" → AWS Config

### Đặt lịch và thi
- [ ] Đề luyện đạt trên 80% hai lần liên tiếp → đặt lịch thi ngay
- [ ] Đăng ký qua Pearson VUE (online hoặc test center), chọn ngôn ngữ
- [ ] Ngày thi: đánh dấu câu khó rồi quay lại sau
- [ ] Ngày thi: loại 2 đáp án sai trước khi chọn
- [ ] Ngày thi: không bỏ trống câu nào
- [ ] THI ĐỖ 🎉

---

## Kiểm soát chi phí (làm xuyên suốt)

- [ ] Budget cảnh báo đã bật từ tuần 1
- [ ] Sau mỗi buổi lab: xóa NAT Gateway, ALB, RDS, EKS, Elastic IP không dùng
- [ ] Mỗi tuần vào Billing xem có dịch vụ nào đang chạy ngầm không
- [ ] Kiểm tra Free Tier hiện hành (từ giữa 2025 chuyển sang dạng credit có thời hạn)

## Sổ ghi câu sai

| Ngày | Dịch vụ | Mình chọn | Đáp án đúng | Vì sao sai | Từ khóa |
|---|---|---|---|---|---|
| | | | | | |
