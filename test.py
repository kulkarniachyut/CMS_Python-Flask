def outer():
    x = 1
    def inner():
     print x # 1
    return inner
foo = outer()
foo
foo.func_closure
foo()
