# libComXML

This library permits XML generation from Python objects

```xml
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
</CATALOG>
```

```python
from libcomxml.core import XmlModel, XmlField


class Cd(XmlModel):
    def __init__(self, 'CD'):
        data = XmlField('CD')
        title = XmlField('TITLE')
        artist = XmlField('ARTIST')
        country = XmlField('COUNTRY')
        company = XmlField('COMPANY')
        price = XmlField('PRICE')
        year = XmlField('YEAR')


class Catalog(XmlModel):
    def __init__(self, 'CATALOG'):
        self.cds = []


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
catalog.build_tree()
print catalog
```
