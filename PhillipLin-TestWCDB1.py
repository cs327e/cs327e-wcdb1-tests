#!/usr/bin/env python

# ---------------------------
# cs327e-wcdb1/TestWCDB1.py
# Copyright (C) 2013
# Team: Byte Me
# --------------------------

# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.ElementTree

from WCDB1 import xml_read, xml_import, xml_export, wcdb1_solve

# -----------
# TestWCDB1
# -----------

class TestWCDB1 (unittest.TestCase) :
    # --------
    # xml_read
    # --------

    def test_read_1 (self) :
         r = StringIO.StringIO("<WorldCrisisDatabase><Crisis></Crisis></WorldCrisisDatabase>");
         xml_string = xml_read(r);
         self.assert_(xml_string == "<WorldCrisisDatabase><Crisis></Crisis></WorldCrisisDatabase>");

    def test_read_2 (self) :
         r = StringIO.StringIO("<WorldCrisisDatabase>\n<Crisis>\n</Crisis>\n</WorldCrisisDatabase>");
         xml_string = xml_read(r);
         self.assert_(xml_string == "<WorldCrisisDatabase>\n<Crisis>\n</Crisis>\n</WorldCrisisDatabase>");

    def test_read_3 (self) :
         r = StringIO.StringIO("<WorldCrisisDatabase>\t\t\t\n\t<Crisis>\t\t\n</Crisis>\n\t</WorldCrisisDatabase>");
         xml_string = xml_read(r);
         self.assert_(xml_string == "<WorldCrisisDatabase>\t\t\t\n\t<Crisis>\t\t\n</Crisis>\n\t</WorldCrisisDatabase>");

    # ----
    # xml_import
    # ----

    def test_import_1 (self) :
         ET = xml.etree.ElementTree
         r = "<WorldCrisisDatabase><Crisis></Crisis></WorldCrisisDatabase>"
         et = xml_import(ET, r)
         a = ET.Element('WorldCrisisDatabase')
         b = ET.SubElement(a, 'Crisis')
         self.assert_(ET.tostring(et, encoding="us-ascii", method="xml") == ET.tostring(a, encoding="us-ascii", method="xml"))

    def test_import_2 (self) :
         ET = xml.etree.ElementTree
         r = "<a><b></b><c><d></d><e></e></c></a>"
         et = xml_import(ET, r)
         a = ET.Element('a')
         b = ET.SubElement(a, 'b')
         c = ET.SubElement(a, 'c')
         d = ET.SubElement(c, 'd')
         e = ET.SubElement(c, 'e')
         self.assert_(ET.tostring(et, encoding="us-ascii", method="xml") == ET.tostring(a, encoding="us-ascii", method="xml"))

    def test_import_3 (self) :
         ET = xml.etree.ElementTree
         r = "<a><b></b><c><d/><e/></c></a>"
         et = xml_import(ET, r)
         a = ET.Element('a')
         b = ET.SubElement(a, 'b')
         c = ET.SubElement(a, 'c')
         d = ET.SubElement(c, 'd')
         e = ET.SubElement(c, 'e')
         self.assert_(ET.tostring(et, encoding="us-ascii", method="xml") == ET.tostring(a, encoding="us-ascii", method="xml"))

    # -----
    # xml_export
    # -----

    def test_export_1 (self) :
        ET = xml.etree.ElementTree 
        w = StringIO.StringIO()
        a = ET.Element('WorldCrisisDatabase')
        b = ET.SubElement(a, 'Crisis')
        xml_export(w, ET, a)
        self.assert_(w.getvalue() == "<WorldCrisisDatabase><Crisis /></WorldCrisisDatabase>")

    def test_export_2 (self) :
        ET = xml.etree.ElementTree 
        w = StringIO.StringIO()
        a = ET.Element('a')
        b = ET.SubElement(a, 'b')
        c = ET.SubElement(a, 'c')
        d = ET.SubElement(c, 'd')
        e = ET.SubElement(c, 'e')
        xml_export(w, ET, a)
        self.assert_(w.getvalue() == "<a><b /><c><d /><e /></c></a>")

    def test_export_3 (self) :
        ET = xml.etree.ElementTree 
        w = StringIO.StringIO()
        a = ET.Element('a')
        b = ET.SubElement(a, 'b')
        c = ET.SubElement(b, 'c')
        d = ET.SubElement(c, 'd')
        e = ET.SubElement(d, 'e')
        xml_export(w, ET, a)
        self.assert_(w.getvalue() == "<a><b><c><d><e /></d></c></b></a>")

    # -----------
    # wcdb1_solve
    # -----------

    def test_solve_1 (self) :
        ET = xml.etree.ElementTree
        r = StringIO.StringIO("<WorldCrisisDatabase><Crisis></Crisis></WorldCrisisDatabase>")
        w = StringIO.StringIO()
        wcdb1_solve(r, w, ET)
        self.assert_(w.getvalue() == "<WorldCrisisDatabase><Crisis /></WorldCrisisDatabase>")

    def test_solve_2 (self) :
        ET = xml.etree.ElementTree
        r = StringIO.StringIO("<a><b></b><c><d></d><e></e></c></a>")
        w = StringIO.StringIO()
        wcdb1_solve(r, w, ET)
        self.assert_(w.getvalue() == "<a><b /><c><d /><e /></c></a>")
        
    def test_solve_3 (self) :
        ET = xml.etree.ElementTree
        r = StringIO.StringIO("<a><b><c><d><e></e></d></c></b></a>")
        w = StringIO.StringIO()
        wcdb1_solve(r, w, ET)
        self.assert_(w.getvalue() == "<a><b><c><d><e /></d></c></b></a>")




# ----
# main
# ----

print("TestWCDB1.py")
unittest.main()
print("Done.")
