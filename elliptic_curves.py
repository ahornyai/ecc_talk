from manim import *
from manimlib.mobject.mobject import *

from manim_slides import Slide

# Most of the code were taken from here: https://github.com/thud/eccdemo MIT License (credits for thud)

from manimlib.utils.space_ops import angle_of_vector

L,U,R,D = LEFT, UP, RIGHT, DOWN
NUMBER_PLANE = None

class EllipticCurveIntroduction(Slide):
    def construct(self):
        short_weierstrass = Tex("Short Weierstrass equation")
        eq = Tex("$y^2 = x^3 + ax + b$").scale(1.5).next_to(short_weierstrass, DOWN)

        self.play(Write(short_weierstrass), Write(eq))

class MoveAlongPathPiece(Animation):
    def __init__(self, mobject, mobject2, path, t_min, t_max, t_min2, t_max2, **kwargs):
        self.mobject = mobject
        self.mobject2 = mobject2
        self.path = path
        self.t_min = t_min
        self.t_max = t_max
        self.t_min2 = t_min2
        self.t_max2 = t_max2
        self.label = kwargs["label"]
        self.labelp = kwargs["labelp"]
        self.label2 = kwargs["label2"]
        self.labelp2 = kwargs["labelp2"]
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        self.point = self.path.get_point_from_function(self.t_min+alpha*(self.t_max-self.t_min))
        self.point2 = self.path.get_point_from_function(self.t_min2+alpha*(self.t_max2-self.t_min2))
        self.mobject.move_to(self.point)
        self.label.next_to(self.point,self.labelp)
        self.mobject2.move_to(self.point2)
        self.label2.next_to(self.point2,self.labelp2)

class MovePointsWithLine(MoveAlongPathPiece):
    def __init__(self, line, *args, **kwargs):
        self.line = line
        super().__init__(*args, **kwargs)

    def interpolate_mobject(self, alpha):
        super().interpolate_mobject(alpha)
        self.line.set_angle(angle_of_vector(self.point2-self.point))
        self.line.move_to(self.point)

class MovePointsWithLineAndThirdPoint(MovePointsWithLine):
    def __init__(self, c2p, p2c, mobject3, *args, **kwargs):
        self.mobject3 = mobject3
        self.c2p = c2p
        self.p2c = p2c
        self.label3 = kwargs["label3"]
        self.labelp3 = kwargs["labelp3"]
        super().__init__(*args, **kwargs)

    def interpolate_mobject(self, alpha):
        super().interpolate_mobject(alpha)
        if self.point[0] == self.point2[0]:
            raise Exception(":skull:")
        c1,c2 = self.p2c(self.point), self.p2c(self.point2)
        m = (c2[1]-c1[1])/(c2[0]-c1[0])
        self.point3 = [m**2-c1[0]-c2[0]]
        self.point3.append(c1[1]+m*(self.point3[0]-c1[0]))
        self.mobject3.move_to(self.c2p(self.point3[0], self.point3[1]))
        self.label3.next_to(self.c2p(self.point3[0], self.point3[1]),self.labelp3)

class EllipticCurveScene(Slide):

    def construct(self):
        global NUMBER_PLANE
        NUMBER_PLANE = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_opacity": 0
            },
            tips= False,
            axis_config = {
                "stroke_width": 4,
                "include_ticks": True,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "font_size": 24,
                "stroke_color": BLUE_E,
                "stroke_opacity": 1,
            },
        )

        self.add(NUMBER_PLANE)
        
        parex = ParametricFunction(function=ec1, t_range=[-5, 5])
        parex2 = ParametricFunction(function=ec2, t_range=[-5, 5])
        parex3 = ParametricFunction(function=ec3, t_range=[-5, 5])
        parex4 = ParametricFunction(function=ec4, t_range=[-5, 5])

        NUMBER_PLANE.add(parex)

        ais = Tex("$a = -1$").scale(.75).move_to(3*UL+2*L)
        bis = Tex("$b = 5$").scale(.75).next_to(ais, DOWN)
        fnis = Tex("$y^2 = x^3 - x + 5$").scale(.75).next_to(bis, DOWN)
        ais2 = Tex("$a = 0$").scale(.75).move_to(3*UL+2*L)
        bis2 = Tex("$b = 0$").scale(.75).next_to(ais, DOWN)
        fnis2 = Tex("$y^2 = x^3$").scale(.75).next_to(bis, DOWN)
        ais3 = Tex("$a = -3$").scale(.75).move_to(3*UL+2*L)
        bis3 = Tex("$b = 2$").scale(.75).next_to(ais, DOWN)
        fnis3 = Tex("$y^2 = x^3 -3x + 2$").scale(.75).next_to(bis, DOWN)
        ais4 = Tex("$a = -2$").scale(.75).move_to(3*UL+2*L)
        bis4 = Tex("$b = 2$").scale(.75).next_to(ais, DOWN)
        fnis4 = Tex("$y^2 = x^3 - 2x + 2$").scale(.75).next_to(bis, DOWN)
        empty = Circle(radius=0.2)

        self.play(
            Create(parex),
            Write(ais),
            Write(bis),
            Write(fnis),
        )
        
        
        self.next_slide()

        self.play(Transform(parex, parex2), *[Transform(*x) for x in [[ais,ais2],[bis,bis2],[fnis,fnis2]]])
        self.play(
            Create(empty)
        )

        self.next_slide()

        self.remove(empty)
        self.play(
            Transform(
                parex,
                parex3
            ),
            *[Transform(*x) for x in [[ais,ais3],[bis,bis3],[fnis,fnis3]]]
        )
        self.wait(0.5)
        empty.move_to(c2p(1,0))
        
        self.play(
            Create(empty)
        )

        determinant = Tex("$4a^3+27b^2 \\neq 0$").scale(.75).next_to(fnis, DOWN)
        
        self.play(Write(determinant))

        self.next_slide()

        self.remove(empty)
        self.play(
            Transform(
                parex,
                parex4
            ),
            *[Transform(*x) for x in [[ais,ais4],[bis,bis4],[fnis,fnis4]]]
        )
        self.wait(1)
        gp = parex4.get_point_from_function

        pp = Dot(gp(0.1),color=YELLOW)
        pq = Dot(gp(2),color=YELLOW)
        pplab = Tex("$P$",color=YELLOW).scale(0.75).next_to(gp(0.1), LEFT)
        pqlab = Tex("$Q$",color=YELLOW).scale(0.75).next_to(gp(2), 0.707*UR)

        self.play(Create(pp),Create(pq),Write(pplab),Write(pqlab))
        self.play(
            MoveAlongPathPiece(
                pp,
                pq,
                parex4,
                0.1,1.5,
                2,2.75,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR
            )
        )
        self.play(
            MoveAlongPathPiece(
                pp,
                pq,
                parex4,
                1.5,0.1,
                2.75,2.3,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR
            )
        )

        jline = Line()
        jline.set_angle(angle_of_vector(gp(2.3)-gp(0.1)))
        jline.move_to(gp(0.1))
        jline.set_length(20)
        jline.set_opacity(0.8)
        
        self.play(
            Create(jline)
        )
        self.play(
            MovePointsWithLine(
                jline,
                pp,
                pq,
                parex4,
                0.1,0.2,
                2.3,2.1,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR
            )
        )
        point, point2 = NUMBER_PLANE.point_to_coords(gp(0.2)), NUMBER_PLANE.point_to_coords(gp(2.1))

        pr = Dot(color=BLUE)
        m = (point2[1]-point[1])*(point2[0]-point[0])**-1
        point3 = [m**2-point[0]-point2[0]]
        point3.append(point[1]+m*(point3[0]-point[0]))
        pr.move_to(NUMBER_PLANE.coords_to_point(point3[0], point3[1]))
        prlab = Tex("$R$",color=BLUE).scale(0.75).next_to(NUMBER_PLANE.coords_to_point(point3[0], point3[1]), 0.707*DR)

        self.play(
            Create(pr),
            Write(prlab)
        )

        self.play(
            MovePointsWithLineAndThirdPoint(
                NUMBER_PLANE.coords_to_point,
                NUMBER_PLANE.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                0.2,-0.3,
                2.1,2.4,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        self.next_slide()
        
        self.play(
            MovePointsWithLineAndThirdPoint(
                NUMBER_PLANE.coords_to_point,
                NUMBER_PLANE.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                -0.3,-0.3,
                2.4,0.301,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        self.next_slide()

        self.play(
            MovePointsWithLineAndThirdPoint(
                NUMBER_PLANE.coords_to_point,
                NUMBER_PLANE.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                -0.3,-0.3,
                0.301,2.4,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )
        
        self.wait(1)
        
        m_t = Tex("$m = \\frac{\Delta y}{\Delta x} = \\frac{y_p-y_q}{x_p-x_q}$").scale(.75).move_to(D+5*R)
        lineeq_t = Tex(
                """\\begin{align*}
                y-y_P &= m(x-x_P)\\\\
                \implies y &= y_P + m(x-x_P)
                \\end{align*}
                """).scale(.75).next_to(m_t, 1.25*DOWN)
        
        self.play(Write(m_t), Write(lineeq_t))

        self.next_slide()

        intersectedline_t = Tex("\\begin{align*}\pm \sqrt{x^3+ax+b} \\\\ = y_P + m(x-x_P) \\end{align*}").scale(.75).next_to(m_t, 1.25*DOWN)
        self.play(
            Transform(
                lineeq_t,
                intersectedline_t
            )
        )

        self.next_slide()
        
        rxry_t = Tex(
                """\\begin{align*}
                x_R=m^2-x_P-x_Q\\\\
                y_R=y_P+m(x_R-x_P)
                \\end{align*}
                """).scale(.75).next_to(m_t, 1.25*DOWN)
        
        self.play(
            Transform(
                lineeq_t,
                rxry_t
            )
        )

        self.play(
            MovePointsWithLineAndThirdPoint(
                NUMBER_PLANE.coords_to_point,
                NUMBER_PLANE.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                -0.3,0.1,
                2.4,0.6001,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        self.next_slide()

        self.play(
            MovePointsWithLineAndThirdPoint(
                NUMBER_PLANE.coords_to_point,
                NUMBER_PLANE.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                0.1,0.6,
                0.6001,0.6001,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        self.wait(1)

        mtaneq_t = Tex("$m_{\\textrm{tan}} = $").scale(.75).move_to(U+3*R)
        mtanrhs = Tex("$\\frac{\mathrm{d}}{\mathrm{d}x} \left( \pm \sqrt{x^3+ax+b} \\right)$").scale(.75).next_to(mtaneq_t, RIGHT)
        mtanrhs2 = Tex("$\pm \\frac{3x_P^2+a}{2\sqrt{x_P^3+ax+b}}$").scale(.75).next_to(mtaneq_t, RIGHT)
        mtanrhs3 = Tex("$\\frac{3x_P^2+a}{2y_P}$").scale(.75).next_to(mtaneq_t, RIGHT)

        self.play(Write(mtaneq_t),Write(mtanrhs))

        self.next_slide()
        self.play(
            Transform(
                mtanrhs,
                mtanrhs2
            )
        )
        self.next_slide()
        self.play(
            Transform(
                mtanrhs,
                mtanrhs3
            )
        )
        self.wait(.25)
        self.play(
            mtaneq_t.animate.shift(1.25*R),
            mtanrhs.animate.shift(1.25*R)
        )

        self.wait(1)
        self.play(
            MovePointsWithLineAndThirdPoint(
                NUMBER_PLANE.coords_to_point,
                NUMBER_PLANE.point_to_coords,
                pr,
                jline,
                pp,
                pq,
                parex4,
                0.6,-0.6,
                0.6001,0.6001,
                label=pplab,
                labelp=LEFT,
                label2=pqlab,
                labelp2=0.707*UR,
                label3=prlab,
                labelp3=0.707*DR
            )
        )

        infarrow = Arrow(
            start=U*4+L*1.5+DL,
            end=UP*4+L*1.5,
            color=YELLOW
        )
        pointatinfinity_t = Tex("``The Point at Infinity''", color=YELLOW).scale(.75).next_to(infarrow, DL)

        self.play(
            Create(infarrow),
            Write(pointatinfinity_t),
            ais.animate.shift(1.5*D),
            bis.animate.shift(1.5*D),
            fnis.animate.shift(1.5*D),
            determinant.animate.shift(1.5*D),
        )

class EllipticCurveAdditionScene(Slide):

    def construct(self):
        global NUMBER_PLANE
        NUMBER_PLANE = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_opacity": 0
            },
            tips= False,
            axis_config = {
                "stroke_width": 4,
                "include_ticks": True,
                "line_to_number_buff": SMALL_BUFF,
                "label_direction": DR,
                "font_size": 24,
                "stroke_color": BLUE_E,
                "stroke_opacity": 1,
            },
        )

        self.add(NUMBER_PLANE)

        parex = ParametricFunction(function=ec, t_range=[-5, 5])
        gp = parex.get_point_from_function

        fnis = Tex("$y^2 = x^3 - 2x + 2$").scale(.75).move_to(3*U+4*L)

        NUMBER_PLANE.add(parex)

        self.play(
            Create(parex),
            Write(fnis),
        )

        point, point2 = NUMBER_PLANE.point_to_coords(gp(0.1)), NUMBER_PLANE.point_to_coords(gp(2))

        pp = Dot(gp(0.1),color=YELLOW)
        pq = Dot(gp(2),color=YELLOW)
        pr = Dot(color=BLUE)
        pplab = Tex("$P$",color=YELLOW).scale(0.75).next_to(gp(0.1), LEFT)
        pqlab = Tex("$Q$",color=YELLOW).scale(0.75).next_to(gp(2), 0.707*UR)

        m = (point2[1]-point[1])*(point2[0]-point[0])**-1
        point3 = [m**2-point[0]-point2[0]]
        point3.append(point[1]+m*(point3[0]-point[0]))
        pr.move_to(NUMBER_PLANE.coords_to_point(point3[0], point3[1]))
        prlab = Tex("$R$",color=BLUE).scale(0.75).next_to(NUMBER_PLANE.coords_to_point(point3[0], point3[1]), 0.707*DR)

        prneg = Dot(color=RED).move_to(NUMBER_PLANE.coords_to_point(point3[0],-point3[1]))
        prneglab = Tex("$-R$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(point3[0],-point3[1]), 0.707*UR)
        prnegline = Line(start=pr,end=prneg,color=RED)

        jline = Line()
        jline.set_angle(angle_of_vector(gp(2)-gp(0.1)))
        jline.move_to(gp(0.1))
        jline.set_length(20)
        jline.set_opacity(0.8)

        self.play(Create(pp),Create(pq),Create(pr),Create(jline),Write(pplab),Write(pqlab), Write(prlab))

        ppqpreqz = Tex("$P + Q + R = 0$").scale(1.25).move_to(LEFT*4+D*2)
        ppqpreqz2 = Tex("$P + Q = -R$").scale(1.25).move_to(LEFT*4+D*2)

        self.play(Write(ppqpreqz))
        
        self.next_slide()

        self.play(
            Transform(
                ppqpreqz,
                ppqpreqz2
            ),
            Create(prnegline)
        )

        self.play(Create(prneg), Write(prneglab))

        pass

class EllipticCurveOverGF(Slide):

    def construct(self):
        global NUMBER_PLANE
        NUMBER_PLANE = NumberPlane(
            x_range=[0, 36, 5],
            y_range=[0, 36, 5],
            x_length=9,
            y_length=5,
            background_line_style={
                "stroke_opacity": 0
            },
            tips= False,
            axis_config = {
                "stroke_width": 4,
                "include_ticks": True,
                "include_numbers": True,
                "label_direction": D,
                "font_size": 24,
                "stroke_color": BLUE_E,
                "stroke_opacity": 1,
            }
        ).move_to(2*R)

        self.add(NUMBER_PLANE)

        p = 37

        ppp = [6,24]
        pp = Dot(NUMBER_PLANE.coords_to_point(*ppp),color=YELLOW)
        pqp = [13,8]
        pq = Dot(NUMBER_PLANE.coords_to_point(*pqp),color=YELLOW)
        pplab = Tex("$P$",color=YELLOW).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*ppp), .707*UL)
        pqlab = Tex("$Q$",color=YELLOW).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*pqp), .707*UL)

        points = []
        for x in range(p):
            for y in range(p):
                if (x == ppp[0] and y == ppp[1]) or (x == pqp[0] and y == pqp[1]):
                    continue
                if y**2 % p == (x**3 -2*x +2)%p:
                    points.append(NUMBER_PLANE.coords_to_point(x,y))
                    points.append(NUMBER_PLANE.coords_to_point(x,p-y))
        
        dots = [Dot(x) for x in points]
        self.play(
            *[Create(x) for x in dots],
            Create(pp),
            Create(pq),
            Write(pplab),
            Write(pqlab),
        )
        
        self.wait(1)

        mlfn, disc = self.modline(p,ppp,pqp)
        ml = ParametricFunction(function=mlfn, t_range=[0, 36], discontinuities=disc)

        self.play(Create(ml))
        self.wait(1)

        prp = [27,13]
        pr = Dot(NUMBER_PLANE.coords_to_point(*prp),color=BLUE)
        prlab = Tex("$R$",color=BLUE).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prp), .707*UL)

        prpn = [27,p-13]
        prn = Dot(NUMBER_PLANE.coords_to_point(*prpn),color=RED)
        prnlab = Tex("$-R$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn), .707*UL)
        jl = Line(start=pr, end=prn, color=RED)

        self.play(
            Create(pr),
            Write(prlab)
        )

        self.play(
            Create(jl)
        )

        self.play(
            Create(prn),
            Write(prnlab)
        )

        m_t = Tex("$m = \\frac{\Delta y}{\Delta x} = \\frac{y_P-y_Q}{x_P-x_Q}$").scale(.75).move_to(3*U+5*L)
        m_t2 = Tex("\\begin{align*}m &= \Delta y (\Delta x)^{-1} \\\\ &= (y_P-y_Q)(x_P-x_Q)^{-1}\\end{align*}").scale(.7).move_to(3*U+5*L)

        self.play(
            Write(m_t)
        )

        self.next_slide()

        self.play(
            Transform(
                m_t,
                m_t2
            )
        )
        
        self.next_slide()

        closure_t = Tex("1. Closure",color=YELLOW).move_to(2*U+5*L)
        assoc_t = Tex("2. Associativity",color=YELLOW).next_to(closure_t, D)
        ident_t = Tex("3. Identity Element",color=YELLOW).scale(.75).next_to(assoc_t, D)
        inverse_t = Tex("4. Inverse Elements",color=YELLOW).scale(.75).next_to(ident_t, D)

        self.play(Write(closure_t))
        self.wait(.5)

        ppp2 = [6,13]
        pp2 = Dot(NUMBER_PLANE.coords_to_point(*ppp2),color=YELLOW)
        pqp2 = [11,4]
        pq2 = Dot(NUMBER_PLANE.coords_to_point(*pqp2),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp,pq,pr,prn,ml,jl,prlab,prnlab]],
            *[Create(x) for x in [pp2,pq2]],
            pplab.animate.next_to(NUMBER_PLANE.coords_to_point(*ppp2),.707*UL),
            pqlab.animate.next_to(NUMBER_PLANE.coords_to_point(*pqp2),.707*UL)
        )

        mlfn, disc = self.modline(p,ppp2,pqp2)
        ml = ParametricFunction(function=mlfn, t_range=[0, 36], discontinuities=disc)

        prp2 = [4,p-13]
        pr2 = Dot(NUMBER_PLANE.coords_to_point(*prp2),color=BLUE)

        prpn2 = [4,13]
        prn2 = Dot(NUMBER_PLANE.coords_to_point(*prpn2),color=RED)
        jl2 = Line(start=pr2, end=prn2, color=RED)

        prlab.next_to(NUMBER_PLANE.coords_to_point(*prp2),.707*UL)
        prnlab.next_to(NUMBER_PLANE.coords_to_point(*prpn2),.707*UL)
        self.play(
            Create(ml),
            Create(pr2),
            Write(prlab),
        )
        self.play(
            Create(jl2),
            Create(prn2),
            Write(prnlab)
        )

        self.wait(1)

        ppp3 = [4,13]
        pp3 = Dot(NUMBER_PLANE.coords_to_point(*ppp3),color=YELLOW)
        pqp3 = [4,13]
        pq3 = Dot(NUMBER_PLANE.coords_to_point(*pqp3),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp2,pq2,pr2,prn2,ml,jl2,prlab,prnlab]],
            *[Create(x) for x in [pp3,pq3]],
            pplab.animate.next_to(NUMBER_PLANE.coords_to_point(*ppp3),.707*UL),
            pqlab.animate.next_to(NUMBER_PLANE.coords_to_point(*pqp3),.707*UR)
        )

        mlfn, disc = self.modline(p,ppp3,pqp3)
        ml = ParametricFunction(function=mlfn, t_range=[0, 36], discontinuities=disc)

        prp3 = [26,p-5]
        pr3 = Dot(NUMBER_PLANE.coords_to_point(*prp3),color=BLUE)

        prpn3 = [26,5]
        prn3 = Dot(NUMBER_PLANE.coords_to_point(*prpn3),color=RED)
        jl3 = Line(start=pr3, end=prn3, color=RED)

        prlab.next_to(NUMBER_PLANE.coords_to_point(*prp3),.707*UL)
        prnlab.next_to(NUMBER_PLANE.coords_to_point(*prpn3),.707*UL)
        self.play(
            Create(ml),
            Create(pr3),
            Write(prlab),
        )
        self.play(
            Create(jl3),
            Create(prn3),
            Write(prnlab)
        )

        self.wait(2)

        ppp4 = [6,24]
        pp4 = Dot(NUMBER_PLANE.coords_to_point(*ppp4),color=YELLOW)
        pqp4 = [13,8]
        pq4 = Dot(NUMBER_PLANE.coords_to_point(*pqp4),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp3,pq3,pr3,prn3,ml,jl3,prlab,prnlab]],
            *[Create(x) for x in [pp4,pq4]],
            pplab.animate.next_to(NUMBER_PLANE.coords_to_point(*ppp4),.707*UL),
            pqlab.animate.next_to(NUMBER_PLANE.coords_to_point(*pqp4),.707*UL)
        )

        mlfn, disc = self.modline(p,ppp4,pqp4)
        ml = ParametricFunction(function=mlfn, t_range=[0, 36], discontinuities=disc)

        prp4 = [27,13]
        pr4 = Dot(NUMBER_PLANE.coords_to_point(*prp4),color=BLUE)

        prpn4 = [27,p-13]
        prn4 = Dot(NUMBER_PLANE.coords_to_point(*prpn4),color=RED)
        jl4 = Line(start=pr4, end=prn4, color=RED)

        prlab.next_to(NUMBER_PLANE.coords_to_point(*prp4),.707*UL)
        prnlab.next_to(NUMBER_PLANE.coords_to_point(*prpn4),.707*UL)
        self.play(
            Create(ml),
            Create(pr4),
            Write(prlab),
        )
        self.play(
            Create(jl4),
            Create(prn4),
            Write(prnlab)
        )

        self.wait(1)

        self.play(
            FadeToColor(
                closure_t,
                GREEN
            )
        )

        self.next_slide()

        self.play(
            Write(assoc_t)
        )

        self.play(
            FadeOut(prn4),
            FadeOut(prnlab),
            FadeOut(jl4)
        )

        self.play(
            pr4.animate.move_to(NUMBER_PLANE.coords_to_point(*ppp4)),
            prlab.animate.next_to(NUMBER_PLANE.coords_to_point(*ppp4),.707*UL),
            pp4.animate.move_to(NUMBER_PLANE.coords_to_point(*pqp4)),
            pplab.animate.next_to(NUMBER_PLANE.coords_to_point(*pqp4),.707*UL),
            pq4.animate.move_to(NUMBER_PLANE.coords_to_point(*prp4)),
            pqlab.animate.next_to(NUMBER_PLANE.coords_to_point(*prp4),.707*UL),
        )

        self.next_slide()

        self.play(
            FadeToColor(
                assoc_t,
                GREEN
            )
        )
        self.wait(0.3)

        self.play(
            Write(ident_t)
        )

        self.wait(1)

        ppp5 = [6,24]
        pp5 = Dot(NUMBER_PLANE.coords_to_point(*ppp5),color=YELLOW)
        pqp5 = [6,p-24]
        pq5 = Dot(NUMBER_PLANE.coords_to_point(*pqp5),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp4,pq4,pr4,prn4,ml,jl4,prlab,prnlab]],
            *[Create(x) for x in [pp5,pq5]],
            pplab.animate.next_to(NUMBER_PLANE.coords_to_point(*ppp5),.707*UL),
            pqlab.animate.next_to(NUMBER_PLANE.coords_to_point(*pqp5),.707*UL)
        )

        ml = Line(start=NUMBER_PLANE.coords_to_point(ppp5[0],0), end=NUMBER_PLANE.coords_to_point(ppp5[0],p-1))

        self.play(
            Create(ml),
        )

        infarrow = Arrow(
                start=U*4+.75*L+DR,
                end=UP*4+.75*L,
                color=RED
            )
        pointatinfinity_t = Tex("``The Point at Infinity''", color=RED).scale(.75).next_to(infarrow, DR)

        self.play(
            Create(infarrow),
            Write(pointatinfinity_t)
        )

        self.wait(2)
        self.play(
            FadeToColor(
                ident_t,
                GREEN
            )
        )

        self.next_slide()

        self.play(
            Write(inverse_t)
        )
        self.play(
            Transform(
                pqlab,
                Tex("$-P$",color=GREEN).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*pqp5), 0.707*UL)
            ),
            FadeToColor(
                pq5,
                GREEN
            )
        )

        self.next_slide()

        self.play(
            FadeToColor(
                inverse_t,
                GREEN
            )
        )

        self.play(
            *[FadeOut(x, shift=DOWN) for x in [closure_t, assoc_t, ident_t, inverse_t]]
        )

        self.wait(.5)

        mmulp = Tex("$kP=\\underbrace{P+P+P+\\ldots+P}_{k\\text{-times}}$").scale(.5).next_to(U+7*L)

        self.play(
            Write(mmulp)
        )

        self.wait(1)

        ppp6 = [4,13]
        pp6 = Dot(NUMBER_PLANE.coords_to_point(*ppp6),color=YELLOW)
        pqp6 = [4,13]
        pq6 = Dot(NUMBER_PLANE.coords_to_point(*pqp6),color=YELLOW)

        self.play(
            *[FadeOut(x) for x in [pp5,pq5,ml,pqlab,infarrow,pointatinfinity_t]],
            *[Create(x) for x in [pp6,pq6]],
            pplab.animate.next_to(NUMBER_PLANE.coords_to_point(*ppp6),.707*UL)
        )

        mlfn, disc = self.modline(p,ppp6,pqp6)
        ml = ParametricFunction(function=mlfn, t_range=[0, 36], discontinuities=disc)

        prp6 = [26,p-5]
        pr6 = Dot(NUMBER_PLANE.coords_to_point(*prp6),color=BLUE)

        prpn6 = [26,5]
        prn6 = Dot(NUMBER_PLANE.coords_to_point(*prpn6),color=RED)
        jl6 = Line(start=pr6, end=prn6, color=RED)

        prlab.next_to(NUMBER_PLANE.coords_to_point(*prp6),.707*UL)
        prnlab = Tex("$2P$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn6),.707*UL)
        self.play(
            Create(ml),
            Create(pr6),
        )
        self.play(
            Create(jl6),
            Create(prn6),
            Write(prnlab)
        )

        # next slide

        ppp7 = [4,13]
        pp7 = Dot(NUMBER_PLANE.coords_to_point(*ppp7),color=YELLOW)
        pqp7 = [26,5]
        pq7 = Dot(NUMBER_PLANE.coords_to_point(*pqp7),color=YELLOW)

        pqlab = Tex("$2P$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn6),.707*UL)

        self.play(
            *[FadeOut(x) for x in [pp6,pq6,pr6,jl6,ml,pqlab]],
            *[Create(x) for x in [pp7,pq7]],
            FadeIn(pqlab)
        )

        mlfn, disc = self.modline(p,ppp7,pqp7)
        ml = ParametricFunction(function=mlfn, t_range=[0, 36], discontinuities=disc)

        prp7 = [16,p-25]
        pr7 = Dot(NUMBER_PLANE.coords_to_point(*prp7),color=BLUE)

        prpn7 = [16,25]
        prn7 = Dot(NUMBER_PLANE.coords_to_point(*prpn7),color=RED)
        jl7 = Line(start=pr7, end=prn7, color=RED)

        prlab.next_to(NUMBER_PLANE.coords_to_point(*prp7),.707*UL)
        prnlab7 = Tex("$3P$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn7),.707*UL)
        self.play(
            Create(ml),
            Create(pr7),
        )
        self.play(
            Create(jl7),
            Create(prn7),
            Write(prnlab7)
        )

        # next slide

        ppp8 = [4,13]
        pp8 = Dot(NUMBER_PLANE.coords_to_point(*ppp8),color=YELLOW)
        pqp8 = [16,25]
        pq8 = Dot(NUMBER_PLANE.coords_to_point(*pqp8),color=YELLOW)

        pqlab = Tex("$3P$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn6),.707*UL)

        self.play(
            *[FadeOut(x) for x in [pp7,pq7,pr7,jl7,ml,pqlab]],
            *[Create(x) for x in [pp8,pq8]],
            FadeIn(pqlab)
        )

        mlfn, disc = self.modline(p,ppp8,pqp8)
        ml = ParametricFunction(function=mlfn, t_range=[0, 36], discontinuities=disc)

        prp8 = [18,p-10]
        pr8 = Dot(NUMBER_PLANE.coords_to_point(*prp8),color=BLUE)

        prpn8 = [18,10]
        prn8 = Dot(NUMBER_PLANE.coords_to_point(*prpn8),color=RED)
        jl8 = Line(start=pr8, end=prn8, color=RED)

        prlab.next_to(NUMBER_PLANE.coords_to_point(*prp8),.707*UL)
        prnlab8 = Tex("$4P$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn8),L)
        self.play(
            Create(ml),
            Create(pr8)
        )
        self.play(
            Create(jl8),
            Create(prn8),
            Write(prnlab8)
        )

        self.next_slide()

        self.play(
            Transform(
                prnlab8,
                Tex("$dP=H$",color=RED).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn8),L)
            ),
            Transform(
                prnlab7,
                Tex("$(d-1)P$",color=YELLOW).scale(.75).next_to(NUMBER_PLANE.coords_to_point(*prpn7),.707*UL)
            ),
            *[FadeOut(x) for x in [pqlab,prn6,prnlab]]
        )

        dpeqh = Tex("$dP=H$",color=RED).scale(.75).move_to(5*L+D)
        self.play(
            Write(dpeqh)
        )

    def modline(self, p, ppp, pqp):
        m = 0
        if (ppp[0] == pqp[0]) and (ppp[1] == pqp[1]):
            denom = pow(2*ppp[1], p-2, p)
            m = ((3*ppp[0]**2-2)*denom)%p
        else:
            denom = pow(pqp[0]-ppp[0], p-2, p)
            m = ((pqp[1]-ppp[1])*denom)%p

        disc = []
        x = 0
        i = -10

        while x < p:
            x = ((i*p-ppp[1])/m) + ppp[0]
            disc.append(x)
            i+=1

        def modlinefn(t):
            return NUMBER_PLANE.coords_to_point(t, (ppp[1] + m*(t-ppp[0]))%p)
        return (modlinefn, disc)

class EfficientMultiplication(Slide):

    def construct(self):
        a = Tex("$100P =$", "2(", "2[", "P + 2(", "2[2", "(P + 2P)", "]", ")", "]", ")").scale(1.5)
        a_1 = Tex("$100P =$", "2(", "2[", "P + 2(", "2[2", "(3P)", "]", ")", "]", ")").scale(1.5)
        a_2 = Tex("$100P =$", "2(", "2[", "P + 2(", "2[6P]", ")", "]", ")").scale(1.5)
        a_3 = Tex("$100P =$", "2(", "2[", "P + 2(", "12P", ")", "]", ")").scale(1.5)
        a_4 = Tex("$100P =$", "2(", "2[", "P + 24P", "]", ")").scale(1.5)
        a_5 = Tex("$100P =$", "2(", "2[", "25P", "]", ")").scale(1.5)
        a_6 = Tex("$100P =$", "2(", "50P", ")").scale(1.5)
        a_7 = Tex("$100P =$", "100P").scale(1.5)

        self.play(Write(a))

        self.next_slide()
        self.play(TransformMatchingTex(a, a_1))

        self.next_slide()
        self.play(TransformMatchingTex(a_1, a_2))

        self.next_slide()
        self.play(TransformMatchingTex(a_2, a_3))

        self.next_slide()
        self.play(TransformMatchingTex(a_3, a_4))

        self.next_slide()
        self.play(TransformMatchingTex(a_4, a_5))

        self.next_slide()
        self.play(TransformMatchingTex(a_5, a_6))

        self.next_slide()
        self.play(TransformMatchingTex(a_6, a_7))
        
        steps = Tex("We only need $\lceil \log_{2}d \\rceil$ steps").set_color(YELLOW)

        self.play(
            a_7.animate.move_to(UP),
            Write(steps)
        )
        pass

class GroupOrderScene(Slide):

    def construct(self):
        mul = Tex("$kP=\\underbrace{P+P+P+\\ldots+P}_{k\\text{-times}} = 0$").set_color(YELLOW)
        o = Tex("If $k = m * o(P)$ where $m \in \mathbb{Z}$")

        self.play(Write(mul))
        
        self.next_slide()
        
        self.play(
            mul.animate.move_to(UP),
            Write(o)
        )

        self.next_slide()

        img = ImageMobject("./order.png").scale(2.3)

        self.play(FadeOut(mul, shift=DOWN), FadeOut(o, shift=DOWN))
        self.play(FadeIn(img))

class ECDHScene(Slide):

    def construct(self):
        apos = LEFT*4.25
        bpos = RIGHT*4.5

        alice = Tex("Alice",color=YELLOW)
        alice.move_to(apos)
        self.play(Write(alice))
        
        bob = Tex("Bob")
        bob.move_to(bpos)
        self.play(Write(bob))

        arrow = ArcBetweenPoints(apos, bpos)
        arrow.add_tip(tip_length=.2)
        arrow.shift(DOWN*0.5)
        self.play(Create(arrow))

        h_a = Tex("$H_a$",color=YELLOW).scale(0.5).next_to(apos,UP*1.5+3*L)
        h_a_inf = Tex("(Alice's public key point)",color=YELLOW).scale(.5).next_to(h_a, R)
        d_a = Tex("$d_a$",color=YELLOW).scale(0.5).next_to(h_a,UP)
        d_a_inf = Tex("(Alice's private key)",color=YELLOW).scale(.5).next_to(d_a, R)
        h_b = Tex("$H_b$").scale(0.5).next_to(bpos,UP*1.5+3*L)
        h_b_inf = Tex("(Bob's public key point)").scale(.5).next_to(h_b, R)
        d_b = Tex("$d_b$").scale(0.5).next_to(h_b, U)
        d_b_inf = Tex("(Bob's private key)").scale(.5).next_to(d_b, R)
        self.play(*[Write(x) for x in [h_a,h_a_inf,d_a,d_a_inf,h_b,h_b_inf,d_b,d_b_inf]])

        self.next_slide()

        self.play(
            h_a.animate.next_to(bpos,UP*1.5+3*L),
            h_a_inf.animate.next_to(h_b,R),
            h_b.animate.next_to(apos,UP*1.5+3*L),
            h_b_inf.animate.next_to(h_a,R)
        )

        self.next_slide()

        self.play(
            *[FadeOut(x, shift=DOWN) for x in [h_a_inf,h_b_inf,d_a_inf,d_b_inf]],
            h_a.animate.scale(2),
            h_b.animate.scale(2),
            d_a.animate.scale(2),
            d_b.animate.scale(2),
        )

        self.play(
            h_a.animate.shift(R),
            h_b.animate.shift(R),
        )
        
        self.wait(.5)

        self.play(
            d_a.animate.next_to(h_b,.5*L),
            d_b.animate.next_to(h_a,.5*L),
        )

        self.wait(.5)

        h_a2 = Tex("$(d_a G)$").next_to(h_a,0)
        h_b2 = Tex("$(d_b G)$").next_to(h_b,0)
        h_a3 = Tex("$d_a G$").next_to(h_a,0)
        h_b3 = Tex("$d_b G$").next_to(h_b,0)

        self.play(
            Transform(
                h_a,
                h_a2
            ),
            Transform(
                h_b,
                h_b2
            ),
            d_a.animate.shift(.1*L),
            d_b.animate.shift(.1*L),
        )

        self.play(
            FadeToColor(d_a,WHITE),
            Transform(
                h_a,
                h_a3
            ),
            Transform(
                h_b,
                h_b3
            )
        )

        self.wait(.5)

        mid = UP*2
        eq = Tex("$=$").move_to(mid)

        lhs = VGroup(h_b,d_a)
        rhs = VGroup(h_a,d_b)

        self.play(
            Write(eq),
            lhs.animate.next_to(mid,1.2*L),
            rhs.animate.next_to(mid,1.2*R),
        )

        self.next_slide()

        eve = Tex("Eve",color=RED)
        indicator = Circle(radius=0.6).move_to(eve.get_center()).set_color(RED)

        self.play(Write(eve))
        self.play(Create(indicator))
        
        ecdlh = Tex("Elliptic Curve Discrete Logarithm Problem",color=YELLOW).move_to(UP)
        self.play(Write(ecdlh))

        self.next_slide()

        self.play(
            *[FadeOut(x, shift=DOWN) for x in [eve,indicator, lhs, rhs, eq, alice, bob, arrow]],
        )

        self.play(
            ecdlh.animate.move_to(3*UP)
        )

        attacks = BulletedList("Pohlig-Hellman", "Baby-Step Giant-Step", "Pollard's rho", "MOV attack", "Smart's attack", "Singular curve")
        attacks.align_to(ecdlh)

        self.play(
            LaggedStartMap(FadeIn, attacks, shift=0.5 * DOWN, lag_ratio=0.25)
        )

        eq = Tex("$Q = d*P$").next_to(attacks, DOWN)
        d_unknown = Tex("d = ?").next_to(eq, DOWN)

        self.play(Write(eq), Write(d_unknown))


def c2p(x,y):
    return NUMBER_PLANE.coords_to_point(x,y)

def ec1(t):
    a,b = -1,5
    c = 1.90416
    if t <= 0:
        x = -t - c
        return c2p(x, -((x**3 +a*x + b)**.5))
    x = t - c
    return c2p(x, (x**3 +a*x +b)**.5)

def ec2(t):
    a,b = 0,0
    c = 0
    if t <= 0:
        x = -t - c
        return c2p(x, -((x**3 + a*x + b)**.5))
    x = t - c
    return c2p(x, (x**3 + a*x + b)**.5)

def ec3(t):
    a,b = -3,2
    c = 2
    if t <= 0:
        x = -t - c
        return c2p(x, -((x**3 + a*x + b)**.5))
    x = t - c
    return c2p(x, (x**3 + a*x + b)**.5)

def ec4(t):
    a,b = -2,2
    c = 1.769
    if t <= 0:
        x = -t - c
        return c2p(x, -((x**3 + a*x + b)**.5))
    x = t - c
    return c2p(x, (x**3 + a*x + b)**.5)

def ec(t):
    a,b = -2,2
    c = 1.769
    if t <= 0:
        x = -t - c
        return c2p(x, -((x**3 + a*x + b)**.5))
    x = t - c
    return c2p(x, (x**3 + a*x + b)**.5)
