class Foo:
    def __init__(self, x: int):
        self.x = x
    
    def __str__(self):
        return f"Foo({self.x})"
