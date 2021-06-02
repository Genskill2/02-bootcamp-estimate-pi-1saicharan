import math
import unittest
import random
def wallis(i):
    pi = 1
    while i!= 0:
        pi =  pi*float((4*(i**2))/((4*(i**2))-1))
        i -= 1
    return pi*2
#monte_carlo function
def monte_carlo(i):
    incircle = 0
    outcircle = 0
    for Needles in range(i):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            incircle += 1
        else :
            outcircle+=1
    area_of_circle = 4*(incircle/float(i))
    area_of_square = 4*((incircle+outcircle)/float(i))
#Counting needles in one quadrant only, so multiply by 4
    return 4*(area_of_circle/area_of_square)
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")

    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)

        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


if __name__ == "__main__":
    unittest.main()
# wallis function
