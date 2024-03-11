from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

class ECDSAScene(Slide):

    def construct(self):
        title = Text("Elliptic Curve Digital Signature Algorithm")

        self.play(Write(title))

        self.next_slide()

        self.play(title.animate.move_to(3*UP))
        self.wait(0.1)
        self.play(Transform(title, Text("ECDSA").move_to(3*UP)))

        r = Tex("$r \equiv [k*G]_x \ (\mathrm{mod}\ q)$").move_to(0.5*UP).set_color(YELLOW)
        s = Tex("$s \equiv k^{-1} * (h + r*d) \ (\mathrm{mod}\ q)$").move_to(0.2*DOWN).set_color(YELLOW) # 0.7 y difference

        self.play(Write(r), Write(s))

        self.next_slide()

        self.play(r.animate.move_to(2*UP), s.animate.move_to(1.3*UP))

        q = Text("q - generator point's order, must be prime").scale(0.5)
        k = Text("k - nonce").scale(0.5).move_to(3*LEFT + 0.5*DOWN)
        point_G = Text("G - generator point on a curve").scale(0.5).move_to(2*RIGHT + 0.5*DOWN)
        h = Text("h - hash digest").scale(0.5).move_to(1.5*RIGHT + 1*DOWN)
        d = Text("d - private key").scale(0.5).move_to(3*LEFT + 1*DOWN)

        self.play(Write(q), Write(k), Write(point_G), Write(h), Write(d))

        self.next_slide()

        self.play(Write(Text("Attack surface?").set_color(YELLOW).move_to(2*DOWN)))
        self.wait(0.1)
        self.play(Write(SurroundingRectangle(k, buff=0.07)), Write(SurroundingRectangle(point_G, buff=0.07)), Write(SurroundingRectangle(h, buff=0.07)))

class CurveballScene(Slide): # TODO

    def construct(self):
        title = Text("Curveball - CVE-2020-0601")

class RepeatedNonceScene(Slide):

    def construct(self):
        title = Text("The classical repeated nonce attack").move_to(3*UP)
        r_1 = Tex("$r_1 \equiv [k*G]_x (\mathrm{mod}\ q)$").move_to(0.5*UP + 3*LEFT).set_color(YELLOW).scale(0.7)
        s_1 = Tex("$s_1 \equiv$", "$\ k^{-1} *$", "$\ (h_1 + r*d) \ (\mathrm{mod}\ q)$").move_to(0.2*DOWN + 3*LEFT).set_color(YELLOW).scale(0.7)
        r_2 = Tex("$r_2 \equiv [k*G]_x (\mathrm{mod}\ q)$").move_to(0.5*UP + 3*RIGHT).set_color(YELLOW).scale(0.7)
        s_2 = Tex("$s_2 \equiv$", "$\ k^{-1} *$", "$\ (h_2 + r*d) \ (\mathrm{mod}\ q)$").move_to(0.2*DOWN + 3*RIGHT).set_color(YELLOW).scale(0.7)

        self.play(Write(title), Write(r_1), Write(s_1), Write(r_2), Write(s_2))

        self.next_slide()

        self.play(FadeOut(r_1, shift=DOWN), FadeOut(r_2, shift=DOWN))
        self.play(s_1.animate.move_to(UP), s_2.animate.move_to(ORIGIN))

        s_1_1 = Tex("$s_1 * k \equiv $", "$\ (h_1 + r*d) \ (\mathrm{mod}\ q)$").move_to(UP).set_color(YELLOW)
        s_1_2 = Tex("$k \equiv $", "$\ s_1^{-1} * \ $", "$ (h_1 + r*d) \ (\mathrm{mod}\ q)$").move_to(UP).set_color(YELLOW)

        s_2_1 = Tex("$s_2 * k \equiv $", "$\ (h_2 + r*d) \ (\mathrm{mod}\ q)$").set_color(YELLOW)
        s_2_2 = Tex("$s_2 *$", "$\ s_1^{-1}*(h_1 + r*d) \ $", "$ \equiv $", "$\ (h_2 + r*d) \ (\mathrm{mod}\ q)$").set_color(YELLOW)
        s_2_3 = Tex("$s_2 *(h_1 + r*d) \ $", "$ \equiv $", "$\ s_1*(h_2 + r*d) \ (\mathrm{mod}\ q)$").set_color(YELLOW)
        s_2_4 = Tex("$s_2 * h_1 + s_2*r*d \ $", "$ \equiv $", "$\ s_1*h_2 + s_1*r*d \ (\mathrm{mod}\ q)$").set_color(YELLOW)
        s_2_5 = Tex("$s_2 * h_1 - s_1*h_2 \ $", "$ \equiv $", "$\ s_1*r*d - s_2*r*d \ (\mathrm{mod}\ q)$").set_color(YELLOW)
        s_2_6 = Tex("$s_2 * h_1 - s_1*h_2 \ $", "$ \equiv $", "$\ d*(s_1*r - s_2*r) \ (\mathrm{mod}\ q)$").set_color(YELLOW)
        s_2_7 = Tex("$(s_2 * h_1 - s_1*h_2)*(s_1*r - s_2*r)^{-1} \ $", "$ \equiv $", "$\ d \ (\mathrm{mod}\ q)$").set_color(YELLOW)

        self.next_slide()
        self.play(TransformMatchingTex(s_1, s_1_1), TransformMatchingTex(s_2, s_2_1))

        self.next_slide()
        self.play(TransformMatchingTex(s_1_1, s_1_2))

        self.next_slide()
        self.play(TransformMatchingTex(s_2_1, s_2_2))
        
        self.next_slide()
        self.play(TransformMatchingTex(s_2_2, s_2_3))

        self.next_slide()
        self.play(TransformMatchingTex(s_2_3, s_2_4))

        self.next_slide()
        self.play(TransformMatchingTex(s_2_4, s_2_5))

        self.next_slide()
        self.play(TransformMatchingTex(s_2_5, s_2_6))

        self.next_slide()
        self.play(TransformMatchingTex(s_2_6, s_2_7))
        self.play(Write(SurroundingRectangle(s_2_7, color=RED)))

        mistake = Tex("But no one would make such a mistake...").move_to(2*DOWN)
        cross = Cross(mistake)

        self.play(Write(mistake))

        self.next_slide()
        self.play(Create(cross))