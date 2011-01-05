# -*- coding: utf-8 -*-

"""
Core classes for libComXML
==========================

This package contains the very basic classes needed for working with the
models that need to be mapped to XML.

"""

# etree import chain
try:
    from lxml import etree
except ImportError:
    try:
        import xml.etree.cElementTree as etree
    except ImportError:
        import xml.etree.ElementTree as etree


class Field(object):
    """Base Field class
    """
    def __init__(self, name, value=None, attributes=None):
        self.name = name
        self.value = value
        self.attributes = attributes or {}

    def __str__(self):
        return "<Field:%s>" % (self.name,)

    def __unicode__(self):
        return self.__str__()


class XmlField(Field):
    """Field with XML capabilities
    """
    def __init__(self, name, value=None, attributes=None):
        super(XmlField, self).__init__(name, value, attributes)

    def _parse_value(self, element, value=None):
        """Generates the XML for the value according to its type
        """
        if not value:
            value = self.value
        if isinstance(value, str):
            element.text = value
        elif isinstance(value, XmlField):
            element.append(value.element())
        elif isinstance(value, list):
            for val in value:
                self._parse_value(element, val)
        else:  # default: cast to string
            element.text = str(value)
        return element

    def element(self):
        """Constructs the lxml.Element that represents the field
        """
        ele = etree.Element(self.name, **self.attributes)
        ele = self._parse_value(ele)
        return ele

    def __str__(self):
        """Returns the XML repr of the field
        """
        return etree.tostring(self.element())

    def __unicode__(self):
        return self.__str__()


class Model(object):
    """Base Model class
    """

    __fields = None

    def __init__(self, name):
        self.name = name

    def _get_fields(self):
        """Lookups the fields of the model and store them in a dict using the
        field name as key.
        """
        if self.__fields:
            return self.__fields
        fields = {}
        for member in dir(self):
            if not member.startswith('_'): 
                s_member = getattr(self, member)
                if isinstance(s_member, Field):
                    fields[s_member.name] = s_member
        self.__fields = fields
        return fields

    _fields = property(fget=_get_fields)

    def __str__(self):
        return "<Model:%s>" % (self.name,)

    def __unicode__(self):
        return self.__str__()

class XmlModel(Model):
    """Model with XML capabilities

    """
    def __init__(self, name):
        self.name = name
        self.root = None
        super(XmlModel, self).__init__(name)

    def set_root(self, root):
        """Sets the root element of the XML representation
        """
        try:
            self.root = getattr(self, root)
        except AttributeError:
            raise AttributeError('You must have a root element')

    def element(self):
        """Constructs the lxml.Element that represents the model
        """
        if not self.root:
            raise NameError('self.root is not defined')
        if not isinstance(self.root, XmlField):
            return etree.Element(self.name)
        # all checks passed, let's return something interesting
        return self.root.element()

