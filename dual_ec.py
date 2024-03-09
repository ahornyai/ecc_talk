from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

class DualECScene(Slide):

    def construct(self):
        title = Text("Dual_EC_DRBG").move_to(3*UP)
        img = ImageMobject("dualec_example.png").scale(1.5).next_to(title, DOWN)

        self.play(Write(title), FadeIn(img, shift=DOWN))

        self.next_slide()
        lets_attack = Text("Dual_EC_DRBG - Time to attack!").move_to(3*UP)

        self.play(FadeOut(img, shift=DOWN), Transform(title, lets_attack))

        steps = BulletedList(
            "Assume $Q = d*P$ and we know the value of d.",
            "We brute force the first two bytes of the output - 65 536 possibilities",
            "$out = r*Q = r*d*P$",
            "But we know d, because that is our backdoor. We can calculate $r*P = out * d^{-1}$",
            "What is $r*P$? The state!!",
            "We get the next value from our super secure RNG using the freshly calculated state, and check if our guess was right for the first two bytes"
        ).next_to(title, DOWN).set_color(YELLOW).scale(0.75)

        self.play(
            LaggedStartMap(FadeIn, steps, shift=0.5 * DOWN, lag_ratio=0.25)
        )

        self.next_slide()
        attack_img = ImageMobject("dualec_attack.png").scale(1.5).next_to(title, DOWN)

        self.play(FadeOut(steps, shift=DOWN), FadeIn(attack_img, shift=DOWN))