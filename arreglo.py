from manim import *

class Array(MovingCameraScene):
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
        text = Text("Con un bucle empezamos a agregar elementos de izquiera a derecha")
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
        text = Text("Stack de nuestro programa")
        text.scale(.4)
        text.move_to(stack.get_center() + [0, 2.5, 0])
        ta = Text(" Esta es la representación de nuestro arreglo en memoria\n Podemos darnos cuenta que es imposible para nosotros\n acceder a un índice mayor al número de elementos de\n nuestro arreglo, pues provocaremos comportamiento\n indefinido")
        ta.scale(.4)
        ta.move_to(text4.get_center() + [1.5, 0, 0])
        st = VGroup(stack, text1, type1, text2, type2, text3, type3, text4, type4, text5, type5, text6, type6, text7, type7, text8, type8)
        cuad = Rectangle(color=BLUE, height=1.7, width=3.2)
        cuad.move_to([st.get_x()-2, text4.get_y() -.095, 0])
        self.play(Create(text), Create(ta), Create(cuad), ApplyMethod(st.shift, LEFT * 2))
        self.wait(3)
