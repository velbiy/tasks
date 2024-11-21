def generate_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += str(i) + str(j)
    return password

n = input('Введите число от 3 до 20: ')
result = generate_password(int(n))
print("пароль:", result)
