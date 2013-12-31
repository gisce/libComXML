# -*- coding: utf-8 -*-
from . import unittest
import locale
import re
from libcomxml.core import XmlField, XmlModel


class Cd(XmlModel):
    def __init__(self):
        self.data = XmlField('CD')
        self.title = XmlField('TITLE')
        self.artist = XmlField('ARTIST')
        self.country = XmlField('COUNTRY')
        self.company = XmlField('COMPANY')
        self.price = XmlField('PRICE')
        self.year = XmlField('YEAR')
        super(Cd, self).__init__('CD', 'data')


class Catalog(XmlModel):
    def __init__(self):
        self.catalog = XmlField('CATALOG')
        self.cds = []
        super(Catalog, self).__init__('CATALOG', 'catalog')


class TestFields(unittest.TestCase):
    def setUp(self):
        self.field = XmlField('Quantity', '10000', attributes={'uom': 'unit'})

    def test_attributes(self):
        self.assertEqual(self.field.attributes, {'uom': 'unit'})
        self.assertEqual(self.field.element().items(), [('uom', 'unit')])

    def test_str(self):
        self.assertEqual(str(self.field),
                         '<Quantity uom="unit">10000</Quantity>')

    def test_value(self):
        self.assertEqual(self.field.element().text, '10000')

    def test_value_rep(self):
        formated = locale.format('%i', value=int(self.field.value),
                                 grouping=True)
        self.field.rep = lambda value: locale.format('%i', value=int(value),
                                                     grouping=True)
        self.assertEqual(formated, self.field.element().text)
        self.assertEqual(str(self.field),
                         '<Quantity uom="unit">%s</Quantity>' % formated)

    def test_update_attributes(self):
        self.field.attributes.update({'uom': 'kg'})
        self.assertEqual(self.field.attributes, {'uom': 'kg'})
        self.assertEqual(self.field.element().items(), [('uom', 'kg')])


class TestModel(unittest.TestCase):

    def setUp(self):
        self.xml = "<?xml version='1.0' encoding='UTF-8'?>\n"
        self.xml += re.sub('\s+<', '<', """
<CATALOG>
    <CD>
        <ARTIST>Bob Dylan</ARTIST>
        <COUNTRY>USA</COUNTRY>
        <COMPANY>Columbia</COMPANY>
        <TITLE>Empire Burlesque</TITLE>
        <YEAR>1985</YEAR>
        <PRICE>10.9</PRICE>
    </CD>
    <CD>
        <ARTIST>Bonnie Tyler</ARTIST>
        <COUNTRY>UK</COUNTRY>
        <COMPANY>CBS Records</COMPANY>
        <TITLE>Hide your hear</TITLE>
        <YEAR>1988</YEAR>
        <PRICE>9.9</PRICE>
    </CD>
</CATALOG>""")
        self.catalog = Catalog()
        cd = Cd()
        cd.feed({
            'title': 'Empire Burlesque',
            'artist': 'Bob Dylan',
            'country': 'USA',
            'company': 'Columbia',
            'price': 10.90,
            'year': 1985
        })

        self.catalog.cds.append(cd)
        cd = Cd()
        cd.feed({
            'title': 'Hide your hear',
            'artist': 'Bonnie Tyler',
            'country': 'UK',
            'company': 'CBS Records',
            'price': 9.90,
            'year': 1988
        })
        self.catalog.cds.append(cd)
        self.catalog.build_tree()

    def test_xml(self):
         self.assertEqual(str(self.catalog), self.xml)