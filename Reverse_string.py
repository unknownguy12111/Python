#   Reversed String Program
def Rev(String):
    return String[::-1]     # Slicing [start:stop:step]

String = input("Enter a string to reverse: ")
reversed_string = Rev(String)
print("Reversed string:", reversed_string)