import math

def rootCalculator():
    a = input("first co-efficient: ")
    b = input("second co-efficient: ")
    c = input("third co-efficient: ")
    
    delta = math.sqrt(b*b - 4*a*c)
    
    x1 = ((-1)*b - delta) / 2*a
    
    x2 = ((-1)*b + delta) / 2*a
    
    print("quadratical has finished! Here are your answers: \n")
    
    print("root 1: %s" %x1)
    print("\nroot 2: %s" %x2)

print("Welcome the Quadratic central!\n\n For Quadratical type 1:\n\n For Quadratical(with steps) type 2:\n")

choice = raw_input("enter selection:")

if (choice == 1):
    rootCalculator()
elif (choice == 2):
    print("not developed yet...")
else:
    print("\nyou didn't enter anything :)")
