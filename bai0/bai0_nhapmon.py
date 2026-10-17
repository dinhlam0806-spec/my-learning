# 1. Khai báo biến (Lưu giá trị vào bộ nhớ)
ten = "Dinh Lam"          # Kiểu chuỗi (string): để trong nháy kép ""
tuoi = 20                 # Kiểu số nguyên (integer)
diem_so = 8.5             # Kiểu số thực (float - có dấu phẩy động)
dang_hoc_ai = True        # Kiểu đúng/sai (boolean: True hoặc False)

# 2. Lệnh print() dùng để in kết quả ra màn hình cho mình xem
print("Tên của tôi là:", ten)
print("Tuổi:", tuoi)
print("Điểm số:", diem_so)

# 3. Tính toán cơ bản
a = 10
b = 3
tong = a + b
thuong = a / b

print("Tổng 10 + 3 =", tong)
print("Thương 10 / 3 =", thuong)


# 1. Vòng lặp for: Duyệt qua một danh sách các con số
print("--- VÍ DỤ VỀ VÒNG LẶP FOR ---")
danh_sach_diem = [5, 7, 8, 9, 4, 10]

for diem in danh_sach_diem:
    print("Điểm hiện tại là:", diem)

# 2. Kết hợp if / else (Đúng / Sai): Phân loại học lực
print("\n--- PHÂN LOẠI ĐIỂM SỐ ---")
for diem in danh_sach_diem:
    if diem >= 8:
        print(f"Điểm {diem}: Giỏi quá, chiến thần AI rồi!")
    elif diem >= 5:
        print(f"Điểm {diem}: Khá, cố gắng thêm xíu nữa nhé.")
    else:
        print(f"Điểm {diem}: Cần cày lại phần này nha.")