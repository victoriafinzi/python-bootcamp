import math

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)


# def greet(name): #name é o parametro, é o nome dado para essa variável
#     print(f"Olá {name}")
#     print(f"Como você está?")
    
# greet("Viq") #argumento é o dado que será passado para o parametro