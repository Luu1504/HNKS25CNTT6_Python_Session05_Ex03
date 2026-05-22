number_of_classroom = int(input("Số lượng phòng họp cần kiểm tra: "))
number_of_chair = int(input("Số lượng ghế của từng phòng: "))
number_of_chair_each_row = int(input("Số ghế mỗi hàng: "))

# Tính toán số hàng ghế thực tế của phòng họp
number_of_rows = number_of_chair // number_of_chair_each_row

# Vòng lặp Tầng 1: Quản lý việc duyệt qua từng phòng họp
for classroom in range(1, number_of_classroom + 1):
    print(f"\n=> SƠ ĐỒ CHỖ NGỒI PHÒNG HỌP THỨ {classroom}:")
    
    # Vòng lặp Tầng 2: Quản lý việc in từng hàng ghế (Hàng dọc)
    for i in range(number_of_rows):
        
        # Vòng lặp Tầng 3: Quản lý việc in số ghế trên hàng đó (Hàng ngang)
        for j in range(number_of_chair_each_row):
            print("*", end="")
            
        # Xuống dòng sau khi đã in xong một hàng ghế
        print()