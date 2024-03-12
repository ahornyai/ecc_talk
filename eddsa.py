from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

class EdDSAIntroductionScene(Slide):

    def construct(self):
        title = Text("EdDSA")

        self.play(Write(title))
        self.wait(0.1)
        self.play(title.animate.move_to(3*UP))

        keygen_group = VGroup()
        keygen = Text("Key generation").move_to(2*UP).set_color(YELLOW)
        privkey = Tex("$a = H(d)[:32]$").next_to(keygen, DOWN)
        pubkey = Tex("$A = a*G$").next_to(privkey, DOWN)

        keygen_group.add(keygen, privkey, pubkey)

        self.play(Write(keygen_group))

        self.next_slide()

        self.play(keygen_group.animate.scale(0.6))
        self.play(keygen_group.animate.shift(4.5*LEFT))

        signing_group = VGroup()

        signing = Text("Signing").move_to(2*UP).set_color(YELLOW)
        r = Tex("$r = H(H(d)[32:] || m)$").next_to(signing, DOWN)
        R = Tex("$R = r*G$").next_to(r, DOWN)
        s = Tex("$S = r + H(R || A || m) * a \ (\mathrm{mod}\ q)$").next_to(R, DOWN)

        signing_group.add(signing, r, R, s)

        self.play(Write(signing_group))

        self.next_slide()

        self.play(signing_group.animate.scale(0.6))
        self.play(signing_group.animate.shift(4.5*RIGHT))

        verifying = Text("Verifying").move_to(DOWN).set_color(YELLOW)
        s_copy = Tex("$S = r + H(R || A || m) * a \ (\mathrm{mod}\ q)$").scale(0.6).move_to(s)
        verify_eq = Tex("$S*G = r*G + H(R || A || m) * a * G \ (\mathrm{mod}\ q)$").next_to(verifying, DOWN)
        verify_eq_final = Tex("$S*G = R + H(R || A || m) * A \ (\mathrm{mod}\ q)$").next_to(verifying, DOWN)

        self.play(Write(verifying))
        self.play(Transform(s_copy, verify_eq))

        self.next_slide()

        self.play(Transform(s_copy, verify_eq_final))

class ExampleEdwardsCurve(Slide):

    def construct(self):
        self.play(FadeIn(ImageMobject("ecdsa_examples/twisted_edwards.png").scale(1.7), shift=DOWN))