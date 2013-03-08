#!/usr/bin/env python

# ---------------------------
# projects/WCDB/TestWCDB1.py
# Copyright (C) 2013
# Team Virus
# ---------------------------

"""
To test the program:
    % python TestWCDB1.py >& TestWCDB1.out
    % chmod ugo+x TestWCDB1.py
    % TestWCDB1.py >& TestWCDB1.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from WCDB1 import main

# --------
# TestWCDB
# --------

class TestWCDB (unittest.TestCase) :

    def test_solve_1 (self) :
        r = StringIO.StringIO("<first>\n<second>\n</second>\n</first>")
        w = StringIO.StringIO()
        main(r, w)
        self.assert_(w.getvalue() == "<first>\n<second>\n</second>\n</first>")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<first>\n<second>\n<three>\n</three>\n</second>\n</first>")
        w = StringIO.StringIO()
        main(r, w)
        self.assert_(w.getvalue() == "<first>\n<second>\n<three>\n</three>\n</second>\n</first>")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<first><second></second></first>")
        w = StringIO.StringIO()
        main(r, w)
        self.assert_(w.getvalue() == "<first><second /></first>")



print "TestWCDB1.py"
unittest.main()
print "Done."
