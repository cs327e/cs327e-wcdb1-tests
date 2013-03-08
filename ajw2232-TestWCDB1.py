# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 01:47:08 2013

@author: Tech Knuckle Support
"""



import StringIO
import unittest

from WCDB1 import WCDB_read, WCDB_print, WCDB_solve

class TestWCDB (unittest.TestCase):
    # ----
    # read
    # ----
    
    def test_read_1 (self):
        r = StringIO.StringIO("Test String")
        a = [""]
        p= WCDB_read(r, a)
        self.assert_(a[0] == "Test String")
        self.assert_(p == True)

    def test_read_2 (self):
        r = StringIO.StringIO("Test String\n Second Line")
        a = [""]
        p= WCDB_read(r, a)
        self.assert_(p == True)
        self.assert_(a[0] == "Test String\n")

    def test_read_3 (self):
        r = StringIO.StringIO("")
        a = [""]
        p= WCDB_read(r, a)
        self.assert_(p == False)
        self.assert_(a[0] == "")
#        
    #----
    # print
    #----
    
    def test_print_1 (self) :
        s = StringIO.StringIO("<Tree><Root>This</Root></Tree>")
        r = s.readline()
        w = StringIO.StringIO()
        WCDB_print(w, r)
        self.assert_(w.getvalue() == "<Tree><Root>This</Root></Tree>")    
    
    def test_print_2 (self) :
        s = StringIO.StringIO("<Should><Be><Same>Text</Same></Be></Should>")
        r = s.readline()
        w = StringIO.StringIO()
        WCDB_print(w, r)
        self.assert_(w.getvalue() == "<Should><Be><Same>Text</Same></Be></Should>")
        
    def test_print_3 (self) :
        s = StringIO.StringIO("<Should><Be><Same>Text</Same><Sub>Checking For Text</Sub></Be></Should>")
        r = s.readline()
        w = StringIO.StringIO()
        WCDB_print(w, r)
        self.assert_(w.getvalue() == "<Should><Be><Same>Text</Same><Sub>Checking For Text</Sub></Be></Should>")
#
#    # ----
#    # solve
#    # ----
#
    def test_solve_1 (self):
        r = StringIO.StringIO('<THU><Team><ACRush>string</ACRush><Jelly>string</Jelly><Cooly>string</Cooly></Team>\
<JiaJia><Team><Ahyangyi>string</Ahyangyi><Dragon>string</Dragon><Cooly><Amber>name</Amber></Cooly></Team>\
</JiaJia></THU>')
        w= StringIO.StringIO()
        WCDB_solve(r, w)
        self.assert_(w.getvalue() == '<THU><Team><ACRush>string</ACRush><Jelly>string</Jelly><Cooly>string</Cooly></Team>\
<JiaJia><Team><Ahyangyi>string</Ahyangyi><Dragon>string</Dragon><Cooly><Amber>name</Amber></Cooly></Team>\
</JiaJia></THU>')

    def test_solve_2 (self):
        r = StringIO.StringIO('<THU><Team><ACRush>again</ACRush><Jelly>again</Jelly><Cooly><Bob>again</Bob>\
</Cooly></Team><JiaJia><Team><Ahyangyi>text</Ahyangyi><Dragon>text</Dragon><Cooly><Amber>again</Amber>\
</Cooly></Team></JiaJia></THU>')
        w= StringIO.StringIO()
        WCDB_solve(r,w)
        self.assert_(w.getvalue() == '<THU><Team><ACRush>again</ACRush><Jelly>again</Jelly><Cooly><Bob>again</Bob>\
</Cooly></Team><JiaJia><Team><Ahyangyi>text</Ahyangyi><Dragon>text</Dragon><Cooly><Amber>again</Amber>\
</Cooly></Team></JiaJia></THU>')

    def test_solve_3 (self):
        r = StringIO.StringIO('<THU><Team><ACRush>Da</ACRush><Jelly>Fudge</Jelly><Cooly><Bob>Is</Bob></Cooly>\
</Team><JiaJia><Team><Ahyangyi>Going</Ahyangyi><Dragon>On</Dragon><Cooly><Amber>With</Amber></Cooly></Team>\
</JiaJia><Win><Team><Matt>This</Matt><Cooly>Piece of Bologna</Cooly></Team></Win></THU>')
        w= StringIO.StringIO()
        WCDB_solve(r,w)
        self.assert_(w.getvalue() == '<THU><Team><ACRush>Da</ACRush><Jelly>Fudge</Jelly><Cooly><Bob>Is</Bob></Cooly>\
</Team><JiaJia><Team><Ahyangyi>Going</Ahyangyi><Dragon>On</Dragon><Cooly><Amber>With</Amber></Cooly></Team>\
</JiaJia><Win><Team><Matt>This</Matt><Cooly>Piece of Bologna</Cooly></Team></Win></THU>')

print "TestWCDB1.py"
unittest.main()
print "Done"
    
