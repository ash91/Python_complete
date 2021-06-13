username = input("What is your username?\n")
password = input("Enter your password?\n")

pwd_len_count = len(password)
hidden_pwd = '*' * pwd_len_count

print(f'Hi {username} your password is {hidden_pwd} and is {pwd_len_count} letters long')
