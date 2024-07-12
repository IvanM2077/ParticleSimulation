'''
import pygame
import random
pygame.init()
height= 1280
width =720
screen = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()
running = True
dt = 0.1
gravity = 10
DiccionarioDeColores ={
    1:"blue",
    2:"red",
    3:"green",
    4:"purple"
}
class Vector():
    def __init__(self,x,y):
        self.x= x
        self.y =y

class ColliderBalls():
    def __init__(self, ListOfBalls):
        self.ListOfBalls = ListOfBalls

    def CheckCollisionsBetweenBalls(self):
        for i,v1 in enumerate(self.ListOfBalls):
            for j, v2 in enumerate(self.ListOfBalls):
                if(i not j):

        return

class Circle():
    def __init__(self, x, y, color, radius):
        self.x=x
        self.y=y
        self.radius = radius
        self.color = color
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
    def Update(self):
        # Aplicar gravedad
        self.vy += gravity * dt
        self.y += self.vy * dt + 0.5 * gravity * dt**2
    def CheckCollider(self):
        # Verificar colisión con los bordes de la pantalla
        if self.y + self.radius >= width: #abajo
            self.y = width - self.radius
            self.vy = -1*self.vy
        if self.y - self.radius <= 0:#arriba
            self.y = self.radius
            self.vy = -1*self.vy

    def Draw(self):
        pygame.draw.circle(surface=screen,color=self.color,center=(int(self.x), int(self.y)),radius=self.radius)
def RandomPosition():
    y=random.randint(0,width)
    x=random.randint(0,height)
    return x, y
def RandomColor():
    c=random.randint(1,4)
    color = DiccionarioDeColores[c]
    return color
List = []
for i in range (50):
    P= RandomPosition()
    Color = RandomColor()
    C=Circle(P[0],P[1], Color,20)
    List.append(C)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    for i, v in enumerate(List):
        v.Draw()
        v.Update()
        v.CheckCollider()
        if(i==1):
            print(v.y, v.vy, v.ay)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

'''

import pygame
import random
import math

pygame.init()

# Dimensiones de la pantalla
height = 1280
width = 720
screen = pygame.display.set_mode((height, width))

clock = pygame.time.Clock()
running = True
dt = 0.1
gravity = 10

# Diccionario de colores para las bolas
DiccionarioDeColores = {
    1: "blue",
    2: "red",
    3: "green",
    4: "purple"
}

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ColliderBalls():
    def __init__(self, ListOfBalls):
        self.ListOfBalls = ListOfBalls

    def CheckCollisionsBetweenBalls(self):
        for i, v1 in enumerate(self.ListOfBalls):
            for j, v2 in enumerate(self.ListOfBalls):
                if i < j:  # Solo chequear colisión entre pares únicos
                    if v1.IsColliding(v2):
                        # Manejar la colisión
                        self.HandleCollision(v1, v2)

    def HandleCollision(self, ball1, ball2):
        try:
            # Vectores de posición y velocidad
            p1 = Vector(ball1.x, ball1.y)
            p2 = Vector(ball2.x, ball2.y)
            v1 = Vector(ball1.vx, ball1.vy)
            v2 = Vector(ball2.vx, ball2.vy)

            # Vector entre los centros de los círculos
            distance = Vector(p2.x - p1.x, p2.y - p1.y)
            distance_length = math.sqrt(distance.x ** 2 + distance.y ** 2)

            # Vectores normalizados
            n = Vector(distance.x / distance_length, distance.y / distance_length)

            # Proyecciones de velocidades en la dirección normal
            v1n = v1.x * n.x + v1.y * n.y
            v2n = v2.x * n.x + v2.y * n.y

            # Nuevas velocidades después de la colisión elástica
            m1 = 1  # Masa del círculo 1 (se asume como 1 para simplificar)
            m2 = 1  # Masa del círculo 2 (se asume como 1 para simplificar)

            #v1n_new = ((m1 - m2) * v1n + 2 * m2 * v2n) / (m1 + m2)
            #v2n_new = ((m2 - m1) * v2n + 2 * m1 * v1n) / (m1 + m2)
            v1n_new =v2n
            v2n_new =v1n
            # Actualizar velocidades en la dirección normal
            v1_new = Vector(v1.x - v1n * n.x + v1n_new * n.x, v1.y - v1n * n.y + v1n_new * n.y)
            v2_new = Vector(v2.x - v2n * n.x + v2n_new * n.x, v2.y - v2n * n.y + v2n_new * n.y)

            # Aplicar nuevas velocidades a los círculos
            ball1.vx, ball1.vy = v1_new.x, v1_new.y
            ball2.vx, ball2.vy = v2_new.x, v2_new.y
        finally:
            return print("Error")


class Circle():
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 0  # Velocidad inicial en x
        self.vy = 0  # Velocidad inicial en y
        self.ax = 0
        self.ay = 0

    def Update(self):
        # Aplicar gravedad
        self.vy += gravity * dt
        self.y += self.vy * dt + 0.5 * gravity * dt**2
        self.x += self.vx * dt  # Actualizar posición en x

    def CheckCollider(self):
        # Verificar colisión con los bordes de la pantalla
        CoeficientImpact = 1
        if self.y + self.radius >= width:  # abajo
            self.y = width - self.radius
            self.vy = -self.vy *CoeficientImpact
        if self.y - self.radius <= 0:  # arriba
            self.y = self.radius
            self.vy = -self.vy*CoeficientImpact
        if self.x + self.radius >= height:  # derecha
            self.x = height - self.radius
            self.vx = -self.vx*CoeficientImpact
        if self.x - self.radius <= 0:  # izquierda
            self.x = self.radius
            self.vx = -self.vx*CoeficientImpact

    def Draw(self):
        #pygame.draw.circle(surface=screen,color=self.color,center=(int(self.x), int(self.y)),radius=self.radius)
        pygame.draw.circle(surface=screen, color=self.color, center=(int(self.x), int(self.y)), radius=self.radius)

    def IsColliding(self, other):
        # Calcular la distancia entre los centros de los dos círculos
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        # Si la distancia es menor o igual a la suma de los radios, hay colisión
        if distance <= self.radius + other.radius:
            return True
        return False

def RandomPosition():
    y = random.randint(0, width)
    x = random.randint(0, height)
    return x, y

def RandomColor():
    c = random.randint(1, 4)
    color = DiccionarioDeColores[c]
    return color

# Crear lista de círculos
List = []
for i in range(400):
    P = RandomPosition()
    Color = RandomColor()
    C = Circle(P[0], P[1], "blue", 20)
    List.append(C)

# Bucle principal
collider = ColliderBalls(List)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for i, v in enumerate(List):
        v.Draw()
        v.Update()
        v.CheckCollider()

    # Verificar colisiones entre las bolas
    collider.CheckCollisionsBetweenBalls()

    pygame.display.flip()
    #clock.tick()

pygame.quit()

#import Particle as p
#particle=p.particle(1,2,3,4)