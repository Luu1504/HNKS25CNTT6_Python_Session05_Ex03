number_of_classroom = int(input("Số lượng phòng họp cần kiểm tra: "))

if number_of_classroom <= 0:
    print("Số lượng phòng học không hợp lệ")
    print("Chương trình kết thúc")
else:
    # Biến cờ hiệu dùng để kiểm soát việc dừng chương trình khi phòng quá lớn
    is_running = True
    
    for classroom in range(1, number_of_classroom + 1):
        if is_running:
            print(f"\n--- NHẬP LIỆU PHÒNG HỌP THỨ {classroom} ---")
            number_of_chair = int(input("Số lượng ghế của phòng: "))
            number_of_chair_each_row = int(input("Số ghế mỗi hàng: "))

            if number_of_chair <= 0 or number_of_chair_each_row <= 0:
                print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            else:
                number_of_rows = number_of_chair // number_of_chair_each_row

                if number_of_rows > 10 or number_of_chair_each_row > 10:
                    print("Phòng quá lớn. Dừng nhập dữ liệu")
                    # Hạ cờ hiệu xuống False để các phòng phía sau không chạy nữa
                    is_running = False
                else:
                    print(f"=> SƠ ĐỒ CHỖ NGỒI PHÒNG HỌP THỨ {classroom}:")
                    
                    for i in range(number_of_rows):
                        for j in range(number_of_chair_each_row):
                            print("*", end="")
                        print()