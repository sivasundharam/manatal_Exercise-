import unittest
from lottry import lottry_gam

 
class lottry_res_test(unittest.TestCase):

    ''' Class conatins 4 test cases for lottry game program'''

 
    def test_count_ball(self):

        '''test the length of the result'''

        co_li = lottry_gam()
        self.assertEqual(len(co_li),10,"Length of the result should be 10")

 

    def test_duplicate_ball(self):

        '''Test for duplicates in the result'''

        du_li = lottry_gam()
        self.assertEqual(len(du_li),len(set(du_li)),"There is duplicate in the result")

 

    def test_random_ball(self):

        '''Testing the consecutive results'''

        ran_li_1 = lottry_gam()
        ran_li_2 = lottry_gam()
        self.assertNotEqual(ran_li_1,ran_li_2, "Consecutive result are same")

 

    def test_intersection_ball(self):

        '''Testing the consecuitve result has no more than 5 ball matching'''

        in_li_1 = set(lottry_gam())
        in_li_2 = set(lottry_gam())
        in_len = len(list(in_li_1&in_li_2))
        
        if in_len > 5:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

 

 

 

 

if __name__ =="__main__":

    unittest.main()
