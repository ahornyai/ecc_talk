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

class RepeatedNonceExampleScene(Slide):

    def construct(self):
        ps3 = Text("PlayStation 3").move_to(3*UP)
        ps3_img = ImageMobject("./ecdsa_examples/sony_ps3.png").next_to(ps3, DOWN)

        self.play(Write(ps3))
        self.play(FadeIn(ps3_img, shift=DOWN))

        self.next_slide()

        self.play(FadeOut(ps3, shift=DOWN), FadeOut(ps3_img, shift=DOWN))

        android = Text("Android SecureRandom").move_to(3*UP)
        android_img = ImageMobject("./ecdsa_examples/android_securerandom.png").scale(1.5).next_to(android, DOWN)

        self.play(Write(android))
        self.play(FadeIn(android_img, shift=DOWN))

        self.next_slide()

        self.play(FadeOut(android, shift=DOWN), FadeOut(android_img, shift=DOWN))

        blockchain = Text("blockchain.info - random.org incident").move_to(3*UP)
        blockchain_img = ImageMobject("./ecdsa_examples/blockchain_random_org.png").next_to(blockchain, DOWN)

        self.play(Write(blockchain))
        self.play(FadeIn(blockchain_img, shift=DOWN))

class BiasedNonceAttackScene(Slide):

    def construct(self):
        title = Text("Biased nonce lattice attacks")

        self.play(Write(title))

        self.next_slide()
        self.play(title.animate.move_to(3*UP))

        what_if = Text("What if the few most significant bits of our nonces are constantly all zero?").scale(0.6).move_to(UP)
        then = Tex("$ \implies$ our nonce k will be way smaller than our private key d").set_color(YELLOW)

        self.play(Write(what_if))
        self.play(Write(then))
        
        k_group = VGroup()

        k_1 = Tex("$k_1 \equiv s_1^{-1} * h_1 + s_1^{-1} * r*d \ (\mathrm{mod}\ q)$").move_to(DOWN)
        k_2 = Tex("$k_2 \equiv s_2^{-1} * h_2 + s_2^{-1} * r*d \ (\mathrm{mod}\ q)$").next_to(k_1, DOWN)

        k_group.add(k_1, k_2)

        self.play(Write(k_group))

        self.next_slide()

        group = VGroup()
        k_vec = Matrix(np.transpose([["k_1", "k_2"]])).move_to(2*DOWN + 4*LEFT)
        eq = Tex("$ \equiv $").move_to(2*DOWN + 3*LEFT)
        c_vec = Matrix(np.transpose([["s_1^{-1} * h_1", "s_2^{-1} * h_2"]])).move_to(2*DOWN + 1.4*LEFT)
        plus = Tex("$ + $").move_to(2*DOWN + 0.2*RIGHT)
        d_vec = Matrix(np.transpose([["s_1^{-1} * r*d", "s_2^{-1} * r*d"]])).move_to(2*DOWN + 2*RIGHT)
        mod = Tex("$(\mathrm{mod}\ q)$").move_to(2*DOWN + 4.5*RIGHT)
        vec_equation = Tex("$ \\vec{k} \equiv \\vec{h} + d*\\vec{r} \ (\mathrm{mod}\ q)$").move_to(3.5*DOWN)

        group.add(k_vec.get_brackets(), k_vec.get_columns()[0])
        group.add(eq, plus, mod)
        group.add(c_vec.get_brackets(), c_vec.get_columns()[0])
        group.add(d_vec.get_brackets(), d_vec.get_columns()[0])

        self.play(Transform(k_group, group))
        self.play(Write(vec_equation))

class ShortVectorScene(Slide):
    
    def construct(self):
        plane = NumberPlane()

        h_loc = np.array((0.3, 1.5, 0))
        r_loc = np.array((0.6, 1.2, 0))
        r_1_loc = r_loc - h_loc

        h = Arrow(start=ORIGIN, end=h_loc, buff=0).set_color(RED)
        r = Arrow(start=ORIGIN, end=r_loc, buff=0).set_color(GREEN)

        dots = []

        self.add(plane)

        # really bad solution but this will be good enough for now
        for i in range(-25, 25):
            for j in range(-25, 25):
                dots.append(Dot(i*h_loc + j*r_loc))
        

        self.play(GrowArrow(h), GrowArrow(r))
        
        self.next_slide()
        self.play(LaggedStartMap(FadeIn, dots, shift=0.5 * DOWN, lag_ratio=0.01))

        self.next_slide()

        self.play(r.animate.rotate(PI))
        self.play(r.animate.shift(-r_1_loc))

        shortest_vector = Arrow(start=ORIGIN, end=-r_1_loc, buff=0).set_color(PINK)
        shortest_vector.stroke_width = 6
        
        self.next_slide()
        self.play(GrowArrow(shortest_vector))
        self.play(FadeOut(r), FadeOut(h))

class LLLMatrixScene(Slide):

    def construct(self):
        title = Text("Lenstra-Lenstra-Lovász (LLL) algorithm").move_to(3*UP)
        basis = Matrix(np.transpose([
            ["q", "0"],
            ["0", "q"],
            ["h_1'", "h_2'"],
            ["r_1'", "r_2'"]
        ])).set_color(YELLOW)
        h_prime = Tex("$h' \equiv s^{-1} * h \ (\mathrm{mod}\ q)$").scale(0.75).move_to(2*UP)
        r_prime = Tex("$r' \equiv s^{-1} * r \ (\mathrm{mod}\ q)$").scale(0.75).next_to(h_prime, DOWN)

        self.play(Write(title), Write(h_prime), Write(r_prime), FadeIn(basis.get_brackets()))
        self.play(LaggedStartMap(FadeIn, basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.25))

        arr = Arrow(start=DOWN, end=2*DOWN).scale(1.5)

        self.play(GrowArrow(arr))

        reduced_basis = Matrix(np.transpose([
            ["k_1", "k_2"],
            ["?", "?"],
            ["?", "?"],
            ["?", "?"]
        ])).set_color(YELLOW).next_to(arr, DOWN)

        self.play(FadeIn(reduced_basis.get_brackets()), LaggedStartMap(FadeIn, reduced_basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.25))

        self.next_slide()

        self.play(
            FadeOut(basis.get_brackets(), shift=DOWN), 
            LaggedStartMap(FadeOut, basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.1),
            FadeOut(reduced_basis.get_brackets(), shift=DOWN), 
            LaggedStartMap(FadeOut, reduced_basis.get_columns(), shift=0.5 * DOWN, lag_ratio=0.1),
            FadeOut(h_prime, shift=DOWN), FadeOut(r_prime, shift=DOWN),
            FadeOut(arr)
        )

        msb_attack = ImageMobject("ecdsa_examples/msb_attack_code.png").scale(1.15).next_to(title, DOWN)
        self.play(FadeIn(msb_attack, shift=DOWN))

class BonusAttackScene(Slide):

    def construct(self):
        title = Text("Bonus attacks").move_to(3*UP)
        attacks = BulletedList(
            "Private key can be recovered with any amount of nonce leakage (in some cases even less than one bit is enough)",
            "LadderLeak: Breaking ECDSA with Less than One Bit of Nonce Leakage - https://www.youtube.com/watch?v=Nk1uqe8Z7k4",
            "Polynonce attack - pretty novel - nonces generated by LCG-s can be broken",
            "https://research.kudelskisecurity.com/2023/03/06/polynonce-a-tale-of-a-novel-ecdsa-attack-and-bitcoin-tears/"
        ).scale(0.7).set_color(YELLOW)

        self.play(Write(title), LaggedStartMap(FadeIn, attacks, shift=0.5 * DOWN, lag_ratio=0.1))
