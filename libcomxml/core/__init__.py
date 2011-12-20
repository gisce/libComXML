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
        """Constructor

        :param name: the name of the field
        :param value: the value of the field
        :param attributes: a dict with optional field attributes
        """
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
    def __init__(self, name, value=None, parent=None, attributes=None):
        """Constructor

        .. see: Field.__init__

        :param attribute: the name of the parent field, for the XML repr.
        """
        self.parent = parent
        super(XmlField, self).__init__(name, value=value, attributes=attributes)

    def _parse_value(self, element, value=None):
        """Generates the XML for the value according to its type
        """
        if not value:
            value = self.value
        if value:
            if isinstance(value, str):
                element.text = value
            elif isinstance(value, XmlField):
                element.append(value.element())
            elif isinstance(value, XmlModel):
                value.build_tree()
                element.append(value.doc_root)
            elif isinstance(value, list):
                for val in value:
                    if isinstance(val, XmlField):
                        val.parent = element.tag
                    self._parse_value(element, val)
            else:  # default: cast to string
                element.text = str(value)
        return element

    def element(self, parent=None):
        """Constructs the lxml.Element that represents the field

        :param parent: an etree Element to be used as parent for this one
        """
        if parent is not None:
            ele = etree.SubElement(parent, self.name, **self.attributes)
        else:
            ele = etree.Element(self.name, **self.attributes)
        ele = self._parse_value(ele)
        return ele

    def __str__(self):
        """Returns the XML repr of the field

        It does not take care of the parent field, if any.
        """
        return etree.tostring(self.element())

    def __unicode__(self):
        return self.__str__()


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
            return self._sort_order
        return self._fields.keys()


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
                if (isinstance(s_member, Field) or
                    isinstance(s_member, Model)):
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
                    field.value = vals[key]
                elif isinstance(field, Model) and isinstance(vals[key], Model):
                    field = vals[key]


    def __str__(self):
        return "<Model:%s>" % (self.name,)

    def __unicode__(self):
        return self.__str__()

class XmlModel(Model):
    """Model with XML capabilities

    This class is intended to be subclassed and used as follows:

    >>> from libcomxml.core import XmlField, XmlModel
    >>> class Cliente(XmlModel):
    ...     _sort_order = ('cliente', 'cli_urls', 'apellido1', 'apellido2',
    ...                    'nombre')
    ...     cliente = XmlField('Cliente')
    ...     nombre = XmlField('Nombre', value='Pepe', parent='Cliente')
    ...     apellido1 = XmlField('Apellido', value='Gotera', parent='Cliente')
    ...     apellido2 = XmlField('Apellido', value='Otilio', parent='Cliente')
    ...     cli_urls = XmlField('Urls', value=[
                        XmlField('Email', value='mailto:pepe@otilio.com'),
                        XmlField('XMPP', value='xmpp:pepe@otilio.com')
                        ], parent='Cliente')
    ...
    >>> class FacturaF1(XmlModel):
    ...     factura = XmlField('Factura')
    ...     numero = XmlField('Numero', value=1234, parent='Factura')
    ...     datos_cliente = Cliente('Cliente', root='cliente')
    ...
    >>> f1 = FacturaF1('Factura', root='factura')
    >>> f1.build_tree()
    >>> print(f1)
    <Factura><Cliente><Urls><Email>mailto:pepe@otilio.com</Email><XMPP>xmpp:pepe@otilio.com</XMPP></Urls><Apellido>Gotera</Apellido><Apellido>Otilio</Apellido><Nombre>Pepe</Nombre></Cliente><Numero>1234</Numero></Factura>
    """

    def __init__(self, name, root):
        self.name = name
        super(XmlModel, self).__init__(name)
        self.root = getattr(self, root)
        self.doc_root = self.root.element()


    def build_tree(self):
        """Bulids the tree with all the fields converted to Elements
        """
        for key in self.sorted_fields():
            field = self._fields[key]
            if field != self.root:
                if isinstance(field, XmlModel):
                    field.build_tree()
                    self.doc_root.append(field.doc_root)
                elif (field.parent or self.root.name) == self.root.name:
                    field = field.element(parent=self.doc_root)
                else:
                    nodes = [n for n in self.doc_root.iterdescendants(
                                            tag=field.parent)]
                    if nodes:
                        field = field.element(parent=nodes[0])
                    #else:
                    #    raise RuntimeError("No parent found!")


    def feed(self, vals):
        """On an XmlModel we have to rebuild the tree after feeding the fields'
        values.
        """
        super(XmlModel, self).feed(vals)
        self.build_tree()


    def __str__(self):
        return etree.tostring(self.doc_root)


    def __unicode__(self):
        return self.__str__()


