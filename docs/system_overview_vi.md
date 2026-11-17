# Tổng quan hệ thống SQ3K — ISAS 2026

Tài liệu này là điểm bắt đầu bằng tiếng Việt. Cấu hình kỹ thuật đầy đủ nằm trong [method.md](method.md), còn số liệu và giới hạn đánh giá nằm trong [results.md](results.md).

## Hai luồng dự đoán

Luồng chính biến các quan sát BLE thành fingerprint 10 giây, bước 2 giây, rồi dùng Random Forest phân cấp để dự đoán một trong 22 lớp. Fingerprint có 175 đặc trưng, gồm tín hiệu của cửa sổ hiện tại và lịch sử của tám fingerprint trước đó.

Trong đánh giá có nhãn, specialist dùng các context BLE không chồng lấp dài 50 giây để đề xuất sửa một số dự đoán thuộc 14 lớp phòng. Gate strong_plus_local chỉ chấp nhận sửa khi các điều kiện về context, độ bất định, nguồn được bảo vệ, target, cluster và margin đều đạt.

Luồng inference ẩn chỉ dùng mô hình chính 10 giây và bộ làm trơn centered. Nó không dùng specialist hoặc gate. Cả context 50 giây và bộ làm trơn centered đều có thể dùng dữ liệu sau thời điểm dự đoán hiện tại; vì vậy phương pháp được đánh giá theo batch/offline, không phải streaming nhân quả.

## Đọc số liệu

Kết quả session-grouped là chẩn đoán trong cùng giai đoạn và có khả năng lạc quan do các session không tương đương với các chuyến thăm độc lập. Số liệu 80/332 chuyến thăm và 44.3–44.8% cửa sổ có cùng chuyến thăm trong train là giá trị bài báo báo cáo, nhưng audit log tương ứng chưa được lưu trong gói bằng chứng đã rà soát.

Với LODO cố định 22 lớp, điểm Macro-F1 thô của DLCS nhỉnh hơn main một chút. Sau cùng bộ làm trơn, thứ tự đổi lại và DLCS thấp hơn main. Kết quả chỉ gồm bốn ngày tại một cơ sở; LODO không phải forward-chaining và cấu hình gate được khóa trước khi đánh giá.

Xem [results.md](results.md) để biết bảng đầy đủ, độ lệch chuẩn, audit gate, và trạng thái nguồn của từng nhận định.

## Dữ liệu và bằng chứng

Dữ liệu challenge không có trong repository. Người có quyền truy cập có thể dùng manifest JSON cục bộ để ánh xạ các vai trò dữ liệu vào archive; không đưa manifest hoặc tên member cụ thể vào Git. Hai tệp tọa độ trong config được giữ nguyên theo quyết định của người dùng.

- [Data governance](data.md): dữ liệu, manifest, quyền sử dụng.
- [Authorized reproduction](reproducibility.md): các bước tái tạo có kiểm soát; script và notebook inference tồn tại nhưng không được chạy trong lần rebuild này.
- [Evidence ledger](evidence-ledger.md): nguồn, mức bằng chứng và câu chữ công khai.
- [Open questions](open-questions.md): những dữ liệu cần bổ sung trước khi nâng mức xác nhận.
