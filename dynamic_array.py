from manim import *

class DynamicArray(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        rect = Rectangle(color=WHITE, height=.7, width=5.6, grid_xstep=.7)
        #self.play(Create(rect))
        text = Text("Se declara un arreglo de 8 elementos, vacio")
        text.scale(.4)
        grupo = VGroup(rect, text)
        text.move_to([0,rect.get_y()+1,0])
        self.play(Create(grupo))
        self.wait(1)
        # ------
        self.remove(text)
        text = Text("Con un bucle empezamos a agregar elementos de izquierda a derecha")
        text.scale(.4)
        text.move_to([0,rect.get_y()+1,0])
        numero1 = MathTex("1")
        numero1.move_to(rect.get_center() + [-(.7*3)-.35,0,0])
        self.play(Create(text))
        self.play(Create(numero1))

        #----
        numero2 = MathTex("2")
        numero2.move_to(rect.get_center() + [-(.7*2)-.35,0,0])
        self.play(Create(numero2))

        numero3 = MathTex("3")
        numero3.move_to(rect.get_center() + [-(.7)-.35,0,0])
        self.play(Create(numero3))

        numero4 = MathTex("4")
        numero4.move_to(rect.get_center() + [-0.35,0,0])
        self.play(Create(numero4))

        numero5 = MathTex("5")
        numero5.move_to(rect.get_center() + [.35,0,0])
        self.play(Create(numero5))

        numero6 = MathTex("6")
        numero6.move_to(rect.get_center() + [+(.7)+.35,0,0])
        self.play(Create(numero6))

        numero7 = MathTex("7")
        numero7.move_to(rect.get_center() + [+(.7*2)+.35,0,0])
        self.play(Create(numero7))

        numero8 = MathTex("8")
        numero8.move_to(rect.get_center() + [(.7*3)+.35,0,0])
        self.play(Create(numero8))
        self.remove(text)
        grupo = VGroup(rect, numero1,  numero2, numero3, numero4, numero5, numero6, numero7, numero8)
        self.play(ApplyMethod(grupo.shift, DOWN * 3))
        self.play(ApplyMethod(grupo.scale,  .8))

        stack = Rectangle(color=WHITE, height=4, width=3, grid_xstep=3, grid_ystep=.2)
        #-----
        text1 = Text("0xkjfafkj")
        text1.scale(.2)
        text1.move_to(stack.get_center() + [1.2,(0.2*8)+.1,0])

        type1 = Text("int")
        type1.scale(.2)
        type1.move_to(stack.get_center() + [-1.3,(0.2*8)+.1,0])
        g = VGroup(type1, text1)
        #-----

        self.play(Create(stack))
        self.play(Create(g))

        #-----
        text2 = Text("0xkjfafkj")
        text2.scale(.2)
        text2.move_to(stack.get_center() + [1.2,(0.2*7)+.1,0])

        type2 = Text("int")
        type2.scale(.2)
        type2.move_to(stack.get_center() + [-1.3,(0.2*7)+.1,0])
        self.play(Create(text2),Create( type2))
        #-----

        #-----
        text3 = Text("0xkjfafkj")
        text3.scale(.2)
        text3.move_to(stack.get_center() + [1.2,(0.2*6)+.1,0])

        type3 = Text("int")
        type3.scale(.2)
        type3.move_to(stack.get_center() + [-1.3,(0.2*6)+.1,0])
        self.play(Create(text3),Create( type3))

        #-----
        #-----
        text4 = Text("0xkjfafkj")
        text4.scale(.2)
        text4.move_to(stack.get_center() + [1.2,(0.2*5)+.1,0])

        type4 = Text("int")
        type4.scale(.2)
        type4.move_to(stack.get_center() + [-1.3,(0.2*5)+.1,0])
        self.play(Create(text4),Create( type4))
        #-----
        #-----
        text5 = Text("0xkjfafkj")
        text5.scale(.2)
        text5.move_to(stack.get_center() + [1.2,(0.2*4)+.1,0])

        type5 = Text("int")
        type5.scale(.2)
        type5.move_to(stack.get_center() + [-1.3,(0.2*4)+.1,0])
        self.play(Create(text5),Create( type5))
        #-----
        #-----
        text6 = Text("0xkjfafkj")
        text6.scale(.2)
        text6.move_to(stack.get_center() + [1.2,(0.2*3)+.1,0])

        type6 = Text("int")
        type6.scale(.2)
        type6.move_to(stack.get_center() + [-1.3,(0.2*3)+.1,0])
        self.play(Create(text6),Create( type6))
        #-----
        #-----
        text7 = Text("0xkjfafkj")
        text7.scale(.2)
        text7.move_to(stack.get_center() + [1.2,(0.2*2)+.1,0])

        type7 = Text("int")
        type7.scale(.2)
        type7.move_to(stack.get_center() + [-1.3,(0.2*2)+.1,0])
        self.play(Create(text7),Create( type7))
        #-----
        #-----
        text8 = Text("0xkjfafkj")
        text8.scale(.2)
        text8.move_to(stack.get_center() + [1.2,(0.2)+.1,0])

        type8 = Text("int")
        type8.scale(.2)
        type8.move_to(stack.get_center() + [-1.3,(0.2)+.1,0])
        self.play(Create(text8),Create( type8))
        #-----

        self.play(self.camera.frame.animate.scale(0.6).move_to(text4))
        self.wait(2)
        self.play(Restore(self.camera.frame))
        text = Text("Heap de nuestro programa")
        text.scale(.4)
        text.move_to(stack.get_center() + [0, 2.5, 0])
        ta = Text(" Esta es la representación de nuestro arreglo dínamico\n en memoria, hasta el momento no hay núnguna diferencia\n con el arreglo sencillo, veamos que sucede al tratar de agregar\n un elemento al final del arreglo.")
        ta.scale(.4)
        ta.move_to(text4.get_center() + [2, 0, 0])
        st = VGroup(stack, text1, type1, text2, type2, text3, type3, text4, type4, text5, type5, text6, type6, text7, type7, text8, type8)
        cuad = Rectangle(color=BLUE, height=1.7, width=3.2)
        cuad.move_to([st.get_x()-2, text4.get_y() -.095, 0])
        self.play(Create(text), Create(ta), Create(cuad), ApplyMethod(st.shift, LEFT * 2))
        self.wait(4)
        self.remove(cuad, ta, st)
        grupo.scale(.7)
        self.play(ApplyMethod(grupo.shift, UP * 3))

        nt = Text("Visualización del heap como una cinta")  
        nt.scale(.6)
        nt.move_to(text.get_center())
        self.play(ReplacementTransform(text, nt))
        rect1 = Rectangle(color=WHITE, height=.7, width=6.3, grid_xstep=.7)
        rect1.scale(.8)
        rect1.scale(.7)
        rect1.next_to(grupo, RIGHT)
        rect2 = Rectangle(color=WHITE, height=.7, width=6.3, grid_xstep=.7)
        rect2.scale(.8)
        rect2.scale(.7)
        rect2.next_to(grupo, LEFT)
        tt = Text("Todos los campos coloreados son campos ocupados")  
        tt.scale(.4)
        tt.move_to(grupo.get_center() + [0,-2,0])
        self.play(Create(rect1), Create(rect2), Write(tt))
        # TODO, hacer que los cuadros tengan color 

        # Ahora sigue llamar a calloc()
        llamada = Text("Llamada a calloc()\nBuscará el espacio en el heap y reubicará el arreglo")
        llamada.scale(.4)
        llamada.move_to(tt.get_center())
        self.play(ReplacementTransform(tt, llamada))
        #self.play(ApplyMethod(numero1.shift, RIGHT))
        # TODO: Cambiar de color cuando se encuentre el espacio
        self.wait(2)
        enc = Text("Espacio encontrado")
        enc.scale(.4)
        enc.move_to(llamada.get_center())
        print(numero1.get_center())
        print(numero2.get_center())
        print(numero3.get_center())

        self.play(ReplacementTransform(llamada, enc))

        self.play(ApplyMethod(numero1.move_to, rect1.get_center() + [-(.392*2)-(.392*2),0,0]))
        #----
        self.play(ApplyMethod(numero2.move_to, rect1.get_center() + [-(.392)-(.392*2),0,0]))

        self.play(ApplyMethod(numero3.move_to, rect1.get_center() + [-(.392*2),0,0]))

        self.play(ApplyMethod(numero4.move_to, rect1.get_center() + [(.392)-(.392*2),0,0]))

        self.play(ApplyMethod(numero5.move_to, rect1.get_center()))

        self.play(ApplyMethod(numero6.move_to, rect1.get_center() + [(.392),0,0]))

        self.play(ApplyMethod(numero7.move_to, rect1.get_center() + [(.392)+(.392),0,0]))

        self.play(ApplyMethod(numero8.move_to, rect1.get_center() + [(.392*2)+(.392),0,0]))

        numero9 = MathTex("9")
        numero9.scale(.8)
        numero9.scale(.7)
        numero9.set_color(RED)
        self.play(ApplyMethod(numero9.move_to, numero8.get_center() + [0.392, 0, 0]))
        ag = Text("Agregado con éxito")
        ag.scale(.4)
        ag.move_to(enc.get_center())
        self.play(ReplacementTransform(enc, ag))

        self.wait(3)
