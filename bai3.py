number_of_classroom = int(input("Số lượng phòng họp cần kiểm tra: "))
number_of_chair = int(input("Số lượng ghế của từng phòng: "))
number_of_chair_each_row = int(input("Số ghế mỗi hàng: "))

for i in range(1 , number_of_chair_each_row + 1):
    for j in range(1 , number_of_chair + 1):
        print("*" , end="")
    print()