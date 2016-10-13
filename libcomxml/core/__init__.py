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
import re


def get_xml_default_encoding():
    xml_enc = 'UTF-8'

    return xml_enc


def clean_xml(xml_string):
    return re.sub('\s+<', '<', xml_string)


class Field(object):
    """Base Field class
    """

    def __init__(self, name, value=None, attributes=None, rep=None):
        """
        :param name: the name of the field super(Cabecera, self).__init__(name, root)
        :param value: the value of the field
        :param attributes: a dict with optional field attributes
        :param rep: function that returns the representation of 'value'
        """
        self.name = name
        self.__value = value
        self.attributes = attributes or {}
        self.rep = rep

    def get_value(self):
        """self.__value getter
        """
        # if we have a rep function, use it
        if self.rep and self.__value is not None:
            return self.rep(self.__value)
        # else, return the raw value
        return self.__value


    def set_value(self, value):
        """self.__value setter
        """
        self.__value = value


    value = property(get_value, set_value)


    def __str__(self):
        return (u"<Field:{0!s}>".format(self.name)).encode('utf8')

    def __unicode__(self):
        return unicode(self.__str__(), 'utf8')


class XmlField(Field):
    """Field with XML capabilities
    """
    def __init__(self, name, value=None, parent=None, attributes=None,
                 rep=None, namespace=None):
        """
        :param name: the name of the field super(Cabecera, self).__init__(name, root)
        :param value: the value of the field
        :param parent: the parent node
        :param attributes: a dict with optional field attributes
        :param rep: function that returns the representation of 'value'
        :param namespace: namespace associated with element
        """
        self.parent = parent
        self.xml_enc = get_xml_default_encoding()
        self.namespace = namespace

        super(XmlField, self).__init__(name, value=value,
                                       attributes=attributes, rep=rep)

    def _parse_list(self, element, value):
        for val in value:
            if isinstance(val, XmlField):
                val.parent = element.tag
                self.parse_value(element, val)
            elif isinstance(val, XmlModel):
                val.build_tree()
                element.append(val.doc_root)

    def _parse_value(self, element, value=None):
        """Generates the XML for the value according to its type
        """
        if not value:
            value = self.value
        if value is not None:
            if isinstance(value, str):
                element.text = unicode(value, 'utf8')
            elif isinstance(value, XmlField):
                element.append(value.element())
            elif isinstance(value, XmlModel):
                value.build_tree()
                element.append(value.doc_root)
            elif isinstance(value, list):
                self._parse_list(element, value)
            else:  # default: cast to unicode
                element.text = u"{0!s}".format(value)

        return element

    def element(self, parent=None):
        """Constructs the lxml.Element that represents the field

        :param parent: an etree Element to be used as parent for this one
        """
        if self.namespace:
            name = '{{{0!s}}}{1!s}'.format(self.namespace, self.name)
        else:
            name = self.name
        if parent is not None:
            ele = etree.SubElement(parent, name, **self.attributes)
        else:
            ele = etree.Element(name, **self.attributes)
        ele = self._parse_value(ele)
        return ele

    def __str__(self):
        """Returns the XML repr of the field

        It does not take care of the parent field, if any.
        """
        return etree.tostring(self.element(), encoding=self.xml_enc)

    def __unicode__(self):
        return unicode(self.__str__(), self.xml_enc)


class Model(object):
    """Base Model class
    """

    __fields = None
    _sort_order = None

    def __init__(self, name):
        self.name = name

    def sorted_fields(self):
        """Returns a sorted list of the model fields' names.
        """
        if self._sort_order:
            return [field for field in self._sort_order if field in dir(self)]
        return self._fields.keys()

    def _get_fields(self):
        """Lookups the fields of the model and store them in a dict using the
        field name as key.
        """
        #if self.__fields:
        #    return self.__fields
        fields = {}
        for member in dir(self):
            if not member.startswith('_'): 
                s_member = getattr(self, member)
                if (isinstance(s_member, Field) or
                    isinstance(s_member, Model) or
                    isinstance(s_member, list)):
                    fields[member] = s_member
        self.__fields = fields
        return fields

    _fields = property(fget=_get_fields)

    def feed(self, vals):
        """Populates the vals dictionary to the value property of the fields.

        :param vals: a dictionary with key:value pairs for this model's fields.
        """

        for key in vals:
            if hasattr(self, key):
                field = getattr(self, key)
                if isinstance(field, Field):
                    setattr(field, 'value', vals[key])
                elif isinstance(field, Model) and isinstance(vals[key], Model):
                    setattr(self, key, vals[key])
                else:
                    setattr(self, key, vals[key])


    def __str__(self):
        return (u"<Model:{0!s}>".format(self.name)).encode('utf8')

    def __unicode__(self):
        return unicode(self.__str__(), 'utf8')


class XmlModel(Model):
    """Model with XML capabilities

    This class is intended to be subclassed and used as follows:

    """

    def __init__(self, name, root, drop_empty=True):
        self.name = name
        super(XmlModel, self).__init__(name)
        self.root = getattr(self, root)
        self.doc_root = self.root.element()
        self.built = False
        self.drop_empty = drop_empty
        self._pretty_print = False
        self.xml_enc = get_xml_default_encoding()

    def set_xml_encoding(self, encoding):
        self.xml_enc = encoding

    def build_tree(self):
        """Bulids the tree with all the fields converted to Elements
        """
        if self.built:
            return
        self.doc_root = self.root.element()
        for key in self.sorted_fields():
            if key not in self._fields:
                continue
            field = self._fields[key]
            if field != self.root:
                if isinstance(field, XmlModel):
                    field.build_tree()
                    if (self.drop_empty and field.drop_empty
                        and len(field.doc_root) == 0):
                        continue
                    self.doc_root.append(field.doc_root)
                elif isinstance(field, list):
                    # we just allow XmlFields and XmlModels
                    # Also xml as str for memory management
                    for item in field:
                        if isinstance(item, XmlField):
                            ele = item.element()
                            if self.drop_empty and len(ele) == 0:
                                continue
                            self.doc_root.append(ele)
                        elif isinstance(item, XmlModel):
                            item.build_tree()
                            if self.drop_empty and len(item.doc_root) == 0:
                                continue
                            self.doc_root.append(item.doc_root)
                        elif isinstance(item, str):
                            ele = etree.fromstring(clean_xml(item))
                            self.doc_root.append(ele)
                        item = None
                elif (field.parent or self.root.name) == self.root.name:
                    ele = field.element()
                    if self.drop_empty and len(ele) == 0 and not ele.text:
                        continue
                    ele = field.element(parent=self.doc_root)
                else:
                    nodes = [n for n in self.doc_root.iterdescendants(
                                            tag=field.parent)]
                    if nodes:
                        ele = field.element()
                        if (self.drop_empty and len(ele) == 0 and not ele.text):
                            continue
                        ele = field.element(parent=nodes[0])
                    #else:
                    #    raise RuntimeError("No parent found!")
        self.built = True

    @property
    def pretty_print(self):
        return self._pretty_print

    @pretty_print.setter
    def pretty_print(self, val):
        if not isinstance(val, bool):
            raise TypeError
        self._pretty_print = val

    def __str__(self):
        return etree.tostring(self.doc_root, xml_declaration=True,
                              pretty_print=self.pretty_print,
                              encoding=self.xml_enc)

    def __unicode__(self):
        return unicode(self.__str__(), self.xml_enc)

    def serialize(self):
        return etree.tostring(
            self.doc_root, xml_declaration=True,
            pretty_print=self.pretty_print,
            encoding=self.xml_enc
        )
