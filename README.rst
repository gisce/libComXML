=========
libComXML
=========

.. image:: https://travis-ci.org/gisce/libComXML.png?branch=master
    :target: https://travis-ci.org/gisce/libComXML
    :alt: Build Status
    
.. image:: https://coveralls.io/repos/github/gisce/libComXML/badge.svg?branch=master
    :target: https://coveralls.io/github/gisce/libComXML?branch=master


This library permits XML generation from Python objects

.. code-block:: xml

    <CATALOG>
      <CD>
        <TITLE>Empire Burlesque</TITLE>
        <ARTIST>Bob Dylan</ARTIST>
        <COUNTRY>USA</COUNTRY>
        <COMPANY>Columbia</COMPANY>
        <PRICE>10.90</PRICE>
        <YEAR>1985</YEAR>
      </CD>
      <CD>
        <TITLE>Hide your heart</TITLE>
        <ARTIST>Bonnie Tyler</ARTIST>
        <COUNTRY>UK</COUNTRY>
        <COMPANY>CBS Records</COMPANY>
        <PRICE>9.90</PRICE>
        <YEAR>1988</YEAR>
      </CD>
      <CD>
        <TITLE>Tupelo Honey</TITLE>
        <ARTIST>Van Morrison</ARTIST>
        <COUNTRY>UK</COUNTRY>
        <COMPANY>Polydor</COMPANY>
        <PRICE>8.20</PRICE>
        <YEAR>1971</YEAR>
      </CD>
    </CATALOG>


.. code-block:: python

    from libcomxml.core import XmlModel, XmlField


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


    catalog = Catalog()
    cd = Cd()
    cd.feed({
        'title': 'Empire Burlesque',
        'artist': 'Bob Dylan',
        'country': 'USA',
        'company': 'Columbia',
        'price': 10.90,
        'year': 1985
    })
    catalog.cds.append(cd)
    cd = Cd()
    cd.feed({
        'title': 'Hide your hear',
        'artist': 'Bonnie Tyler',
        'country': 'UK',
        'company': 'CBS Records',
        'price': 9.90,
        'year': 1988
    })
    catalog.cds.append(cd)
    # Also we can add XML String directly as a new element
    cd = """<CD>
            <TITLE>Tupelo Honey</TITLE>
            <ARTIST>Van Morrison</ARTIST>
            <COUNTRY>UK</COUNTRY>
            <COMPANY>Polydor</COMPANY>
            <PRICE>8.20</PRICE>
            <YEAR>1971</YEAR>
            </CD>"""
    self.catalog.cds.append(cd)
    catalog.build_tree()
    print catalog
