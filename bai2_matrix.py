# Biểu diễn ma trận 2x2 trong Python (2 hàng, 2 cột)
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]

# In ra từng hàng của ma trận
print("Ma trận A:")
for row in matrix_A:
    print(row)

# Phép cộng hai ma trận: Cộng từng phần tử ở cùng vị trí lại với nhau
matrix_cong = [
    [matrix_A[i][j] + matrix_B[i][j] for j in range(len(matrix_A[0]))]
    for i in range(len(matrix_A))
]

print("Kết quả cộng ma trận A + B =", matrix_cong)