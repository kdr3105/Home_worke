# def hello():
#     print("hello")
# def wrap(another_func) :
#     print("Я получаю функцию и возвращаю,как есть")
#     return another_func
#
# new_hello = wrap(hello)
# new_hello()

def function_l():
    print("hello")
def function_2():
    print("bye")
funcs = [function_l, function_2]
funcs[0]()
funcs[1]()

# Будет работать и выводить
# hello
# bye