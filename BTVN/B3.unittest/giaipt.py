def giaipt(a,b):
	if a != 0:
		return -b/a
	elif b != 0:
		return "Phương trình vô nghiệm."
	else:
		return "Phương trình có vô số nghiệm."

if __name__ == "__main__":
	print('Nhập vào 2 hệ số a và b của phương trình bậc nhất:')

	print('Nhập a:')
	a = float(input())

	print('Nhập b:')
	b = float(input())

	print(giaipt(a,b))

