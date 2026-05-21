number_of_invoices_in_shift = int(input("Nhập số lượng hóa đơn trong ca: "))
max = 0
min = 0

for i in range(1 , number_of_invoices_in_shift + 1):
    value_invoices = int(input(f"Giá trị của hóa đơn thứ {i}: "))

    if i == 1:
        max = value_invoices
        min = value_invoices
    else:
        if value_invoices > max:
            max = value_invoices
        else:
            min = value_invoices

print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print(f"Hóa đơn có giá trị cao nhất: {max} VNĐ")
print(f"Hóa đơn có giá trị thấp nhất: {min} VNĐ")
