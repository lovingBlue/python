# encoding=utf-8

matrix = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12]]

# 第一种方法：列表推导式

matrix_transpose = [[row[i] for row in matrix] for i in range(4)]
print matrix_transpose

# 第二种方法：利用 zip 方法

matrix_transpose2 = list(zip(*matrix))
print matrix_transpose2
