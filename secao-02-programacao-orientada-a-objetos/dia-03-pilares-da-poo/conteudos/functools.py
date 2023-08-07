import functools


@functools.singledispatch
def func(parâmetro):
    print(parâmetro)


@func.register(int)
def _(parâmetro):
    print(parâmetro * 2)


@func.register
def _(parâmetro: float):
    print(parâmetro * 5)


func(4)
func(4.0)
func("4")
