'''
Created on Jun 28, 2017

@author: Matt
'''
import unittest
import bowling


class Test(unittest.TestCase):
    def test_lower_case_perfect_game(self):
        x = bowling.calc_score("xxxxxxxxxxxx")
        print (x)
        self.assertEqual(x, "The total score for this game: 300")

    def test_upper_case_perfect_game(self):
        x = bowling.calc_score("XXXXXXXXXXXX")
        print (x)
        self.assertEqual(x, "The total score for this game: 300")
    
    def test_gutter_balls(self):
        x = bowling.calc_score("9-9-9-9-9-9-9-9-9-9-")
        print (x)
        self.assertEqual(x, "The total score for this game: 90")
    
    def test_spares(self):
        x = bowling.calc_score("5/5/5/5/5/5/5/5/5/5/5")
        print (x)
        self.assertEqual(x, "The total score for this game: 150")
    
    def test_mixed_game(self):
        x = bowling.calc_score("X7/9-X-88/-6XXX81")
        print (x)
        self.assertEqual(x, "The total score for this game: 167")
    
    def test_trim_white_space(self):
        x = bowling.calc_score(" X7/9-X-88/-6XXX81 ")
        print (x)
        self.assertEqual(x, "The total score for this game: 167")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()