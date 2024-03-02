from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

class GroupScene(Slide):

    def construct(self):
        groups = Text("Groups", color=YELLOW).scale(1.5)

        abstract_group = Tex("(G, $*$)")
        abstract_group.next_to(groups, DOWN)

        self.play(Write(groups), Write(abstract_group))
        
        self.next_slide()
        self.play(groups.animate.move_to(3*UP + LEFT).scale(2/3), abstract_group.animate.move_to(3*UP + 2*RIGHT)) # scaling back to 1

        # closure
        closure = Text("Closure").scale(1.5)

        self.play(Write(closure))
        self.wait(0.25)
        self.play(closure.animate.move_to(2*UP))

        product_in_group = Tex("$a * b \in G$").next_to(closure, DOWN)
        element_in_group = Tex("$\\forall a,b \in G$").next_to(product_in_group, DOWN)

        self.play(Write(product_in_group))
        self.play(Write(element_in_group))

        self.next_slide()
        self.play(
            closure.animate.scale(1/2).move_to(3*LEFT + 2*UP), 
            product_in_group.animate().scale(2/3).move_to(RIGHT + 2*UP), 
            element_in_group.animate().scale(2/3).move_to(3*RIGHT + 2*UP)
        )

        self.next_slide()

        # associativity
        associativity = Text("Associativity").scale(1.5)

        self.play(Write(associativity))
        self.wait(0.25)
        self.play(associativity.animate.move_to(UP))

        associativity_in_group = Tex("$a*(b*c) = (a*b)*c$").next_to(associativity, DOWN)
        forall_as_in_group = Tex("$\\forall a,b,c \in G$").next_to(associativity_in_group, DOWN)

        self.play(Write(associativity_in_group))
        self.play(Write(forall_as_in_group))

        self.next_slide()
        self.play(
            associativity.animate.scale(1/2).move_to(3.5*LEFT + UP), 
            associativity_in_group.animate().scale(2/3).move_to(0.3*RIGHT + UP), 
            forall_as_in_group.animate().scale(2/3).move_to(3*RIGHT + UP)
        )

        # identity
        identity = Text("Identity Element").move_to(DOWN).scale(1.5)

        self.play(Write(identity))
        self.wait(0.25)
        self.play(identity.animate.move_to(ORIGIN))

        identity_in_group = Tex("$e*a = a$").next_to(identity, DOWN)
        forall_id_in_group = Tex("$\\exists e \\in G \\; \\forall a \in G$").next_to(identity_in_group, DOWN)

        self.play(Write(identity_in_group))
        self.play(Write(forall_id_in_group))

        self.next_slide()
        self.play(
            identity.animate.scale(1/2).move_to(3*LEFT), 
            identity_in_group.animate().scale(2/3).move_to(0.3*RIGHT), 
            forall_id_in_group.animate().scale(2/3).move_to(3*RIGHT)
        )

        # inverse
        inverse = Text("Inverse Elements").move_to(2*DOWN).scale(1.5)

        self.play(Write(inverse))
        self.wait(0.25)
        self.play(inverse.animate.move_to(DOWN))

        inverse_in_group = Tex("$a*a^{-1} = e$").next_to(inverse, DOWN)
        forall_inv_in_group = Tex("$\\exists a^{-1} \\in G \\; \\forall a \in G$").next_to(inverse_in_group, DOWN)

        self.play(Write(inverse_in_group))
        self.play(Write(forall_inv_in_group))

        self.next_slide()
        self.play(
            inverse.animate.scale(1/2).move_to(3*LEFT + DOWN), 
            inverse_in_group.animate().scale(2/3).move_to(0.3*RIGHT + DOWN), 
            forall_inv_in_group.animate().scale(2/3).move_to(3*RIGHT + DOWN)
        )
        
        self.next_slide()

        # transform to integer example
        example = Text("Example", color=YELLOW).move_to(groups.get_center())
        int_group = Tex("$(\mathbb{Z}, +)$").move_to(abstract_group.get_center())

        product_in_int = Tex("$a + b \in \mathbb{Z}$").scale(2/3).move_to(product_in_group.get_center())
        element_in_int = Tex("$\\forall a,b \in \mathbb{Z}$").scale(2/3).move_to(element_in_group.get_center())

        associativity_in_int = Tex("$a+(b+c) = (a+b)+c$").scale(2/3).move_to(associativity_in_group.get_center())
        forall_as_in_int = Tex("$\\forall a,b,c \in \mathbb{Z}$").scale(2/3).move_to(forall_as_in_group.get_center())

        identity_in_int = Tex("$0+a = a$").scale(2/3).move_to(identity_in_group.get_center())
        forall_id_in_int = Tex("$\\exists 0 \\in \mathbb{Z} \\; \\forall a \in \mathbb{Z}$").scale(2/3).move_to(forall_id_in_group.get_center())

        inverse_in_int = Tex("$a+(-a) = 0$").scale(2/3).move_to(inverse_in_group.get_center())
        forall_inv_in_int = Tex("$\\exists {-a} \\in \mathbb{Z} \\; \\forall a \in \mathbb{Z}$").scale(2/3).move_to(forall_inv_in_group.get_center())

        self.play(
            Transform(groups, example),
            Transform(abstract_group, int_group),

            Transform(product_in_group, product_in_int),
            Transform(element_in_group, element_in_int),

            Transform(associativity_in_group, associativity_in_int),
            Transform(forall_as_in_group, forall_as_in_int),

            Transform(identity_in_group, identity_in_int),
            Transform(forall_id_in_group,forall_id_in_int),

            Transform(inverse_in_group, inverse_in_int),
            Transform(forall_inv_in_group,forall_inv_in_int),
        )