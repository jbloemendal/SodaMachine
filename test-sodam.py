#!/anaconda/bin/python

'''
Copyright 2018 Jannis Bloemendal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

On Object State Testing (Adaptation Python)
D.C. Kunk, N. Suchak, J. Gao, P. Hsia
https://pdfs.semanticscholar.org/c099/37b9d87cf8020fc897b882c412229f5a7c68.pdf
'''

import unittest
from sodam import SodaMachine

class SodaMachineTest(unittest.TestCase):

    # test each methods
    def test_canWithDraw(self):
        sodaM = SodaMachine()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_add50c(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.canWithDraw())

    def test_return50cs(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.return50cs()
        self.assertEqual(False, sodaM.canWithDraw())
      
    def test_draw_path1(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.draw()
        self.assertEqual(False, sodaM.canWithDraw())
  
    def test_draw_path2(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.draw()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_reset(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.draw()
        sodaM.reset()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_Return1E(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.return50cs()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_add1E_d1E(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.draw()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.canWithDraw())

    def test_add200c(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.draw()
        self.assertEqual(True, sodaM.canWithDraw())

    '''
    Combinatorial test

    1) All combinations
    s m f n
    0 0 0 0   0E
    0 0 0 1   50c
    0 0 1 0   1E
    0 0 1 1   1E
    0 1 0 0   50c
    0 1 0 1   1E
    0 1 1 0   1E
    0 1 1 1   150c
    1 0 0 0   1E
    1 0 0 1   1E
    1 0 1 0   2E
    1 0 1 1   2E
    1 1 0 0   1E
    1 1 0 1   150c
    1 1 1 0   2E
    1 1 1 1   250c


    2) Two pair interaction?
    s m f n
    0 0 0 0   0E
    0 0 0 1   50c
    0 0 1 0   1E
    0 0 1 1   1E
    1 0 1 1   2E   ! s
    1 0 0 1   1E
    1 0 0 0   1E
    1 0 1 0   2E   ! f
    0 1 0 0   50c
    0 1 0 1   1E
    1 1 0 1   150c
    1 1 0 0   1E
    1 1 1 0   2E   ! f
    1 1 1 1   250c 
    0 1 1 1   150c ! s
    0 1 1 0   1E

    => fruits and soda
    '''

    def test_comb1(self):
        sodaM = SodaMachine()
        self.assertEqual(False, sodaM.draw(False, False, False, False))

    def test_comb2(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.draw(False, False, False, True))

    def test_comb3(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.draw(True, False, False, False))

    def test_comb4(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.draw(True, False, False, True))

if __name__ == '__main__':
    unittest.main()
