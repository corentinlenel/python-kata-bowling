import package.test_bowling_game as tc

def suite():
    suite = tc.unittest.TestSuite()
    suite.addTest(tc.GameTest('setUp'))
    suite.addTest(tc.GameTest('test_gutter_game'))
    suite.addTest(tc.GameTest('test_all_ones'))
    suite.addTest(tc.GameTest('test_one_spare'))
    suite.addTest(tc.GameTest('test_one_strike'))
    suite.addTest(tc.GameTest('test_perfect_game'))
    suite.addTest(tc.GameTest('test_simple_game'))
    suite.addTest(tc.GameTest('test_last_strike'))
    return suite

if __name__ == '__main__':
    runner = tc.unittest.TextTestRunner(verbosity=10)
    runner.run(suite())



 