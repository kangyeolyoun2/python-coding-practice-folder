def outer_func():
    a = 20
    
    def inner_func():
        a = 30
        print("Namespace:", __name__)
    inner_func()
    
a = 10
outer_func()
print("Namespace:", __name__)
