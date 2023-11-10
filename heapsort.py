from manim import *

class HeapSort(MovingCameraScene):
    def construct(self):
        title = Title("Algoritmo Heap Sort")
        self.play(Create(title))
        self.camera.frame.save_state()

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

#-------Lineas desde nodo 2 a nodos 5 y 6---------------------
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
        lgroup = VGroup(linea1,linea2,linea3,linea4,linea5,linea6, linea7) 
        grupoC = VGroup(rootg, cgroup1, cgroup2, cgroup3, cgroup4, cgroup5, cgroup6, cgroup7, lgroup)

        cuadrado = Rectangle(color=WHITE, height=.7, width=5.6, grid_xstep=.7)
        cuadrado.move_to([0,0,0]);
        
        numero1 = MathTex("1")
        numero1.move_to([5.6/2 - 5.6 + 0.35 ,0,0])
        numero2 = MathTex("6")
        numero2.move_to([5.6/2 - 4.9 + 0.35 ,0,0])
        numero3 = MathTex("3")
        numero3.move_to([5.6/2 - 4.2 + 0.35 ,0,0])
        numero4 = MathTex("2")
        numero4.move_to([5.6/2 - 3.5 + 0.35 ,0,0])
        numero5 = MathTex("8")
        numero5.move_to([5.6/2 - 2.8 + 0.35 ,0,0])
        numero6 = MathTex("5")
        numero6.move_to([5.6/2 - 2.1 + 0.35 ,0,0])
        numero7 = MathTex("4")
        numero7.move_to([5.6/2 - 1.4 + 0.35 ,0,0])
        numero8 = MathTex("7")
        numero8.move_to([5.6/2 - 0.7 + 0.35 ,0,0])


        grupoC.shift(DOWN * 2)


        sp1 = numero1.get_center() + np.array(  [0, 0.35, 0])
        ep1 = numero2.get_center() + np.array(  [0, 0.35, 0])  
        cw1 = ArcBetweenPoints(sp1, ep1, angle= -TAU/4)
        dw1 = Dot(ep1, color=BLUE, radius=0.03)

        ep2 = numero3.get_center() + np.array(  [0, 0.35, 0])  
        cw2 = ArcBetweenPoints(sp1, ep2, angle= -TAU/4)
        dw2 = Dot(ep2, color=RED, radius=0.03)

        sp3 = numero4.get_center() + np.array(  [0, -0.35, 0])
        ep1 = numero2.get_center() + np.array(  [0, -0.35, 0])  
        cw3 = ArcBetweenPoints(ep1, sp3, angle= TAU/4)
        dw3 = Dot(sp3, color=BLUE, radius=0.03)

        sp4 = numero5.get_center() + np.array(  [0, -0.35, 0])  
        cw4 = ArcBetweenPoints(ep1, sp4, angle= TAU/4)
        dw4 = Dot(sp4, color=RED, radius=0.03)

        ep2 = numero3.get_center() + np.array(  [0.04, 0.35, 0])  
        sp5 = numero6.get_center() + np.array(  [0, 0.35, 0])
        cw5 = ArcBetweenPoints(ep2, sp5, angle= -TAU/4)
        dw5 = Dot(sp5, color=BLUE, radius=0.03)

        sp6 = numero7.get_center() + np.array(  [0, 0.35, 0])
        cw6 = ArcBetweenPoints(ep2, sp6, angle= -TAU/4)
        dw6 = Dot(sp6, color=RED, radius=0.03)

        ep7 = numero8.get_center() + np.array(  [0, -0.35, 0])
        cw7 = ArcBetweenPoints(sp3, ep7, angle= TAU/4)
        dw7 = Dot(ep7, color=BLUE, radius=0.03)


        lista = VGroup(cuadrado, numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8)

        no = VGroup(cw1,dw1,cw2,dw2,cw3,dw3,cw4,dw4,cw5,dw5, cw6, dw6, cw7, dw7)


        self.play(Create(lista))

        self.play(self.camera.frame.animate.scale(0.5).move_to(cuadrado))
        self.wait(1)
        self.play(Create(no))
        self.play(Restore(self.camera.frame))
        cuad = VGroup(lista,no)
        self.play(Transform(cuad, grupoC))

        cuadrado = Rectangle(color=WHITE, height=.7, width=5.6, grid_xstep=.7)
        cuadrado.move_to([0,0,0]);
        
        numero1 = MathTex("1")
        numero1.move_to([5.6/2 - 5.6 + 0.35 ,0,0])
        numero2 = MathTex("6")
        numero2.move_to([5.6/2 - 4.9 + 0.35 ,0,0])
        numero3 = MathTex("3")
        numero3.move_to([5.6/2 - 4.2 + 0.35 ,0,0])
        numero4 = MathTex("2")
        numero4.move_to([5.6/2 - 3.5 + 0.35 ,0,0])
        numero5 = MathTex("8")
        numero5.move_to([5.6/2 - 2.8 + 0.35 ,0,0])
        numero6 = MathTex("5")
        numero6.move_to([5.6/2 - 2.1 + 0.35 ,0,0])
        numero7 = MathTex("4")
        numero7.move_to([5.6/2 - 1.4 + 0.35 ,0,0])
        numero8 = MathTex("7")
        numero8.move_to([5.6/2 - 0.7 + 0.35 ,0,0])


        lista = VGroup(cuadrado, numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8)
        arrt = Text("Vista del arreglo:")

        lista.shift(DOWN * 3)
        arrt.move_to(lista.get_center() + [-1.95,0.6,0])
        arrt.scale(0.4)

        tformula = MathTex(r"\text{Pivote (} k \text{):}")
        tformula.move_to(lista.get_center() + [3.6, 0, 0])
        tformula.scale(0.6)
        formula = MathTex(r"\Bigl \lfloor \frac{n}{2} \Bigr\rfloor \text{ }n = |V(G)|, \text{ }k=4")
        formula.move_to(lista.get_center() + [5.9, 0, 0])
        formula.scale(0.6)
        paq = VGroup(tformula, formula)
        lista.shift(LEFT * 2)
        arrt.shift(LEFT * 2)
        paq.shift(LEFT * 2)

        self.play(Create(lista))
        self.play(Create(arrt))
        self.play(Create(paq))
        self.wait(1)

        max_heapify = Text("Algoritmo Max Heapify")
        max_heapify.move_to([-3.4,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-1.4,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # Animación max heapify índice 4 del arreglo
        self.remove(tformula)
        self.remove(formula)
        self.remove(cuad)
        self.add(grupoC)
        
        circle3.save_state()
        circle7.save_state()
        linea7.save_state()

        # Estados originales segunda animación:
        circle1.save_state()
        linea5.save_state()
        circle5.save_state()
        linea6.save_state()
        circle6.save_state()

        k = MathTex("k")
        k.move_to([5.6/2 - 3.5 + 0.35 ,-0.3,0])
        k.shift(DOWN*2)
        k.scale(0.6)
        dotk = Dot(color=RED);
        dotk.move_to([5.6/2 - 3.5 + 0.35 ,-0.5,0])
        dotk.shift(DOWN*2)
        dotk.scale(0.4)

        # ----- Primera animación
        self.play(Create(dotk),Create(k),
                  lista.animate.shift(RIGHT * 2),
                  arrt.animate.shift(RIGHT * 0.5),
                  arrt.animate.shift(DOWN * 0.6),
                  ApplyMethod(circle3.set_color,YELLOW),
                  ApplyMethod(linea7.set_color,YELLOW),
                  ApplyMethod(circle7.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea7))
        self.play(Swap(number3, number7))
        self.wait(2)
        self.play(Restore(circle3), Restore(circle7), Restore(linea7))
        self.play(Restore(self.camera.frame))

        self.play(Swap(numero4, numero8))

        self.play(ApplyMethod(k.move_to,k.get_center() + [-0.7,0,0]),)
        self.play(ApplyMethod(dotk.move_to,dotk.get_center() + [-0.7,0,0]))

        self.wait(2)

        # ------ Siguiente animación

        self.play(ApplyMethod(circle1.set_color,YELLOW),
                  ApplyMethod(linea5.set_color,YELLOW),
                  ApplyMethod(circle6.set_color, YELLOW))


        self.play(self.camera.frame.animate.scale(0.5).move_to(linea5))
        self.wait(2)
        self.play(Restore(circle1), Restore(circle6), Restore(linea5))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(circle1.set_color,YELLOW),
                  ApplyMethod(linea6.set_color,YELLOW),
                  ApplyMethod(circle5.set_color, YELLOW))


        self.play(self.camera.frame.animate.scale(0.5).move_to(linea6))
        self.wait(2)
        self.play(Restore(circle1), Restore(circle5), Restore(linea6))
        self.play(Restore(self.camera.frame))
        self.play(Swap(number1, number5))

        # --- Manipulación de la lista
        self.play(Swap(numero3, numero6))

        self.play(ApplyMethod(k.move_to,k.get_center() + [-0.7,0,0]),)
        self.play(ApplyMethod(dotk.move_to,dotk.get_center() + [-0.7,0,0]))
        self.wait(2)

        # ------ Siguiente animación (animación 3)
        circle2.save_state()
        circle3.save_state()
        linea4.save_state()

        circle4.save_state()
        linea3.save_state()

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea4.set_color,YELLOW),
                  ApplyMethod(circle3.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea4))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle3), Restore(linea4))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea3.set_color,YELLOW),
                  ApplyMethod(circle4.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea3))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle4), Restore(linea3))
        self.play(Restore(self.camera.frame))
        self.play(Swap(number2, number4))

        # --- Manipulación de la lista
        self.play(Swap(numero2, numero5))

        self.play(ApplyMethod(k.move_to,k.get_center() + [-0.7,0,0]))
        self.play(ApplyMethod(dotk.move_to,dotk.get_center() + [-0.7,0,0]))
        self.wait(2)

        # ------ Siguiente animación (animación 4)
        root.save_state()
        circle2.save_state()
        linea1.save_state()

        circle1.save_state()
        linea2.save_state()

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea1.set_color,YELLOW),
                  ApplyMethod(circle2.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea1))
        self.wait(2)
        self.play(Restore(root), Restore(circle2), Restore(linea1))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea2.set_color,YELLOW),
                  ApplyMethod(circle1.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea2))
        self.wait(2)
        self.play(Restore(root), Restore(circle1), Restore(linea2))
        self.play(Restore(self.camera.frame))
        self.play(Swap(rootn, number4))

        # --- Manipulación de la lista
        self.play(Swap(numero1, numero5))

        self.wait(2)

        # ------ Siguiente animación (animación 5)
        self.play(self.camera.frame.animate.scale(0.5).move_to(circle2))
        self.play(Restore(self.camera.frame))

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea4.set_color,YELLOW),
                  ApplyMethod(circle3.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea4))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle3), Restore(linea4))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea3.set_color,YELLOW),
                  ApplyMethod(circle4.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea3))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle4), Restore(linea3))
        self.play(Restore(self.camera.frame))
        self.play(Swap(rootn, number7))

        # --- Manipulación de la lista
        self.play(Swap(numero1, numero8))

        self.wait(2)

        # --- Ultima animación, cambio posiciones del 2 por el 1

        self.play(self.camera.frame.animate.scale(0.5).move_to(circle3))
        self.play(Restore(self.camera.frame))

        self.play(ApplyMethod(circle3.set_color,YELLOW),
                  ApplyMethod(linea7.set_color,YELLOW),
                  ApplyMethod(circle7.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea7))
        self.wait(2)
        self.play(Restore(circle3), Restore(circle7), Restore(linea7))
        self.play(Restore(self.camera.frame))
        self.play(Swap(rootn, number3))

        self.play(Swap(numero1, numero4))
        self.remove(k)
        self.remove(dotk)

        self.wait(2)

        # --- Titulo mover la cima al final
        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Mover la cima al final y reducir el tamaño de la lista en una unidad")
        max_heapify.move_to([-1.2,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-3.62,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # --- Mover la cima al final

        self.play(Swap(numero5, numero1))
        self.play(Swap(rootn, number4))
        self.play(ApplyMethod(circle7.set_color, PURPLE_D))

        # Hacer Max heapify 

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Algoritmo Max Heapify desde la cima")
        max_heapify.move_to([-2.65,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-2.15,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # Algoritmo max heapify desde la cima (1)

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea1.set_color,YELLOW),
                  ApplyMethod(circle2.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea1))
        self.wait(2)
        self.play(Restore(root), Restore(circle2), Restore(linea1))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea2.set_color,YELLOW),
                  ApplyMethod(circle1.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea2))
        self.wait(2)
        self.play(Restore(root), Restore(circle1), Restore(linea2))
        self.play(Restore(self.camera.frame))
        self.play(Swap(rootn, number7))

        # --- Manipulación de la lista
        self.play(Swap(numero1, numero8))

        self.wait(2)

        # ------ Siguiente animación cambio de posicion del 1 con el 6
        self.play(self.camera.frame.animate.scale(0.5).move_to(circle2))
        self.play(Restore(self.camera.frame))

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea4.set_color,YELLOW),
                  ApplyMethod(circle3.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea4))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle3), Restore(linea4))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea3.set_color,YELLOW),
                  ApplyMethod(circle4.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea3))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle4), Restore(linea3))
        self.play(Restore(self.camera.frame))
        self.play(Swap(rootn, number2))

        # --- Manipulación de la lista
        self.play(Swap(numero1, numero2))

        self.wait(2)

        # --- Mover la cima al final

        self.play(Swap(number6, number7))
        self.play(Swap(numero8, numero7))
        self.play(ApplyMethod(circle6.set_color, PURPLE_D))

        # Algoritmo max heapify desde la cima (4)

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea1.set_color,YELLOW),
                  ApplyMethod(circle2.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea1))
        self.wait(2)
        self.play(Restore(root), Restore(circle2), Restore(linea1))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea2.set_color,YELLOW),
                  ApplyMethod(circle1.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea2))
        self.wait(2)
        self.play(Restore(root), Restore(circle1), Restore(linea2))
        self.play(Restore(self.camera.frame))
        self.play(Swap(number6, number2))

        # --- Manipulación de la lista
        self.play(Swap(numero7, numero2))

        # ------ Siguiente animación (4) sin cambio de posicion

        self.play(self.camera.frame.animate.scale(0.5).move_to(circle2))
        self.play(Restore(self.camera.frame))

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea4.set_color,YELLOW),
                  ApplyMethod(circle3.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea4))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle3), Restore(linea4))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea3.set_color,YELLOW),
                  ApplyMethod(circle4.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea3))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle4), Restore(linea3))
        self.play(Restore(self.camera.frame))

        self.wait(2)

        # --- Titulo mover la cima al final

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Mover la cima al final y reducir el tamaño de la lista en una unidad")
        max_heapify.move_to([-1.2,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-3.62,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # --- Mover la cima al final

        self.play(Swap(numero2, numero3))
        self.play(Swap(number2, number1))
        self.play(ApplyMethod(circle5.set_color, PURPLE_D))

        # Hacer Max heapify 

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Algoritmo Max Heapify desde la cima")
        max_heapify.move_to([-2.65,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-2.15,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # Algoritmo max heapify desde la cima (3)
        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea1.set_color,YELLOW),
                  ApplyMethod(circle2.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea1))
        self.wait(2)
        self.play(Restore(root), Restore(circle2), Restore(linea1))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea2.set_color,YELLOW),
                  ApplyMethod(circle1.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea2))
        self.wait(2)
        self.play(Restore(root), Restore(circle1), Restore(linea2))
        self.play(Restore(self.camera.frame))
        self.play(Swap(number1, number5))

        # --- Manipulación de la lista
        self.play(Swap(numero3, numero6))

        self.wait(2)

        # --- Titulo mover la cima al final

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Mover la cima al final y reducir el tamaño de la lista en una unidad")
        max_heapify.move_to([-1.2,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-3.62,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # --- Mover la cima al final

        self.play(Swap(numero1, numero6))
        self.play(Swap(rootn, number5))
        self.play(ApplyMethod(circle4.set_color, PURPLE_D))

        # Hacer Max heapify 

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Algoritmo Max Heapify desde la cima")
        max_heapify.move_to([-2.65,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-2.15,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # Algoritmo max heapify desde la cima (1)
        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea1.set_color,YELLOW),
                  ApplyMethod(circle2.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea1))
        self.wait(2)
        self.play(Restore(root), Restore(circle2), Restore(linea1))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea2.set_color,YELLOW),
                  ApplyMethod(circle1.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea2))
        self.wait(2)
        self.play(Restore(root), Restore(circle1), Restore(linea2))
        self.play(Restore(self.camera.frame))
        self.play(Swap(rootn, number6))

        # --- Manipulación de la lista
        self.play(Swap(numero1, numero7))

        # ------ Siguiente animación cambio de posicion del 1 con el 2
        self.play(self.camera.frame.animate.scale(0.5).move_to(circle2))
        self.play(Restore(self.camera.frame))

        self.play(ApplyMethod(circle2.set_color,YELLOW),
                  ApplyMethod(linea4.set_color,YELLOW),
                  ApplyMethod(circle3.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea4))
        self.play(Swap(rootn, number3))
        self.wait(2)
        self.play(Restore(circle2), Restore(circle3), Restore(linea4))
        self.play(Restore(self.camera.frame))

        # --- Manipulación de la lista
        self.play(Swap(numero1, numero4))
        self.wait(2)

        # --- Titulo mover la cima al final
        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Mover la cima al final y reducir el tamaño de la lista en una unidad")
        max_heapify.move_to([-1.2,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-3.62,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # --- Mover la cima al final

        self.play(Swap(numero7, numero1))
        self.play(Swap(rootn, number6))
        self.play(ApplyMethod(circle3.set_color, PURPLE_D))

        # Hacer Max heapify 

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Algoritmo Max Heapify desde la cima")
        max_heapify.move_to([-2.65,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-2.15,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # Algoritmo max heapify desde la cima (1)

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea1.set_color,YELLOW),
                  ApplyMethod(circle2.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea1))
        self.wait(2)
        self.play(Restore(root), Restore(circle2), Restore(linea1))
        self.play(Restore(self.camera.frame))

        # --- Camara a la derecha

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea2.set_color,YELLOW),
                  ApplyMethod(circle1.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea2))
        self.wait(2)
        self.play(Restore(root), Restore(circle1), Restore(linea2))
        self.play(Restore(self.camera.frame))
        self.play(Swap(rootn, number1))

        # --- Manipulación de la lista
        self.play(Swap(numero1, numero3))

        self.wait(2)

        # --- Titulo mover la cima al final
        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Mover la cima al final y reducir el tamaño de la lista en una unidad")
        max_heapify.move_to([-1.2,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-3.62,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # --- Mover la cima al final

        self.play(Swap(numero3, numero1))
        self.play(Swap(rootn, number1))
        self.play(ApplyMethod(circle1.set_color,PURPLE_D))

        # Hacer Max heapify 

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Algoritmo Max Heapify desde la cima")
        max_heapify.move_to([-2.65,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-2.15,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # Algoritmo max heapify desde la cima (1)

        self.play(ApplyMethod(root.set_color,YELLOW),
                  ApplyMethod(linea1.set_color,YELLOW),
                  ApplyMethod(circle2.set_color, YELLOW))

        self.play(self.camera.frame.animate.scale(0.5).move_to(linea1))
        self.play(Swap(rootn, number3))
        self.wait(2)
        self.play(Restore(root), Restore(circle2), Restore(linea1))
        self.play(Restore(self.camera.frame))
        self.play(Swap(numero4, numero1))
        self.wait(2)

        # --- Titulo mover la cima al final
        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Mover la cima al final y reducir el tamaño de la lista en una unidad")
        max_heapify.move_to([-1.2,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-3.62,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # --- Mover la cima al final

        self.play(Swap(numero4, numero1))
        self.play(Swap(rootn, number3))
        self.play(ApplyMethod(circle2.set_color,PURPLE_D))

        # Hacer Max heapify 

        self.remove(max_heapify)
        self.remove(dot)
        max_heapify = Text("Algoritmo Max Heapify desde la cima")
        max_heapify.move_to([-2.65,2,0])
        dot = Dot(color=RED)
        dot.scale(0.4)
        dot.move_to(max_heapify.get_center() + [-2.15,0,0])
        max_heapify.scale(0.4)
        self.play(Create(max_heapify),Create(dot))
        self.play(Flash(dot, color=RED, flash_radius=0.1))

        # Algoritmo max heapify desde la cima (1)

        self.play(ApplyMethod(root.set_color,YELLOW))
        self.play(self.camera.frame.animate.scale(0.5).move_to(rootn))
        self.play(Restore(self.camera.frame))
        self.play(Flash(
            root, line_length=1,
            num_lines=30, color=YELLOW,
            flash_radius= 0.5 + SMALL_BUFF,
            time_width=0.3, run_time=2,
            rate_func = rush_from
        ))
        self.play(ApplyMethod(root.set_color,PURPLE_D))
        self.remove(lista)
        self.remove(lista)
        self.remove(max_heapify)
        self.remove(dot)
        self.remove(cuad)
        self.remove(arrt)
        self.play(Transform(grupoC, lista))
        self.remove(grupoC)
        self.play(lista.animate.shift(UP * 3))
        self.wait(3)
