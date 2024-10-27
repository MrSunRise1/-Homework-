#Практическое задание по модулю: "Подробнее о функциях."
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data) :
    one_sum = 0
    if isinstance(data, (tuple , list , set)) :
        for element in data :
            one_sum += calculate_structure_sum(element)
    elif isinstance(data , dict) :
        for key , value in data.items() :
            one_sum += calculate_structure_sum(key)
            one_sum += calculate_structure_sum(value)
    elif isinstance(data , (int , float)) :
        one_sum += data
    elif isinstance(data , str) :
        one_sum += len(data)
    return one_sum

result = calculate_structure_sum(data_structure)
print(result)

