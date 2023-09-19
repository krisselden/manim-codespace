from manim import *
from scipy.special import comb


class NckRect(MovingCameraScene):
    def construct(self):
        n = 5
        k = 3
        nCk = comb(n, k, exact=True)
        rect = Rectangle(width=nCk, height=k)
        bu = BraceLabel(rect, r"{n \choose k}", UP)
        br = BraceLabel(rect, r"k", RIGHT)
        self.add(rect)

        self.play(GrowFromCenter(bu), GrowFromCenter(br))
        self.wait()

        fixed = Rectangle(width=comb(n-1, k-1, exact=True), height=1)
        fixed.align_to(rect, DL)
        left = Rectangle(width=comb(n-1, k-1, exact=True), height=k-1)
        left.align_to(rect, UL)
        right = Rectangle(width=comb(n-1, k, exact=True), height=k)
        right.align_to(rect, UR)

        bul = BraceLabel(left, "k - 1", LEFT)
        bfl = BraceLabel(fixed, "1", LEFT)
        bdl = BraceLabel(fixed, "{n-1 \choose k-1}", DOWN);
        bdr = BraceLabel(right, "{n-1 \choose k}", DOWN);

        self.play(GrowFromCenter(bdr), GrowFromCenter(bdl), GrowFromCenter(bul), GrowFromCenter(bfl), Create(left), Create(right))
        self.wait()
