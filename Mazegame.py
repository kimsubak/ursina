from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


def input(key):
      if key == 'escape':
        app.quit()



__ = False






app = Ursina()






class player(FirstPersonController):
       def __init__(self):
              super().__init__(
                speed = 30,
                model = 'cube',
                jump_height = 20,
                Collider = 'box',
                scale = 1
                
        )


class Warp():
     def __init__(self):
          super().__init__(
               
          )



class exit(Entity):
    def __init__(self,i,j):
        super().__init__(
            model = 'cube',
            scale = (5, 5, 5),
            color = color.black90,
            position = ( i*5, 0, j*5)
            )
        self.player = player
        self.text = Text(
             text = 'ty',
             scale = 2,
             origin = (0,0),
             visible = False
             
        )
    def update(self):
        self.clear()
    def clear(self):
        dis = (self.player.position - self.position).length()
        print(dis)
        if dis < 3:
             self.player.enabled = False
             self.text.visible = True

player = player()
#EditorCamera()

p = False

Map = [
    [11,12,13,14,15,16,17,18,19,20,21,23,24,'e',26,27,28,29,30],
    [11,12,13,__,15,16,17,18,19,20,21,23,24,__,26,27,28,29,30],
    [11,12,13,__,__,__,__,18,19,20,21,23,24,__,26,27,28,29,30],
    [11,12,13,14,15,16,__,18,19,20,21,23,24,__,26,27,28,29,30],
    [11,12,13,14,15,16,__,__,__,__,21,23,24,__,__,27,28,29,30],
    [11,12,13,14,15,16,__,18,19,20,21,23,24,25,__,__,28,29,30],
    [11,__,__,14,15,16,__,__,19,20,21,23,24,25,26,__,28,29,30],
    [11,12,__,14,15,16,17,__,19,20,__,__,__,__,__,__,28,29,30],
    [11,12,__,14,15,16,17,__,19,20,__,23,'d',25,26,__,__,__,30],
    [11,__,__,__,__,__,__,__,__,__,__,23,24,25,26,27,28,__,30],
    [11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,'p',30]
]

brick2 = load_texture('brick2.png')



duck = Entity(
      model = 'model/duck.fbx',
      texture = 'imeges\duck.png',
      scale = 0.1,
      Collider = 'mesh',
      color = 'black'
      
)


for i in range(len(Map)):
     for j in range(len(Map[i])):
            if Map[i][j] :
                    if Map[i][j] == 'p':
                        player.position = (i*5 , 0 , j*5)
                        continue
                    if Map[i][j] == 'd':
                        duck.position = (i*5 , 5 , j*5)
                        continue
                    if Map[i][j] == 'e':
                          exitdoor = exit(i,j)
                          continue



                    wall = Entity(
                        model = 'cube',
                        #color = color.brown,
                        scale = (5, 10, 5),
                        position = (i * 5, 1, j * 5),
                        collider = 'box',
                        texture = 'brick2'
                    )







ground = Entity(
    model = "plane",
    color = color.gray,
    position = (0, 1, 0),
    scale = (200, 20, 200),
    collider = "mesh"
)



app.run()
