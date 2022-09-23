# Задача 1. Создание словаря из файла
with open('cook_instructions.txt', 'rt', encoding= 'utf8') as file_with_receipt:
    cook_book = {}
    for line in file_with_receipt:
        dish = line.strip()
        ingredient_count = file_with_receipt.readline()
        ingredients = []
        for i in range(int(ingredient_count)):
            component = file_with_receipt.readline()
            name, quantity, measure = component.split(' | ')
            ingredient = {}
            ingredient['ingredient_name'] = name
            ingredient['ingredient_quantity'] = quantity
            ingredient['ingredient_measure'] = measure
            ingredients.append(ingredient)
            cook_book[dish] = ingredients
        empty = file_with_receipt.readline()
    print(f'Кулинарная книга: {cook_book}')

# Задача 2. Список покупок
def get_shop_list_by_dishes(dishes, number_of_persons):
    shop_list = {}
    for dish in dishes:
        for dish_name, ingredients in cook_book.items():
            if dish not in shop_list.keys():
                if dish_name == dish:
                    for ingredient in ingredients:
                        name = ingredient['ingredient_name']
                        quantity = int(ingredient['ingredient_quantity']) * number_of_persons
                        measure = ingredient['ingredient_measure']
                        parchase = {}
                        parchase['measure'] = measure
                        parchase['quantity'] = quantity
                        shop_list[name] = parchase
            else:
                parchase['quantity'] += int(ingredients[ingredient_quantity]) * number_of_persons
    print(f'Список покупок: {shop_list}')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3)

# Задача 3. Объединение и сортировка файлов
dict_quantity = {}

quantity_lines_1 = 0
with open('1.txt', 'rt', encoding='utf8') as file_1:
    for line in file_1:
        quantity_lines_1 += 1
dict_quantity[quantity_lines_1] = 1

quantity_lines_2 = 0
with open('2.txt', 'rt', encoding='utf8') as file_2:
    for line in file_2:
        quantity_lines_2 += 1
dict_quantity[quantity_lines_2] = 2

quantity_lines_3 = 0
with open('3.txt', 'rt', encoding='utf8') as file_3:
    for line in file_3:
        quantity_lines_3 += 1
dict_quantity[quantity_lines_3] = 3


order = sorted(dict_quantity)


with open('result_joining.txt', 'wt', encoding='utf8') as result_file:
    for i in order:
        for number_lines, number_file in dict_quantity.items():
            if i == number_lines:
                path = str(number_file)+ '.txt'
                with open(path, 'rt', encoding='utf8') as file:
                    lines_to_write = file.readlines()
                    result_file.writelines(path)
                    result_file.write('\n')
                    result_file.writelines(str(i))
                    result_file.write('\n')
                    result_file.writelines(lines_to_write)
                    result_file.write('\n')



