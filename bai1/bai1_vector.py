# Tự viết và hiểu bản chất vector
a = [1, 2, 3]
b = [4, 5, 6]

# 1. Phép cộng vector: Lấy từng phần tử tương ứng cộng lại với nhau
vector_cong = [a[i] + b[i] for i in range(len(a))]
print("Cộng vector a + b = ", vector_cong)

# 2. Phép nhân vô hướng (Dot Product): nhân phần tử rồi cộng lại

dot_product = sum(a[i] * b[i] for i in range(len(a)))
print("Tích vô hướng a · b = ", dot_product)
print("Thu nghiem nhanh moi")