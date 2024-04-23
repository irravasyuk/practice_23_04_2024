# Завдання 1
# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.
# import pickle
#
# input_numbers = input('Введіть список цілих чисел: ')
#
# numbers = []
#
# for num in input_numbers.split(' '):
#     numbers.append(int(num))
#
# with open('data.pickle', 'wb') as file:
#     pickle.dump(numbers, file)
#
# with open('data.pickle', 'rb') as file:
#     loaded_numbers = pickle.load(file)
#
# print('Список цілих чисел: ', loaded_numbers)


# Завдання 2
# При старті програми з’являється меню з наступними
# пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також
# застосуйте стиснення/розпакування даних.
# import pickle
#
# initial_data = [1, 2, 3, 4, 5]
# data = initial_data
#
# def load_data():
#     try:
#         with open('data.pickle', 'rb') as file:
#             data = pickle.load(file)
#             print('Дані завантажено.')
#             return data
#     except FileNotFoundError:
#         print('Такого файлу немає.')
#         return initial_data
#
# def save_data(data):
#     with open('data.pickle', 'wb') as file:
#         pickle.dump(data, file)
#         print('Дані збережено.')
#
# def add_data(data):
#     add = input('Введіть дані для додавання: ')
#     data.append(add)
#     save_data(data)
#
# def delete_data(data):
#     try:
#         index = int(input('Введіть індекс елемента, який потрібно видалити: '))
#         if 0 <= index < len(data):
#             remove_data = data.pop(index)
#             save_data(data)
#             print(f'Елемент {remove_data} видалено.')
#         else:
#             print('Такого елемента немає в списку')
#     except ValueError:
#         print('Введено неправильний індекс.')
#
# while True:
#     print("\nМеню:")
#     print("1. Завантаження даних")
#     print("2. Збереження даних")
#     print("3. Додавання даних")
#     print("4. Видалення даних")
#     print("5. Вихід")
#
#     choice = input("Оберіть пункт меню: ")
#
#     if choice == '1':
#         data = load_data()
#         print(data)
#     elif choice == '2':
#         save_data(data)
#     elif choice == '3':
#         add_data(data)
#     elif choice == '4':
#         delete_data(data)
#     elif choice == '5':
#         break
#     else:
#         print("Неправильний вибір.")

# Завдання 3
# Маємо певний словник з логінами і паролями користувачів.
# Логін використовується як ключ, пароль —
# як значення. Реалізуйте: додавання, видалення, пошук,
# редагування, збереження та завантаження даних
# (використовуючи стиснення та розпакування).
import pickle
import gzip

def save_data(data, filename):
    with gzip.open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_dict(filename):
    with gzip.open(filename, 'rb') as file:
        return pickle.load(file)

def add_data(data, key, value):
    data[key] = value

def delete_data(data, key):
    if key in data:
        data.pop(key, None)

def search_data(data, key):
    return key in data

def edit_data(data, key, value):
    if key in data:
        data[key] = value

users = {}
save_data(users, 'users.gz')
add_data(users, 'user1', '22222')
add_data(users, 'user2', '11111')
print(load_dict('users.gz'))
delete_data(users, 'user1')
print(search_data(users, 'user1'))
edit_data(users, 'user2', '00000')
print(users)




