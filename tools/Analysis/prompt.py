from llama_index.core.prompts import PromptTemplate, PromptType

DEFAULT_INSTRUCTION_STR = (
    "1. Convert the query to executable Python code.\n"
    "2. Format the code properly with consistent indentation (use 4 spaces for each level).\n"
    "3. Use clear and descriptive variable names.\n"
    "4. Separate logical sections of code with blank lines for readability.\n"
    "5. Include all necessary function definitions and variable assignments.\n"
    "6. Do not quote or escape the code in any way.\n"
    "7. Avoid using input() or any other user input functions.\n"
    "8. Ensure all variables used are properly defined within the code.\n"
    "9. Use appropriate whitespace around operators and after commas.\n"
    "10. Follow PEP 8 style guidelines for naming conventions and code layout.\n"
    "11. The variable `df` is already defined, and shouldn't be redefined in the code.\n"
    "12. For matplotlib plots, use plt.figure() to create figures, but don't call plt.show().\n"
    "13. Avoid generating too long code that make execution time too long.\n"
    "14. Do not include any import statements in the code.\n"
)


# 1. Xác định đầu vào và đầu ra
# - Đầu vào: Dạng tensor chứa dữ liệu chuỗi (sequence data)
# - Đầu ra: Dạng tensor chứa dự đoán cho các bước tiếp theo

# 2. Thiết lập các tham số
# - Số units trong lớp LSTM: Chọn một giá trị phù hợp với kích thước dữ liệu
# - Số lớp LSTM: Thêm nhiều lớp nếu cần học các mẫu phức tạp hơn
# - Kích thước batch: Số mẫu xử lý cùng lúc trong quá trình huấn luyện
# - Epoch: Số lần lặp qua toàn bộ dữ liệu

# 3. Tạo model LSTM
# - Sử dụng lớp LSTM từ tensorflow.keras.layers
# - Xác định số units, kích hoạt (activation) và hàm trả về (return sequence)
# - Thêm các lớp bổ trợ như Dense nếu cần thiết (ví dụ, dự đoán đa lớp)

# 4. Cấu hình optimizer và loss function
# - Chọn optimizer (ví dụ, adam) và loss function (ví dụ, categorical_crossentropy)
# - Điều chỉnh learning rate nếu cần

# 5. Chuẩn bị dữ liệu
# - Chuyển đổi dữ liệu thành dạng tensor phù hợp với model LSTM
# - Chia dữ liệu thành tập huấn luyện và đánh giá (train/test split)

# 6. Huấn luyện model
# - Sử dụng model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
# - Theo dõi quá trình huấn luyện bằng cách in ra loss 

# 7. Đánh giá model (tùy chọn)
# - Sử dụng model.evaluate(x_test, y_test) để đánh giá hiệu suất trên tập test

# 8. Lưu model (tùy chọn)
# - Sử dụng model.save('lstm_model.h5') để lưu model đã huấn luyện

# Lưu ý: Đây là hướng dẫn cơ bản. Bạn có thể tùy chỉnh và thêm các bước khác tùy thuộc vào nhu cầu cụ thể của mình.
# Ví dụ, bạn có thể:
# - Thêm lớp Embedding để nhúng dữ liệu văn bản thành vector
# - Sử dụng lớp Dropout để chống overfitting
# - Thực hiện validation trong quá trình huấn luyện

