class ColliderOfParticles():
    def __init__(self, ListOfParticles):
        self.ListOfParticles = ListOfParticles

    def checkColliderBetweenBalls(self):
        for i , v1 in enumerate(self.ListOfParticles):
            for j, v2 in enumerate(self.ListOfParticles):
                if(i != j):
                    return



