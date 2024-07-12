import random
height= 1280
width =720
coefImpact =1
running = True
dt = 0.1
gravity = 10
DiccionarioDeColores ={
    1:"blue",
    2:"red",
    3:"green",
    4:"purple"
}
def RandomPosition():
    y=random.randint(0,width)
    x=random.randint(0,height)
    return x, y
def RandomColor():
    c=random.randint(1,4)
    color = DiccionarioDeColores[c]
    return color
