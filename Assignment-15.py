
import gc

class Demo:
    def __init__(self, name):
        self.name = name

# Create objects
obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

print("Garbage collection enabled:", gc.isenabled())

# Create circular reference
obj1.ref = obj2
obj2.ref = obj1

# Delete references
del obj1
del obj2

print("Collecting garbage...")

# Manually collect garbage
collected = gc.collect()

print("Objects collected:", collected)

# Disable automatic garbage collection
gc.disable()
print("Garbage collection disabled:", gc.isenabled())

# Enable automatic garbage collection
gc.enable()
print("Garbage collection enabled:", gc.isenabled())
