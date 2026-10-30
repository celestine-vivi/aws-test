# AWS SAA Quiz 01: 40 câu tình huống

> Cách làm: che phần đáp án ở cuối file, làm hết 40 câu trong 60 phút, ghi đáp án vào bảng điểm, rồi mới mở phần giải thích.
> Mục tiêu: trên 32/40 (80%). Câu sai ghi vào "Sổ ghi câu sai" trong file checklist.
> Từ khóa tiếng Anh in nghiêng là từ khóa hay gặp trong đề thật, hãy để ý cách chúng dẫn tới đáp án.

## Bảng điểm

| Câu | Chọn | Đúng/Sai | | Câu | Chọn | Đúng/Sai | | Câu | Chọn | Đúng/Sai | | Câu | Chọn | Đúng/Sai |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | 11 | | | | 21 | | | | 31 | | |
| 2 | | | | 12 | | | | 22 | | | | 32 | | |
| 3 | | | | 13 | | | | 23 | | | | 33 | | |
| 4 | | | | 14 | | | | 24 | | | | 34 | | |
| 5 | | | | 15 | | | | 25 | | | | 35 | | |
| 6 | | | | 16 | | | | 26 | | | | 36 | | |
| 7 | | | | 17 | | | | 27 | | | | 37 | | |
| 8 | | | | 18 | | | | 28 | | | | 38 | | |
| 9 | | | | 19 | | | | 29 | | | | 39 | | |
| 10 | | | | 20 | | | | 30 | | | | 40 | | |

Tổng: ____ / 40

---

## Phần câu hỏi

**Câu 1.** Một công ty lưu ảnh sản phẩm trong S3 và phân phối qua CloudFront. Yêu cầu: người dùng chỉ được tải ảnh qua CloudFront, truy cập thẳng vào URL S3 phải bị từ chối. Giải pháp nào đúng?
- A. Bật Block Public Access và cấp public-read cho từng object
- B. Dùng CloudFront *Origin Access Control (OAC)* và bucket policy chỉ cho phép service principal của CloudFront
- C. Tạo presigned URL cho từng ảnh và nhúng vào CloudFront
- D. Bật S3 static website hosting và trỏ CloudFront vào website endpoint

**Câu 2.** EC2 trong private subnet cần đọc ghi S3 với lượng dữ liệu lớn. Hiện tại traffic đi qua NAT Gateway và chi phí tăng cao. Cách nào *most cost-effective* mà vẫn giữ traffic không ra Internet?
- A. Thay NAT Gateway bằng NAT Instance
- B. Tạo *Gateway VPC Endpoint* cho S3 và thêm route vào route table của private subnet
- C. Tạo Interface VPC Endpoint cho S3
- D. Gắn Internet Gateway cho private subnet

**Câu 3.** Web app nhận đơn hàng với lượng truy cập tăng đột biến theo giờ. Khi tầng xử lý quá tải, một số đơn bị mất. Kiến trúc nào giúp *decouple* và không mất đơn?
- A. Tăng kích thước instance tầng xử lý
- B. Đặt SQS queue giữa web tier và worker tier, worker đọc từ queue
- C. Dùng SNS gửi thẳng đơn tới worker
- D. Dùng Kinesis Data Firehose đẩy đơn vào S3

**Câu 4.** Hệ thống thanh toán yêu cầu các message được xử lý *đúng thứ tự* và *không trùng lặp*. Chọn dịch vụ.
- A. SQS Standard queue
- B. SQS FIFO queue
- C. SNS topic
- D. EventBridge

**Câu 5.** RDS MySQL phục vụ production. Bộ phận báo cáo chạy các query nặng làm app chậm. Cách nào giải quyết với ít thay đổi nhất?
- A. Bật Multi-AZ và trỏ báo cáo vào standby
- B. Tạo *Read Replica* và trỏ báo cáo vào replica
- C. Nâng instance class của RDS
- D. Chuyển dữ liệu sang DynamoDB

**Câu 6.** RDS PostgreSQL phải tiếp tục hoạt động nếu một AZ gặp sự cố, với *automatic failover* và endpoint không đổi. Chọn cấu hình.
- A. Read Replica ở AZ khác
- B. *Multi-AZ deployment*
- C. Snapshot tự động hàng giờ
- D. Aurora Global Database

**Câu 7.** Nhiều EC2 Linux ở nhiều AZ cần *shared file system* chuẩn POSIX, tự scale dung lượng. Chọn dịch vụ.
- A. EBS Multi-Attach
- B. S3
- C. *EFS*
- D. Instance store

**Câu 8.** Ứng dụng Windows cần file share giao thức *SMB*, tích hợp *Active Directory*. Chọn dịch vụ.
- A. EFS
- B. *FSx for Windows File Server*
- C. FSx for Lustre
- D. S3 File Gateway

**Câu 9.** Workload *HPC* cần file system *high-throughput, low-latency*, xử lý dữ liệu đang nằm trong S3. Chọn dịch vụ.
- A. EFS
- B. FSx for Windows File Server
- C. *FSx for Lustre*
- D. EBS io2

**Câu 10.** Dữ liệu log được truy cập khoảng một lần mỗi tháng, khi cần phải đọc *ngay lập tức*, phải chịu được mất một AZ. Chọn storage class *lowest cost*.
- A. S3 Standard
- B. *S3 Standard-IA*
- C. S3 One Zone-IA
- D. S3 Glacier Deep Archive

**Câu 11.** Hồ sơ tài chính phải lưu 7 năm theo quy định, gần như không bao giờ đọc, khi cần có thể chờ *12 giờ*. Chọn storage class *lowest cost*.
- A. S3 Standard-IA
- B. S3 Glacier Instant Retrieval
- C. S3 Glacier Flexible Retrieval
- D. *S3 Glacier Deep Archive*

**Câu 12.** Một data lake có mẫu truy cập *unpredictable*, công ty muốn tự động tối ưu chi phí mà không cần phân tích pattern. Chọn storage class.
- A. S3 Standard
- B. *S3 Intelligent-Tiering*
- C. S3 Standard-IA với lifecycle
- D. S3 Glacier Instant Retrieval

**Câu 13.** Job xử lý ảnh chạy hàng đêm, có thể *chịu được gián đoạn* và chạy lại. Chọn mô hình compute *lowest cost*.
- A. On-Demand
- B. Reserved Instances
- C. *Spot Instances*
- D. Dedicated Hosts

**Câu 14.** Workload ổn định chạy 24/7 trong 3 năm tới, công ty muốn giảm chi phí nhưng vẫn *linh hoạt đổi instance family và region*. Chọn.
- A. Standard Reserved Instances
- B. *Compute Savings Plans*
- C. EC2 Instance Savings Plans
- D. Spot Fleet

**Câu 15.** Game online có người chơi toàn cầu dùng giao thức UDP, cần *static IP* và *failover nhanh* giữa các region. Chọn dịch vụ.
- A. CloudFront
- B. Route 53 latency routing
- C. *Global Accelerator*
- D. Elastic IP ở mỗi region

**Câu 16.** Người dùng ở nhiều châu lục tải file tĩnh dung lượng lớn từ S3 ở Tokyo và than chậm. Cách giảm latency *least operational overhead*.
- A. Tạo bucket ở mỗi region và sync thủ công
- B. Dùng *CloudFront* với origin là bucket
- C. Bật S3 Transfer Acceleration
- D. Dùng Global Accelerator

**Câu 17.** App deploy ở 3 region, muốn Route 53 trả về region cho *độ trễ thấp nhất* với từng người dùng. Chọn routing policy.
- A. Weighted
- B. Geolocation
- C. *Latency-based*
- D. Multivalue answer

**Câu 18.** Site chính ở us-east-1, site dự phòng ở ap-northeast-1. Khi site chính lỗi, DNS phải tự chuyển sang dự phòng. Chọn.
- A. Simple routing với 2 IP
- B. *Failover routing* kèm health check
- C. Weighted routing 100/0
- D. Geoproximity routing

**Câu 19.** App cần lưu mật khẩu RDS, yêu cầu *tự động rotate* định kỳ. Chọn dịch vụ.
- A. Systems Manager Parameter Store (SecureString)
- B. *Secrets Manager*
- C. KMS
- D. IAM

**Câu 20.** Bộ phận bảo mật cần biết *ai đã gọi API nào*, lúc nào, từ IP nào trong tài khoản AWS. Chọn.
- A. CloudWatch Logs
- B. *CloudTrail*
- C. AWS Config
- D. VPC Flow Logs

**Câu 21.** Công ty muốn phát hiện khi có EBS volume *không mã hóa* được tạo ra và ghi nhận lịch sử cấu hình của resource. Chọn.
- A. CloudTrail
- B. *AWS Config* với managed rule
- C. Trusted Advisor
- D. Inspector

**Câu 22.** Web app sau ALB bị tấn công *SQL injection* và *XSS*. Chọn dịch vụ bảo vệ.
- A. Shield Standard
- B. *AWS WAF* gắn vào ALB
- C. GuardDuty
- D. Security Group

**Câu 23.** Cần phát hiện *hoạt động đáng ngờ* như EC2 giao tiếp với địa chỉ IP độc hại, credential bị dùng bất thường, dựa trên VPC Flow Logs, DNS logs, CloudTrail. Chọn.
- A. Inspector
- B. Macie
- C. *GuardDuty*
- D. Detective

**Câu 24.** Công ty cần quét S3 để tìm *dữ liệu cá nhân (PII)* như số thẻ, số điện thoại. Chọn.
- A. GuardDuty
- B. *Macie*
- C. Inspector
- D. Config

**Câu 25.** Trong AWS Organizations, admin muốn *cấm* mọi member account tạo resource ngoài region ap-northeast-1, kể cả admin của account đó. Chọn.
- A. IAM policy ở từng account
- B. *Service Control Policy (SCP)* ở OU
- C. Permission boundary
- D. Resource-based policy

**Câu 26.** Cần truy cập shell vào EC2 ở private subnet, *không mở cổng SSH*, không bastion host, có log phiên làm việc. Chọn.
- A. Bastion host ở public subnet
- B. *Systems Manager Session Manager*
- C. EC2 Instance Connect
- D. Site-to-Site VPN

**Câu 27.** Dữ liệu trong S3 phải mã hóa at rest bằng key do công ty *quản lý và rotate*, có *audit* mỗi lần key được dùng. Chọn.
- A. SSE-S3
- B. *SSE-KMS với customer managed key*
- C. SSE-C
- D. Client-side encryption với key tự lưu

**Câu 28.** Lambda kết nối RDS MySQL. Khi concurrency cao, RDS báo *too many connections*. Giải pháp *ít thay đổi code nhất*.
- A. Tăng max_connections của RDS
- B. Dùng *RDS Proxy* giữa Lambda và RDS
- C. Chuyển sang DynamoDB
- D. Giảm concurrency của Lambda

**Câu 29.** DynamoDB phục vụ workload *read-heavy*, cần latency *microsecond* cho dữ liệu hay đọc. Chọn.
- A. Tăng RCU
- B. Global Secondary Index
- C. *DAX*
- D. ElastiCache Memcached

**Câu 30.** Bảng DynamoDB có partition key là `orderId`. Sau khi tạo bảng, cần query theo `customerId`. Chọn.
- A. Local Secondary Index
- B. *Global Secondary Index*
- C. Scan với filter
- D. Tạo bảng mới

**Câu 31.** Hàng nghìn thiết bị IoT gửi dữ liệu *real-time*, nhiều ứng dụng cần đọc cùng một stream và *replay* dữ liệu trong 24 giờ. Chọn.
- A. SQS
- B. *Kinesis Data Streams*
- C. Kinesis Data Firehose
- D. SNS

**Câu 32.** Cần đưa streaming log vào S3 *near real-time*, có nén và chuyển định dạng Parquet, *không viết consumer code*. Chọn.
- A. Kinesis Data Streams + Lambda
- B. *Kinesis Data Firehose*
- C. SQS + EC2 consumer
- D. DataSync

**Câu 33.** Phân tích viên cần chạy *SQL trực tiếp trên file CSV/Parquet trong S3*, không muốn quản lý server, trả tiền theo lượng dữ liệu quét. Chọn.
- A. Redshift
- B. RDS
- C. *Athena*
- D. EMR

**Câu 34.** Auto Scaling Group scale out chậm vì mỗi instance mất 10 phút cài phần mềm trong user data. Cách rút ngắn.
- A. Tăng cooldown
- B. Dùng *golden AMI* đã cài sẵn phần mềm
- C. Dùng instance lớn hơn
- D. Dùng scheduled scaling

**Câu 35.** Người dùng bị *mất session* khi ASG scale in. Giải pháp bền vững nhất.
- A. Bật sticky session trên ALB
- B. *Lưu session vào ElastiCache hoặc DynamoDB*
- C. Tắt scale in
- D. Dùng NLB thay ALB

**Câu 36.** Data center on-premises cần kết nối tới VPC với *băng thông cao, latency ổn định, không đi qua Internet*. Chọn.
- A. Site-to-Site VPN
- B. *Direct Connect*
- C. VPC peering
- D. Client VPN

**Câu 37.** Cần kết nối on-premises tới VPC *nhanh trong vài ngày*, mã hóa, chi phí thấp, chấp nhận đi qua Internet. Chọn.
- A. Direct Connect
- B. *Site-to-Site VPN*
- C. Transit Gateway riêng lẻ
- D. PrivateLink

**Câu 38.** Công ty có 30 VPC ở nhiều account và 2 data center, muốn kết nối tất cả theo mô hình *hub-and-spoke*, tránh mesh peering. Chọn.
- A. VPC peering giữa từng cặp
- B. *Transit Gateway*
- C. PrivateLink
- D. Direct Connect Gateway

**Câu 39.** Kế hoạch DR yêu cầu *RTO vài phút*, *RPO vài giây*, chi phí thấp hơn active-active. Chọn chiến lược.
- A. Backup and restore
- B. Pilot light
- C. *Warm standby*
- D. Multi-site active-active

**Câu 40.** Một đối tác có account AWS riêng cần đọc bucket S3 của công ty theo cách *an toàn, tạm thời, không chia sẻ access key*. Chọn.
- A. Tạo IAM user cho đối tác và gửi access key
- B. *Tạo IAM role với trust policy tới account đối tác (kèm external ID), đối tác AssumeRole*
- C. Bật public read cho bucket
- D. Gửi presigned URL có hạn 7 ngày cho mọi object

---

## Phần đáp án và giải thích

Domain: SEC = Secure, RES = Resilient, PERF = High-Performing, COST = Cost-Optimized

| Câu | Đáp án | Domain | Giải thích ngắn |
|---|---|---|---|
| 1 | B | SEC | OAC là cách chuẩn hiện nay (thay OAI). Bucket policy chỉ cho principal `cloudfront.amazonaws.com` với điều kiện SourceArn là distribution. Presigned URL (C) vẫn cho truy cập thẳng S3. |
| 2 | B | COST | Gateway endpoint cho S3 và DynamoDB miễn phí, traffic không qua NAT. Interface endpoint (C) có cho S3 nhưng tính tiền theo giờ, không phải cost-effective nhất. |
| 3 | B | RES | SQS giữ message bền vững, worker kéo theo tốc độ của mình. SNS (C) là push, worker quá tải vẫn mất. |
| 4 | B | RES | FIFO đảm bảo thứ tự và exactly-once trong deduplication window. Standard là at-least-once, best-effort ordering. |
| 5 | B | PERF | Read Replica tách tải đọc. Standby của Multi-AZ (A) không nhận traffic đọc với RDS thường. |
| 6 | B | RES | Multi-AZ là synchronous standby, failover tự động, DNS endpoint giữ nguyên. Read Replica (A) phải promote thủ công. |
| 7 | C | PERF | EFS là NFS, multi-AZ, elastic. EBS Multi-Attach (A) chỉ trong một AZ và cần io1/io2 với cluster-aware FS. |
| 8 | B | PERF | FSx for Windows hỗ trợ SMB, NTFS ACL, tích hợp AD. EFS chỉ NFS. |
| 9 | C | PERF | FSx for Lustre dành cho HPC, ML, có thể link với S3 để lazy-load. |
| 10 | B | COST | Standard-IA rẻ hơn Standard, lấy ngay, lưu đa AZ. One Zone-IA (C) không chịu được mất AZ. Deep Archive (D) mất hàng giờ. |
| 11 | D | COST | Deep Archive rẻ nhất, retrieval standard 12 giờ. Flexible (C) đắt hơn một chút, retrieval 3 đến 5 giờ hoặc 12 giờ bulk. |
| 12 | B | COST | Intelligent-Tiering tự chuyển tier theo access, có phí monitoring nhỏ, không phí retrieval. |
| 13 | C | COST | Spot giảm tới 90%, phù hợp job chịu gián đoạn. |
| 14 | B | COST | Compute Savings Plans linh hoạt nhất: đổi family, size, region, kể cả Fargate và Lambda. EC2 Instance SP (C) khóa family và region. |
| 15 | C | PERF | Global Accelerator cho 2 anycast static IP, hỗ trợ TCP/UDP, failover theo health check trong giây. CloudFront chỉ HTTP/HTTPS. |
| 16 | B | PERF | CloudFront cache ở edge, cấu hình một lần. Transfer Acceleration (C) tăng tốc upload, không phải download phân phối. |
| 17 | C | PERF | Latency-based routing đo latency từ người dùng tới region. Geolocation (B) dựa theo vị trí địa lý, không theo latency. |
| 18 | B | RES | Failover routing cần health check trên primary. Weighted 100/0 (C) không tự chuyển. |
| 19 | B | SEC | Secrets Manager có rotation tích hợp cho RDS. Parameter Store (A) không tự rotate. |
| 20 | B | SEC | CloudTrail ghi API call ở mức account. Config (C) ghi trạng thái cấu hình, không ghi ai gọi. |
| 21 | B | SEC | Config rule `encrypted-volumes` đánh giá liên tục và lưu configuration history. |
| 22 | B | SEC | WAF lọc tầng 7 với managed rule SQLi, XSS. Shield (A) chống DDoS, không chống SQLi. |
| 23 | C | SEC | GuardDuty là threat detection dùng chính 3 nguồn log đó. Inspector (A) quét lỗ hổng, Macie (B) tìm dữ liệu nhạy cảm. |
| 24 | B | SEC | Macie dùng ML phát hiện PII trong S3. |
| 25 | B | SEC | SCP là guardrail áp cho cả root/admin của member account. IAM policy (A) admin có thể tự sửa. |
| 26 | B | SEC | Session Manager qua SSM Agent, không cần inbound port, log ra CloudWatch/S3. |
| 27 | B | SEC | SSE-KMS với CMK: công ty quản lý rotation, mọi lần dùng key đều ghi vào CloudTrail. SSE-S3 (A) không audit được theo key. |
| 28 | B | PERF | RDS Proxy pool và share connection, Lambda chỉ đổi endpoint. |
| 29 | C | PERF | DAX là cache in-memory riêng cho DynamoDB, tương thích API, latency microsecond. |
| 30 | B | PERF | GSI tạo được sau khi có bảng, partition key khác. LSI (A) chỉ tạo lúc tạo bảng và dùng chung partition key. |
| 31 | B | PERF | Kinesis Data Streams cho nhiều consumer đọc cùng stream và replay (mặc định 24h). SQS message đọc xong là mất. |
| 32 | B | PERF | Firehose là fully managed delivery, có convert sang Parquet và nén, không cần code. |
| 33 | C | PERF | Athena serverless, query S3 trực tiếp, trả tiền theo TB quét. |
| 34 | B | PERF | Pre-bake AMI (EC2 Image Builder) rút thời gian boot. Warm pool cũng đúng nếu có trong đáp án. |
| 35 | B | RES | Externalize session để stateless. Sticky session (A) vẫn mất khi instance bị terminate. |
| 36 | B | PERF | Direct Connect là đường riêng, latency ổn định, 1 đến 100 Gbps. Thời gian setup tính bằng tuần tới tháng. |
| 37 | B | COST | Site-to-Site VPN dựng trong vài giờ, mã hóa IPsec, rẻ. |
| 38 | B | RES | Transit Gateway là hub trung tâm, hỗ trợ cross-account qua RAM, nối VPN và Direct Connect. |
| 39 | C | RES | Warm standby: bản sao chạy ở quy mô nhỏ, scale lên khi failover, RTO phút. Pilot light (B) chỉ chạy core (DB), RTO hàng chục phút. |
| 40 | B | SEC | Cross-account role với external ID chống confused deputy, credential tạm thời qua STS. |

## Thống kê theo domain (tự điền)

| Domain | Số câu | Đúng | Tỷ lệ |
|---|---|---|---|
| SEC | 13 | | |
| RES | 8 | | |
| PERF | 14 | | |
| COST | 5 | | |
