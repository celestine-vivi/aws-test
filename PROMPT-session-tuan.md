# Prompt mẫu cho session học từng tuần

Cách dùng: mở session Claude mới trong thư mục này (Desktop\AWS), copy một khối dưới đây dán vào tin nhắn đầu tiên. Claude sẽ tự đọc CLAUDE.md và checklist để biết quy trình.

---

## Mở đầu tuần

```
Hôm nay tôi bắt đầu học Tuần __ trong AWS-SAA-checklist.md.
Hãy đọc phần tuần đó rồi giảng lần lượt từng mục Lý thuyết cho tôi, mỗi mục xong hỏi tôi 1 đến 2 câu nhanh để kiểm tra.
Sau phần lý thuyết thì hướng dẫn tôi làm từng lab trong mục Hands-on.
```

## Tiếp tục tuần đang dở (session mới)

```
Tôi đang học Tuần __ trong AWS-SAA-checklist.md, đã xong các mục đã tick [x].
Hãy tiếp tục từ mục chưa tick đầu tiên.
```

## Xin quiz cuối tuần

```
Tôi đã học xong Tuần __. Hãy sinh quiz cuối tuần theo quy cách trong CLAUDE.md và lưu vào quiz/tuan-__.md.
Đừng đưa đáp án trong chat, tôi sẽ làm xong rồi gửi đáp án cho bạn chấm.
```

## Gửi đáp án để chấm

```
Đáp án của tôi cho quiz/tuan-__.md:
1-A, 2-B, 3-C, ...
Hãy chấm điểm, giải thích các câu sai, ghi câu sai vào so-ghi-cau-sai.md, và tick Mốc kiểm tra trong checklist nếu tôi đạt.
```

## Ôn lại chỗ yếu

```
Tôi làm quiz tuần __ được __/__. Các câu sai nằm ở dịch vụ: ____.
Hãy giảng lại đúng các chỗ đó, so sánh với dịch vụ dễ nhầm, rồi cho tôi 10 câu mini quiz chỉ về phần này.
```

## Ôn tổng hợp (tuần 10 trở đi)

```
Tôi đã học hết tuần 1 đến 9. Hãy cho tôi làm AWS-SAA-quiz-01.md, sau đó chấm và chỉ ra domain nào tôi yếu nhất dựa trên bảng thống kê theo domain.
```

---

## Gợi ý số tuần và tên file quiz

| Tuần trong checklist | Tên file quiz | Số câu |
|---|---|---|
| Tuần 1 | quiz/tuan-01.md | 30 |
| Tuần 2 đến 3 | quiz/tuan-02-03.md | 40 |
| Tuần 4 đến 5 | quiz/tuan-04-05.md | 40 |
| Tuần 6 | quiz/tuan-06.md | 30 |
| Tuần 7 | quiz/tuan-07.md | 30 |
| Tuần 8 | quiz/tuan-08.md | 30 |
| Tuần 9 | quiz/tuan-09.md | 30 |
| Tuần 10 đến 12 | AWS-SAA-quiz-01.md rồi đề Tutorials Dojo | 40 trở lên |
