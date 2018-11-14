def print_word(A):
    print(A[::-1])


word = []
var_for_exit = ""
print("ДЛЯ ВИХОДА ДЛЯ ВЫХОДА: 1")
print("ДЛЯ ВЫВОДА СЛОВ: w")
while var_for_exit != "1":

    var_for_exit = input("ВВЕДІТЬ СЛОВА")
    if var_for_exit == "w":
        print_word(word)
        word.clear()
        continue
    word.append(var_for_exit)
