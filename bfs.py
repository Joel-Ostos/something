from manim import *
import networkx as nx


class BFS(Scene):
    def construct(self):
        meta = 1,6,3,2,8,5,4,7
        title = Title("Busqueda Primero en Anchura")

#--------ROOT--------------------------------------
        root = Circle(radius=0.3, color=RED)
        rootn = MathTex("1")
        rootg = VGroup(root, rootn)
        root.move_to([0,3,0])
        rootn.move_to([0,3,0])
#-----------------------------------------------------

#-------Lineas root a nodos 1 y 2---------------------
        linea1 = Line(start=[-0.3,3,0],  end=[-1.5,2.5,0]);
        linea2 = Line(start=[ 0.3,3,0],  end=[ 1.5,2.5,0]);
#-----------------------------------------------------

#-------Nodos 1 y 2---------------------
        circle1 = Circle(radius=0.3, color=RED);
        circle1.move_to([1.6,2.2,0])

        number1 = MathTex("3")
        number1.move_to([1.6,2.2,0])

        circle2 = Circle(radius=0.3, color=RED)
        number2 = MathTex("6")
        number2.move_to([-1.6,2.2,0])

        circle2.move_to([-1.6,2.2,0])
#-----------------------------------------------------

#-------Lineas desde nodo 1 a nodos 3 y 4---------------------
        linea3 = Line(start=[-1.28,2.2,0], end=[-0.9, 1.75,0]);
        linea4 = Line(start=[-1.92,2.2,0], end=[-2.3, 1.75,0]);
#-----------------------------------------------------

#-------Nodos 3 y 4---------------------
        circle3 = Circle(radius=0.3, color=RED);
        circle3.move_to([-2.5,1.5,0])
        number3 = MathTex("2")
        number3.move_to([-2.5,1.5,0])

        circle4 = Circle(radius=0.3, color=RED)
        number4 = MathTex("8")
        number4.move_to([-0.7,1.5,0])

        circle4.move_to([-0.7,1.5,0])
#-----------------------------------------------------

#-------Lineas desde nodo 1 a nodos 3 y 4---------------------
        linea5 = Line(start=[1.28,2.2,0], end=[0.9, 1.75,0]);
        linea6 = Line(start=[1.92,2.2,0], end=[2.3, 1.75,0]);
#-----------------------------------------------------

#-------Nodos 5 y 6---------------------
        circle5 = Circle(radius=0.3, color=RED);
        circle5.move_to([2.5,1.5,0])
        number5 = MathTex("5")
        number5.move_to([2.5,1.5,0])

        circle6 = Circle(radius=0.3, color=RED)
        circle6.move_to([0.7,1.5,0])
        number6 = MathTex("4")
        number6.move_to([0.7,1.5,0])

#-----------------------------------------------------

#-------Lineas desde nodo 1 a nodos 3 y 4---------------------
        linea7 = Line(start=[-2.82,1.5,0], end=[-3.3, 1.1,0]);
#-----------------------------------------------------

#-------Nodo 7----------------------------------------
        circle7 = Circle(radius=0.3, color=RED);
        circle7.move_to([-3.4,0.8,0])
        number7 = MathTex("7")
        number7.move_to([-3.4,0.8,0])
#-----------------------------------------------------

#-------Agrupación de los circulos (nodos) 1 y 2------

        cgroup1 = VGroup(circle1, number1)
        cgroup2 = VGroup(circle2, number2)
        cgroup3 = VGroup(circle3, number3)
        cgroup4 = VGroup(circle4, number4)
        cgroup5 = VGroup(circle5, number5)
        cgroup6 = VGroup(circle6, number6)
        cgroup7 = VGroup(circle7, number7)
#-----------------------------------------------------

#  Grupo de las líneas
        lgroup = VGroup(linea1,linea2,linea3,linea4,linea5,linea6, linea7)


#--Grupo contenedor de todo---------------------------
        grupoC = VGroup(rootg, cgroup1, cgroup2, cgroup3, cgroup4, cgroup5, cgroup6, cgroup7, lgroup)
        grupoC.shift(DOWN * 1.5);
#-----------------------------------------------------

#--Declaración de la cola y el texto---------------------------
        queue = Rectangle(width=0.7, height=2.8, grid_xstep=1, grid_ystep=.7)
        queue.move_to([ 4, 0, 0])

        queuet = Text("Estado de la cola")
        queuet.scale(.4)
        queuet.move_to([ 4, 1.7, 0])
#-----------------------------------------------------

#--Declaración de la lista de visitados y el texto----
        visited = Rectangle(width=5.6, height=.7, grid_xstep=0.7, grid_ystep=1)
        visited.move_to([0,-2.6,0])

        vist = Text("Nodos visitados")
        vist.scale(.4)
        vist.move_to([-2, -2,0])
#-----------------------------------------------------


#--Declaración del nodo current y el texto------------
        curr = Rectangle(width=.7, height=.7)
        curr.move_to([4,-2.6, 0])

        currt = Text("Actual")
        currt.scale(.4)
        currt.move_to([4, -2,0])
        cur = VGroup(curr, currt)
#-----------------------------------------------------
        textos = VGroup(visited, vist, curr, currt, queue, queuet)

# ANIMACIONES
        self.play(Create(title))
        self.play(Create(grupoC))
        self.play(Create(textos))
        self.wait(1)
    
        
        self.play(ApplyMethod(root.set_color,YELLOW))
        mov = rootn.copy()
        mov.set_color(RED)
        self.play(ApplyMethod(mov.move_to, curr.get_center()))
        self.play(ApplyMethod(rootn.copy().move_to, [ -2.46, -2.6, 0]))
        self.play(ApplyMethod(linea2.set_color,YELLOW))
        self.play(ApplyMethod(linea1.set_color,YELLOW))
        
        self.play(ApplyMethod(circle2.set_color, BLUE))

        cola1 = number2.copy()
        cola2 = number1.copy()

        self.play(ApplyMethod(cola1.move_to, [ 4, -1.05, 0] ))
        self.play(ApplyMethod(number2.copy().move_to, [ -2.46 + 0.7, -2.6, 0] ))
        self.wait(1)
        
        self.play(ApplyMethod(circle1.set_color,BLUE))
        self.play(ApplyMethod(cola2.move_to, [ 4 , -0.35, 0] ))
        self.play(ApplyMethod(number1.copy().move_to, [ -1.76 + 0.7, -2.6, 0] ))
        self.wait(1)

        # Segundo ciclo
        # Normalizando de nuevo
        self.play(ApplyMethod(linea2.set_color,WHITE))
        self.play(ApplyMethod(linea1.set_color,WHITE))
        self.play(ApplyMethod(root.set_color,BLUE))
        self.play(ApplyMethod(mov.set_color,BLACK))
        # ----------------------------------------------

        self.play(ApplyMethod(circle2.set_color,YELLOW))
        mov = number2.copy()
        cola1.set_color(RED)
        self.play(ApplyMethod(cola2.move_to, cola1.get_center()))
        self.play(ApplyMethod(cola1.move_to, curr.get_center()))
        self.play(ApplyMethod(linea3.set_color,YELLOW))
        self.play(ApplyMethod(linea4.set_color,YELLOW))
        self.wait(1)

        self.play(ApplyMethod(circle3.set_color, BLUE))
        cola3 = number3.copy()
        self.play(ApplyMethod(cola3.move_to, [ 4, -1.05+0.7, 0] ))
        self.play(ApplyMethod(number3.copy().move_to, [ -1.76 + 1.4, -2.6, 0] ))
        self.wait(1)
        
        self.play(ApplyMethod(circle4.set_color,BLUE))
        cola4 = number4.copy()
        self.play(ApplyMethod(cola4.move_to, [ 4 , -1.05+1.4, 0] ))
        self.play(ApplyMethod(number4.copy().move_to, [ -1.76 + 2.1, -2.6, 0] ))
        self.wait(1)
        self.play(ApplyMethod(cola1.set_color,BLACK))

        # Tercera secuencia:

        # Normalizando de nuevo
        self.play(ApplyMethod(linea3.set_color,WHITE))
        self.play(ApplyMethod(linea4.set_color,WHITE))
        self.play(ApplyMethod(circle2.set_color,BLUE))
        # -----------

        self.play(ApplyMethod(circle1.set_color,YELLOW))
        cola2.set_color(RED)
        self.play(ApplyMethod(cola4.move_to,cola3.get_center()))
        self.play(ApplyMethod(cola3.move_to,cola2.get_center()))
        self.play(ApplyMethod(cola2.move_to,curr.get_center()))
        self.play(ApplyMethod(linea5.set_color,YELLOW))
        self.play(ApplyMethod(linea6.set_color,YELLOW))

        self.play(ApplyMethod(circle6.set_color,BLUE))
        cola5 = number6.copy()
        self.play(ApplyMethod(cola5.move_to,[ 4, -1.05 + 1.4, 0]))
        self.play(ApplyMethod(circle6.set_color,BLUE))
        self.play(ApplyMethod(number6.copy().move_to, [ -1.76 + 2.8, -2.6, 0] ))


        self.wait(1)

        cola6 = number5.copy()
        self.play(ApplyMethod(circle5.set_color,BLUE))
        self.play(ApplyMethod(cola6.move_to,[ 4, -1.05 + 2.1, 0]))
        self.play(ApplyMethod(number5.copy().move_to, [ -1.76 + 3.5, -2.6, 0] ))
        self.wait(1)

        # Animación 3
        # Normalizar de nuevo
        self.play(ApplyMethod(linea5.set_color,WHITE))
        self.play(ApplyMethod(linea6.set_color,WHITE))
        self.play(ApplyMethod(circle1.set_color,BLUE))
        self.wait(1)

        self.play(ApplyMethod(circle3.set_color, YELLOW))
        self.play(ApplyMethod(cola2.set_color , BLACK))

        cola2 = cola3
        cola3 = cola4

        self.play(ApplyMethod(cola6.move_to, cola5.get_center()))
        self.play(ApplyMethod(cola5.move_to, cola4.get_center()))
        self.play(ApplyMethod(cola4.move_to, cola3.get_center()))
        self.play(ApplyMethod(cola3.move_to, cola2.get_center()))
        self.play(ApplyMethod(cola2.move_to, curr.get_center()))
        self.play(ApplyMethod(cola2.set_color , RED))
        self.play(ApplyMethod(linea7.set_color, YELLOW))
        self.play(ApplyMethod(circle7.set_color, BLUE))

        cola7 = number7.copy()

        self.play(ApplyMethod(cola7.move_to,[ 4, -1.05 + 2.1, 0]))
        self.play(ApplyMethod(number7.copy().move_to, [ -1.76 + 4.2, -2.6, 0] ))

        self.wait(1)

        self.play(ApplyMethod(linea7.set_color,WHITE))
        self.play(ApplyMethod(circle3.set_color,BLUE))
        self.play(ApplyMethod(cola2.set_color , BLACK))

        self.play(ApplyMethod(cola7.move_to, [4, -0.35 + 0.7, 0]))
        self.play(ApplyMethod(cola6.move_to, [ 4, -1.05 + 0.7, 0] ))
        self.play(ApplyMethod(cola5.move_to, [ 4, -0.35 - 0.7 , 0] ))
        self.play(ApplyMethod(cola3.move_to, curr.get_center()))
        self.play(ApplyMethod(cola3.set_color , RED))
        self.play(Wiggle(cola3))

        self.wait(1)

        self.play(ApplyMethod(cola3.set_color , BLACK))

        self.play(ApplyMethod(cola7.move_to, [4, -0.35, 0]))
        self.play(ApplyMethod(cola6.move_to, [ 4, -1.05, 0] ))
        self.play(ApplyMethod(cola5.move_to, curr.get_center() ))
        self.play(ApplyMethod(cola5.set_color , RED))
        self.play(Wiggle(cola5))
        self.wait(1)

        self.play(ApplyMethod(cola5.set_color , BLACK))

        self.play(ApplyMethod(cola7.move_to, [4, -0.35-0.7, 0]))
        self.play(ApplyMethod(cola6.move_to, curr.get_center() ))
        self.play(ApplyMethod(cola6.set_color, RED ))
        self.play(Wiggle(cola6))
        self.wait(1)

        self.play(ApplyMethod(cola6.set_color, BLACK ))
        self.play(ApplyMethod(cola7.move_to, curr.get_center()))
        self.play(ApplyMethod(cola7.set_color, RED ))
        self.play(Wiggle(cola7))
        self.wait(1)
        self.play(ApplyMethod(cola7.set_color, BLACK ))
        self.wait(3)
