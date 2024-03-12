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
        whoami = Text("whoami").move_to(3*UP)

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
        overview = Text("Chapters").move_to(3*UP)
        overview_list = BulletedList("Math introduction", "Elliptic curves", "A famous NSA backdoor", "ECDSA", "EdDSA", color=YELLOW)
        rect = SurroundingRectangle(overview_list[0])

        self.play(
            Write(overview),
            LaggedStartMap(FadeIn, overview_list, shift=0.5 * DOWN, lag_ratio=0.25)
        )

        self.play(DrawBorderThenFill(rect))

class GitHubScene(Slide):

    def construct(self):
        img = ImageMobject("ecdsa_examples/github_ecc_cryptanalysis.png").scale(0.8)
        url = Text("https://github.com/ahornyai/ecc_cryptanalysis").scale(0.7).next_to(img, DOWN)

        self.play(FadeIn(img, shift=DOWN), Write(url))

class EndingScene(Slide):

    def construct(self):
        thanks = Text("Thanks for your attention").move_to(2*UP).set_color(YELLOW)
        github_logo = ImageMobject("logo/github.png").scale(0.5).move_to(4*LEFT + 2.5*DOWN)
        linkedin_logo = ImageMobject("logo/linkedin.png").scale(0.4).move_to(5*RIGHT + 2.5*DOWN)
        github = Text("ahornyai").scale(0.5).next_to(github_logo, LEFT)
        linkedin = Text("Hornyai Alex").scale(0.5).next_to(linkedin_logo, LEFT)

        self.play(Write(thanks), FadeIn(github_logo, shift=DOWN), FadeIn(linkedin_logo, shift=DOWN), Write(github), Write(linkedin))