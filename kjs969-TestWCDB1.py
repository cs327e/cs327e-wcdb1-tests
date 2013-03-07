#!/usr/bin/env python

# ---------------------------
# Copyright (C) 2013
# Team: Better Late Than Never
# --------------------------

# -------
# imports
# -------

import StringIO
import unittest
import os
import xml.etree.ElementTree as ET

from WCDB1 import WCDB1_read, WCDB1_write, WCDB1_solve

# -----------
# TestWCDB1
# -----------

class TestWCDB1 (unittest.TestCase) :
 
    # -----------
    # WCDB1_read
    # -----------
    
    def test_read_1 (self):
        r = StringIO.StringIO("<country>\n<state></state>\n</country>")
        WCDB1_read(r)
        f = open("temp", 'r')
        lines = f.readlines()
        f.close()
        self.assert_(lines[0] == "<country>\n")
        self.assert_(lines[1] == "<state></state>\n")
        self.assert_(lines[2] == "</country>")

    
    def test_read_2 (self):
        r = StringIO.StringIO("<country></country>")
        WCDB1_read(r)
        f = open("temp", 'r')
        lines = f.readlines()
        f.close()
        self.assert_(lines[0] == "<country></country>")

    def test_read_3 (self):
        r = StringIO.StringIO("<a><b></b>\n<c><d>\n</d><e>\n</e></c></a>")
        WCDB1_read(r)
        f = open("temp", 'r')
        lines = f.readlines()
        f.close()
        self.assert_(lines[0] == "<a><b></b>\n")
        self.assert_(lines[1] == "<c><d>\n")
        self.assert_(lines[2] == "</d><e>\n")
        self.assert_(lines[3] == "</e></c></a>")


    # -----------
    # WCDB1_write
    # -----------
   
    def test_write_1 (self):
        f = open('temp', 'w')
        f.close()
        w = StringIO.StringIO()
        a = ET.Element('a')
        b = ET.SubElement(a, 'b')
        c = ET.SubElement(a, 'c')
        d = ET.SubElement(c, 'd')
        lst = ET.tostring(a)
        root = ET.fromstring(lst)
        tree = ET.ElementTree(root)
        WCDB1_write(w, tree)
        self.assert_(w.getvalue() == "<a><b /><c><d /></c></a>")
        
    def test_write_2 (self):
        f = open('temp', 'w')
        f.close()
        w = StringIO.StringIO()
        a = ET.Element('a')
        b = ET.SubElement(a, 'b')
        c = ET.SubElement(a, 'c')
        d = ET.SubElement(a, 'd')
        e = ET.SubElement(b, 'e')
        lst = ET.tostring(a)
        root = ET.fromstring(lst)
        tree = ET.ElementTree(root)
        WCDB1_write(w, tree)
        self.assert_(w.getvalue() == "<a><b><e /></b><c /><d /></a>")

    def test_write_3 (self):
        f = open('temp', 'w')
        f.close()
        w = StringIO.StringIO()
        a = ET.Element('a')
        b = ET.SubElement(a, 'b')
        c = ET.SubElement(a, 'c')
        d = ET.SubElement(a, 'd')
        e = ET.SubElement(b, 'e')
        f = ET.SubElement(c, 'f')
        g = ET.SubElement(f, 'g')
        lst = ET.tostring(a)
        root = ET.fromstring(lst)
        tree = ET.ElementTree(root)
        WCDB1_write(w, tree)
        self.assert_(w.getvalue() == "<a><b><e /></b><c><f><g /></f></c><d /></a>")
        
   
    # -----------
    # WCDB1_solve
    # -----------

    def test_solve_1 (self) :
        r = StringIO.StringIO("<WorldCrisisDatabase>\n<Crisis></Crisis>\n</WorldCrisisDatabase>")
        w = StringIO.StringIO()
        WCDB1_solve(r, w)
        self.assert_(w.getvalue() == "<WorldCrisisDatabase>\n<Crisis />\n</WorldCrisisDatabase>")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<a><b></b><c><d></d><e></e></c></a>")
        w = StringIO.StringIO()
        WCDB1_solve(r, w)
        self.assert_(w.getvalue() == "<a><b /><c><d /><e /></c></a>")
        
    def test_solve_3(self):
        
        w1 = StringIO.StringIO()
        w2 = StringIO.StringIO()
        r = StringIO.StringIO("""
    <Bookstore>
      <Book ISBN="ISBN-0-13-713526-2" Price="100" Authors="JU JW">
        <Title>A First Course in Database Systems</Title>
      </Book>
      <Book ISBN="ISBN-0-13-815504-6" Price="85" Authors="HG JU JW">
        <Title>Database Systems: The Complete Book</Title>
        <Remark>
          Amazon.com says: Buy this book bundled with
          <BookRef book="ISBN-0-13-713526-2" /> - a great deal!
        </Remark>
      </Book>
      <Author Ident="HG">
        <First_Name>Hector</First_Name>
        <Last_Name>Garcia-Molina</Last_Name>
      </Author>
      <Author Ident="JU">
        <First_Name>Jeffrey</First_Name>
        <Last_Name>Ullman</Last_Name>
      </Author>
      <Author Ident="JW">
        <First_Name>Jennifer</First_Name>
        <Last_Name>Widom</Last_Name>
      </Author>
    </Bookstore>
    """)
        WCDB1_solve(r, w1)
        r2 = StringIO.StringIO(w1.getvalue())
        WCDB1_solve(r2, w2)
        self.assert_(w1.getvalue() == w2.getvalue())




# ----
# main
# ----

print("TestWCDB1.py")
unittest.main()
print("Done.")
