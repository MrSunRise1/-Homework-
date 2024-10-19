#Практическое задание по модулю: "Основные операторы"
# n=(от 3 до 20)
# result= пароль для одного введенного числа
def generate_pairs(n) :
    result = []
    for i in range(1 , 20) :
        for j in range(i+1 , 20) :
            if n % (i + j)== 0 :
                result.append((i , j))
    return result
n = int(input("Введите число от 3 до 20: "))
if 3<= n <= 20 :
    pairs = generate_pairs(n)
    print(pairs)
else:
    print("Число должно быть от 3 до 20")