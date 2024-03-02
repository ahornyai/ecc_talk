from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

class AbelianGroupScene(Slide):

    def construct(self):
        groups = Text("Abelian Groups", color=YELLOW).scale(1.5)

        abstract_group = Tex("(G, $*$)")
        abstract_group.next_to(groups, DOWN)

        self.play(Write(groups), Write(abstract_group))
        
        self.next_slide()
        self.play(groups.animate.move_to(3*UP + LEFT).scale(2/3), abstract_group.animate.move_to(3*UP + 3*RIGHT)) # scaling back to 1

        # commutativity
        commutativity = Text("Commutativity").scale(1.5)

        self.play(Write(commutativity))
        self.wait(0.25)
        self.play(commutativity.animate.move_to(UP))

        product_in_group = Tex("$a * b = b * a$").next_to(commutativity, DOWN)
        element_in_group = Tex("$\\forall a,b \in G$").next_to(product_in_group, DOWN)

        self.play(Write(product_in_group))
        self.play(Write(element_in_group))

        self.next_slide()
