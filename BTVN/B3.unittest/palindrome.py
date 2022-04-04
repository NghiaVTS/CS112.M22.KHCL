def palindrome(text):
  if len(text) <= 1:
      return False
  text = text.strip().lower().replace(' ', '')

  #strip() dùng để xoá hết các dấu cách ở 2 đầu chuỗi
  #lower() dùng để chuyển toàn bộ chữ hoa trong chuỗi thành chữ thường
  #replace() dùng để thay toàn bộ ký tự ' ' thành '' 
  
  return text == text[::-1]

if __name__ == "__main__":
  print('Nhập vào một chuỗi:')
  text = input()
  print(palindrome(text))