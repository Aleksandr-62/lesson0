# def proba(a, b, c=3):
#     print(a + b + c)
#
#
# proba(2, 4)
# ___ф-ция Максимум в списке__
#
# def find_max(list_):
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
#
#
# print(find_max([2, 4, 67, -10, 0, 8]))
#
# # __ ф-ция Подсчтет четных чисел в списке ___
#
# def coun_even(list_):
#     couter = 0
#     for i in list_:
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             couter += 1
#     return couter
#
# print(coun_even([2, 4, 3, 5, 6, 7, 9]))
#
# # __ ф-ция  Уникальный список ________
#
# def unique(list_):
#     new_list = []
#     for i in list_:
#         if i not in new_list:
#             new_list.append(i)
#
#     return new_list
#
# print(unique([2, 4, 2, 7, 4, 9, 7, 5, 4, 3, 5, 6, 6, 7, 1]))


# __ Набросок калькулятор ________


import tkinter as tk  # импорт библиотеки и присвоение имя tk

window = tk.Tk()

def add():  # __ ф-ция для кнопки "+"
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.insert(0, res)


window.title('Калькулятор')
window.geometry("350x350")  # виджет окно (Windows)
window.resizable(False, False)  #фикс.размер окна
button_add = tk.Button(window, text='+', height=2, command=add) # виджет кнопка
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', height=2)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', height=2)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/', height=2)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28) # виджет окно ввода
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=275)
number1 = tk.Label(window, text = 'Введите первое число')  #Виджен надпись
number1.place(x=100, y=50)
number2 = tk.Label(window, text = 'Введите второе число')
number2.place(x=100, y=125)
answer = tk.Label(window, text = 'Ответ')
answer.place(x=100, y=250)
window.mainloop()

