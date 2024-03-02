from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

class TitleScene(Slide):
    def construct(self):
        # title slide
        ecc_crypto = Text("Elliptic curve cryptography").scale(1.5)
        author = Text("Alex Hornyai", color=YELLOW)
        author.next_to(ecc_crypto, DOWN)

        self.play(Write(ecc_crypto))
        self.wait(0.25)
        self.play(Write(author))
        self.wait()

        self.next_slide()

        # whoami slide
        whoami = Title("whoami")

        self.play(
            FadeOut(author), 
            Transform(ecc_crypto, whoami)
        )
        self.wait(0.25)
        
        list = BulletedList("CTF player", "secondary school student", "IT security and cryptography fan", "Main categories: Cryptography, web, binary exploitation", color=YELLOW)
        list.align_to(whoami)
        self.play(
            LaggedStartMap(FadeIn, list, shift=0.5 * DOWN, lag_ratio=0.25)
        )

class OverviewScene(Slide):

    def construct(self):
        overview = Title("Overview")
        overview_list = BulletedList("Math introduction", "Elliptic curves", "A famous NSA backdoor", "ECDSA", "EdDSA", color=YELLOW)
        rect = SurroundingRectangle(overview_list[0])

        self.play(
            Write(overview),
            LaggedStartMap(FadeIn, overview_list, shift=0.5 * DOWN, lag_ratio=0.25)
        )

        self.next_slide()

        self.play(DrawBorderThenFill(rect))
