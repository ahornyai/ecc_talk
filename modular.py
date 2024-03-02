from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

# Some parts were taken from here: https://github.com/thud/eccdemo MIT License (credits for thud)

def modtxt(a,n,m=-1):
    if m == -1: m = a%n
    return Tex("$"+str(a)+" \equiv "+str(m)+" \ (\mathrm{mod}\ "+str(n)+")$")

class ModularScene(Slide):

    def construct(self):
        modular = Text("Modular arithmetic", color=YELLOW).scale(1.5)

        self.play(Write(modular))
        
        self.next_slide()
        
        fivemodthree = modtxt(5,3)
        
        self.play(
            modular.animate.move_to(3*UP).scale(2/3),
            Write(fivemodthree)
        )
        self.next_slide()

        a = 6
        for n in range(4,6):
            for i in range(2):
                self.play(Transform(fivemodthree,modtxt(a,n)))
                self.next_slide()
                
                a+=1

        self.play(Transform(
                fivemodthree,
                Tex("$a \equiv b \ (\mathrm{mod}\ n)$")
            ),
        )
        self.play(fivemodthree.animate.shift(UP))

        naturalnumbers = copy.deepcopy(fivemodthree)
        true_if = Tex("If $a-b$ = $kn$ where $k \\in \mathbb{Z}$").next_to(naturalnumbers, DOWN)

        self.play(Write(true_if))

        self.next_slide()

        self.play(Transform(naturalnumbers, Tex("$\mathbb{Z}/{n}\mathbb{Z} = \{ 0,1,2,...,n-2,n-1 \}$").next_to(true_if, DOWN)))


class ModularEquations(Slide):

    def construct(self):
        modular = Text("Equations", color=YELLOW).move_to(3*UP)

        self.play(Write(modular))

        inv_of_5 = modtxt("a*5", "14", "1")
        inv_of_5_sol = modtxt("3*5", "14", "1")
        inv_of_5_sym = modtxt("5^{-1}", "14", "3")
        
        self.play(
            Write(inv_of_5)
        )

        table_5 = IntegerTable([[i for i in range(14)], [5*i%14 for i in range(14)]], h_buff=1).scale(0.5).move_to(DOWN)
        self.play(FadeIn(table_5))
        
        self.next_slide()

        self.play(FadeOut(table_5))
        self.play(
            Transform(
                inv_of_5,
                inv_of_5_sol
            ),
        )

        self.next_slide()

        self.play(
            Transform(
                inv_of_5,
                inv_of_5_sym
            )
        )

        python_impl = Code(code="pow(5, -1, 14)", language="python", insert_line_no=False).next_to(inv_of_5, DOWN)

        self.play(FadeIn(python_impl, shift=DOWN))
        self.next_slide()

        inv_of_7 = modtxt("a*7", "14", "1")
        
        self.play(
            FadeOut(python_impl, shift=DOWN),
            Transform(
                inv_of_5,
                inv_of_7
            )
        )

        table_7 = IntegerTable([[i for i in range(14)], [7*i%14 for i in range(14)]], h_buff=1).scale(0.5).move_to(DOWN)
        self.play(FadeIn(table_7))

        self.next_slide()

        self.play(FadeOut(table_7))
        reason = Tex("$gcd(7, 14) = 7 \\neq 1$ $\\leftrightarrow$ no inverse :(").move_to(DOWN)

        self.play(Write(reason))

        self.next_slide()

        self.play(FadeOut(reason), FadeOut(inv_of_5))

        nisprime = Tex("$n = p$").scale(2)

        self.play(
            Write(nisprime),
        )
