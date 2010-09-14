# ./bindings/Facturacion.py
# PyXB bindings for NamespaceModule
# NSM:a83c9feab95e4a15cdca0fc67c51e0fb9e2c4f25
# Generated 2010-09-14 18:12:35.205680 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e26cece4-c01a-11df-9d3d-0025646a9043')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://localhost/elegibilidad', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a Python instance."""
    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=Namespace.fallbackNamespace(), location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)


# Atomic SimpleTypeDefinition
class Decimal14 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal14')
    _Documentation = None
Decimal14._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
Decimal14._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal14._InitializeFacetMap(Decimal14._CF_totalDigits,
   Decimal14._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal14', Decimal14)

# Atomic SimpleTypeDefinition
class X30 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X30')
    _Documentation = None
X30._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30L))
X30._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X30._InitializeFacetMap(X30._CF_maxLength,
   X30._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X30', X30)

# Atomic SimpleTypeDefinition
class STD_ANON (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
STD_ANON._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive,
   STD_ANON._CF_totalDigits,
   STD_ANON._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Version (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Version')
    _Documentation = None
Version._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
Version._InitializeFacetMap(Version._CF_length)
Namespace.addCategoryObject('typeBinding', u'Version', Version)

# Atomic SimpleTypeDefinition
class TipoVia (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo de Identificador de los datos del usuario
			AC	ACCESO
			AF	AFUERAS
			AG	AGRUPACI&#211;N
			AL	ALAMEDA
			AR	ARRABAL
			AU	AUTOP/AUTOV&#205;A
			AV	AVENIDA
			BC	BARRANCO
			BD	BARRIADA
			BL	BLOQUE
			BO	BARRIO
			CA	COLONIA
			CF	CALLEJ&#211;N
			CI	CARRIL
			CL	CALLE
			CM	COMPLEJO
			CN	CAMINO
			CO	COOPERATIVA
			CR	CARRETERA
			CS	CASA
			CT	CUESTA
			DI	DISEMINADO EXTRARRADIO
			ED	EDIFICIO
			EN	ENTRADA
			FC	FINCA
			FI	FICTICIO
			GL	GLORIETA
			GR	GRUPO
			MA	MAS&#205;A
			MU	MUELLE
			MZ	MANZANA
			NU	NUCLEO
			PA	PARQUE
			PB	POBLADO
			PD	PARTIDA
			PE	PASEO
			PI	POL.INDUSTRIAL
			PJ	PARAJE
			PL	PANTALAN
			PO	POL&#205;GONO
			PQ	PARQUE
			PR	PROLONGACI&#211;N
			PS	PASAJE
			PT	PLAZOLETA
			PY	PLAYA
			PZ	PLAZA
			RA	RAMBLA
			RD	RONDA
			RS	RESIDENCIAL
			SD	SENDA
			TR	TRAVES&#205;A
			UR	URBANIZACI&#211;N
			VI	VIAL
			ZN	ZONA
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoVia')
    _Documentation = u'Tipo de Identificador de los datos del usuario\n\t\t\tAC\tACCESO\n\t\t\tAF\tAFUERAS\n\t\t\tAG\tAGRUPACI\xd3N\n\t\t\tAL\tALAMEDA\n\t\t\tAR\tARRABAL\n\t\t\tAU\tAUTOP/AUTOV\xcdA\n\t\t\tAV\tAVENIDA\n\t\t\tBC\tBARRANCO\n\t\t\tBD\tBARRIADA\n\t\t\tBL\tBLOQUE\n\t\t\tBO\tBARRIO\n\t\t\tCA\tCOLONIA\n\t\t\tCF\tCALLEJ\xd3N\n\t\t\tCI\tCARRIL\n\t\t\tCL\tCALLE\n\t\t\tCM\tCOMPLEJO\n\t\t\tCN\tCAMINO\n\t\t\tCO\tCOOPERATIVA\n\t\t\tCR\tCARRETERA\n\t\t\tCS\tCASA\n\t\t\tCT\tCUESTA\n\t\t\tDI\tDISEMINADO EXTRARRADIO\n\t\t\tED\tEDIFICIO\n\t\t\tEN\tENTRADA\n\t\t\tFC\tFINCA\n\t\t\tFI\tFICTICIO\n\t\t\tGL\tGLORIETA\n\t\t\tGR\tGRUPO\n\t\t\tMA\tMAS\xcdA\n\t\t\tMU\tMUELLE\n\t\t\tMZ\tMANZANA\n\t\t\tNU\tNUCLEO\n\t\t\tPA\tPARQUE\n\t\t\tPB\tPOBLADO\n\t\t\tPD\tPARTIDA\n\t\t\tPE\tPASEO\n\t\t\tPI\tPOL.INDUSTRIAL\n\t\t\tPJ\tPARAJE\n\t\t\tPL\tPANTALAN\n\t\t\tPO\tPOL\xcdGONO\n\t\t\tPQ\tPARQUE\n\t\t\tPR\tPROLONGACI\xd3N\n\t\t\tPS\tPASAJE\n\t\t\tPT\tPLAZOLETA\n\t\t\tPY\tPLAYA\n\t\t\tPZ\tPLAZA\n\t\t\tRA\tRAMBLA\n\t\t\tRD\tRONDA\n\t\t\tRS\tRESIDENCIAL\n\t\t\tSD\tSENDA\n\t\t\tTR\tTRAVES\xcdA\n\t\t\tUR\tURBANIZACI\xd3N\n\t\t\tVI\tVIAL\n\t\t\tZN\tZONA\n\t\t\t'
TipoVia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoVia, enum_prefix=None)
TipoVia.AC = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'AC')
TipoVia.AF = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'AF')
TipoVia.AG = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'AG')
TipoVia.AL = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'AL')
TipoVia.AR = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'AR')
TipoVia.AU = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'AU')
TipoVia.AV = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'AV')
TipoVia.BC = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'BC')
TipoVia.BD = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'BD')
TipoVia.BL = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'BL')
TipoVia.BO = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'BO')
TipoVia.CA = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CA')
TipoVia.CF = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CF')
TipoVia.CI = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CI')
TipoVia.CL = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CL')
TipoVia.CM = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CM')
TipoVia.CN = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CN')
TipoVia.CO = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CO')
TipoVia.CR = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CR')
TipoVia.CS = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CS')
TipoVia.CT = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'CT')
TipoVia.DI = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'DI')
TipoVia.ED = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'ED')
TipoVia.EN = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'EN')
TipoVia.FC = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'FC')
TipoVia.FI = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'FI')
TipoVia.GL = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'GL')
TipoVia.GR = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'GR')
TipoVia.MA = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'MA')
TipoVia.MU = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'MU')
TipoVia.MZ = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'MZ')
TipoVia.NU = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'NU')
TipoVia.PA = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PA')
TipoVia.PB = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PB')
TipoVia.PD = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PD')
TipoVia.PE = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PE')
TipoVia.PI = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PI')
TipoVia.PJ = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PJ')
TipoVia.PL = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PL')
TipoVia.PO = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PO')
TipoVia.PQ = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PQ')
TipoVia.PR = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PR')
TipoVia.PS = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PS')
TipoVia.PT = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PT')
TipoVia.PY = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PY')
TipoVia.PZ = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'PZ')
TipoVia.RA = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'RA')
TipoVia.RD = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'RD')
TipoVia.RS = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'RS')
TipoVia.SD = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'SD')
TipoVia.TR = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'TR')
TipoVia.UR = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'UR')
TipoVia.VI = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'VI')
TipoVia.ZN = TipoVia._CF_enumeration.addEnumeration(unicode_value=u'ZN')
TipoVia._InitializeFacetMap(TipoVia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoVia', TipoVia)

# Atomic SimpleTypeDefinition
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(240L))
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_maxLength,
   STD_ANON_._CF_minLength)

# Atomic SimpleTypeDefinition
class Servicio (pyxb.binding.datatypes.integer, pyxb.binding.basis.enumeration_mixin):

    """servicio administrativo"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Servicio')
    _Documentation = u'servicio administrativo'
Servicio._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Servicio, enum_prefix=None)
Servicio._CF_enumeration.addEnumeration(unicode_value=u'001')
Servicio._CF_enumeration.addEnumeration(unicode_value=u'002')
Servicio._CF_enumeration.addEnumeration(unicode_value=u'003')
Servicio._CF_enumeration.addEnumeration(unicode_value=u'004')
Servicio._CF_enumeration.addEnumeration(unicode_value=u'005')
Servicio._CF_enumeration.addEnumeration(unicode_value=u'006')
Servicio._InitializeFacetMap(Servicio._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Servicio', Servicio)

# Atomic SimpleTypeDefinition
class Decimal4 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal4')
    _Documentation = None
Decimal4._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(4L))
Decimal4._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal4._InitializeFacetMap(Decimal4._CF_totalDigits,
   Decimal4._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal4', Decimal4)

# Atomic SimpleTypeDefinition
class X120 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X120')
    _Documentation = None
X120._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120L))
X120._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X120._InitializeFacetMap(X120._CF_maxLength,
   X120._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X120', X120)

# Atomic SimpleTypeDefinition
class CUPS (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CUPS')
    _Documentation = None
CUPS._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(22L))
CUPS._InitializeFacetMap(CUPS._CF_length)
Namespace.addCategoryObject('typeBinding', u'CUPS', CUPS)

# Atomic SimpleTypeDefinition
class TipoMoneda (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			01	Pesetas
			02	Euros
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoMoneda')
    _Documentation = u'\n\t\t\t01\tPesetas\n\t\t\t02\tEuros\n\t\t\t'
TipoMoneda._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoMoneda, enum_prefix=None)
TipoMoneda.n01 = TipoMoneda._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoMoneda.n02 = TipoMoneda._CF_enumeration.addEnumeration(unicode_value=u'02')
TipoMoneda._InitializeFacetMap(TipoMoneda._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoMoneda', TipoMoneda)

# Atomic SimpleTypeDefinition
class Decimal2 (pyxb.binding.datatypes.integer):

    """decimal de dos digitos"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal2')
    _Documentation = u'decimal de dos digitos'
Decimal2._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(2L))
Decimal2._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal2._InitializeFacetMap(Decimal2._CF_totalDigits,
   Decimal2._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal2', Decimal2)

# Atomic SimpleTypeDefinition
class IndicativoNSA (pyxb.binding.datatypes.string):

    """indicativo modificaciones administrativas (N no lleva modificaciones administrativas/ S tiene modificaciones administrativas/ A ambas)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoNSA')
    _Documentation = u'indicativo modificaciones administrativas (N no lleva modificaciones administrativas/ S tiene modificaciones administrativas/ A ambas)'
IndicativoNSA._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoNSA._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoNSA._CF_pattern.addPattern(pattern=u'N|S|A')
IndicativoNSA._InitializeFacetMap(IndicativoNSA._CF_length,
   IndicativoNSA._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoNSA', IndicativoNSA)

# Atomic SimpleTypeDefinition
class STD_ANON_2 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_2._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_2._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_totalDigits,
   STD_ANON_2._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Decimal7 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal7')
    _Documentation = None
Decimal7._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(7L))
Decimal7._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal7._InitializeFacetMap(Decimal7._CF_totalDigits,
   Decimal7._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal7', Decimal7)

# Atomic SimpleTypeDefinition
class X45 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X45')
    _Documentation = None
X45._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(45L))
X45._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X45._InitializeFacetMap(X45._CF_maxLength,
   X45._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X45', X45)

# Atomic SimpleTypeDefinition
class MarcaAparato (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MarcaAparato')
    _Documentation = None
MarcaAparato._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
MarcaAparato._InitializeFacetMap(MarcaAparato._CF_length)
Namespace.addCategoryObject('typeBinding', u'MarcaAparato', MarcaAparato)

# Atomic SimpleTypeDefinition
class AnomaliaMedida (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """codigo anomalia Medidas - Activacion
			01	Punto de Medida Inaccesible
			02	Punto de Medida Ilocalizable
			03	Presunto fraude
			04	Registrador apagado
			05	Registrador no comunica
			99	Otras anomalias
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnomaliaMedida')
    _Documentation = u'codigo anomalia Medidas - Activacion\n\t\t\t01\tPunto de Medida Inaccesible\n\t\t\t02\tPunto de Medida Ilocalizable\n\t\t\t03\tPresunto fraude\n\t\t\t04\tRegistrador apagado\n\t\t\t05\tRegistrador no comunica\n\t\t\t99\tOtras anomalias\n\t\t\t'
AnomaliaMedida._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AnomaliaMedida, enum_prefix=None)
AnomaliaMedida.n01 = AnomaliaMedida._CF_enumeration.addEnumeration(unicode_value=u'01')
AnomaliaMedida.n02 = AnomaliaMedida._CF_enumeration.addEnumeration(unicode_value=u'02')
AnomaliaMedida.n03 = AnomaliaMedida._CF_enumeration.addEnumeration(unicode_value=u'03')
AnomaliaMedida.n04 = AnomaliaMedida._CF_enumeration.addEnumeration(unicode_value=u'04')
AnomaliaMedida.n05 = AnomaliaMedida._CF_enumeration.addEnumeration(unicode_value=u'05')
AnomaliaMedida.n99 = AnomaliaMedida._CF_enumeration.addEnumeration(unicode_value=u'99')
AnomaliaMedida._InitializeFacetMap(AnomaliaMedida._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AnomaliaMedida', AnomaliaMedida)

# Atomic SimpleTypeDefinition
class IndicativoYCD (pyxb.binding.datatypes.string):

    """indicativo equipo medida (Y Ya instalado/ C Cliente Instala/ D Distribuidora Instala)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoYCD')
    _Documentation = u'indicativo equipo medida (Y Ya instalado/ C Cliente Instala/ D Distribuidora Instala)'
IndicativoYCD._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoYCD._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoYCD._CF_pattern.addPattern(pattern=u'Y|C|D')
IndicativoYCD._InitializeFacetMap(IndicativoYCD._CF_length,
   IndicativoYCD._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoYCD', IndicativoYCD)

# Atomic SimpleTypeDefinition
class EstadoTelefono (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Estado Telefono Tabla 41
			1	CORRECTO	
			2	NO PROBADO	
			3	L&#205;NEA TELEF. FUERA SERVICIO	
			4	M&#211;DEM NO ENLAZA	
			5	REGISTRADOR DESPROGRAMADO	
			6	FALLA LA DIRE DE ENLACE	
			7	FALLA EL PTO Y CLAVE MEDIDA	
			8	EL REGISTRAD O MIDE CEROS	
			9	OTRAS	
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EstadoTelefono')
    _Documentation = u'Estado Telefono Tabla 41\n\t\t\t1\tCORRECTO\t\n\t\t\t2\tNO PROBADO\t\n\t\t\t3\tL\xcdNEA TELEF. FUERA SERVICIO\t\n\t\t\t4\tM\xd3DEM NO ENLAZA\t\n\t\t\t5\tREGISTRADOR DESPROGRAMADO\t\n\t\t\t6\tFALLA LA DIRE DE ENLACE\t\n\t\t\t7\tFALLA EL PTO Y CLAVE MEDIDA\t\n\t\t\t8\tEL REGISTRAD O MIDE CEROS\t\n\t\t\t9\tOTRAS\t\n\t\t\t'
EstadoTelefono._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EstadoTelefono, enum_prefix=None)
EstadoTelefono.n1 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'1')
EstadoTelefono.n2 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'2')
EstadoTelefono.n3 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'3')
EstadoTelefono.n4 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'4')
EstadoTelefono.n5 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'5')
EstadoTelefono.n6 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'6')
EstadoTelefono.n7 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'7')
EstadoTelefono.n8 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'8')
EstadoTelefono.n9 = EstadoTelefono._CF_enumeration.addEnumeration(unicode_value=u'9')
EstadoTelefono._InitializeFacetMap(EstadoTelefono._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'EstadoTelefono', EstadoTelefono)

# Atomic SimpleTypeDefinition
class Puerta (pyxb.binding.datatypes.string):

    """Puerta"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Puerta')
    _Documentation = u'Puerta'
Puerta._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
Puerta._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
Puerta._InitializeFacetMap(Puerta._CF_maxLength,
   Puerta._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'Puerta', Puerta)

# Atomic SimpleTypeDefinition
class TipoReclamacion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo Reclamacion Tabla 57
			01-Atenci&#243;n personal
			02-Facturaci&#243;n
			03-Cobro
			04-Contrataci&#243;n
			05-Gesti&#243;n de Acometidas
			06-Calidad de Suministro
			07-Situaci&#243;n de Instalaciones
			08-Otros da&#241;os
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoReclamacion')
    _Documentation = u'Tipo Reclamacion Tabla 57\n\t\t\t01-Atenci\xf3n personal\n\t\t\t02-Facturaci\xf3n\n\t\t\t03-Cobro\n\t\t\t04-Contrataci\xf3n\n\t\t\t05-Gesti\xf3n de Acometidas\n\t\t\t06-Calidad de Suministro\n\t\t\t07-Situaci\xf3n de Instalaciones\n\t\t\t08-Otros da\xf1os\n\t\t\t'
TipoReclamacion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoReclamacion, enum_prefix=None)
TipoReclamacion.n01 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoReclamacion.n02 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'02')
TipoReclamacion.n03 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'03')
TipoReclamacion.n04 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'04')
TipoReclamacion.n05 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'05')
TipoReclamacion.n06 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'06')
TipoReclamacion.n07 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'07')
TipoReclamacion.n08 = TipoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'08')
TipoReclamacion._InitializeFacetMap(TipoReclamacion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoReclamacion', TipoReclamacion)

# Atomic SimpleTypeDefinition
class TipoAparato (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo Aparato
			BP	BLOQUE PRUEBAS	
			CA	CONTADOR ACTIVA	
			CC	CONTADOR COMBINADO	
			CG	CONTADOR REGISTRADOR	
			CO	CONTACTOR	
			CR	CONTADOR REACTIVA	
			CT	CONTADOR TARIFADOR	
			G	S.V.R.	
			H	U.M.P.	
			IH	INTERRUPTOR HORARIO	
			IP	I.C.P.	
			MO	MODEM	
			P	CONTADOR RPM	
			RG	REGISTRADOR	
			RT	RELE SELECTOR TENSION	
			TA	TARIFADOR	
			TC	TRANSFORMADOR COMBINADO	
			TI	TRANSFORMADOR INTENSIDAD	
			TP	TRNSFORMADOR POTENCIA	
			TT	TRNSFORMADOR DE TENSI&#211;N	
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoAparato')
    _Documentation = u'Tipo Aparato\n\t\t\tBP\tBLOQUE PRUEBAS\t\n\t\t\tCA\tCONTADOR ACTIVA\t\n\t\t\tCC\tCONTADOR COMBINADO\t\n\t\t\tCG\tCONTADOR REGISTRADOR\t\n\t\t\tCO\tCONTACTOR\t\n\t\t\tCR\tCONTADOR REACTIVA\t\n\t\t\tCT\tCONTADOR TARIFADOR\t\n\t\t\tG\tS.V.R.\t\n\t\t\tH\tU.M.P.\t\n\t\t\tIH\tINTERRUPTOR HORARIO\t\n\t\t\tIP\tI.C.P.\t\n\t\t\tMO\tMODEM\t\n\t\t\tP\tCONTADOR RPM\t\n\t\t\tRG\tREGISTRADOR\t\n\t\t\tRT\tRELE SELECTOR TENSION\t\n\t\t\tTA\tTARIFADOR\t\n\t\t\tTC\tTRANSFORMADOR COMBINADO\t\n\t\t\tTI\tTRANSFORMADOR INTENSIDAD\t\n\t\t\tTP\tTRNSFORMADOR POTENCIA\t\n\t\t\tTT\tTRNSFORMADOR DE TENSI\xd3N\t\n\t\t\t'
TipoAparato._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoAparato, enum_prefix=None)
TipoAparato.BP = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'BP')
TipoAparato.CA = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'CA')
TipoAparato.CC = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'CC')
TipoAparato.CG = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'CG')
TipoAparato.CO = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'CO')
TipoAparato.CR = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'CR')
TipoAparato.CT = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'CT')
TipoAparato.G = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'G')
TipoAparato.H = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'H')
TipoAparato.IH = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'IH')
TipoAparato.IP = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'IP')
TipoAparato.MO = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'MO')
TipoAparato.P = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'P')
TipoAparato.RG = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'RG')
TipoAparato.RT = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'RT')
TipoAparato.TA = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'TA')
TipoAparato.TC = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'TC')
TipoAparato.TI = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'TI')
TipoAparato.TP = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'TP')
TipoAparato.TT = TipoAparato._CF_enumeration.addEnumeration(unicode_value=u'TT')
TipoAparato._InitializeFacetMap(TipoAparato._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoAparato', TipoAparato)

# Atomic SimpleTypeDefinition
class CodigoMotivoRechazo (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """codigo motivo del rechazo
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoMotivoRechazo')
    _Documentation = u'codigo motivo del rechazo\n\t\t\t'
CodigoMotivoRechazo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodigoMotivoRechazo, enum_prefix=None)
CodigoMotivoRechazo.n01 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'01')
CodigoMotivoRechazo.n02 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'02')
CodigoMotivoRechazo.n03 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'03')
CodigoMotivoRechazo.n04 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'04')
CodigoMotivoRechazo.n05 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'05')
CodigoMotivoRechazo.n06 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'06')
CodigoMotivoRechazo.n07 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'07')
CodigoMotivoRechazo.n08 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'08')
CodigoMotivoRechazo.n09 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'09')
CodigoMotivoRechazo.n10 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'10')
CodigoMotivoRechazo.n11 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'11')
CodigoMotivoRechazo.n12 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'12')
CodigoMotivoRechazo.n13 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'13')
CodigoMotivoRechazo.n14 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'14')
CodigoMotivoRechazo.n15 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'15')
CodigoMotivoRechazo.n16 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'16')
CodigoMotivoRechazo.n17 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'17')
CodigoMotivoRechazo.n18 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'18')
CodigoMotivoRechazo.n19 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'19')
CodigoMotivoRechazo.n20 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'20')
CodigoMotivoRechazo.n21 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'21')
CodigoMotivoRechazo.n22 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'22')
CodigoMotivoRechazo.n23 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'23')
CodigoMotivoRechazo.n24 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'24')
CodigoMotivoRechazo.n25 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'25')
CodigoMotivoRechazo.n26 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'26')
CodigoMotivoRechazo.n27 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'27')
CodigoMotivoRechazo.n28 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'28')
CodigoMotivoRechazo.n29 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'29')
CodigoMotivoRechazo.n30 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'30')
CodigoMotivoRechazo.n31 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'31')
CodigoMotivoRechazo.n32 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'32')
CodigoMotivoRechazo.n33 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'33')
CodigoMotivoRechazo.n99 = CodigoMotivoRechazo._CF_enumeration.addEnumeration(unicode_value=u'99')
CodigoMotivoRechazo._InitializeFacetMap(CodigoMotivoRechazo._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CodigoMotivoRechazo', CodigoMotivoRechazo)

# Atomic SimpleTypeDefinition
class Potencia (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Potencia')
    _Documentation = None
Potencia._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
Potencia._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Potencia._InitializeFacetMap(Potencia._CF_totalDigits,
   Potencia._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Potencia', Potencia)

# Atomic SimpleTypeDefinition
class X2 (pyxb.binding.datatypes.string):

    """cadena de dos caracteres"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X2')
    _Documentation = u'cadena de dos caracteres'
X2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
X2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X2._InitializeFacetMap(X2._CF_maxLength,
   X2._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X2', X2)

# Atomic SimpleTypeDefinition
class X25 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X25')
    _Documentation = None
X25._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
X25._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X25._InitializeFacetMap(X25._CF_maxLength,
   X25._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X25', X25)

# Atomic SimpleTypeDefinition
class CodigoRegistro (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoRegistro')
    _Documentation = None
CodigoRegistro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
CodigoRegistro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
CodigoRegistro._InitializeFacetMap(CodigoRegistro._CF_maxLength,
   CodigoRegistro._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'CodigoRegistro', CodigoRegistro)

# Atomic SimpleTypeDefinition
class TipoPropiedadAparato (pyxb.binding.datatypes.string):

    """tipo de propiedad del aparato 1-Distribuidora 2-Cliente 3-Comercializadora 4-Otros"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoPropiedadAparato')
    _Documentation = u'tipo de propiedad del aparato 1-Distribuidora 2-Cliente 3-Comercializadora 4-Otros'
TipoPropiedadAparato._CF_pattern = pyxb.binding.facets.CF_pattern()
TipoPropiedadAparato._CF_pattern.addPattern(pattern=u'[1-4]')
TipoPropiedadAparato._InitializeFacetMap(TipoPropiedadAparato._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TipoPropiedadAparato', TipoPropiedadAparato)

# Atomic SimpleTypeDefinition
class MagnitudMedida (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MagnitudMedida')
    _Documentation = None
MagnitudMedida._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MagnitudMedida, enum_prefix=None)
MagnitudMedida.AE = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'AE')
MagnitudMedida.AS = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'AS')
MagnitudMedida.R1 = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'R1')
MagnitudMedida.R2 = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'R2')
MagnitudMedida.R3 = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'R3')
MagnitudMedida.R4 = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'R4')
MagnitudMedida.PM = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'PM')
MagnitudMedida.EP = MagnitudMedida._CF_enumeration.addEnumeration(unicode_value=u'EP')
MagnitudMedida._InitializeFacetMap(MagnitudMedida._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MagnitudMedida', MagnitudMedida)

# Atomic SimpleTypeDefinition
class MotivoRechazoSolicitudInfRegistroPS (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Motivos de rechazo a solicitud de informacion de registro de Punto de Suministro
			01 - Punto suministro Inexistente
			02 - Inexistencia de contrato regulado previo en vigor
			03 - CUPS no coincide con el CUPS del contrato regulado 
			04 - Numero contrato regulado previo no coincide con el aportado
			05 - Negativa del consumidor
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MotivoRechazoSolicitudInfRegistroPS')
    _Documentation = u'Motivos de rechazo a solicitud de informacion de registro de Punto de Suministro\n\t\t\t01 - Punto suministro Inexistente\n\t\t\t02 - Inexistencia de contrato regulado previo en vigor\n\t\t\t03 - CUPS no coincide con el CUPS del contrato regulado \n\t\t\t04 - Numero contrato regulado previo no coincide con el aportado\n\t\t\t05 - Negativa del consumidor\n\t\t\t'
MotivoRechazoSolicitudInfRegistroPS._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MotivoRechazoSolicitudInfRegistroPS, enum_prefix=None)
MotivoRechazoSolicitudInfRegistroPS.n01 = MotivoRechazoSolicitudInfRegistroPS._CF_enumeration.addEnumeration(unicode_value=u'01')
MotivoRechazoSolicitudInfRegistroPS.n02 = MotivoRechazoSolicitudInfRegistroPS._CF_enumeration.addEnumeration(unicode_value=u'02')
MotivoRechazoSolicitudInfRegistroPS.n03 = MotivoRechazoSolicitudInfRegistroPS._CF_enumeration.addEnumeration(unicode_value=u'03')
MotivoRechazoSolicitudInfRegistroPS.n04 = MotivoRechazoSolicitudInfRegistroPS._CF_enumeration.addEnumeration(unicode_value=u'04')
MotivoRechazoSolicitudInfRegistroPS.n05 = MotivoRechazoSolicitudInfRegistroPS._CF_enumeration.addEnumeration(unicode_value=u'05')
MotivoRechazoSolicitudInfRegistroPS._InitializeFacetMap(MotivoRechazoSolicitudInfRegistroPS._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MotivoRechazoSolicitudInfRegistroPS', MotivoRechazoSolicitudInfRegistroPS)

# Atomic SimpleTypeDefinition
class Escalera (pyxb.binding.datatypes.string):

    """Escalera"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Escalera')
    _Documentation = u'Escalera'
Escalera._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
Escalera._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
Escalera._InitializeFacetMap(Escalera._CF_maxLength,
   Escalera._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'Escalera', Escalera)

# Atomic SimpleTypeDefinition
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_3._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxLength,
   STD_ANON_3._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_4 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_4._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_4, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_4._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_4._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_minInclusive,
   STD_ANON_4._CF_totalDigits,
   STD_ANON_4._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class X20 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X20')
    _Documentation = None
X20._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
X20._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X20._InitializeFacetMap(X20._CF_maxLength,
   X20._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X20', X20)

# Atomic SimpleTypeDefinition
class STD_ANON_5 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_5._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
STD_ANON_5._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_totalDigits,
   STD_ANON_5._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class X15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X15')
    _Documentation = None
X15._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
X15._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X15._InitializeFacetMap(X15._CF_maxLength,
   X15._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X15', X15)

# Atomic SimpleTypeDefinition
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_maxLength,
   STD_ANON_6._CF_minLength)

# Atomic SimpleTypeDefinition
class TipoContrato (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """tipo de contrato  ATR  Tabla 9
			01	Anual
			02	Eventual
			03	Temporada
			04	Energia Adicional
			05	Suministro a instalaciones acogidos al regimen especial
			06	Interconexiones internacionales
			07	Suministro de Obras
			08	Suministro de Socorros
			09	Eventual a tanto alzado
			10	Pruebas
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoContrato')
    _Documentation = u'tipo de contrato  ATR  Tabla 9\n\t\t\t01\tAnual\n\t\t\t02\tEventual\n\t\t\t03\tTemporada\n\t\t\t04\tEnergia Adicional\n\t\t\t05\tSuministro a instalaciones acogidos al regimen especial\n\t\t\t06\tInterconexiones internacionales\n\t\t\t07\tSuministro de Obras\n\t\t\t08\tSuministro de Socorros\n\t\t\t09\tEventual a tanto alzado\n\t\t\t10\tPruebas\n\t\t\t'
TipoContrato._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoContrato, enum_prefix=None)
TipoContrato.n01 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoContrato.n02 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'02')
TipoContrato.n03 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'03')
TipoContrato.n04 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'04')
TipoContrato.n05 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'05')
TipoContrato.n06 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'06')
TipoContrato.n07 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'07')
TipoContrato.n08 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'08')
TipoContrato.n09 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'09')
TipoContrato.n10 = TipoContrato._CF_enumeration.addEnumeration(unicode_value=u'10')
TipoContrato._InitializeFacetMap(TipoContrato._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoContrato', TipoContrato)

# Atomic SimpleTypeDefinition
class Decimal12 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal12')
    _Documentation = None
Decimal12._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
Decimal12._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal12._InitializeFacetMap(Decimal12._CF_totalDigits,
   Decimal12._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal12', Decimal12)

# Atomic SimpleTypeDefinition
class Mes (Decimal12):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Mes')
    _Documentation = None
Mes._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Mes, value=pyxb.binding.datatypes.long(0L))
Mes._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=Mes, value=pyxb.binding.datatypes.long(12L))
Mes._InitializeFacetMap(Mes._CF_minInclusive,
   Mes._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'Mes', Mes)

# Atomic SimpleTypeDefinition
class TipoDHActiva (pyxb.binding.datatypes.string):

    """tipo de discriminacion horaria activa"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoDHActiva')
    _Documentation = u'tipo de discriminacion horaria activa'
TipoDHActiva._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
TipoDHActiva._InitializeFacetMap(TipoDHActiva._CF_length)
Namespace.addCategoryObject('typeBinding', u'TipoDHActiva', TipoDHActiva)

# Atomic SimpleTypeDefinition
class TipoAclaradorFinca (pyxb.binding.datatypes.string):

    """Tipo aclarador de finca	"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoAclaradorFinca')
    _Documentation = u'Tipo aclarador de finca\t'
TipoAclaradorFinca._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
TipoAclaradorFinca._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
TipoAclaradorFinca._InitializeFacetMap(TipoAclaradorFinca._CF_maxLength,
   TipoAclaradorFinca._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'TipoAclaradorFinca', TipoAclaradorFinca)

# Atomic SimpleTypeDefinition
class STD_ANON_7 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_7._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_7, value=pyxb.binding.datatypes.integer(0L))
STD_ANON_7._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(2L))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_minInclusive,
   STD_ANON_7._CF_totalDigits)

# Atomic SimpleTypeDefinition
class IndicativoTipoCambioTitular (pyxb.binding.datatypes.string):

    """indicativo de tipo de cambio de titular (T Traspaso/ S Subrogaci&#243;n/ J   Justo t&#237;tulo o cambio a su nombre/ B Baja y alta simult&#225;nea sin ruptura de ciclo/ H Baja y alta simult&#225;nea con lectura real y ruptura de facturaci&#243;n/ A Cambia solo datos administrativos: cuando se pide modificar datos del cliente que no afectan a la titularidad: direcci&#243;n de env&#237;o, tel&#233;fono de contacto...etc
)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoTipoCambioTitular')
    _Documentation = u'indicativo de tipo de cambio de titular (T Traspaso/ S Subrogaci\xf3n/ J   Justo t\xedtulo o cambio a su nombre/ B Baja y alta simult\xe1nea sin ruptura de ciclo/ H Baja y alta simult\xe1nea con lectura real y ruptura de facturaci\xf3n/ A Cambia solo datos administrativos: cuando se pide modificar datos del cliente que no afectan a la titularidad: direcci\xf3n de env\xedo, tel\xe9fono de contacto...etc\n)'
IndicativoTipoCambioTitular._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoTipoCambioTitular._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoTipoCambioTitular._CF_pattern.addPattern(pattern=u'T|S|J|B|H|A')
IndicativoTipoCambioTitular._InitializeFacetMap(IndicativoTipoCambioTitular._CF_length,
   IndicativoTipoCambioTitular._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoTipoCambioTitular', IndicativoTipoCambioTitular)

# Atomic SimpleTypeDefinition
class ExcesoPotFact (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExcesoPotFact')
    _Documentation = None
ExcesoPotFact._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
ExcesoPotFact._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
ExcesoPotFact._InitializeFacetMap(ExcesoPotFact._CF_totalDigits,
   ExcesoPotFact._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'ExcesoPotFact', ExcesoPotFact)

# Atomic SimpleTypeDefinition
class DecimalS10V2 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DecimalS10V2')
    _Documentation = None
DecimalS10V2._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
DecimalS10V2._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
DecimalS10V2._InitializeFacetMap(DecimalS10V2._CF_totalDigits,
   DecimalS10V2._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'DecimalS10V2', DecimalS10V2)

# Atomic SimpleTypeDefinition
class IndicativoNCD (pyxb.binding.datatypes.string):

    """indicativo ICP/Equipo (N no se sabe/ C aportado cliente/ D aportado Distribuidora)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoNCD')
    _Documentation = u'indicativo ICP/Equipo (N no se sabe/ C aportado cliente/ D aportado Distribuidora)'
IndicativoNCD._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoNCD._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoNCD._CF_pattern.addPattern(pattern=u'N|C|D')
IndicativoNCD._InitializeFacetMap(IndicativoNCD._CF_length,
   IndicativoNCD._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoNCD', IndicativoNCD)

# Atomic SimpleTypeDefinition
class STD_ANON_8 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_8._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_8._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_totalDigits,
   STD_ANON_8._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Energia (pyxb.binding.datatypes.integer):

    """Energia"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Energia')
    _Documentation = u'Energia'
Energia._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
Energia._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Energia._InitializeFacetMap(Energia._CF_totalDigits,
   Energia._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Energia', Energia)

# Atomic SimpleTypeDefinition
class X11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X11')
    _Documentation = None
X11._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(11L))
X11._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X11._InitializeFacetMap(X11._CF_maxLength,
   X11._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X11', X11)

# Atomic SimpleTypeDefinition
class TipoFactura (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			01	Normal
			02	Modificaci&#243;n de Contrato
			03	Baja de Contrato
			04	Derechos de Contratacion
			05	Deposito de garant&#237;a
			06	Inspecci&#243;n
			07	Atenciones (verificaciones, )
			08	Indemnizacion
			09	Intereses de demora
			10	Servicios
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoFactura')
    _Documentation = u'\n\t\t\t01\tNormal\n\t\t\t02\tModificaci\xf3n de Contrato\n\t\t\t03\tBaja de Contrato\n\t\t\t04\tDerechos de Contratacion\n\t\t\t05\tDeposito de garant\xeda\n\t\t\t06\tInspecci\xf3n\n\t\t\t07\tAtenciones (verificaciones, )\n\t\t\t08\tIndemnizacion\n\t\t\t09\tIntereses de demora\n\t\t\t10\tServicios\n\t\t\t'
TipoFactura._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoFactura, enum_prefix=None)
TipoFactura.n01 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoFactura.n02 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'02')
TipoFactura.n03 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'03')
TipoFactura.n04 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'04')
TipoFactura.n05 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'05')
TipoFactura.n06 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'06')
TipoFactura.n07 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'07')
TipoFactura.n08 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'08')
TipoFactura.n09 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'09')
TipoFactura.n10 = TipoFactura._CF_enumeration.addEnumeration(unicode_value=u'10')
TipoFactura._InitializeFacetMap(TipoFactura._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoFactura', TipoFactura)

# Atomic SimpleTypeDefinition
class X400 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X400')
    _Documentation = None
X400._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(400L))
X400._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X400._InitializeFacetMap(X400._CF_maxLength,
   X400._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X400', X400)

# Atomic SimpleTypeDefinition
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_9._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(17L))
STD_ANON_9._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_maxLength,
   STD_ANON_9._CF_minLength)

# Atomic SimpleTypeDefinition
class X1000 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X1000')
    _Documentation = None
X1000._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1000L))
X1000._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X1000._InitializeFacetMap(X1000._CF_maxLength,
   X1000._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X1000', X1000)

# Atomic SimpleTypeDefinition
class TiposEquipoMedida (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """codigo Tipos de Equipos de Medida
			L01	Tipo 1	
			L02	Tipo 2	
			L03	Tipo 3	
			L04	Tipo 4 - 6 per&#237;odos	
			L05	Tipo 4 - horario	
			L06	Tipo 5 - un per&#237;odo	
			L07	Tipo 5 - dos per&#237;odos	
			L08	Tipo 5 - seis per&#237;odos	
			L09	Tipo 5 - horario	
			L10	Tipo 4 - transitorio	
			R00	Sin discriminaci&#243;n Horaria	
			R01	Sin contador discriminador	
			R02	Dos per&#237;odos	
			R03	Tres per&#237;odos, sin discriminaci&#243;n de s&#225;bados y festivos	
			R04	Tres per&#237;odos, con discriminaci&#243;n de s&#225;bados y festivos	
			R05	Cinco per&#237;odos	
			R06	Seis per&#237;odos	
			R07	Siete per&#237;dos
			L00	El que corresponda Reglamentariamente		
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TiposEquipoMedida')
    _Documentation = u'codigo Tipos de Equipos de Medida\n\t\t\tL01\tTipo 1\t\n\t\t\tL02\tTipo 2\t\n\t\t\tL03\tTipo 3\t\n\t\t\tL04\tTipo 4 - 6 per\xedodos\t\n\t\t\tL05\tTipo 4 - horario\t\n\t\t\tL06\tTipo 5 - un per\xedodo\t\n\t\t\tL07\tTipo 5 - dos per\xedodos\t\n\t\t\tL08\tTipo 5 - seis per\xedodos\t\n\t\t\tL09\tTipo 5 - horario\t\n\t\t\tL10\tTipo 4 - transitorio\t\n\t\t\tR00\tSin discriminaci\xf3n Horaria\t\n\t\t\tR01\tSin contador discriminador\t\n\t\t\tR02\tDos per\xedodos\t\n\t\t\tR03\tTres per\xedodos, sin discriminaci\xf3n de s\xe1bados y festivos\t\n\t\t\tR04\tTres per\xedodos, con discriminaci\xf3n de s\xe1bados y festivos\t\n\t\t\tR05\tCinco per\xedodos\t\n\t\t\tR06\tSeis per\xedodos\t\n\t\t\tR07\tSiete per\xeddos\n\t\t\tL00\tEl que corresponda Reglamentariamente\t\t\n\t\t\t'
TiposEquipoMedida._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TiposEquipoMedida, enum_prefix=None)
TiposEquipoMedida.L01 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L01')
TiposEquipoMedida.L02 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L02')
TiposEquipoMedida.L03 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L03')
TiposEquipoMedida.L04 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L04')
TiposEquipoMedida.L05 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L05')
TiposEquipoMedida.L06 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L06')
TiposEquipoMedida.L07 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L07')
TiposEquipoMedida.L08 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L08')
TiposEquipoMedida.L09 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L09')
TiposEquipoMedida.L10 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L10')
TiposEquipoMedida.R00 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R00')
TiposEquipoMedida.R01 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R01')
TiposEquipoMedida.R02 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R02')
TiposEquipoMedida.R03 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R03')
TiposEquipoMedida.R04 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R04')
TiposEquipoMedida.R05 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R05')
TiposEquipoMedida.R06 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R06')
TiposEquipoMedida.R07 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R07')
TiposEquipoMedida.L00 = TiposEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L00')
TiposEquipoMedida._InitializeFacetMap(TiposEquipoMedida._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TiposEquipoMedida', TiposEquipoMedida)

# Atomic SimpleTypeDefinition
class TipoCodigoPeriodoDH (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			00	Totalizador
			01	Punta+Llano
			03	Valle
			10	Totalizador
			20	Totalizador
			21	Punta
			22	Llano+Valle
			30	Totalizador
			31	Punta
			32	Llano
			33	Valle
			40	Totalizador
			41	Punta
			42	Llano
			43	Valle
			50	Totalizador
			51	Punta Alto
			52	Llano
			53	Valle
			54	Supervalle
			55	Punta Pico
			60	Totalizador
			61	Periodo 1
			62	Per&#237;odo 2
			63	Per&#237;odo 3
			64	Per&#237;odo 4
			65	Per&#237;odo 5
			66	Per&#237;odo 6
			70	Totalizador
			71	Periodo 1
			72	Per&#237;odo 2
			73	Per&#237;odo 3
			74	Per&#237;odo 4
			75	Per&#237;odo 5
			76	Per&#237;odo 6
			77	Per&#237;odo 7
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoCodigoPeriodoDH')
    _Documentation = u'\n\t\t\t00\tTotalizador\n\t\t\t01\tPunta+Llano\n\t\t\t03\tValle\n\t\t\t10\tTotalizador\n\t\t\t20\tTotalizador\n\t\t\t21\tPunta\n\t\t\t22\tLlano+Valle\n\t\t\t30\tTotalizador\n\t\t\t31\tPunta\n\t\t\t32\tLlano\n\t\t\t33\tValle\n\t\t\t40\tTotalizador\n\t\t\t41\tPunta\n\t\t\t42\tLlano\n\t\t\t43\tValle\n\t\t\t50\tTotalizador\n\t\t\t51\tPunta Alto\n\t\t\t52\tLlano\n\t\t\t53\tValle\n\t\t\t54\tSupervalle\n\t\t\t55\tPunta Pico\n\t\t\t60\tTotalizador\n\t\t\t61\tPeriodo 1\n\t\t\t62\tPer\xedodo 2\n\t\t\t63\tPer\xedodo 3\n\t\t\t64\tPer\xedodo 4\n\t\t\t65\tPer\xedodo 5\n\t\t\t66\tPer\xedodo 6\n\t\t\t70\tTotalizador\n\t\t\t71\tPeriodo 1\n\t\t\t72\tPer\xedodo 2\n\t\t\t73\tPer\xedodo 3\n\t\t\t74\tPer\xedodo 4\n\t\t\t75\tPer\xedodo 5\n\t\t\t76\tPer\xedodo 6\n\t\t\t77\tPer\xedodo 7\n\t\t\t'
TipoCodigoPeriodoDH._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoCodigoPeriodoDH, enum_prefix=None)
TipoCodigoPeriodoDH.n00 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'00')
TipoCodigoPeriodoDH.n01 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoCodigoPeriodoDH.n03 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'03')
TipoCodigoPeriodoDH.n10 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'10')
TipoCodigoPeriodoDH.n20 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'20')
TipoCodigoPeriodoDH.n21 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'21')
TipoCodigoPeriodoDH.n22 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'22')
TipoCodigoPeriodoDH.n30 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'30')
TipoCodigoPeriodoDH.n31 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'31')
TipoCodigoPeriodoDH.n32 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'32')
TipoCodigoPeriodoDH.n33 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'33')
TipoCodigoPeriodoDH.n40 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'40')
TipoCodigoPeriodoDH.n41 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'41')
TipoCodigoPeriodoDH.n42 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'42')
TipoCodigoPeriodoDH.n43 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'43')
TipoCodigoPeriodoDH.n50 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'50')
TipoCodigoPeriodoDH.n51 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'51')
TipoCodigoPeriodoDH.n52 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'52')
TipoCodigoPeriodoDH.n53 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'53')
TipoCodigoPeriodoDH.n54 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'54')
TipoCodigoPeriodoDH.n55 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'55')
TipoCodigoPeriodoDH.n60 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'60')
TipoCodigoPeriodoDH.n61 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'61')
TipoCodigoPeriodoDH.n62 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'62')
TipoCodigoPeriodoDH.n63 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'63')
TipoCodigoPeriodoDH.n64 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'64')
TipoCodigoPeriodoDH.n65 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'65')
TipoCodigoPeriodoDH.n66 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'66')
TipoCodigoPeriodoDH.n70 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'70')
TipoCodigoPeriodoDH.n71 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'71')
TipoCodigoPeriodoDH.n72 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'72')
TipoCodigoPeriodoDH.n73 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'73')
TipoCodigoPeriodoDH.n74 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'74')
TipoCodigoPeriodoDH.n75 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'75')
TipoCodigoPeriodoDH.n76 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'76')
TipoCodigoPeriodoDH.n77 = TipoCodigoPeriodoDH._CF_enumeration.addEnumeration(unicode_value=u'77')
TipoCodigoPeriodoDH._InitializeFacetMap(TipoCodigoPeriodoDH._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoCodigoPeriodoDH', TipoCodigoPeriodoDH)

# Atomic SimpleTypeDefinition
class TipoActivacion (pyxb.binding.datatypes.string):

    """S = Activado con las condiciones solicitadas y A = Activado con las condiciones vigentes anteriores a la solicitud"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoActivacion')
    _Documentation = u'S = Activado con las condiciones solicitadas y A = Activado con las condiciones vigentes anteriores a la solicitud'
TipoActivacion._CF_pattern = pyxb.binding.facets.CF_pattern()
TipoActivacion._CF_pattern.addPattern(pattern=u'S|A')
TipoActivacion._InitializeFacetMap(TipoActivacion._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TipoActivacion', TipoActivacion)

# Atomic SimpleTypeDefinition
class Importe (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Importe')
    _Documentation = None
Importe._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
Importe._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Importe._InitializeFacetMap(Importe._CF_totalDigits,
   Importe._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Importe', Importe)

# Atomic SimpleTypeDefinition
class X9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X9')
    _Documentation = None
X9._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9L))
X9._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X9._InitializeFacetMap(X9._CF_maxLength,
   X9._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X9', X9)

# Atomic SimpleTypeDefinition
class STD_ANON_10 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_10._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_10._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_totalDigits,
   STD_ANON_10._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_11 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_11._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_11, value=pyxb.binding.datatypes.integer(0L))
STD_ANON_11._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_minInclusive,
   STD_ANON_11._CF_totalDigits)

# Atomic SimpleTypeDefinition
class DecimalS9V3 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DecimalS9V3')
    _Documentation = None
DecimalS9V3._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
DecimalS9V3._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
DecimalS9V3._InitializeFacetMap(DecimalS9V3._CF_totalDigits,
   DecimalS9V3._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'DecimalS9V3', DecimalS9V3)

# Atomic SimpleTypeDefinition
class CodigoContrato (Decimal12):

    """codigo contrato ATR"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoContrato')
    _Documentation = u'codigo contrato ATR'
CodigoContrato._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'CodigoContrato', CodigoContrato)

# Atomic SimpleTypeDefinition
class STD_ANON_12 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_12._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
STD_ANON_12._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_totalDigits,
   STD_ANON_12._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class TipoFacturaRectificadora (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			A	Anuladora
			B	Anuladora con Sustituyente
			N	Normal
			R	Rectificadora
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoFacturaRectificadora')
    _Documentation = u'\n\t\t\tA\tAnuladora\n\t\t\tB\tAnuladora con Sustituyente\n\t\t\tN\tNormal\n\t\t\tR\tRectificadora\n\t\t\t'
TipoFacturaRectificadora._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoFacturaRectificadora, enum_prefix=None)
TipoFacturaRectificadora.A = TipoFacturaRectificadora._CF_enumeration.addEnumeration(unicode_value=u'A')
TipoFacturaRectificadora.B = TipoFacturaRectificadora._CF_enumeration.addEnumeration(unicode_value=u'B')
TipoFacturaRectificadora.N = TipoFacturaRectificadora._CF_enumeration.addEnumeration(unicode_value=u'N')
TipoFacturaRectificadora.R = TipoFacturaRectificadora._CF_enumeration.addEnumeration(unicode_value=u'R')
TipoFacturaRectificadora._InitializeFacetMap(TipoFacturaRectificadora._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoFacturaRectificadora', TipoFacturaRectificadora)

# Atomic SimpleTypeDefinition
class STD_ANON_13 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_13._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15L))
STD_ANON_13._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_totalDigits,
   STD_ANON_13._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class CodigoDH (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Codigo DH   Tabla 52
			0 Sin Discriminacion
			1 Sin Contador Discriminador
			2 Tarifa 2.0 nocturna o contador con doble tarifa
			3 Con contador triple tarifa sin discriminacion sabados y festivos
			4 Con contador triple tarifa y discriminacion sabados y festivos	
			5 Con contador de quintuple tarifa	
			6 THP
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoDH')
    _Documentation = u'Codigo DH   Tabla 52\n\t\t\t0 Sin Discriminacion\n\t\t\t1 Sin Contador Discriminador\n\t\t\t2 Tarifa 2.0 nocturna o contador con doble tarifa\n\t\t\t3 Con contador triple tarifa sin discriminacion sabados y festivos\n\t\t\t4 Con contador triple tarifa y discriminacion sabados y festivos\t\n\t\t\t5 Con contador de quintuple tarifa\t\n\t\t\t6 THP\n\t\t\t'
CodigoDH._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodigoDH, enum_prefix=None)
CodigoDH.n0 = CodigoDH._CF_enumeration.addEnumeration(unicode_value=u'0')
CodigoDH.n1 = CodigoDH._CF_enumeration.addEnumeration(unicode_value=u'1')
CodigoDH.n2 = CodigoDH._CF_enumeration.addEnumeration(unicode_value=u'2')
CodigoDH.n3 = CodigoDH._CF_enumeration.addEnumeration(unicode_value=u'3')
CodigoDH.n4 = CodigoDH._CF_enumeration.addEnumeration(unicode_value=u'4')
CodigoDH.n5 = CodigoDH._CF_enumeration.addEnumeration(unicode_value=u'5')
CodigoDH.n6 = CodigoDH._CF_enumeration.addEnumeration(unicode_value=u'6')
CodigoDH._InitializeFacetMap(CodigoDH._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CodigoDH', CodigoDH)

# Atomic SimpleTypeDefinition
class STD_ANON_14 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_14._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_14, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_14._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
STD_ANON_14._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_minInclusive,
   STD_ANON_14._CF_totalDigits,
   STD_ANON_14._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Procedencia (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """10 Telemedida
11 Telemedida corregida
20 TPL
21 TPL corregida
30 Visual
31 Visual corregida
40 Estimada
50 Autolectura
99 Sin lectura"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Procedencia')
    _Documentation = u'10 Telemedida\n11 Telemedida corregida\n20 TPL\n21 TPL corregida\n30 Visual\n31 Visual corregida\n40 Estimada\n50 Autolectura\n99 Sin lectura'
Procedencia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Procedencia, enum_prefix=None)
Procedencia.n10 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'10')
Procedencia.n11 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'11')
Procedencia.n20 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'20')
Procedencia.n21 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'21')
Procedencia.n30 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'30')
Procedencia.n31 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'31')
Procedencia.n40 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'40')
Procedencia.n50 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'50')
Procedencia.n99 = Procedencia._CF_enumeration.addEnumeration(unicode_value=u'99')
Procedencia._InitializeFacetMap(Procedencia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Procedencia', Procedencia)

# Atomic SimpleTypeDefinition
class STD_ANON_15 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_15._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_15._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_totalDigits,
   STD_ANON_15._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Tarifa (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """tipo Tarifa  
			001	2.0.A	
			002	2.0.N.A 	
			003	3.0A	
			004	2.0DHA					
			011	3.1A	
			012	6.1	
			013	6.2	
			014	6.3	
			015	6.4	
			016	6.5
			027	1.2.P	1.2.P	GRAL. C.U. 36 A 72,5 KV PEAJES
			028	3.0.P	3.0.P	B.T. PEAJES GRAL.UT. NORMAL
			029	4.0.P	4.0.P	B.T. PEAJES GRAL.LARGA UT.
			030	B.0.P	B.0.P	ALUMBRADO PUBLICO PEAJES
			031	B6.4	B6.4	PEAJE AT IMPORTACION  145 KV
			032	D.1.P	D.1.P	A.T. DISTRIB.PEAJ.36KV
			033	D.2.P	D.2.P	A.T. DISTRIB.PEAJ.36-72,5KV
			034	D.3.P	D.3.P	A.T. DISTRIB.PEAJ.72,5-145KV
			035	D.4.P	D.4.P	A.T. DISTRIB.PEAJ.145KV
			036	GAT1P	GAT1P	GRAL. AT 1 KV A . 14 KV PEAJES
			037	GAT2P	GAT2P	GRAL. AT 14 KV A . 36 KV PEAJE
			038	GAT3P	GAT3P	GRAL. AT 36 A. 72,5 KV PEAJES
			039	GAT4P	GAT4P	GRAL. AT 72,5 A . 145 KV PEAJE
			040	GAT5P	GAT5P	GRAL. AT .145 KV. PEAJES
			041	R.0.P	R.0.P	B.T. PEAJES RIEGOS AGRICOLAS
			042	T.1.P	T.1.P	A.T.TRACC.PEAJ . 36 KV
			043	T.2.P	T.2.P	A.T.TRACC.PEAJ. 36,72,5 KV  
			044	T.3.P	T.3.P	A.T.TRACC.PEAJ. 72,5 KV
			045	TAGA1	TAGA1	GRAL AT  PEAJE TRAMO 1 TENSION
			046	TAGA2	TAGA2	GRAL AT  PEAJE TRAMO 2 TENSION
			047	TAGA3	TAGA3	GRAL AT  PEAJE TRAMO 3 TENSION
			048	TAGA4	TAGA4	GRAL AT  PEAJE TRAMO 4 TENSION
			049	TAGA5	TAGA5	GRAL AT  PEAJE TRAMO 5 TENSION
			050	TAGA6	TAGA6	TARIFA CONEXION INTERNACIONAL
			101	T.1	
			102	T.2	
			103	T.3	
			110	1.0	
			111	R.1	
			112	R.2	
			113	R.3	
			120	2.0	
			122	G4, 36 kV  T  72,5 kV	
			123	G4, 72,5 kV , T , 145 kV	
			124	G4, T . 145 kV	
			130	2.0N	
			131	D.1	
			132	D.2	
			133	D.3	
			134	D.4	
			141	T.H.P.  T.36kV	
			142	T.H.P.  36 kV . T . 72,5 kV	
			143	T.H.P.  72,5 kV  T .145 kV	
			144	T.H.P.  T . 145 kV	
			299	PEAJE TAJO.SEGURA	
			300	TRASVASE TAJO SEGURA	
			310	3.0	
			410	4.0	
			500	EMPLEADOS	
			501	CONSUMOS PROPIOS	
			502	CONSUMOS OTRAS ACTIVIDADES	
			503	CONSUMOS GRATUITOS	
			504	CONCESIONES ADMINISTRATIVAS	
			505	CONCESIONES ADMVAS. TAJO.SEGURA	
			510	B.0	
			520	R.0	
			610	1.1	
			620	1.1 INT	
			640	2.1	
			650	2.1 INT	
			660	3.1	
			670	3.1 INT	
			710	1.2		
			720	1.2 INT	
			730	2.2	
			740	2.2 INT	
			750	3.2	
			760	3.2 INT	
			810	1.3	
			820	1.3 INT	
			840	2.3	
			850	2.3 INT	
			860	3.3	
			870	3.3 INT	
			901   Tf. Peaje BT 2.0  Modo 2
			902   Tf. Peaje BT 2.0N Modo 2
			910	1.4	
			920	1.4 INT	
			940	2.4	
			950	2.4 INT	
			960	3.4	
			970	3.4 INT	
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Tarifa')
    _Documentation = u'tipo Tarifa  \n\t\t\t001\t2.0.A\t\n\t\t\t002\t2.0.N.A \t\n\t\t\t003\t3.0A\t\n\t\t\t004\t2.0DHA\t\t\t\t\t\n\t\t\t011\t3.1A\t\n\t\t\t012\t6.1\t\n\t\t\t013\t6.2\t\n\t\t\t014\t6.3\t\n\t\t\t015\t6.4\t\n\t\t\t016\t6.5\n\t\t\t027\t1.2.P\t1.2.P\tGRAL. C.U. 36 A 72,5 KV PEAJES\n\t\t\t028\t3.0.P\t3.0.P\tB.T. PEAJES GRAL.UT. NORMAL\n\t\t\t029\t4.0.P\t4.0.P\tB.T. PEAJES GRAL.LARGA UT.\n\t\t\t030\tB.0.P\tB.0.P\tALUMBRADO PUBLICO PEAJES\n\t\t\t031\tB6.4\tB6.4\tPEAJE AT IMPORTACION  145 KV\n\t\t\t032\tD.1.P\tD.1.P\tA.T. DISTRIB.PEAJ.36KV\n\t\t\t033\tD.2.P\tD.2.P\tA.T. DISTRIB.PEAJ.36-72,5KV\n\t\t\t034\tD.3.P\tD.3.P\tA.T. DISTRIB.PEAJ.72,5-145KV\n\t\t\t035\tD.4.P\tD.4.P\tA.T. DISTRIB.PEAJ.145KV\n\t\t\t036\tGAT1P\tGAT1P\tGRAL. AT 1 KV A . 14 KV PEAJES\n\t\t\t037\tGAT2P\tGAT2P\tGRAL. AT 14 KV A . 36 KV PEAJE\n\t\t\t038\tGAT3P\tGAT3P\tGRAL. AT 36 A. 72,5 KV PEAJES\n\t\t\t039\tGAT4P\tGAT4P\tGRAL. AT 72,5 A . 145 KV PEAJE\n\t\t\t040\tGAT5P\tGAT5P\tGRAL. AT .145 KV. PEAJES\n\t\t\t041\tR.0.P\tR.0.P\tB.T. PEAJES RIEGOS AGRICOLAS\n\t\t\t042\tT.1.P\tT.1.P\tA.T.TRACC.PEAJ . 36 KV\n\t\t\t043\tT.2.P\tT.2.P\tA.T.TRACC.PEAJ. 36,72,5 KV  \n\t\t\t044\tT.3.P\tT.3.P\tA.T.TRACC.PEAJ. 72,5 KV\n\t\t\t045\tTAGA1\tTAGA1\tGRAL AT  PEAJE TRAMO 1 TENSION\n\t\t\t046\tTAGA2\tTAGA2\tGRAL AT  PEAJE TRAMO 2 TENSION\n\t\t\t047\tTAGA3\tTAGA3\tGRAL AT  PEAJE TRAMO 3 TENSION\n\t\t\t048\tTAGA4\tTAGA4\tGRAL AT  PEAJE TRAMO 4 TENSION\n\t\t\t049\tTAGA5\tTAGA5\tGRAL AT  PEAJE TRAMO 5 TENSION\n\t\t\t050\tTAGA6\tTAGA6\tTARIFA CONEXION INTERNACIONAL\n\t\t\t101\tT.1\t\n\t\t\t102\tT.2\t\n\t\t\t103\tT.3\t\n\t\t\t110\t1.0\t\n\t\t\t111\tR.1\t\n\t\t\t112\tR.2\t\n\t\t\t113\tR.3\t\n\t\t\t120\t2.0\t\n\t\t\t122\tG4, 36 kV  T  72,5 kV\t\n\t\t\t123\tG4, 72,5 kV , T , 145 kV\t\n\t\t\t124\tG4, T . 145 kV\t\n\t\t\t130\t2.0N\t\n\t\t\t131\tD.1\t\n\t\t\t132\tD.2\t\n\t\t\t133\tD.3\t\n\t\t\t134\tD.4\t\n\t\t\t141\tT.H.P.  T.36kV\t\n\t\t\t142\tT.H.P.  36 kV . T . 72,5 kV\t\n\t\t\t143\tT.H.P.  72,5 kV  T .145 kV\t\n\t\t\t144\tT.H.P.  T . 145 kV\t\n\t\t\t299\tPEAJE TAJO.SEGURA\t\n\t\t\t300\tTRASVASE TAJO SEGURA\t\n\t\t\t310\t3.0\t\n\t\t\t410\t4.0\t\n\t\t\t500\tEMPLEADOS\t\n\t\t\t501\tCONSUMOS PROPIOS\t\n\t\t\t502\tCONSUMOS OTRAS ACTIVIDADES\t\n\t\t\t503\tCONSUMOS GRATUITOS\t\n\t\t\t504\tCONCESIONES ADMINISTRATIVAS\t\n\t\t\t505\tCONCESIONES ADMVAS. TAJO.SEGURA\t\n\t\t\t510\tB.0\t\n\t\t\t520\tR.0\t\n\t\t\t610\t1.1\t\n\t\t\t620\t1.1 INT\t\n\t\t\t640\t2.1\t\n\t\t\t650\t2.1 INT\t\n\t\t\t660\t3.1\t\n\t\t\t670\t3.1 INT\t\n\t\t\t710\t1.2\t\t\n\t\t\t720\t1.2 INT\t\n\t\t\t730\t2.2\t\n\t\t\t740\t2.2 INT\t\n\t\t\t750\t3.2\t\n\t\t\t760\t3.2 INT\t\n\t\t\t810\t1.3\t\n\t\t\t820\t1.3 INT\t\n\t\t\t840\t2.3\t\n\t\t\t850\t2.3 INT\t\n\t\t\t860\t3.3\t\n\t\t\t870\t3.3 INT\t\n\t\t\t901   Tf. Peaje BT 2.0  Modo 2\n\t\t\t902   Tf. Peaje BT 2.0N Modo 2\n\t\t\t910\t1.4\t\n\t\t\t920\t1.4 INT\t\n\t\t\t940\t2.4\t\n\t\t\t950\t2.4 INT\t\n\t\t\t960\t3.4\t\n\t\t\t970\t3.4 INT\t\n\t\t\t'
Tarifa._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Tarifa, enum_prefix=None)
Tarifa.n001 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'001')
Tarifa.n002 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'002')
Tarifa.n003 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'003')
Tarifa.n004 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'004')
Tarifa.n011 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'011')
Tarifa.n012 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'012')
Tarifa.n013 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'013')
Tarifa.n014 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'014')
Tarifa.n015 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'015')
Tarifa.n016 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'016')
Tarifa.n027 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'027')
Tarifa.n028 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'028')
Tarifa.n029 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'029')
Tarifa.n030 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'030')
Tarifa.n031 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'031')
Tarifa.n032 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'032')
Tarifa.n033 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'033')
Tarifa.n034 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'034')
Tarifa.n035 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'035')
Tarifa.n036 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'036')
Tarifa.n037 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'037')
Tarifa.n038 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'038')
Tarifa.n039 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'039')
Tarifa.n040 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'040')
Tarifa.n041 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'041')
Tarifa.n042 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'042')
Tarifa.n043 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'043')
Tarifa.n044 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'044')
Tarifa.n045 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'045')
Tarifa.n046 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'046')
Tarifa.n047 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'047')
Tarifa.n048 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'048')
Tarifa.n049 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'049')
Tarifa.n050 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'050')
Tarifa.n101 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'101')
Tarifa.n102 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'102')
Tarifa.n103 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'103')
Tarifa.n110 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'110')
Tarifa.n111 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'111')
Tarifa.n112 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'112')
Tarifa.n113 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'113')
Tarifa.n120 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'120')
Tarifa.n122 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'122')
Tarifa.n123 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'123')
Tarifa.n124 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'124')
Tarifa.n130 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'130')
Tarifa.n131 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'131')
Tarifa.n132 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'132')
Tarifa.n133 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'133')
Tarifa.n134 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'134')
Tarifa.n141 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'141')
Tarifa.n142 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'142')
Tarifa.n143 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'143')
Tarifa.n144 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'144')
Tarifa.n299 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'299')
Tarifa.n300 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'300')
Tarifa.n310 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'310')
Tarifa.n410 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'410')
Tarifa.n500 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'500')
Tarifa.n501 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'501')
Tarifa.n502 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'502')
Tarifa.n503 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'503')
Tarifa.n504 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'504')
Tarifa.n505 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'505')
Tarifa.n510 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'510')
Tarifa.n520 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'520')
Tarifa.n610 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'610')
Tarifa.n620 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'620')
Tarifa.n640 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'640')
Tarifa.n650 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'650')
Tarifa.n660 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'660')
Tarifa.n670 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'670')
Tarifa.n710 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'710')
Tarifa.n720 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'720')
Tarifa.n730 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'730')
Tarifa.n740 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'740')
Tarifa.n750 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'750')
Tarifa.n760 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'760')
Tarifa.n810 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'810')
Tarifa.n820 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'820')
Tarifa.n840 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'840')
Tarifa.n850 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'850')
Tarifa.n860 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'860')
Tarifa.n870 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'870')
Tarifa.n901 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'901')
Tarifa.n902 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'902')
Tarifa.n910 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'910')
Tarifa.n920 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'920')
Tarifa.n940 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'940')
Tarifa.n950 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'950')
Tarifa.n960 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'960')
Tarifa.n970 = Tarifa._CF_enumeration.addEnumeration(unicode_value=u'970')
Tarifa._InitializeFacetMap(Tarifa._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Tarifa', Tarifa)

# Atomic SimpleTypeDefinition
class X10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X10')
    _Documentation = None
X10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
X10._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X10._InitializeFacetMap(X10._CF_maxLength,
   X10._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X10', X10)

# Atomic SimpleTypeDefinition
class TipoMovimiento (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Funcion Tabla 31
			CX	Conexi&#243;n y precintado	
			MO	Montaje	
			RE	Reparametrizaci&#243;n	
			DX	Desconexion	
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoMovimiento')
    _Documentation = u'Funcion Tabla 31\n\t\t\tCX\tConexi\xf3n y precintado\t\n\t\t\tMO\tMontaje\t\n\t\t\tRE\tReparametrizaci\xf3n\t\n\t\t\tDX\tDesconexion\t\n\t\t\t'
TipoMovimiento._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoMovimiento, enum_prefix=None)
TipoMovimiento.CX = TipoMovimiento._CF_enumeration.addEnumeration(unicode_value=u'CX')
TipoMovimiento.MO = TipoMovimiento._CF_enumeration.addEnumeration(unicode_value=u'MO')
TipoMovimiento.RE = TipoMovimiento._CF_enumeration.addEnumeration(unicode_value=u'RE')
TipoMovimiento.DX = TipoMovimiento._CF_enumeration.addEnumeration(unicode_value=u'DX')
TipoMovimiento._InitializeFacetMap(TipoMovimiento._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoMovimiento', TipoMovimiento)

# Atomic SimpleTypeDefinition
class X8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X8')
    _Documentation = None
X8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
X8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X8._InitializeFacetMap(X8._CF_maxLength,
   X8._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X8', X8)

# Atomic SimpleTypeDefinition
class Reactiva (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Reactiva')
    _Documentation = None
Reactiva._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
Reactiva._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Reactiva._InitializeFacetMap(Reactiva._CF_totalDigits,
   Reactiva._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Reactiva', Reactiva)

# Atomic SimpleTypeDefinition
class TipoDH (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo discriminacion horaria (Tabla 35)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoDH')
    _Documentation = u'Tipo discriminacion horaria (Tabla 35)'
TipoDH._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoDH, enum_prefix=None)
TipoDH.n0 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'0')
TipoDH.n1 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'1')
TipoDH.n2 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'2')
TipoDH.n3 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'3')
TipoDH.n4 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'4')
TipoDH.n5 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'5')
TipoDH.n6 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'6')
TipoDH.n7 = TipoDH._CF_enumeration.addEnumeration(unicode_value=u'7')
TipoDH._InitializeFacetMap(TipoDH._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoDH', TipoDH)

# Atomic SimpleTypeDefinition
class STD_ANON_16 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_16._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_16._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_totalDigits,
   STD_ANON_16._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_17 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_17._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_maxLength)

# Atomic SimpleTypeDefinition
class STD_ANON_18 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_18._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_18, value=pyxb.binding.datatypes.integer(0L))
STD_ANON_18._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(2L))
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_minInclusive,
   STD_ANON_18._CF_totalDigits)

# Atomic SimpleTypeDefinition
class TipoDHMaximas (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo de discriminacion horaria maximas Tabla 50
			Modo 1 Sin Maximetro
			Modo 2 Con un maximetro
			Modo 3 Con dos maximetros
			Modo 4 Con tres maximetros
			Modo 5 Estacional Tipo A
			Modo 6 Estacional Tipo B
			THP
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoDHMaximas')
    _Documentation = u'Tipo de discriminacion horaria maximas Tabla 50\n\t\t\tModo 1 Sin Maximetro\n\t\t\tModo 2 Con un maximetro\n\t\t\tModo 3 Con dos maximetros\n\t\t\tModo 4 Con tres maximetros\n\t\t\tModo 5 Estacional Tipo A\n\t\t\tModo 6 Estacional Tipo B\n\t\t\tTHP\n\t\t\t'
TipoDHMaximas._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoDHMaximas, enum_prefix=None)
TipoDHMaximas.n1 = TipoDHMaximas._CF_enumeration.addEnumeration(unicode_value=u'1')
TipoDHMaximas.n2 = TipoDHMaximas._CF_enumeration.addEnumeration(unicode_value=u'2')
TipoDHMaximas.n3 = TipoDHMaximas._CF_enumeration.addEnumeration(unicode_value=u'3')
TipoDHMaximas.n4 = TipoDHMaximas._CF_enumeration.addEnumeration(unicode_value=u'4')
TipoDHMaximas.n5 = TipoDHMaximas._CF_enumeration.addEnumeration(unicode_value=u'5')
TipoDHMaximas.n6 = TipoDHMaximas._CF_enumeration.addEnumeration(unicode_value=u'6')
TipoDHMaximas.n7 = TipoDHMaximas._CF_enumeration.addEnumeration(unicode_value=u'7')
TipoDHMaximas._InitializeFacetMap(TipoDHMaximas._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoDHMaximas', TipoDHMaximas)

# Atomic SimpleTypeDefinition
class STD_ANON_19 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_19._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_19, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_19._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
STD_ANON_19._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_minInclusive,
   STD_ANON_19._CF_totalDigits,
   STD_ANON_19._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class SecuencialDeSolicitud (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SecuencialDeSolicitud')
    _Documentation = None
SecuencialDeSolicitud._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
SecuencialDeSolicitud._InitializeFacetMap(SecuencialDeSolicitud._CF_length)
Namespace.addCategoryObject('typeBinding', u'SecuencialDeSolicitud', SecuencialDeSolicitud)

# Atomic SimpleTypeDefinition
class CodigoDelProceso (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoDelProceso')
    _Documentation = None
CodigoDelProceso._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
CodigoDelProceso._InitializeFacetMap(CodigoDelProceso._CF_length)
Namespace.addCategoryObject('typeBinding', u'CodigoDelProceso', CodigoDelProceso)

# Atomic SimpleTypeDefinition
class FuncionAparato (pyxb.binding.datatypes.string):

    """C = control y M = Medicion"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FuncionAparato')
    _Documentation = u'C = control y M = Medicion'
FuncionAparato._CF_pattern = pyxb.binding.facets.CF_pattern()
FuncionAparato._CF_pattern.addPattern(pattern=u'C|M')
FuncionAparato._InitializeFacetMap(FuncionAparato._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'FuncionAparato', FuncionAparato)

# Atomic SimpleTypeDefinition
class Decimal13 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal13')
    _Documentation = None
Decimal13._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
Decimal13._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal13._InitializeFacetMap(Decimal13._CF_totalDigits,
   Decimal13._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal13', Decimal13)

# Atomic SimpleTypeDefinition
class Decimal10 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal10')
    _Documentation = None
Decimal10._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(10L))
Decimal10._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal10._InitializeFacetMap(Decimal10._CF_totalDigits,
   Decimal10._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal10', Decimal10)

# Atomic SimpleTypeDefinition
class STD_ANON_20 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_20._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
STD_ANON_20._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_maxLength,
   STD_ANON_20._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_21 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_21._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_21._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_totalDigits,
   STD_ANON_21._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Piso (pyxb.binding.datatypes.string):

    """Piso"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Piso')
    _Documentation = u'Piso'
Piso._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
Piso._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
Piso._InitializeFacetMap(Piso._CF_maxLength,
   Piso._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'Piso', Piso)

# Atomic SimpleTypeDefinition
class CodPM (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodPM')
    _Documentation = None
CodPM._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(22L))
CodPM._InitializeFacetMap(CodPM._CF_length)
Namespace.addCategoryObject('typeBinding', u'CodPM', CodPM)

# Atomic SimpleTypeDefinition
class STD_ANON_22 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_22._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_22, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_22._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(6L))
STD_ANON_22._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_minInclusive,
   STD_ANON_22._CF_totalDigits,
   STD_ANON_22._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class TipoIdentificador (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo de Identificador de los datos del usuario
				CI	CIF
				CT	Carta trabajo
				DN	DNI
				NI	NIF
				NV	N.I.V.A.
				OT	N
				PS	Pasaporte
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoIdentificador')
    _Documentation = u'Tipo de Identificador de los datos del usuario\n\t\t\t\tCI\tCIF\n\t\t\t\tCT\tCarta trabajo\n\t\t\t\tDN\tDNI\n\t\t\t\tNI\tNIF\n\t\t\t\tNV\tN.I.V.A.\n\t\t\t\tOT\tN\n\t\t\t\tPS\tPasaporte\n\t\t\t'
TipoIdentificador._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoIdentificador, enum_prefix=None)
TipoIdentificador.CI = TipoIdentificador._CF_enumeration.addEnumeration(unicode_value=u'CI')
TipoIdentificador.CT = TipoIdentificador._CF_enumeration.addEnumeration(unicode_value=u'CT')
TipoIdentificador.DN = TipoIdentificador._CF_enumeration.addEnumeration(unicode_value=u'DN')
TipoIdentificador.NI = TipoIdentificador._CF_enumeration.addEnumeration(unicode_value=u'NI')
TipoIdentificador.NV = TipoIdentificador._CF_enumeration.addEnumeration(unicode_value=u'NV')
TipoIdentificador.OT = TipoIdentificador._CF_enumeration.addEnumeration(unicode_value=u'OT')
TipoIdentificador.PS = TipoIdentificador._CF_enumeration.addEnumeration(unicode_value=u'PS')
TipoIdentificador._InitializeFacetMap(TipoIdentificador._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoIdentificador', TipoIdentificador)

# Atomic SimpleTypeDefinition
class IndicativoSi (pyxb.binding.datatypes.string):

    """ Siempre Si """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoSi')
    _Documentation = u' Siempre Si '
IndicativoSi._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoSi._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoSi._CF_pattern.addPattern(pattern=u'S')
IndicativoSi._InitializeFacetMap(IndicativoSi._CF_length,
   IndicativoSi._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoSi', IndicativoSi)

# Atomic SimpleTypeDefinition
class ReactivaFact (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReactivaFact')
    _Documentation = None
ReactivaFact._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
ReactivaFact._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
ReactivaFact._InitializeFacetMap(ReactivaFact._CF_totalDigits,
   ReactivaFact._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'ReactivaFact', ReactivaFact)

# Atomic SimpleTypeDefinition
class TipoFacturacion (pyxb.binding.datatypes.integer, pyxb.binding.basis.enumeration_mixin):

    """Tipo Facturacion
			0000 Facturacion Normal
			1001 Refacturacion positiva
			2001 Refacturacion negativa
			3001 Facturacion complementaria	
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoFacturacion')
    _Documentation = u'Tipo Facturacion\n\t\t\t0000 Facturacion Normal\n\t\t\t1001 Refacturacion positiva\n\t\t\t2001 Refacturacion negativa\n\t\t\t3001 Facturacion complementaria\t\n\t\t\t'
TipoFacturacion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoFacturacion, enum_prefix=None)
TipoFacturacion._CF_enumeration.addEnumeration(unicode_value=u'0000')
TipoFacturacion._CF_enumeration.addEnumeration(unicode_value=u'1001')
TipoFacturacion._CF_enumeration.addEnumeration(unicode_value=u'2001')
TipoFacturacion._CF_enumeration.addEnumeration(unicode_value=u'3001')
TipoFacturacion._InitializeFacetMap(TipoFacturacion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoFacturacion', TipoFacturacion)

# Atomic SimpleTypeDefinition
class IndicativoLFC (pyxb.binding.datatypes.string):

    """indicativo Tipo Activaci&#243;n prevista (L con ciclo de lectura/ F fecha fija/ C tras actuaci&#243;n en campo)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoLFC')
    _Documentation = u'indicativo Tipo Activaci\xf3n prevista (L con ciclo de lectura/ F fecha fija/ C tras actuaci\xf3n en campo)'
IndicativoLFC._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoLFC._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoLFC._CF_pattern.addPattern(pattern=u'L|F|C')
IndicativoLFC._InitializeFacetMap(IndicativoLFC._CF_length,
   IndicativoLFC._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoLFC', IndicativoLFC)

# Atomic SimpleTypeDefinition
class X3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X3')
    _Documentation = None
X3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
X3._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X3._InitializeFacetMap(X3._CF_maxLength,
   X3._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X3', X3)

# Atomic SimpleTypeDefinition
class Indicativo (pyxb.binding.datatypes.string):

    """valor de verdad (S o N)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Indicativo')
    _Documentation = u'valor de verdad (S o N)'
Indicativo._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
Indicativo._CF_pattern = pyxb.binding.facets.CF_pattern()
Indicativo._CF_pattern.addPattern(pattern=u'S|N')
Indicativo._InitializeFacetMap(Indicativo._CF_length,
   Indicativo._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Indicativo', Indicativo)

# Atomic SimpleTypeDefinition
class STD_ANON_23 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_23._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_23._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_totalDigits,
   STD_ANON_23._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Decimal9 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal9')
    _Documentation = None
Decimal9._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(9L))
Decimal9._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal9._InitializeFacetMap(Decimal9._CF_totalDigits,
   Decimal9._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal9', Decimal9)

# Atomic SimpleTypeDefinition
class STD_ANON_24 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_24._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_24, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_24._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5L))
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_minInclusive,
   STD_ANON_24._CF_totalDigits)

# Atomic SimpleTypeDefinition
class Agente (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Agente')
    _Documentation = None
Agente._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
Agente._InitializeFacetMap(Agente._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'Agente', Agente)

# Atomic SimpleTypeDefinition
class Decimal5 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal5')
    _Documentation = None
Decimal5._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5L))
Decimal5._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal5._InitializeFacetMap(Decimal5._CF_totalDigits,
   Decimal5._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal5', Decimal5)

# Atomic SimpleTypeDefinition
class STD_ANON_25 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_25._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_25, value=pyxb.binding.datatypes.integer(0L))
STD_ANON_25._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_minInclusive,
   STD_ANON_25._CF_totalDigits)

# Atomic SimpleTypeDefinition
class CodigoRetorno (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """codigo de retorno
			O	OK         Todo bien
			E	Error      No se puede continuar
			W	Warning    Se ha producido una incidencia pero se puede continuar
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoRetorno')
    _Documentation = u'codigo de retorno\n\t\t\tO\tOK         Todo bien\n\t\t\tE\tError      No se puede continuar\n\t\t\tW\tWarning    Se ha producido una incidencia pero se puede continuar\n\t\t\t'
CodigoRetorno._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodigoRetorno, enum_prefix=None)
CodigoRetorno.O = CodigoRetorno._CF_enumeration.addEnumeration(unicode_value=u'O')
CodigoRetorno.E = CodigoRetorno._CF_enumeration.addEnumeration(unicode_value=u'E')
CodigoRetorno.W = CodigoRetorno._CF_enumeration.addEnumeration(unicode_value=u'W')
CodigoRetorno._InitializeFacetMap(CodigoRetorno._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CodigoRetorno', CodigoRetorno)

# Atomic SimpleTypeDefinition
class STD_ANON_26 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_26._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_26, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_26._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
STD_ANON_26._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_minInclusive,
   STD_ANON_26._CF_totalDigits,
   STD_ANON_26._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Decimal11 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal11')
    _Documentation = None
Decimal11._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
Decimal11._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal11._InitializeFacetMap(Decimal11._CF_totalDigits,
   Decimal11._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal11', Decimal11)

# Atomic SimpleTypeDefinition
class X4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X4')
    _Documentation = None
X4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
X4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X4._InitializeFacetMap(X4._CF_maxLength,
   X4._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X4', X4)

# Atomic SimpleTypeDefinition
class TipoReclamante (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo Reclamante Tabla 60
			1-Cliente
			2-Afectado no titular
			3-Compa&#241;&#237;a de seguros
			4-Abogado del cliente
			5-OMIC
			6-Consumo
			7-Industria
			8-Otros
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoReclamante')
    _Documentation = u'Tipo Reclamante Tabla 60\n\t\t\t1-Cliente\n\t\t\t2-Afectado no titular\n\t\t\t3-Compa\xf1\xeda de seguros\n\t\t\t4-Abogado del cliente\n\t\t\t5-OMIC\n\t\t\t6-Consumo\n\t\t\t7-Industria\n\t\t\t8-Otros\n\t\t\t'
TipoReclamante._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoReclamante, enum_prefix=None)
TipoReclamante.n1 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'1')
TipoReclamante.n2 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'2')
TipoReclamante.n3 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'3')
TipoReclamante.n4 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'4')
TipoReclamante.n5 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'5')
TipoReclamante.n6 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'6')
TipoReclamante.n7 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'7')
TipoReclamante.n8 = TipoReclamante._CF_enumeration.addEnumeration(unicode_value=u'8')
TipoReclamante._InitializeFacetMap(TipoReclamante._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoReclamante', TipoReclamante)

# Atomic SimpleTypeDefinition
class STD_ANON_27 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_27._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15L))
STD_ANON_27._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_totalDigits,
   STD_ANON_27._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class EstadoPM (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """  Estado PM Tabla 39 
			 1   Alta
			 2   Baja
			 3   Tramitacion de Alta
			 4   Tramitacion de Baja
			 5   Tramitacion de Modificacion
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EstadoPM')
    _Documentation = u'  Estado PM Tabla 39 \n\t\t\t 1   Alta\n\t\t\t 2   Baja\n\t\t\t 3   Tramitacion de Alta\n\t\t\t 4   Tramitacion de Baja\n\t\t\t 5   Tramitacion de Modificacion\n\t\t\t'
EstadoPM._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EstadoPM, enum_prefix=None)
EstadoPM.n1 = EstadoPM._CF_enumeration.addEnumeration(unicode_value=u'1')
EstadoPM.n2 = EstadoPM._CF_enumeration.addEnumeration(unicode_value=u'2')
EstadoPM.n3 = EstadoPM._CF_enumeration.addEnumeration(unicode_value=u'3')
EstadoPM.n4 = EstadoPM._CF_enumeration.addEnumeration(unicode_value=u'4')
EstadoPM.n5 = EstadoPM._CF_enumeration.addEnumeration(unicode_value=u'5')
EstadoPM._InitializeFacetMap(EstadoPM._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'EstadoPM', EstadoPM)

# Atomic SimpleTypeDefinition
class STD_ANON_28 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_28._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
STD_ANON_28._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_totalDigits,
   STD_ANON_28._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_29 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_29._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12L))
STD_ANON_29._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_totalDigits,
   STD_ANON_29._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class IndicativoNo (pyxb.binding.datatypes.string):

    """ Siempre NO """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoNo')
    _Documentation = u' Siempre NO '
IndicativoNo._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoNo._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoNo._CF_pattern.addPattern(pattern=u'N')
IndicativoNo._InitializeFacetMap(IndicativoNo._CF_length,
   IndicativoNo._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoNo', IndicativoNo)

# Atomic SimpleTypeDefinition
class ModoFacturacionPotencia (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Modo facturacion potencia Tabla 50
			Modo 1 Sin Maximetro
			Modo 2 Con un maximetro
			Modo 3 Con dos maximetros
			Modo 4 Con tres maximetros
			Modo 5 Estacional Tipo A
			Modo 6 Estacional Tipo B
			THP
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModoFacturacionPotencia')
    _Documentation = u'Modo facturacion potencia Tabla 50\n\t\t\tModo 1 Sin Maximetro\n\t\t\tModo 2 Con un maximetro\n\t\t\tModo 3 Con dos maximetros\n\t\t\tModo 4 Con tres maximetros\n\t\t\tModo 5 Estacional Tipo A\n\t\t\tModo 6 Estacional Tipo B\n\t\t\tTHP\n\t\t\t'
ModoFacturacionPotencia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ModoFacturacionPotencia, enum_prefix=None)
ModoFacturacionPotencia.n1 = ModoFacturacionPotencia._CF_enumeration.addEnumeration(unicode_value=u'1')
ModoFacturacionPotencia.n2 = ModoFacturacionPotencia._CF_enumeration.addEnumeration(unicode_value=u'2')
ModoFacturacionPotencia.n3 = ModoFacturacionPotencia._CF_enumeration.addEnumeration(unicode_value=u'3')
ModoFacturacionPotencia.n4 = ModoFacturacionPotencia._CF_enumeration.addEnumeration(unicode_value=u'4')
ModoFacturacionPotencia.n5 = ModoFacturacionPotencia._CF_enumeration.addEnumeration(unicode_value=u'5')
ModoFacturacionPotencia.n6 = ModoFacturacionPotencia._CF_enumeration.addEnumeration(unicode_value=u'6')
ModoFacturacionPotencia.n7 = ModoFacturacionPotencia._CF_enumeration.addEnumeration(unicode_value=u'7')
ModoFacturacionPotencia._InitializeFacetMap(ModoFacturacionPotencia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ModoFacturacionPotencia', ModoFacturacionPotencia)

# Atomic SimpleTypeDefinition
class STD_ANON_30 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_30._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_30, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_30._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
STD_ANON_30._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_minInclusive,
   STD_ANON_30._CF_totalDigits,
   STD_ANON_30._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Decimal3 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal3')
    _Documentation = None
Decimal3._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(3L))
Decimal3._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal3._InitializeFacetMap(Decimal3._CF_totalDigits,
   Decimal3._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal3', Decimal3)

# Atomic SimpleTypeDefinition
class X5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X5')
    _Documentation = None
X5._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5L))
X5._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X5._InitializeFacetMap(X5._CF_maxLength,
   X5._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X5', X5)

# Atomic SimpleTypeDefinition
class IndSustitutoMandatario (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Sustituto o Mandatario  
			S	Sustituto	
			M	Mandatario
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndSustitutoMandatario')
    _Documentation = u'Sustituto o Mandatario  \n\t\t\tS\tSustituto\t\n\t\t\tM\tMandatario\n\t\t\t'
IndSustitutoMandatario._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IndSustitutoMandatario, enum_prefix=None)
IndSustitutoMandatario.S = IndSustitutoMandatario._CF_enumeration.addEnumeration(unicode_value=u'S')
IndSustitutoMandatario.M = IndSustitutoMandatario._CF_enumeration.addEnumeration(unicode_value=u'M')
IndSustitutoMandatario._InitializeFacetMap(IndSustitutoMandatario._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'IndSustitutoMandatario', IndSustitutoMandatario)

# Atomic SimpleTypeDefinition
class STD_ANON_31 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_31._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_31, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_31._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
STD_ANON_31._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_minInclusive,
   STD_ANON_31._CF_totalDigits,
   STD_ANON_31._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class RdoReclamacion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Resultado de la Reclamacion Tabla 58
			01-Disculpas. Tomamos nota para evitar a futuro
			02-No estimar a futuro
			03-Error lectura. Se rectifica
			04-Factura  correcta
			05-Falta de lecturas. Se comunica a lecturas
			06-Se cambia ICP y se refactura
			07-Se cambia E.M y se rectifica
			08-I.H. averiado. Se refactura seg&#250;n hist&#243;ricos
			09-Se refactura seg&#250;n Verificaci&#243;n Oficial E.M.
			10-Liquidaci&#243;n Inspecci&#243;n correcta, en base articulo 96 Real Decreto  (anomal&#237;a AM) o Articulo 87 (fraude)
			11-Circuito cruzado. Se refactura para abonar o cargar (   kWh)
			12-Corte correcto, derechos de reconexi&#243;n correctos
			13-Titular del contrato es responsable de la deuda
			14-No se pudo asignar cobro por no poder identificar el ingreso, por falta de datos
			15-Deuda correcta, por subrogaci&#243;n de contrato o Traspaso
			16-Se devuelve. Pago duplicado
			17-Derechos de contrataci&#243;n correctos
			18-Procede el cobro de derechos de enganche  (actuaci&#243;n en la medida)
			19-Se corrige contrato
			20-Se notifica al servicio operativo correspondiente para corregir situaci&#243;n reclamada
			21-Instalaci&#243;n ajena a la Distribuidora
			22-No hay incidencia que pueda provocar da&#241;os
			23-Pedimos facturas para analizar
			24-Trasladamos a contrata para atenci&#243;n da&#241;os
			25-Se debe solicitar apertura de expediente para modificaci&#243;n de acometida
			26-No procede indemnizaci&#243;n por poda/tala
			27-Atenderemos da&#241;os
			28-Corte programado correctamente notificado
			29-Corte err&#243;neo. Estudiamos
			30-Tensiones dentro margen legal 
			31-Se corrigen tensiones
			32-Actuaci&#243;n de nuestras protecciones, no justifica da&#241;os
			33-Aver&#237;a instalaci&#243;n particular cliente
			34-Aver&#237;a en instalaciones de terceros
			35-Aver&#237;a causada por terceros
			36-El tiempo interrupci&#243;n no justifica perdidas de perecederos
			37-Indemnizaci&#243;n de calidad por RD 1955/2000 y orden ECO 797/2002
			38-Prescrita
			39-No es competencia de la Distribuidora
			40-Se indemniza por incumplimiento de calidad seg&#250;n articulo 105 del RD 1955/2000
			41-Ya contestada. Reiteramos nuestra anterior contestaci&#243;n
			42-Otros
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RdoReclamacion')
    _Documentation = u'Resultado de la Reclamacion Tabla 58\n\t\t\t01-Disculpas. Tomamos nota para evitar a futuro\n\t\t\t02-No estimar a futuro\n\t\t\t03-Error lectura. Se rectifica\n\t\t\t04-Factura  correcta\n\t\t\t05-Falta de lecturas. Se comunica a lecturas\n\t\t\t06-Se cambia ICP y se refactura\n\t\t\t07-Se cambia E.M y se rectifica\n\t\t\t08-I.H. averiado. Se refactura seg\xfan hist\xf3ricos\n\t\t\t09-Se refactura seg\xfan Verificaci\xf3n Oficial E.M.\n\t\t\t10-Liquidaci\xf3n Inspecci\xf3n correcta, en base articulo 96 Real Decreto  (anomal\xeda AM) o Articulo 87 (fraude)\n\t\t\t11-Circuito cruzado. Se refactura para abonar o cargar (   kWh)\n\t\t\t12-Corte correcto, derechos de reconexi\xf3n correctos\n\t\t\t13-Titular del contrato es responsable de la deuda\n\t\t\t14-No se pudo asignar cobro por no poder identificar el ingreso, por falta de datos\n\t\t\t15-Deuda correcta, por subrogaci\xf3n de contrato o Traspaso\n\t\t\t16-Se devuelve. Pago duplicado\n\t\t\t17-Derechos de contrataci\xf3n correctos\n\t\t\t18-Procede el cobro de derechos de enganche  (actuaci\xf3n en la medida)\n\t\t\t19-Se corrige contrato\n\t\t\t20-Se notifica al servicio operativo correspondiente para corregir situaci\xf3n reclamada\n\t\t\t21-Instalaci\xf3n ajena a la Distribuidora\n\t\t\t22-No hay incidencia que pueda provocar da\xf1os\n\t\t\t23-Pedimos facturas para analizar\n\t\t\t24-Trasladamos a contrata para atenci\xf3n da\xf1os\n\t\t\t25-Se debe solicitar apertura de expediente para modificaci\xf3n de acometida\n\t\t\t26-No procede indemnizaci\xf3n por poda/tala\n\t\t\t27-Atenderemos da\xf1os\n\t\t\t28-Corte programado correctamente notificado\n\t\t\t29-Corte err\xf3neo. Estudiamos\n\t\t\t30-Tensiones dentro margen legal \n\t\t\t31-Se corrigen tensiones\n\t\t\t32-Actuaci\xf3n de nuestras protecciones, no justifica da\xf1os\n\t\t\t33-Aver\xeda instalaci\xf3n particular cliente\n\t\t\t34-Aver\xeda en instalaciones de terceros\n\t\t\t35-Aver\xeda causada por terceros\n\t\t\t36-El tiempo interrupci\xf3n no justifica perdidas de perecederos\n\t\t\t37-Indemnizaci\xf3n de calidad por RD 1955/2000 y orden ECO 797/2002\n\t\t\t38-Prescrita\n\t\t\t39-No es competencia de la Distribuidora\n\t\t\t40-Se indemniza por incumplimiento de calidad seg\xfan articulo 105 del RD 1955/2000\n\t\t\t41-Ya contestada. Reiteramos nuestra anterior contestaci\xf3n\n\t\t\t42-Otros\n\t\t\t'
RdoReclamacion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RdoReclamacion, enum_prefix=None)
RdoReclamacion.n01 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'01')
RdoReclamacion.n02 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'02')
RdoReclamacion.n03 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'03')
RdoReclamacion.n04 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'04')
RdoReclamacion.n05 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'05')
RdoReclamacion.n06 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'06')
RdoReclamacion.n07 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'07')
RdoReclamacion.n08 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'08')
RdoReclamacion.n09 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'09')
RdoReclamacion.n10 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'10')
RdoReclamacion.n11 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'11')
RdoReclamacion.n12 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'12')
RdoReclamacion.n13 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'13')
RdoReclamacion.n14 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'14')
RdoReclamacion.n15 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'15')
RdoReclamacion.n16 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'16')
RdoReclamacion.n17 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'17')
RdoReclamacion.n18 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'18')
RdoReclamacion.n19 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'19')
RdoReclamacion.n20 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'20')
RdoReclamacion.n21 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'21')
RdoReclamacion.n22 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'22')
RdoReclamacion.n23 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'23')
RdoReclamacion.n24 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'24')
RdoReclamacion.n25 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'25')
RdoReclamacion.n26 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'26')
RdoReclamacion.n27 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'27')
RdoReclamacion.n28 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'28')
RdoReclamacion.n29 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'29')
RdoReclamacion.n30 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'30')
RdoReclamacion.n31 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'31')
RdoReclamacion.n32 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'32')
RdoReclamacion.n33 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'33')
RdoReclamacion.n34 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'34')
RdoReclamacion.n35 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'35')
RdoReclamacion.n36 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'36')
RdoReclamacion.n37 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'37')
RdoReclamacion.n38 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'38')
RdoReclamacion.n39 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'39')
RdoReclamacion.n40 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'40')
RdoReclamacion.n41 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'41')
RdoReclamacion.n42 = RdoReclamacion._CF_enumeration.addEnumeration(unicode_value=u'42')
RdoReclamacion._InitializeFacetMap(RdoReclamacion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RdoReclamacion', RdoReclamacion)

# Atomic SimpleTypeDefinition
class STD_ANON_32 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_32._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_maxLength,
   STD_ANON_32._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_33 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_33._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(26L))
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_maxLength)

# Atomic SimpleTypeDefinition
class STD_ANON_34 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_34._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_34, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_34._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(9L))
STD_ANON_34._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
STD_ANON_34._InitializeFacetMap(STD_ANON_34._CF_minInclusive,
   STD_ANON_34._CF_totalDigits,
   STD_ANON_34._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class TipoAnomalia (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipos de Anomal&#237;a o fraude
			A100	CONTADOR SIN CONTRATO, ERROR ADMINISTRATIVO
			A101	SERVICIO DIRECTO NO CONTROLADO          
			A102	FACTURACION INTERCAMBIO ACTIVA/REACTIVA 
			A103	ERROR EN LECTURA DE CONSUMOS DE ENERGIA 
			A104	ERROR EN LA DIRECCION DEL SUMINISTRO    
			A105	NC CONTADOR MAL O NO ESTA EN BASE DATOS 
			A107	EL CONTADOR NO SE LEE                   
			A108	EL CONTADOR FACTURADO NO ES DEL CLIENTE
			A110	NO SE FACTURA CONSUMO DE ENERGIA REACTIV
			A111	COEFICIENTE DE FACTURACION ERRONEO      
			A112	CLAVE DE TENSION ERRONEA                
			A115	CLAVE ICP ERRONEA O NO ESTA  EN B. DATOS
			A116	EL ICP NO ESTA INSTALADO Y SE FACTURA
			A117	EL ICP ESTA INSTALADO Y NO SE FACTURA   
			A118	ACTIVIDAD ECONOMICA (CNAE) INADECUADA   
			A119	BAJA REALIZADA SE SIGUE FACTURANDO      
			A120	TARIFA MAL APLICADA
			A121	LEIDO NO FACTURADO
			A199	OTRAS ANOMALIAS ADMINISTRATIVAS         
			F200		CONEXION DIRECTA SIN CONTRATO           
			F201		CONEXION DIRECTA CON CONTRATO           
			F202		TOMA CLANDESTINA ANTES DEL CONTADOR     
			F203		CONTADOR TALADRADO                      
			F204		CONTADOR FORZADO                        
			F205		CONTADOR CON PUENTE DE TENSION MANIPULAD
			F206		A.M.CAMBIADO SIN CONOCIMIENTO DE IBERDR.
			F207		CAMBIO PLACA DE CORACTERISTICAS TRAFO. TENS.
			F208		CAMBIO PLACA DE CORACTERISTICAS CONTADOR
			F209		TENSI&#211;N INTERRUMPIDA  EN TRAFO INTENSIDAD
			F210		INTENSIDAD INTERRUMPIDA EN TRAFO INTENSIDAD
			F211		CAMBIO PLACA DE CORACTERISTICAS TRAFO. INTENSIDAD
			F212		CAMBIO FASE/NEUTRO CON NEUTRO ARTIFICIAL
			F213		INVERSION ENTRADA - SALIDA EN CONTADOR  
			F214		PUENTE ENTRADA - SALIDA EN LA MISMA FASE
			F215		USO TRASFORMADOR CONGREJO
			F216		COMBINACI&#211;N ENTRE CONTADORES
			F217		MANIPULACION EN RELOJERIA DEL CONTADOR  
			F218		DISCRIMINACI&#211;N HORARIA MANIPULADA
			F219		EL ICP ESTA PUENTEADO, CAMBIADO O MANIP.
			F220		MAYOR POTENCIA EN SERVICIOS TEMPORALES  
			F221		CESION DE ENERGIA
			F223		CONTADOR INSTALADO SIN CONTRATO         
			F224		USO DISTINTO AL CONTRATADO              
			F225		INTENSIDAD INVERTIDA 
			F226		TENSION PERMUTADA 
			F298		EQUIPO DE MEDIDA DESAPARECIDO
			F299		OTROS FRAUDES                           
			I900		CENTRALIZACION PELIGROSA                
			I905		IMPEDIMENTO DE ACCESO POR FALTA DE LLAVE
			I906		MIRILLA ENVEJECIDA (CAMBIO A.M.)        
			I907		CONTADOR ALTURA SUPERIOR A 2,5 M.       
			I908		SUMINISTRO DE EMERGENCIA O SOCORRO      
			I910		CERRADO,NO VIVEN MUC.TIEMPO O CESE NEGOC
			I912		CERRADO, VIVIENDA VERANEO O 2&#170; VIVIENDA 
			I913		CASA EN RUINAS O DERRUIDA               
			I914		VIVEN PERO SOLO ESTAN POR LA NOCHE      
			I915		SOLO FINES DE SEMANA                    
			I916		ILOCALIZABLE (LOS VECINOS NO SABEN NADA)
			I921		NO ABREN INTENCIONADAMENTE              
			I922		ACCESO EN MAL ESTADO                    
			I923		SOLAR                                   
			I924		REGISTR. APAGADO (SIN TENSI&#243;N)          
			T001		CONTADOR PARADO PORQUE NO ENGRANA       
			T002		CONTADOR CON CONEXI&#211;N INVERTIDA         
			T003		CONT. CON BOBINA TENS. INTERRUM/DESCON. 
			T005		CONTADOR PARADO POR DISCO AGARROTADO    
			T006		CONTADOR QUEMADO POR SOBRECARGA         
			T007		CONTADOR CON MARCHA DEFECTUOSA          
			T008		CONTADOR MARCHA EN VACIO                
			T009		CONTADOR RETRASA                        
			T010		CONTADOR DESPRENDIDO                    
			T011		CONTADOR ROTO                           
			T019		CONTADOR SIN CUBREBORNAS / HILOS        
			T024		CONTADORES PERMUTADOS ENTRE CLIENTES    
			T025		CONTADOR REACTIVO SIN INSTALAR          
			T026		CONTADOR REACTIVO PARADO POR AVERIA     
			T027		CONTADOR REACTIVO PARADO POR CAPACITIVA 
			T028		CONTADOR REACTIVO INSTALADO POR ACTIVO  
			T029		CONT.REACTIV SENTIDO GIRO INVERTIDO(RST)
			T030		TRANSFORMADOR DE INTENSIDAD AVERIADO    
			T031		TRAFO. DE INTENSIDAD MAL CONECTADO      
			T032		TRAFO.DE  INTENSIDAD CON LA RELACION MAL
			T033		TRAF. INT. NO AJUSTADO A POTEN. CONTRATO
			T035		TRAFO DE TENSI&#211;N AVERIADO
			T036		TRAFO DE TENSION MAL CONECTADO
			T037		INTENSIDAD INVERTIDA 
			T038		TENSION PERMUTADA 
			T039		TENSION O INTENSIDAD ABIERTA   
			T040		INTERRUPTOR CONTROL POTENCIA AVERIADO   
			T041		ICP NO CORTA LA FASE DE LA INSTALACION  
			T042		EL ICP NO CORTA TODA LA INSTALACION     
			T047		ICP MAYOR QUE  POTENCIA DE CONTRATO     
			T048		ICP MENOR  QUE POTENCIA DE CONTRATO     
			T049		CLIENTE SIN LIMITAR                     
			T050		NO SE TOMA LECTURA INJUSTIFICADAMENTE   
			T060		INTERRUPTOR HORARIO MAL CONECTADO       
			T061		INTERRUPTOR HORARIO MAL AJUSTADO        
			T062		INTERRUPTOR HORARIO AVERIADO            
			T065		CONTADOR ELECTRONICO CON FALLOS INTERMITENTES
			T066		ERRORES SUPERIORES A SU CLASE EN ADELANTO
			T067		ERRORES SUPERIORES A SU CLASE EN ATRASO
			T068		FALLO INTERMITENTE EN EL RELOJ
			T069		FALLO DEL DISPLAY O REGISTRADOR DEFECT  
			T070		PROBLEMAS EN EL SOFTWARE DEL CONTADOR   
			T071		LED DE VERIFICACI&#211;N MAL
			T072		INDICADOR DE LA DIRECCIO DE LA ENRGIA MAL
			T073		ENVOLVENTE O CAJA DE BORNAS MAL         
			T074		FALLO EN CONTADOR DE PREPAGO
			T075		INDICACION DE FRAUDE EN EL CONTADOR
			T076		FALLO EN EL CAMBIO DE TARIFA            
			T077		FALLO ENTRADA / SALIDA IMPULSOS
			T078		FALLO DE LA BATERIA
			T079		ENERGIA ACUMULADA Y NO FACTURADA
			T080		TAPA PROTECTORA (CP) ROTA               
			T081		ACOMETIDA MAL                           
			T090		MAXIMA REGISTRADA MAYOR QUE POT. AUTORIZ
			T091		MAXIMETRO AVERIADO
			T094		FALTA PRECINTOS DE INDUSTRIA            
			T095		FALTA PRECIN/CUBREBOR. GENER. EN CENTRAL
			T096		FALTA PRECINTADO EN A.M.                
			T097		FALTA PRECINTADO EN ARMARIO/ENVOLVENTES 
			T098		FALTA PRECINTADO SIN INFLUENCIA EN FRAUD
			T099		OTRAS ANOMALIAS TECNICAS                
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoAnomalia')
    _Documentation = u'Tipos de Anomal\xeda o fraude\n\t\t\tA100\tCONTADOR SIN CONTRATO, ERROR ADMINISTRATIVO\n\t\t\tA101\tSERVICIO DIRECTO NO CONTROLADO          \n\t\t\tA102\tFACTURACION INTERCAMBIO ACTIVA/REACTIVA \n\t\t\tA103\tERROR EN LECTURA DE CONSUMOS DE ENERGIA \n\t\t\tA104\tERROR EN LA DIRECCION DEL SUMINISTRO    \n\t\t\tA105\tNC CONTADOR MAL O NO ESTA EN BASE DATOS \n\t\t\tA107\tEL CONTADOR NO SE LEE                   \n\t\t\tA108\tEL CONTADOR FACTURADO NO ES DEL CLIENTE\n\t\t\tA110\tNO SE FACTURA CONSUMO DE ENERGIA REACTIV\n\t\t\tA111\tCOEFICIENTE DE FACTURACION ERRONEO      \n\t\t\tA112\tCLAVE DE TENSION ERRONEA                \n\t\t\tA115\tCLAVE ICP ERRONEA O NO ESTA  EN B. DATOS\n\t\t\tA116\tEL ICP NO ESTA INSTALADO Y SE FACTURA\n\t\t\tA117\tEL ICP ESTA INSTALADO Y NO SE FACTURA   \n\t\t\tA118\tACTIVIDAD ECONOMICA (CNAE) INADECUADA   \n\t\t\tA119\tBAJA REALIZADA SE SIGUE FACTURANDO      \n\t\t\tA120\tTARIFA MAL APLICADA\n\t\t\tA121\tLEIDO NO FACTURADO\n\t\t\tA199\tOTRAS ANOMALIAS ADMINISTRATIVAS         \n\t\t\tF200\t\tCONEXION DIRECTA SIN CONTRATO           \n\t\t\tF201\t\tCONEXION DIRECTA CON CONTRATO           \n\t\t\tF202\t\tTOMA CLANDESTINA ANTES DEL CONTADOR     \n\t\t\tF203\t\tCONTADOR TALADRADO                      \n\t\t\tF204\t\tCONTADOR FORZADO                        \n\t\t\tF205\t\tCONTADOR CON PUENTE DE TENSION MANIPULAD\n\t\t\tF206\t\tA.M.CAMBIADO SIN CONOCIMIENTO DE IBERDR.\n\t\t\tF207\t\tCAMBIO PLACA DE CORACTERISTICAS TRAFO. TENS.\n\t\t\tF208\t\tCAMBIO PLACA DE CORACTERISTICAS CONTADOR\n\t\t\tF209\t\tTENSI\xd3N INTERRUMPIDA  EN TRAFO INTENSIDAD\n\t\t\tF210\t\tINTENSIDAD INTERRUMPIDA EN TRAFO INTENSIDAD\n\t\t\tF211\t\tCAMBIO PLACA DE CORACTERISTICAS TRAFO. INTENSIDAD\n\t\t\tF212\t\tCAMBIO FASE/NEUTRO CON NEUTRO ARTIFICIAL\n\t\t\tF213\t\tINVERSION ENTRADA - SALIDA EN CONTADOR  \n\t\t\tF214\t\tPUENTE ENTRADA - SALIDA EN LA MISMA FASE\n\t\t\tF215\t\tUSO TRASFORMADOR CONGREJO\n\t\t\tF216\t\tCOMBINACI\xd3N ENTRE CONTADORES\n\t\t\tF217\t\tMANIPULACION EN RELOJERIA DEL CONTADOR  \n\t\t\tF218\t\tDISCRIMINACI\xd3N HORARIA MANIPULADA\n\t\t\tF219\t\tEL ICP ESTA PUENTEADO, CAMBIADO O MANIP.\n\t\t\tF220\t\tMAYOR POTENCIA EN SERVICIOS TEMPORALES  \n\t\t\tF221\t\tCESION DE ENERGIA\n\t\t\tF223\t\tCONTADOR INSTALADO SIN CONTRATO         \n\t\t\tF224\t\tUSO DISTINTO AL CONTRATADO              \n\t\t\tF225\t\tINTENSIDAD INVERTIDA \n\t\t\tF226\t\tTENSION PERMUTADA \n\t\t\tF298\t\tEQUIPO DE MEDIDA DESAPARECIDO\n\t\t\tF299\t\tOTROS FRAUDES                           \n\t\t\tI900\t\tCENTRALIZACION PELIGROSA                \n\t\t\tI905\t\tIMPEDIMENTO DE ACCESO POR FALTA DE LLAVE\n\t\t\tI906\t\tMIRILLA ENVEJECIDA (CAMBIO A.M.)        \n\t\t\tI907\t\tCONTADOR ALTURA SUPERIOR A 2,5 M.       \n\t\t\tI908\t\tSUMINISTRO DE EMERGENCIA O SOCORRO      \n\t\t\tI910\t\tCERRADO,NO VIVEN MUC.TIEMPO O CESE NEGOC\n\t\t\tI912\t\tCERRADO, VIVIENDA VERANEO O 2\xaa VIVIENDA \n\t\t\tI913\t\tCASA EN RUINAS O DERRUIDA               \n\t\t\tI914\t\tVIVEN PERO SOLO ESTAN POR LA NOCHE      \n\t\t\tI915\t\tSOLO FINES DE SEMANA                    \n\t\t\tI916\t\tILOCALIZABLE (LOS VECINOS NO SABEN NADA)\n\t\t\tI921\t\tNO ABREN INTENCIONADAMENTE              \n\t\t\tI922\t\tACCESO EN MAL ESTADO                    \n\t\t\tI923\t\tSOLAR                                   \n\t\t\tI924\t\tREGISTR. APAGADO (SIN TENSI\xf3N)          \n\t\t\tT001\t\tCONTADOR PARADO PORQUE NO ENGRANA       \n\t\t\tT002\t\tCONTADOR CON CONEXI\xd3N INVERTIDA         \n\t\t\tT003\t\tCONT. CON BOBINA TENS. INTERRUM/DESCON. \n\t\t\tT005\t\tCONTADOR PARADO POR DISCO AGARROTADO    \n\t\t\tT006\t\tCONTADOR QUEMADO POR SOBRECARGA         \n\t\t\tT007\t\tCONTADOR CON MARCHA DEFECTUOSA          \n\t\t\tT008\t\tCONTADOR MARCHA EN VACIO                \n\t\t\tT009\t\tCONTADOR RETRASA                        \n\t\t\tT010\t\tCONTADOR DESPRENDIDO                    \n\t\t\tT011\t\tCONTADOR ROTO                           \n\t\t\tT019\t\tCONTADOR SIN CUBREBORNAS / HILOS        \n\t\t\tT024\t\tCONTADORES PERMUTADOS ENTRE CLIENTES    \n\t\t\tT025\t\tCONTADOR REACTIVO SIN INSTALAR          \n\t\t\tT026\t\tCONTADOR REACTIVO PARADO POR AVERIA     \n\t\t\tT027\t\tCONTADOR REACTIVO PARADO POR CAPACITIVA \n\t\t\tT028\t\tCONTADOR REACTIVO INSTALADO POR ACTIVO  \n\t\t\tT029\t\tCONT.REACTIV SENTIDO GIRO INVERTIDO(RST)\n\t\t\tT030\t\tTRANSFORMADOR DE INTENSIDAD AVERIADO    \n\t\t\tT031\t\tTRAFO. DE INTENSIDAD MAL CONECTADO      \n\t\t\tT032\t\tTRAFO.DE  INTENSIDAD CON LA RELACION MAL\n\t\t\tT033\t\tTRAF. INT. NO AJUSTADO A POTEN. CONTRATO\n\t\t\tT035\t\tTRAFO DE TENSI\xd3N AVERIADO\n\t\t\tT036\t\tTRAFO DE TENSION MAL CONECTADO\n\t\t\tT037\t\tINTENSIDAD INVERTIDA \n\t\t\tT038\t\tTENSION PERMUTADA \n\t\t\tT039\t\tTENSION O INTENSIDAD ABIERTA   \n\t\t\tT040\t\tINTERRUPTOR CONTROL POTENCIA AVERIADO   \n\t\t\tT041\t\tICP NO CORTA LA FASE DE LA INSTALACION  \n\t\t\tT042\t\tEL ICP NO CORTA TODA LA INSTALACION     \n\t\t\tT047\t\tICP MAYOR QUE  POTENCIA DE CONTRATO     \n\t\t\tT048\t\tICP MENOR  QUE POTENCIA DE CONTRATO     \n\t\t\tT049\t\tCLIENTE SIN LIMITAR                     \n\t\t\tT050\t\tNO SE TOMA LECTURA INJUSTIFICADAMENTE   \n\t\t\tT060\t\tINTERRUPTOR HORARIO MAL CONECTADO       \n\t\t\tT061\t\tINTERRUPTOR HORARIO MAL AJUSTADO        \n\t\t\tT062\t\tINTERRUPTOR HORARIO AVERIADO            \n\t\t\tT065\t\tCONTADOR ELECTRONICO CON FALLOS INTERMITENTES\n\t\t\tT066\t\tERRORES SUPERIORES A SU CLASE EN ADELANTO\n\t\t\tT067\t\tERRORES SUPERIORES A SU CLASE EN ATRASO\n\t\t\tT068\t\tFALLO INTERMITENTE EN EL RELOJ\n\t\t\tT069\t\tFALLO DEL DISPLAY O REGISTRADOR DEFECT  \n\t\t\tT070\t\tPROBLEMAS EN EL SOFTWARE DEL CONTADOR   \n\t\t\tT071\t\tLED DE VERIFICACI\xd3N MAL\n\t\t\tT072\t\tINDICADOR DE LA DIRECCIO DE LA ENRGIA MAL\n\t\t\tT073\t\tENVOLVENTE O CAJA DE BORNAS MAL         \n\t\t\tT074\t\tFALLO EN CONTADOR DE PREPAGO\n\t\t\tT075\t\tINDICACION DE FRAUDE EN EL CONTADOR\n\t\t\tT076\t\tFALLO EN EL CAMBIO DE TARIFA            \n\t\t\tT077\t\tFALLO ENTRADA / SALIDA IMPULSOS\n\t\t\tT078\t\tFALLO DE LA BATERIA\n\t\t\tT079\t\tENERGIA ACUMULADA Y NO FACTURADA\n\t\t\tT080\t\tTAPA PROTECTORA (CP) ROTA               \n\t\t\tT081\t\tACOMETIDA MAL                           \n\t\t\tT090\t\tMAXIMA REGISTRADA MAYOR QUE POT. AUTORIZ\n\t\t\tT091\t\tMAXIMETRO AVERIADO\n\t\t\tT094\t\tFALTA PRECINTOS DE INDUSTRIA            \n\t\t\tT095\t\tFALTA PRECIN/CUBREBOR. GENER. EN CENTRAL\n\t\t\tT096\t\tFALTA PRECINTADO EN A.M.                \n\t\t\tT097\t\tFALTA PRECINTADO EN ARMARIO/ENVOLVENTES \n\t\t\tT098\t\tFALTA PRECINTADO SIN INFLUENCIA EN FRAUD\n\t\t\tT099\t\tOTRAS ANOMALIAS TECNICAS                \n\t\t\t'
TipoAnomalia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoAnomalia, enum_prefix=None)
TipoAnomalia.A100 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A100')
TipoAnomalia.A101 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A101')
TipoAnomalia.A102 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A102')
TipoAnomalia.A103 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A103')
TipoAnomalia.A104 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A104')
TipoAnomalia.A105 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A105')
TipoAnomalia.A107 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A107')
TipoAnomalia.A108 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A108')
TipoAnomalia.A110 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A110')
TipoAnomalia.A111 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A111')
TipoAnomalia.A112 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A112')
TipoAnomalia.A115 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A115')
TipoAnomalia.A116 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A116')
TipoAnomalia.A117 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A117')
TipoAnomalia.A118 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A118')
TipoAnomalia.A119 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A119')
TipoAnomalia.A120 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A120')
TipoAnomalia.A121 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A121')
TipoAnomalia.A199 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'A199')
TipoAnomalia.F200 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F200')
TipoAnomalia.F201 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F201')
TipoAnomalia.F202 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F202')
TipoAnomalia.F203 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F203')
TipoAnomalia.F204 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F204')
TipoAnomalia.F205 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F205')
TipoAnomalia.F206 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F206')
TipoAnomalia.F207 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F207')
TipoAnomalia.F208 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F208')
TipoAnomalia.F209 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F209')
TipoAnomalia.F210 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F210')
TipoAnomalia.F211 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F211')
TipoAnomalia.F212 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F212')
TipoAnomalia.F213 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F213')
TipoAnomalia.F214 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F214')
TipoAnomalia.F215 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F215')
TipoAnomalia.F216 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F216')
TipoAnomalia.F217 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F217')
TipoAnomalia.F218 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F218')
TipoAnomalia.F219 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F219')
TipoAnomalia.F220 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F220')
TipoAnomalia.F221 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F221')
TipoAnomalia.F222 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F222')
TipoAnomalia.F223 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F223')
TipoAnomalia.F224 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F224')
TipoAnomalia.F225 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F225')
TipoAnomalia.F226 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F226')
TipoAnomalia.F298 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F298')
TipoAnomalia.F299 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'F299')
TipoAnomalia.I900 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I900')
TipoAnomalia.I905 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I905')
TipoAnomalia.I906 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I906')
TipoAnomalia.I907 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I907')
TipoAnomalia.I908 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I908')
TipoAnomalia.I910 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I910')
TipoAnomalia.I912 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I912')
TipoAnomalia.I913 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I913')
TipoAnomalia.I914 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I914')
TipoAnomalia.I915 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I915')
TipoAnomalia.I916 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I916')
TipoAnomalia.I921 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I921')
TipoAnomalia.I922 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I922')
TipoAnomalia.I923 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I923')
TipoAnomalia.I924 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'I924')
TipoAnomalia.T001 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T001')
TipoAnomalia.T002 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T002')
TipoAnomalia.T003 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T003')
TipoAnomalia.T005 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T005')
TipoAnomalia.T006 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T006')
TipoAnomalia.T007 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T007')
TipoAnomalia.T008 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T008')
TipoAnomalia.T009 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T009')
TipoAnomalia.T010 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T010')
TipoAnomalia.T011 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T011')
TipoAnomalia.T019 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T019')
TipoAnomalia.T024 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T024')
TipoAnomalia.T025 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T025')
TipoAnomalia.T026 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T026')
TipoAnomalia.T027 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T027')
TipoAnomalia.T028 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T028')
TipoAnomalia.T029 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T029')
TipoAnomalia.T030 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T030')
TipoAnomalia.T031 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T031')
TipoAnomalia.T032 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T032')
TipoAnomalia.T033 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T033')
TipoAnomalia.T035 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T035')
TipoAnomalia.T036 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T036')
TipoAnomalia.T037 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T037')
TipoAnomalia.T038 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T038')
TipoAnomalia.T039 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T039')
TipoAnomalia.T040 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T040')
TipoAnomalia.T041 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T041')
TipoAnomalia.T042 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T042')
TipoAnomalia.T047 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T047')
TipoAnomalia.T048 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T048')
TipoAnomalia.T049 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T049')
TipoAnomalia.T050 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T050')
TipoAnomalia.T060 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T060')
TipoAnomalia.T061 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T061')
TipoAnomalia.T062 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T062')
TipoAnomalia.T065 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T065')
TipoAnomalia.T066 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T066')
TipoAnomalia.T067 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T067')
TipoAnomalia.T068 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T068')
TipoAnomalia.T069 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T069')
TipoAnomalia.T070 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T070')
TipoAnomalia.T071 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T071')
TipoAnomalia.T072 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T072')
TipoAnomalia.T073 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T073')
TipoAnomalia.T074 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T074')
TipoAnomalia.T075 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T075')
TipoAnomalia.T076 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T076')
TipoAnomalia.T077 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T077')
TipoAnomalia.T078 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T078')
TipoAnomalia.T079 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T079')
TipoAnomalia.T080 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T080')
TipoAnomalia.T081 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T081')
TipoAnomalia.T090 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T090')
TipoAnomalia.T091 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T091')
TipoAnomalia.T094 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T094')
TipoAnomalia.T095 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T095')
TipoAnomalia.T096 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T096')
TipoAnomalia.T097 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T097')
TipoAnomalia.T098 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T098')
TipoAnomalia.T099 = TipoAnomalia._CF_enumeration.addEnumeration(unicode_value=u'T099')
TipoAnomalia._InitializeFacetMap(TipoAnomalia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoAnomalia', TipoAnomalia)

# Atomic SimpleTypeDefinition
class X40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X40')
    _Documentation = None
X40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
X40._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X40._InitializeFacetMap(X40._CF_maxLength,
   X40._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X40', X40)

# Atomic SimpleTypeDefinition
class TipoConcepto (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			01	Indemnizacion
			02	Derechos de extensi&#243;n
			03	Derechos de acceso
			04	Derechos de enganche
			05	Derechos de verificaci&#243;n
			06	Dep&#243;sito de garant&#237;a
			07	Gastos de anulaci&#243;n de contratos
			08	Actuaciones en la medida
			09	Reparametrizaci&#243;n de la medida
			10	2 &#186; Cambio de Comercializador en el periodo de un a&#241;o
			11	Intereses de demora
			12	Verificacion de Equipos de Medida
			13	Derechos de Reconexion
			14	Varios
			15	Gastos de acometida
			16	Abonos
			17	Abono por calidad de suministro
			18	Abono por calidad individual
			19	Coste de reposici&#243;n
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoConcepto')
    _Documentation = u'\n\t\t\t01\tIndemnizacion\n\t\t\t02\tDerechos de extensi\xf3n\n\t\t\t03\tDerechos de acceso\n\t\t\t04\tDerechos de enganche\n\t\t\t05\tDerechos de verificaci\xf3n\n\t\t\t06\tDep\xf3sito de garant\xeda\n\t\t\t07\tGastos de anulaci\xf3n de contratos\n\t\t\t08\tActuaciones en la medida\n\t\t\t09\tReparametrizaci\xf3n de la medida\n\t\t\t10\t2 \xba Cambio de Comercializador en el periodo de un a\xf1o\n\t\t\t11\tIntereses de demora\n\t\t\t12\tVerificacion de Equipos de Medida\n\t\t\t13\tDerechos de Reconexion\n\t\t\t14\tVarios\n\t\t\t15\tGastos de acometida\n\t\t\t16\tAbonos\n\t\t\t17\tAbono por calidad de suministro\n\t\t\t18\tAbono por calidad individual\n\t\t\t19\tCoste de reposici\xf3n\n\t\t\t'
TipoConcepto._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoConcepto, enum_prefix=None)
TipoConcepto.n01 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoConcepto.n02 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'02')
TipoConcepto.n03 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'03')
TipoConcepto.n04 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'04')
TipoConcepto.n05 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'05')
TipoConcepto.n06 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'06')
TipoConcepto.n07 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'07')
TipoConcepto.n08 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'08')
TipoConcepto.n09 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'09')
TipoConcepto.n10 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'10')
TipoConcepto.n11 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'11')
TipoConcepto.n12 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'12')
TipoConcepto.n13 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'13')
TipoConcepto.n14 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'14')
TipoConcepto.n15 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'15')
TipoConcepto.n16 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'16')
TipoConcepto.n17 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'17')
TipoConcepto.n18 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'18')
TipoConcepto.n19 = TipoConcepto._CF_enumeration.addEnumeration(unicode_value=u'19')
TipoConcepto._InitializeFacetMap(TipoConcepto._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoConcepto', TipoConcepto)

# Atomic SimpleTypeDefinition
class DecimalS9V2 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DecimalS9V2')
    _Documentation = None
DecimalS9V2._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
DecimalS9V2._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
DecimalS9V2._InitializeFacetMap(DecimalS9V2._CF_totalDigits,
   DecimalS9V2._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'DecimalS9V2', DecimalS9V2)

# Atomic SimpleTypeDefinition
class MotivoBaja (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Motivo de baja
			01	CESE DEFINITIVO DE SUMINISTRO
			02	RESCISI&#211;N DE CONTRATO DE ENERG&#205;A
			03    CORTE POR IMPAGO
			04	BAJA POR IMPAGO
			05	BAJA SIN DESCONEXION DEFINITIVA DE INSTALACIONES
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MotivoBaja')
    _Documentation = u'Motivo de baja\n\t\t\t01\tCESE DEFINITIVO DE SUMINISTRO\n\t\t\t02\tRESCISI\xd3N DE CONTRATO DE ENERG\xcdA\n\t\t\t03    CORTE POR IMPAGO\n\t\t\t04\tBAJA POR IMPAGO\n\t\t\t05\tBAJA SIN DESCONEXION DEFINITIVA DE INSTALACIONES\n\t\t\t'
MotivoBaja._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MotivoBaja, enum_prefix=None)
MotivoBaja.n01 = MotivoBaja._CF_enumeration.addEnumeration(unicode_value=u'01')
MotivoBaja.n02 = MotivoBaja._CF_enumeration.addEnumeration(unicode_value=u'02')
MotivoBaja.n03 = MotivoBaja._CF_enumeration.addEnumeration(unicode_value=u'03')
MotivoBaja.n04 = MotivoBaja._CF_enumeration.addEnumeration(unicode_value=u'04')
MotivoBaja.n05 = MotivoBaja._CF_enumeration.addEnumeration(unicode_value=u'05')
MotivoBaja._InitializeFacetMap(MotivoBaja._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MotivoBaja', MotivoBaja)

# Atomic SimpleTypeDefinition
class X32 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X32')
    _Documentation = None
X32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32L))
X32._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X32._InitializeFacetMap(X32._CF_maxLength,
   X32._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X32', X32)

# Atomic SimpleTypeDefinition
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_35._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
STD_ANON_35._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_maxLength,
   STD_ANON_35._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_36 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_36._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_36._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_36._InitializeFacetMap(STD_ANON_36._CF_totalDigits,
   STD_ANON_36._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_37 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_37._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(26L))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_maxLength)

# Atomic SimpleTypeDefinition
class TipoPerfilDeConsumo (pyxb.binding.datatypes.string):

    """tipo de Perfil de consumo Valores posibles por determinar por equipo de trabajo de perfiles """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoPerfilDeConsumo')
    _Documentation = u'tipo de Perfil de consumo Valores posibles por determinar por equipo de trabajo de perfiles '
TipoPerfilDeConsumo._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
TipoPerfilDeConsumo._InitializeFacetMap(TipoPerfilDeConsumo._CF_length)
Namespace.addCategoryObject('typeBinding', u'TipoPerfilDeConsumo', TipoPerfilDeConsumo)

# Atomic SimpleTypeDefinition
class CodDatos (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """C&#243;digo de datos Tabla 59
			01-Faltan facturas de da&#241;os
			02-Faltan datos de contacto en suministro
			03-Faltan datos bancarios para pago
			04-Falta fecha de la incidencia
			05-Falta cuantificaci&#243;n de da&#241;os
			06-Faltan datos de lecturas
			07-Otros da&#241;os
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodDatos')
    _Documentation = u'C\xf3digo de datos Tabla 59\n\t\t\t01-Faltan facturas de da\xf1os\n\t\t\t02-Faltan datos de contacto en suministro\n\t\t\t03-Faltan datos bancarios para pago\n\t\t\t04-Falta fecha de la incidencia\n\t\t\t05-Falta cuantificaci\xf3n de da\xf1os\n\t\t\t06-Faltan datos de lecturas\n\t\t\t07-Otros da\xf1os\n\t\t\t'
CodDatos._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodDatos, enum_prefix=None)
CodDatos.n01 = CodDatos._CF_enumeration.addEnumeration(unicode_value=u'01')
CodDatos.n02 = CodDatos._CF_enumeration.addEnumeration(unicode_value=u'02')
CodDatos.n03 = CodDatos._CF_enumeration.addEnumeration(unicode_value=u'03')
CodDatos.n04 = CodDatos._CF_enumeration.addEnumeration(unicode_value=u'04')
CodDatos.n05 = CodDatos._CF_enumeration.addEnumeration(unicode_value=u'05')
CodDatos.n06 = CodDatos._CF_enumeration.addEnumeration(unicode_value=u'06')
CodDatos.n07 = CodDatos._CF_enumeration.addEnumeration(unicode_value=u'07')
CodDatos._InitializeFacetMap(CodDatos._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CodDatos', CodDatos)

# Atomic SimpleTypeDefinition
class FuncionPM (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Funcion Tabla 40
			 C   Comprobante
			 P   Principal
			 R   Redundante					
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FuncionPM')
    _Documentation = u'Funcion Tabla 40\n\t\t\t C   Comprobante\n\t\t\t P   Principal\n\t\t\t R   Redundante\t\t\t\t\t\n\t\t\t'
FuncionPM._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FuncionPM, enum_prefix=None)
FuncionPM.C = FuncionPM._CF_enumeration.addEnumeration(unicode_value=u'C')
FuncionPM.P = FuncionPM._CF_enumeration.addEnumeration(unicode_value=u'P')
FuncionPM.R = FuncionPM._CF_enumeration.addEnumeration(unicode_value=u'R')
FuncionPM._InitializeFacetMap(FuncionPM._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'FuncionPM', FuncionPM)

# Atomic SimpleTypeDefinition
class STD_ANON_38 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_38._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_38, enum_prefix=None)
STD_ANON_38.F = STD_ANON_38._CF_enumeration.addEnumeration(unicode_value=u'F')
STD_ANON_38.S = STD_ANON_38._CF_enumeration.addEnumeration(unicode_value=u'S')
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_enumeration)

# Atomic SimpleTypeDefinition
class TipoFacturacionATR (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo Facturacion ATR Tabla 105
			1-Regular (Periodo completo)
			2-Irregular (Periodo incompleto)
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoFacturacionATR')
    _Documentation = u'Tipo Facturacion ATR Tabla 105\n\t\t\t1-Regular (Periodo completo)\n\t\t\t2-Irregular (Periodo incompleto)\n\t\t\t'
TipoFacturacionATR._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoFacturacionATR, enum_prefix=None)
TipoFacturacionATR.n1 = TipoFacturacionATR._CF_enumeration.addEnumeration(unicode_value=u'1')
TipoFacturacionATR.n2 = TipoFacturacionATR._CF_enumeration.addEnumeration(unicode_value=u'2')
TipoFacturacionATR._InitializeFacetMap(TipoFacturacionATR._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoFacturacionATR', TipoFacturacionATR)

# Atomic SimpleTypeDefinition
class X1 (pyxb.binding.datatypes.string):

    """cadena de un caracter"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X1')
    _Documentation = u'cadena de un caracter'
X1._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X1._InitializeFacetMap(X1._CF_length)
Namespace.addCategoryObject('typeBinding', u'X1', X1)

# Atomic SimpleTypeDefinition
class X13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X13')
    _Documentation = None
X13._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
X13._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X13._InitializeFacetMap(X13._CF_maxLength,
   X13._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X13', X13)

# Atomic SimpleTypeDefinition
class STD_ANON_39 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_39._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_39, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_39._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_39._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_minInclusive,
   STD_ANON_39._CF_totalDigits,
   STD_ANON_39._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_40 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_40._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15L))
STD_ANON_40._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_totalDigits,
   STD_ANON_40._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class Nombre (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nombre')
    _Documentation = None
Nombre._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(45L))
Nombre._InitializeFacetMap(Nombre._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'Nombre', Nombre)

# Atomic SimpleTypeDefinition
class CodigoDeSolicitud (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoDeSolicitud')
    _Documentation = None
CodigoDeSolicitud._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
CodigoDeSolicitud._InitializeFacetMap(CodigoDeSolicitud._CF_length)
Namespace.addCategoryObject('typeBinding', u'CodigoDeSolicitud', CodigoDeSolicitud)

# Atomic SimpleTypeDefinition
class STD_ANON_41 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_41._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_41, enum_prefix=None)
STD_ANON_41.F = STD_ANON_41._CF_enumeration.addEnumeration(unicode_value=u'F')
STD_ANON_41.S = STD_ANON_41._CF_enumeration.addEnumeration(unicode_value=u'S')
STD_ANON_41.O = STD_ANON_41._CF_enumeration.addEnumeration(unicode_value=u'O')
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_enumeration)

# Atomic SimpleTypeDefinition
class TipoContratoATR (X2):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR')
    _Documentation = None
TipoContratoATR._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'TipoContratoATR', TipoContratoATR)

# Atomic SimpleTypeDefinition
class TiposDocumentacion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipos de Documentaci&#243;n
			01	CIE
			02	Acta de Puesta en Marcha
			03	Acta de Inspecci&#243;n
			04	Reclamaci&#243;n
			05	Respuesta a reclamaci&#243;n
			06	Facturas
			07	Otra documentaci&#243;n del cliente
			08	Otros			
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TiposDocumentacion')
    _Documentation = u'Tipos de Documentaci\xf3n\n\t\t\t01\tCIE\n\t\t\t02\tActa de Puesta en Marcha\n\t\t\t03\tActa de Inspecci\xf3n\n\t\t\t04\tReclamaci\xf3n\n\t\t\t05\tRespuesta a reclamaci\xf3n\n\t\t\t06\tFacturas\n\t\t\t07\tOtra documentaci\xf3n del cliente\n\t\t\t08\tOtros\t\t\t\n\t\t\t'
TiposDocumentacion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TiposDocumentacion, enum_prefix=None)
TiposDocumentacion.n01 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'01')
TiposDocumentacion.n02 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'02')
TiposDocumentacion.n03 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'03')
TiposDocumentacion.n04 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'04')
TiposDocumentacion.n05 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'05')
TiposDocumentacion.n06 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'06')
TiposDocumentacion.n07 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'07')
TiposDocumentacion.n08 = TiposDocumentacion._CF_enumeration.addEnumeration(unicode_value=u'08')
TiposDocumentacion._InitializeFacetMap(TiposDocumentacion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TiposDocumentacion', TiposDocumentacion)

# Atomic SimpleTypeDefinition
class CodigoTarifa (pyxb.binding.datatypes.integer):

    """Codigo Tipo Tarifa (se utilizara una tabla de codigos)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoTarifa')
    _Documentation = u'Codigo Tipo Tarifa (se utilizara una tabla de codigos)'
CodigoTarifa._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(3L))
CodigoTarifa._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
CodigoTarifa._InitializeFacetMap(CodigoTarifa._CF_totalDigits,
   CodigoTarifa._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'CodigoTarifa', CodigoTarifa)

# Atomic SimpleTypeDefinition
class STD_ANON_42 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_42._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_42._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_totalDigits,
   STD_ANON_42._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_43 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_43._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_43, value=pyxb.binding.datatypes.integer(0L))
STD_ANON_43._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(11L))
STD_ANON_43._InitializeFacetMap(STD_ANON_43._CF_minInclusive,
   STD_ANON_43._CF_totalDigits)

# Atomic SimpleTypeDefinition
class DecimalS12V3 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DecimalS12V3')
    _Documentation = None
DecimalS12V3._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(15L))
DecimalS12V3._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
DecimalS12V3._InitializeFacetMap(DecimalS12V3._CF_totalDigits,
   DecimalS12V3._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'DecimalS12V3', DecimalS12V3)

# Atomic SimpleTypeDefinition
class STD_ANON_44 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_44._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_44, enum_prefix=None)
STD_ANON_44.F = STD_ANON_44._CF_enumeration.addEnumeration(unicode_value=u'F')
STD_ANON_44.S = STD_ANON_44._CF_enumeration.addEnumeration(unicode_value=u'S')
STD_ANON_44._InitializeFacetMap(STD_ANON_44._CF_enumeration)

# Atomic SimpleTypeDefinition
class STD_ANON_45 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_45._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_45, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_45._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
STD_ANON_45._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_45._InitializeFacetMap(STD_ANON_45._CF_minInclusive,
   STD_ANON_45._CF_totalDigits,
   STD_ANON_45._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_46 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_46._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_46._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_46._InitializeFacetMap(STD_ANON_46._CF_maxLength,
   STD_ANON_46._CF_minLength)

# Atomic SimpleTypeDefinition
class CodigoDePaso (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoDePaso')
    _Documentation = None
CodigoDePaso._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
CodigoDePaso._InitializeFacetMap(CodigoDePaso._CF_length)
Namespace.addCategoryObject('typeBinding', u'CodigoDePaso', CodigoDePaso)

# Atomic SimpleTypeDefinition
class STD_ANON_47 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_47._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_47._CF_pattern.addPattern(pattern=u'[0-9]{2}|[*]{2}')
STD_ANON_47._InitializeFacetMap(STD_ANON_47._CF_pattern)

# Atomic SimpleTypeDefinition
class STD_ANON_48 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_48._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(8L))
STD_ANON_48._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
STD_ANON_48._InitializeFacetMap(STD_ANON_48._CF_totalDigits,
   STD_ANON_48._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_49 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_49._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_49._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_49._InitializeFacetMap(STD_ANON_49._CF_totalDigits,
   STD_ANON_49._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_50 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_50._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(22L))
STD_ANON_50._InitializeFacetMap(STD_ANON_50._CF_length)

# Atomic SimpleTypeDefinition
class STD_ANON_51 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_51._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(26L))
STD_ANON_51._InitializeFacetMap(STD_ANON_51._CF_maxLength)

# Atomic SimpleTypeDefinition
class TiposSuministro (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipos de Suministro
			AL	Almac&#233;n
			AP	Alumbrado publico
			AS	Ascensores
			AT	Antena Telefonia Movil
			BA	Bateria de acumuladores
			CM	Centro de maniobra y control
			EA	Escalera-Ascensor
			ES	Escalera
			FT	Fabrica y Talleres sin Riesgo Especifico
			FV	Inst.Fotovoltaica
			GA	Garaje
			GB	Grupo Bombeo, Riego por Goteo
			HP	Loc.H&#250;medos con Riesgo de Corrosi&#243;n o Polv.
			IN	Nave industrial
			IT	Instalaci&#243;n Temporal en Emplazam.Abierto
			KC	Kioscos/cabinas tfno
			LB	Locales a Baja Temperatura
			LC	Local comercial
			OF	Oficina
			PC	Publica concurrenc&#237;a
			RA	Refugio o Albergue Agricola
			RT	Repetidor de Televisi&#243;n
			SA	Servicios Auxiliares
			SC	Sumtro complementario
			SE	Sumtro eventual
			SG	Servicio general vivienda
			SM	Sem&#225;foro
			SO	Sumtro obras
			TL	Telecomunicaciones
			TR	Trastero
			UF	Uso finca
			UV	Usos varios
			VI	Vivienda			
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TiposSuministro')
    _Documentation = u'Tipos de Suministro\n\t\t\tAL\tAlmac\xe9n\n\t\t\tAP\tAlumbrado publico\n\t\t\tAS\tAscensores\n\t\t\tAT\tAntena Telefonia Movil\n\t\t\tBA\tBateria de acumuladores\n\t\t\tCM\tCentro de maniobra y control\n\t\t\tEA\tEscalera-Ascensor\n\t\t\tES\tEscalera\n\t\t\tFT\tFabrica y Talleres sin Riesgo Especifico\n\t\t\tFV\tInst.Fotovoltaica\n\t\t\tGA\tGaraje\n\t\t\tGB\tGrupo Bombeo, Riego por Goteo\n\t\t\tHP\tLoc.H\xfamedos con Riesgo de Corrosi\xf3n o Polv.\n\t\t\tIN\tNave industrial\n\t\t\tIT\tInstalaci\xf3n Temporal en Emplazam.Abierto\n\t\t\tKC\tKioscos/cabinas tfno\n\t\t\tLB\tLocales a Baja Temperatura\n\t\t\tLC\tLocal comercial\n\t\t\tOF\tOficina\n\t\t\tPC\tPublica concurrenc\xeda\n\t\t\tRA\tRefugio o Albergue Agricola\n\t\t\tRT\tRepetidor de Televisi\xf3n\n\t\t\tSA\tServicios Auxiliares\n\t\t\tSC\tSumtro complementario\n\t\t\tSE\tSumtro eventual\n\t\t\tSG\tServicio general vivienda\n\t\t\tSM\tSem\xe1foro\n\t\t\tSO\tSumtro obras\n\t\t\tTL\tTelecomunicaciones\n\t\t\tTR\tTrastero\n\t\t\tUF\tUso finca\n\t\t\tUV\tUsos varios\n\t\t\tVI\tVivienda\t\t\t\n\t\t\t'
TiposSuministro._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TiposSuministro, enum_prefix=None)
TiposSuministro.AL = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'AL')
TiposSuministro.AP = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'AP')
TiposSuministro.AS = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'AS')
TiposSuministro.AT = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'AT')
TiposSuministro.BA = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'BA')
TiposSuministro.CM = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'CM')
TiposSuministro.EA = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'EA')
TiposSuministro.ES = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'ES')
TiposSuministro.FT = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'FT')
TiposSuministro.FV = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'FV')
TiposSuministro.GA = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'GA')
TiposSuministro.GB = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'GB')
TiposSuministro.HP = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'HP')
TiposSuministro.IN = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'IN')
TiposSuministro.IT = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'IT')
TiposSuministro.KC = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'KC')
TiposSuministro.LB = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'LB')
TiposSuministro.LC = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'LC')
TiposSuministro.OF = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'OF')
TiposSuministro.PC = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'PC')
TiposSuministro.RA = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'RA')
TiposSuministro.RT = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'RT')
TiposSuministro.SA = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'SA')
TiposSuministro.SC = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'SC')
TiposSuministro.SE = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'SE')
TiposSuministro.SG = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'SG')
TiposSuministro.SM = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'SM')
TiposSuministro.SO = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'SO')
TiposSuministro.TL = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'TL')
TiposSuministro.TR = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'TR')
TiposSuministro.UF = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'UF')
TiposSuministro.UV = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'UV')
TiposSuministro.VI = TiposSuministro._CF_enumeration.addEnumeration(unicode_value=u'VI')
TiposSuministro._InitializeFacetMap(TiposSuministro._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TiposSuministro', TiposSuministro)

# Atomic SimpleTypeDefinition
class Codigo (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Codigo')
    _Documentation = None
Codigo._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(22L))
Codigo._InitializeFacetMap(Codigo._CF_length)
Namespace.addCategoryObject('typeBinding', u'Codigo', Codigo)

# Atomic SimpleTypeDefinition
class TipoEquipoMedida (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """tipo de equipo de medida"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida')
    _Documentation = u'tipo de equipo de medida'
TipoEquipoMedida._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoEquipoMedida, enum_prefix=None)
TipoEquipoMedida.L01 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L01')
TipoEquipoMedida.L02 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L02')
TipoEquipoMedida.L03 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L03')
TipoEquipoMedida.L04 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L04')
TipoEquipoMedida.L05 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L05')
TipoEquipoMedida.L06 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L06')
TipoEquipoMedida.L07 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L07')
TipoEquipoMedida.L08 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L08')
TipoEquipoMedida.L09 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L09')
TipoEquipoMedida.L10 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'L10')
TipoEquipoMedida.R00 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R00')
TipoEquipoMedida.R01 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R01')
TipoEquipoMedida.R02 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R02')
TipoEquipoMedida.R03 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R03')
TipoEquipoMedida.R04 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R04')
TipoEquipoMedida.R05 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R05')
TipoEquipoMedida.R06 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R06')
TipoEquipoMedida.R07 = TipoEquipoMedida._CF_enumeration.addEnumeration(unicode_value=u'R07')
TipoEquipoMedida._InitializeFacetMap(TipoEquipoMedida._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoEquipoMedida', TipoEquipoMedida)

# Atomic SimpleTypeDefinition
class X255 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X255')
    _Documentation = None
X255._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255L))
X255._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X255._InitializeFacetMap(X255._CF_maxLength,
   X255._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X255', X255)

# Atomic SimpleTypeDefinition
class STD_ANON_52 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_52._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_52, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_52._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
STD_ANON_52._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
STD_ANON_52._InitializeFacetMap(STD_ANON_52._CF_minInclusive,
   STD_ANON_52._CF_totalDigits,
   STD_ANON_52._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class TarifaATR (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """tipo Tarifa  
			001	2.0.A	
			002	2.0.N.A 	
			003	3.0A	
			004	2.0DHA					
			011	3.1A	
			012	6.1	
			013	6.2	
			014	6.3	
			015	6.4	
			016	6.5
			901   Tf. Peaje BT 2.0  Modo 2
			902   Tf. Peaje BT 2.0N Modo 2		
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TarifaATR')
    _Documentation = u'tipo Tarifa  \n\t\t\t001\t2.0.A\t\n\t\t\t002\t2.0.N.A \t\n\t\t\t003\t3.0A\t\n\t\t\t004\t2.0DHA\t\t\t\t\t\n\t\t\t011\t3.1A\t\n\t\t\t012\t6.1\t\n\t\t\t013\t6.2\t\n\t\t\t014\t6.3\t\n\t\t\t015\t6.4\t\n\t\t\t016\t6.5\n\t\t\t901   Tf. Peaje BT 2.0  Modo 2\n\t\t\t902   Tf. Peaje BT 2.0N Modo 2\t\t\n\t\t\t'
TarifaATR._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TarifaATR, enum_prefix=None)
TarifaATR.n001 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'001')
TarifaATR.n002 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'002')
TarifaATR.n003 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'003')
TarifaATR.n004 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'004')
TarifaATR.n011 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'011')
TarifaATR.n012 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'012')
TarifaATR.n013 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'013')
TarifaATR.n014 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'014')
TarifaATR.n015 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'015')
TarifaATR.n016 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'016')
TarifaATR.n901 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'901')
TarifaATR.n902 = TarifaATR._CF_enumeration.addEnumeration(unicode_value=u'902')
TarifaATR._InitializeFacetMap(TarifaATR._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TarifaATR', TarifaATR)

# Atomic SimpleTypeDefinition
class STD_ANON_53 (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_53._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_53, value=pyxb.binding.datatypes.integer(0L))
STD_ANON_53._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(9L))
STD_ANON_53._InitializeFacetMap(STD_ANON_53._CF_minInclusive,
   STD_ANON_53._CF_totalDigits)

# Atomic SimpleTypeDefinition
class STD_ANON_54 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_54._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_54._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_54._InitializeFacetMap(STD_ANON_54._CF_totalDigits,
   STD_ANON_54._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class LineaNegocio (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ 01 Electrico
 02 Gas """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LineaNegocio')
    _Documentation = u' 01 Electrico\n 02 Gas '
LineaNegocio._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LineaNegocio, enum_prefix=None)
LineaNegocio.n01 = LineaNegocio._CF_enumeration.addEnumeration(unicode_value=u'01')
LineaNegocio.n02 = LineaNegocio._CF_enumeration.addEnumeration(unicode_value=u'02')
LineaNegocio._InitializeFacetMap(LineaNegocio._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LineaNegocio', LineaNegocio)

# Atomic SimpleTypeDefinition
class STD_ANON_55 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_55._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_55._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_55._InitializeFacetMap(STD_ANON_55._CF_totalDigits,
   STD_ANON_55._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class EnergiaFact (pyxb.binding.datatypes.integer):

    """Energia a facturar"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EnergiaFact')
    _Documentation = u'Energia a facturar'
EnergiaFact._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(13L))
EnergiaFact._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
EnergiaFact._InitializeFacetMap(EnergiaFact._CF_totalDigits,
   EnergiaFact._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'EnergiaFact', EnergiaFact)

# Atomic SimpleTypeDefinition
class STD_ANON_56 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_56._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_56, value=pyxb.binding.datatypes.decimal(Decimal('0')))
STD_ANON_56._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(5L))
STD_ANON_56._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_56._InitializeFacetMap(STD_ANON_56._CF_minInclusive,
   STD_ANON_56._CF_totalDigits,
   STD_ANON_56._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class TipoPM (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """tipo de punto de medida
			01	Punto de medida tipo 1	
			02	Punto de medida tipo 2	
			03	Punto de medida tipo 3	
			04	Punto de medida tipo 4	
			05	Punto de medida tipo 5	
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoPM')
    _Documentation = u'tipo de punto de medida\n\t\t\t01\tPunto de medida tipo 1\t\n\t\t\t02\tPunto de medida tipo 2\t\n\t\t\t03\tPunto de medida tipo 3\t\n\t\t\t04\tPunto de medida tipo 4\t\n\t\t\t05\tPunto de medida tipo 5\t\n\t\t\t'
TipoPM._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoPM, enum_prefix=None)
TipoPM.n01 = TipoPM._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoPM.n02 = TipoPM._CF_enumeration.addEnumeration(unicode_value=u'02')
TipoPM.n03 = TipoPM._CF_enumeration.addEnumeration(unicode_value=u'03')
TipoPM.n04 = TipoPM._CF_enumeration.addEnumeration(unicode_value=u'04')
TipoPM.n05 = TipoPM._CF_enumeration.addEnumeration(unicode_value=u'05')
TipoPM._InitializeFacetMap(TipoPM._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoPM', TipoPM)

# Atomic SimpleTypeDefinition
class ModoLecturaPM (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """  Modo Lectura Tabla 38
			 1   Lectura Local Manual
			 2   Lectura Local Optoacoplador
			 3   Lectura Local Puerto Serie
			 4   Telemedida Operativa
			 5   Telemedida no Operativa
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModoLecturaPM')
    _Documentation = u'  Modo Lectura Tabla 38\n\t\t\t 1   Lectura Local Manual\n\t\t\t 2   Lectura Local Optoacoplador\n\t\t\t 3   Lectura Local Puerto Serie\n\t\t\t 4   Telemedida Operativa\n\t\t\t 5   Telemedida no Operativa\n\t\t\t'
ModoLecturaPM._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ModoLecturaPM, enum_prefix=None)
ModoLecturaPM.n1 = ModoLecturaPM._CF_enumeration.addEnumeration(unicode_value=u'1')
ModoLecturaPM.n2 = ModoLecturaPM._CF_enumeration.addEnumeration(unicode_value=u'2')
ModoLecturaPM.n3 = ModoLecturaPM._CF_enumeration.addEnumeration(unicode_value=u'3')
ModoLecturaPM.n4 = ModoLecturaPM._CF_enumeration.addEnumeration(unicode_value=u'4')
ModoLecturaPM.n5 = ModoLecturaPM._CF_enumeration.addEnumeration(unicode_value=u'5')
ModoLecturaPM._InitializeFacetMap(ModoLecturaPM._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ModoLecturaPM', ModoLecturaPM)

# Atomic SimpleTypeDefinition
class TipoPropiedad (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo propietario
			1	Distribuidor	
			2	Cliente	
			3	Comercializador	
			4	Otros
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoPropiedad')
    _Documentation = u'Tipo propietario\n\t\t\t1\tDistribuidor\t\n\t\t\t2\tCliente\t\n\t\t\t3\tComercializador\t\n\t\t\t4\tOtros\n\t\t\t'
TipoPropiedad._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoPropiedad, enum_prefix=None)
TipoPropiedad.n1 = TipoPropiedad._CF_enumeration.addEnumeration(unicode_value=u'1')
TipoPropiedad.n2 = TipoPropiedad._CF_enumeration.addEnumeration(unicode_value=u'2')
TipoPropiedad.n3 = TipoPropiedad._CF_enumeration.addEnumeration(unicode_value=u'3')
TipoPropiedad.n4 = TipoPropiedad._CF_enumeration.addEnumeration(unicode_value=u'4')
TipoPropiedad._InitializeFacetMap(TipoPropiedad._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoPropiedad', TipoPropiedad)

# Atomic SimpleTypeDefinition
class X250 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X250')
    _Documentation = None
X250._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(250L))
X250._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X250._InitializeFacetMap(X250._CF_maxLength,
   X250._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X250', X250)

# Atomic SimpleTypeDefinition
class TipoMotivoAjuste (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
			01	Veriicaci&#243;n equipo de medida
			02	Aver&#237;a en contador
			03	Aver&#237;a en Trafo de Tensi&#243;n
			04	Aver&#237;a en Trafo de intensidad
			05	Desbordamiento del Registrador
			06	Problemas en la sincronizaci&#243;n del registrador
			07	P&#233;rdida de alimentaci&#243;n del registrador
			08	Manipulaci&#243;n de equipos
			09	Servicio Directo (sin EM)
			10	Punto de medida inaccesible
			11	Punto de medida ilocalizable
			99	Otros
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoMotivoAjuste')
    _Documentation = u'\n\t\t\t01\tVeriicaci\xf3n equipo de medida\n\t\t\t02\tAver\xeda en contador\n\t\t\t03\tAver\xeda en Trafo de Tensi\xf3n\n\t\t\t04\tAver\xeda en Trafo de intensidad\n\t\t\t05\tDesbordamiento del Registrador\n\t\t\t06\tProblemas en la sincronizaci\xf3n del registrador\n\t\t\t07\tP\xe9rdida de alimentaci\xf3n del registrador\n\t\t\t08\tManipulaci\xf3n de equipos\n\t\t\t09\tServicio Directo (sin EM)\n\t\t\t10\tPunto de medida inaccesible\n\t\t\t11\tPunto de medida ilocalizable\n\t\t\t99\tOtros\n\t\t\t'
TipoMotivoAjuste._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TipoMotivoAjuste, enum_prefix=None)
TipoMotivoAjuste.n01 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'01')
TipoMotivoAjuste.n02 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'02')
TipoMotivoAjuste.n03 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'03')
TipoMotivoAjuste.n04 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'04')
TipoMotivoAjuste.n05 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'05')
TipoMotivoAjuste.n06 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'06')
TipoMotivoAjuste.n07 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'07')
TipoMotivoAjuste.n08 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'08')
TipoMotivoAjuste.n09 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'09')
TipoMotivoAjuste.n10 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'10')
TipoMotivoAjuste.n11 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'11')
TipoMotivoAjuste.n99 = TipoMotivoAjuste._CF_enumeration.addEnumeration(unicode_value=u'99')
TipoMotivoAjuste._InitializeFacetMap(TipoMotivoAjuste._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'TipoMotivoAjuste', TipoMotivoAjuste)

# Atomic SimpleTypeDefinition
class CodigoMotivoIncidencia (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """codigo motivo de la incidencia
			01	Cliente ausente
			02	Acceso imposibilitado 
			03	Deficiencias en la instalaci&#243;n
			04	Posible anormalidad/fraude
			05	El cliente aporta el equipo y no lo ha puesto a disposici&#243;n la distribuidora
			06	El equipo aportado por el cliente no es el adecuado
			07	Inexistencia de ICP y no se informa sobre quien lo aporta
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CodigoMotivoIncidencia')
    _Documentation = u'codigo motivo de la incidencia\n\t\t\t01\tCliente ausente\n\t\t\t02\tAcceso imposibilitado \n\t\t\t03\tDeficiencias en la instalaci\xf3n\n\t\t\t04\tPosible anormalidad/fraude\n\t\t\t05\tEl cliente aporta el equipo y no lo ha puesto a disposici\xf3n la distribuidora\n\t\t\t06\tEl equipo aportado por el cliente no es el adecuado\n\t\t\t07\tInexistencia de ICP y no se informa sobre quien lo aporta\n\t\t\t'
CodigoMotivoIncidencia._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodigoMotivoIncidencia, enum_prefix=None)
CodigoMotivoIncidencia.n01 = CodigoMotivoIncidencia._CF_enumeration.addEnumeration(unicode_value=u'01')
CodigoMotivoIncidencia.n02 = CodigoMotivoIncidencia._CF_enumeration.addEnumeration(unicode_value=u'02')
CodigoMotivoIncidencia.n03 = CodigoMotivoIncidencia._CF_enumeration.addEnumeration(unicode_value=u'03')
CodigoMotivoIncidencia.n04 = CodigoMotivoIncidencia._CF_enumeration.addEnumeration(unicode_value=u'04')
CodigoMotivoIncidencia.n05 = CodigoMotivoIncidencia._CF_enumeration.addEnumeration(unicode_value=u'05')
CodigoMotivoIncidencia.n06 = CodigoMotivoIncidencia._CF_enumeration.addEnumeration(unicode_value=u'06')
CodigoMotivoIncidencia.n07 = CodigoMotivoIncidencia._CF_enumeration.addEnumeration(unicode_value=u'07')
CodigoMotivoIncidencia._InitializeFacetMap(CodigoMotivoIncidencia._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CodigoMotivoIncidencia', CodigoMotivoIncidencia)

# Atomic SimpleTypeDefinition
class STD_ANON_57 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_57._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_57._InitializeFacetMap(STD_ANON_57._CF_length)

# Atomic SimpleTypeDefinition
class STD_ANON_58 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_58._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
STD_ANON_58._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_58._InitializeFacetMap(STD_ANON_58._CF_maxLength,
   STD_ANON_58._CF_minLength)

# Atomic SimpleTypeDefinition
class AltaBajaModificacion (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AltaBajaModificacion')
    _Documentation = None
AltaBajaModificacion._CF_pattern = pyxb.binding.facets.CF_pattern()
AltaBajaModificacion._CF_pattern.addPattern(pattern=u'A|B|M')
AltaBajaModificacion._InitializeFacetMap(AltaBajaModificacion._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'AltaBajaModificacion', AltaBajaModificacion)

# Atomic SimpleTypeDefinition
class STD_ANON_59 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_59._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
STD_ANON_59._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_59._InitializeFacetMap(STD_ANON_59._CF_maxLength,
   STD_ANON_59._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_60 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_60._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(14L))
STD_ANON_60._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_60._InitializeFacetMap(STD_ANON_60._CF_totalDigits,
   STD_ANON_60._CF_fractionDigits)

# Atomic SimpleTypeDefinition
class InstalacionICP (pyxb.binding.datatypes.integer, pyxb.binding.basis.enumeration_mixin):

    """instalacion y regimen del ICP
			1 - instalado y propiedad del cliente 
			2 - instalado en regimen de alquiler
			3 - no instalado
			4 - desconocido
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InstalacionICP')
    _Documentation = u'instalacion y regimen del ICP\n\t\t\t1 - instalado y propiedad del cliente \n\t\t\t2 - instalado en regimen de alquiler\n\t\t\t3 - no instalado\n\t\t\t4 - desconocido\n\t\t\t'
InstalacionICP._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InstalacionICP, enum_prefix=None)
InstalacionICP._CF_enumeration.addEnumeration(unicode_value=u'1')
InstalacionICP._CF_enumeration.addEnumeration(unicode_value=u'2')
InstalacionICP._CF_enumeration.addEnumeration(unicode_value=u'3')
InstalacionICP._CF_enumeration.addEnumeration(unicode_value=u'4')
InstalacionICP._InitializeFacetMap(InstalacionICP._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'InstalacionICP', InstalacionICP)

# Atomic SimpleTypeDefinition
class IndicativoARO (pyxb.binding.datatypes.string):

    """indicativo Tipo Movimiento Solicitud (A Env&#237;o de Autolecturas/ R Reclamaciones/ O Otras Peticiones"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IndicativoARO')
    _Documentation = u'indicativo Tipo Movimiento Solicitud (A Env\xedo de Autolecturas/ R Reclamaciones/ O Otras Peticiones'
IndicativoARO._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
IndicativoARO._CF_pattern = pyxb.binding.facets.CF_pattern()
IndicativoARO._CF_pattern.addPattern(pattern=u'A|R|O')
IndicativoARO._InitializeFacetMap(IndicativoARO._CF_length,
   IndicativoARO._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IndicativoARO', IndicativoARO)

# Atomic SimpleTypeDefinition
class Decimal1 (pyxb.binding.datatypes.integer):

    """decimal de un digito"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Decimal1')
    _Documentation = u'decimal de un digito'
Decimal1._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(1L))
Decimal1._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(0L))
Decimal1._InitializeFacetMap(Decimal1._CF_totalDigits,
   Decimal1._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'Decimal1', Decimal1)

# Atomic SimpleTypeDefinition
class X6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'X6')
    _Documentation = None
X6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
X6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
X6._InitializeFacetMap(X6._CF_maxLength,
   X6._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'X6', X6)

# Complex type IdCliente with content type ELEMENT_ONLY
class IdCliente (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IdCliente')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Identificador uses Python identifier Identificador
    __Identificador = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identificador'), 'Identificador', '__httplocalhostelegibilidad_IdCliente_httplocalhostelegibilidadIdentificador', False)

    
    Identificador = property(__Identificador.value, __Identificador.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoCIFNIF uses Python identifier TipoCIFNIF
    __TipoCIFNIF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoCIFNIF'), 'TipoCIFNIF', '__httplocalhostelegibilidad_IdCliente_httplocalhostelegibilidadTipoCIFNIF', False)

    
    TipoCIFNIF = property(__TipoCIFNIF.value, __TipoCIFNIF.set, None, u'Tabla 6')


    _ElementMap = {
        __Identificador.name() : __Identificador,
        __TipoCIFNIF.name() : __TipoCIFNIF
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'IdCliente', IdCliente)


# Complex type MedidaAparato with content type ELEMENT_ONLY
class MedidaAparato (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MedidaAparato')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}TextoAnomalia uses Python identifier TextoAnomalia
    __TextoAnomalia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TextoAnomalia'), 'TextoAnomalia', '__httplocalhostelegibilidad_MedidaAparato_httplocalhostelegibilidadTextoAnomalia', False)

    
    TextoAnomalia = property(__TextoAnomalia.value, __TextoAnomalia.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoDH uses Python identifier TipoDH
    __TipoDH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoDH'), 'TipoDH', '__httplocalhostelegibilidad_MedidaAparato_httplocalhostelegibilidadTipoDH', False)

    
    TipoDH = property(__TipoDH.value, __TipoDH.set, None, None)

    
    # Element {http://localhost/elegibilidad}Anomalia uses Python identifier Anomalia
    __Anomalia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Anomalia'), 'Anomalia', '__httplocalhostelegibilidad_MedidaAparato_httplocalhostelegibilidadAnomalia', False)

    
    Anomalia = property(__Anomalia.value, __Anomalia.set, None, None)

    
    # Element {http://localhost/elegibilidad}MagnitudMedida uses Python identifier MagnitudMedida
    __MagnitudMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagnitudMedida'), 'MagnitudMedida', '__httplocalhostelegibilidad_MedidaAparato_httplocalhostelegibilidadMagnitudMedida', False)

    
    MagnitudMedida = property(__MagnitudMedida.value, __MagnitudMedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}Procedencia uses Python identifier Procedencia
    __Procedencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Procedencia'), 'Procedencia', '__httplocalhostelegibilidad_MedidaAparato_httplocalhostelegibilidadProcedencia', False)

    
    Procedencia = property(__Procedencia.value, __Procedencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_MedidaAparato_httplocalhostelegibilidadPeriodo', False)

    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)

    
    # Element {http://localhost/elegibilidad}LecturaAnterior uses Python identifier LecturaAnterior
    __LecturaAnterior = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LecturaAnterior'), 'LecturaAnterior', '__httplocalhostelegibilidad_MedidaAparato_httplocalhostelegibilidadLecturaAnterior', False)

    
    LecturaAnterior = property(__LecturaAnterior.value, __LecturaAnterior.set, None, None)


    _ElementMap = {
        __TextoAnomalia.name() : __TextoAnomalia,
        __TipoDH.name() : __TipoDH,
        __Anomalia.name() : __Anomalia,
        __MagnitudMedida.name() : __MagnitudMedida,
        __Procedencia.name() : __Procedencia,
        __Periodo.name() : __Periodo,
        __LecturaAnterior.name() : __LecturaAnterior
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'MedidaAparato', MedidaAparato)


# Complex type CTD_ANON with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteFacturacionAlquileres uses Python identifier ImporteFacturacionAlquileres
    __ImporteFacturacionAlquileres = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteFacturacionAlquileres'), 'ImporteFacturacionAlquileres', '__httplocalhostelegibilidad_CTD_ANON_httplocalhostelegibilidadImporteFacturacionAlquileres', False)

    
    ImporteFacturacionAlquileres = property(__ImporteFacturacionAlquileres.value, __ImporteFacturacionAlquileres.set, None, u'Suma de alquileres de equipos asociados al CUPS.')


    _ElementMap = {
        __ImporteFacturacionAlquileres.name() : __ImporteFacturacionAlquileres
    }
    _AttributeMap = {
        
    }



# Complex type IdContrato with content type ELEMENT_ONLY
class IdContrato (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IdContrato')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}CodContrato uses Python identifier CodContrato
    __CodContrato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodContrato'), 'CodContrato', '__httplocalhostelegibilidad_IdContrato_httplocalhostelegibilidadCodContrato', False)

    
    CodContrato = property(__CodContrato.value, __CodContrato.set, None, None)


    _ElementMap = {
        __CodContrato.name() : __CodContrato
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'IdContrato', IdContrato)


# Complex type CTD_ANON_ with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PrecioPotencia uses Python identifier PrecioPotencia
    __PrecioPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrecioPotencia'), 'PrecioPotencia', '__httplocalhostelegibilidad_CTD_ANON__httplocalhostelegibilidadPrecioPotencia', False)

    
    PrecioPotencia = property(__PrecioPotencia.value, __PrecioPotencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}PotenciaContratada uses Python identifier PotenciaContratada
    __PotenciaContratada = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciaContratada'), 'PotenciaContratada', '__httplocalhostelegibilidad_CTD_ANON__httplocalhostelegibilidadPotenciaContratada', False)

    
    PotenciaContratada = property(__PotenciaContratada.value, __PotenciaContratada.set, None, u'En watios')

    
    # Element {http://localhost/elegibilidad}PotenciaAFacturar uses Python identifier PotenciaAFacturar
    __PotenciaAFacturar = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciaAFacturar'), 'PotenciaAFacturar', '__httplocalhostelegibilidad_CTD_ANON__httplocalhostelegibilidadPotenciaAFacturar', False)

    
    PotenciaAFacturar = property(__PotenciaAFacturar.value, __PotenciaAFacturar.set, None, u'Potencia a facturar calculada en funci\xf3n de la potencia contratada. En Watios')

    
    # Element {http://localhost/elegibilidad}PotenciaMaxDemandada uses Python identifier PotenciaMaxDemandada
    __PotenciaMaxDemandada = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciaMaxDemandada'), 'PotenciaMaxDemandada', '__httplocalhostelegibilidad_CTD_ANON__httplocalhostelegibilidadPotenciaMaxDemandada', False)

    
    PotenciaMaxDemandada = property(__PotenciaMaxDemandada.value, __PotenciaMaxDemandada.set, None, u' En watios')


    _ElementMap = {
        __PrecioPotencia.name() : __PrecioPotencia,
        __PotenciaContratada.name() : __PotenciaContratada,
        __PotenciaAFacturar.name() : __PotenciaAFacturar,
        __PotenciaMaxDemandada.name() : __PotenciaMaxDemandada
    }
    _AttributeMap = {
        
    }



# Complex type ClienteSinTelefono with content type ELEMENT_ONLY
class ClienteSinTelefono (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClienteSinTelefono')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}TitularContratoVsTitularPago uses Python identifier TitularContratoVsTitularPago
    __TitularContratoVsTitularPago = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TitularContratoVsTitularPago'), 'TitularContratoVsTitularPago', '__httplocalhostelegibilidad_ClienteSinTelefono_httplocalhostelegibilidadTitularContratoVsTitularPago', False)

    
    TitularContratoVsTitularPago = property(__TitularContratoVsTitularPago.value, __TitularContratoVsTitularPago.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdCliente uses Python identifier IdCliente
    __IdCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), 'IdCliente', '__httplocalhostelegibilidad_ClienteSinTelefono_httplocalhostelegibilidadIdCliente', False)

    
    IdCliente = property(__IdCliente.value, __IdCliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}Nombre uses Python identifier Nombre
    __Nombre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), 'Nombre', '__httplocalhostelegibilidad_ClienteSinTelefono_httplocalhostelegibilidadNombre', False)

    
    Nombre = property(__Nombre.value, __Nombre.set, None, None)


    _ElementMap = {
        __TitularContratoVsTitularPago.name() : __TitularContratoVsTitularPago,
        __IdCliente.name() : __IdCliente,
        __Nombre.name() : __Nombre
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ClienteSinTelefono', ClienteSinTelefono)


# Complex type TipoIVAIGIC with content type ELEMENT_ONLY
class TipoIVAIGIC (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoIVAIGIC')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Importe uses Python identifier Importe
    __Importe = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Importe'), 'Importe', '__httplocalhostelegibilidad_TipoIVAIGIC_httplocalhostelegibilidadImporte', False)

    
    Importe = property(__Importe.value, __Importe.set, None, u'En Canarias se informar\xe1 IGIC; en el resto, IVA.')

    
    # Element {http://localhost/elegibilidad}BaseImponible uses Python identifier BaseImponible
    __BaseImponible = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BaseImponible'), 'BaseImponible', '__httplocalhostelegibilidad_TipoIVAIGIC_httplocalhostelegibilidadBaseImponible', False)

    
    BaseImponible = property(__BaseImponible.value, __BaseImponible.set, None, u'En Canarias se informar\xe1 IGIC; en el resto, IVA.')

    
    # Element {http://localhost/elegibilidad}Porcentaje uses Python identifier Porcentaje
    __Porcentaje = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Porcentaje'), 'Porcentaje', '__httplocalhostelegibilidad_TipoIVAIGIC_httplocalhostelegibilidadPorcentaje', False)

    
    Porcentaje = property(__Porcentaje.value, __Porcentaje.set, None, u'En Canarias se informar\xe1 IGIC; en el resto, IVA.')


    _ElementMap = {
        __Importe.name() : __Importe,
        __BaseImponible.name() : __BaseImponible,
        __Porcentaje.name() : __Porcentaje
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'TipoIVAIGIC', TipoIVAIGIC)


# Complex type CTD_ANON_2 with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PrecioEnergiaReactiva uses Python identifier PrecioEnergiaReactiva
    __PrecioEnergiaReactiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrecioEnergiaReactiva'), 'PrecioEnergiaReactiva', '__httplocalhostelegibilidad_CTD_ANON_2_httplocalhostelegibilidadPrecioEnergiaReactiva', False)

    
    PrecioEnergiaReactiva = property(__PrecioEnergiaReactiva.value, __PrecioEnergiaReactiva.set, None, None)

    
    # Element {http://localhost/elegibilidad}ValorEnergiaReactiva uses Python identifier ValorEnergiaReactiva
    __ValorEnergiaReactiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ValorEnergiaReactiva'), 'ValorEnergiaReactiva', '__httplocalhostelegibilidad_CTD_ANON_2_httplocalhostelegibilidadValorEnergiaReactiva', False)

    
    ValorEnergiaReactiva = property(__ValorEnergiaReactiva.value, __ValorEnergiaReactiva.set, None, None)


    _ElementMap = {
        __PrecioEnergiaReactiva.name() : __PrecioEnergiaReactiva,
        __ValorEnergiaReactiva.name() : __ValorEnergiaReactiva
    }
    _AttributeMap = {
        
    }



# Complex type ReactivasAFacturar with content type ELEMENT_ONLY
class ReactivasAFacturar (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReactivasAFacturar')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ReactivaAFacturar uses Python identifier ReactivaAFacturar
    __ReactivaAFacturar = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ReactivaAFacturar'), 'ReactivaAFacturar', '__httplocalhostelegibilidad_ReactivasAFacturar_httplocalhostelegibilidadReactivaAFacturar', True)

    
    ReactivaAFacturar = property(__ReactivaAFacturar.value, __ReactivaAFacturar.set, None, None)


    _ElementMap = {
        __ReactivaAFacturar.name() : __ReactivaAFacturar
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ReactivasAFacturar', ReactivasAFacturar)


# Complex type ImportesTerminoEnergia with content type ELEMENT_ONLY
class ImportesTerminoEnergia (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoEnergia')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTerminoEnergia uses Python identifier ImporteTerminoEnergia
    __ImporteTerminoEnergia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTerminoEnergia'), 'ImporteTerminoEnergia', '__httplocalhostelegibilidad_ImportesTerminoEnergia_httplocalhostelegibilidadImporteTerminoEnergia', True)

    
    ImporteTerminoEnergia = property(__ImporteTerminoEnergia.value, __ImporteTerminoEnergia.set, None, None)


    _ElementMap = {
        __ImporteTerminoEnergia.name() : __ImporteTerminoEnergia
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ImportesTerminoEnergia', ImportesTerminoEnergia)


# Complex type IdReclamante with content type ELEMENT_ONLY
class IdReclamante (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IdReclamante')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Identificador uses Python identifier Identificador
    __Identificador = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identificador'), 'Identificador', '__httplocalhostelegibilidad_IdReclamante_httplocalhostelegibilidadIdentificador', False)

    
    Identificador = property(__Identificador.value, __Identificador.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoCIFNIF uses Python identifier TipoCIFNIF
    __TipoCIFNIF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoCIFNIF'), 'TipoCIFNIF', '__httplocalhostelegibilidad_IdReclamante_httplocalhostelegibilidadTipoCIFNIF', False)

    
    TipoCIFNIF = property(__TipoCIFNIF.value, __TipoCIFNIF.set, None, u'Tabla 6')


    _ElementMap = {
        __Identificador.name() : __Identificador,
        __TipoCIFNIF.name() : __TipoCIFNIF
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'IdReclamante', IdReclamante)


# Complex type CTD_ANON_3 with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}NumeroMeses uses Python identifier NumeroMeses
    __NumeroMeses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroMeses'), 'NumeroMeses', '__httplocalhostelegibilidad_CTD_ANON_3_httplocalhostelegibilidadNumeroMeses', False)

    
    NumeroMeses = property(__NumeroMeses.value, __NumeroMeses.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaDesdeFactura uses Python identifier FechaDesdeFactura
    __FechaDesdeFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeFactura'), 'FechaDesdeFactura', '__httplocalhostelegibilidad_CTD_ANON_3_httplocalhostelegibilidadFechaDesdeFactura', False)

    
    FechaDesdeFactura = property(__FechaDesdeFactura.value, __FechaDesdeFactura.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHastaFactura uses Python identifier FechaHastaFactura
    __FechaHastaFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaFactura'), 'FechaHastaFactura', '__httplocalhostelegibilidad_CTD_ANON_3_httplocalhostelegibilidadFechaHastaFactura', False)

    
    FechaHastaFactura = property(__FechaHastaFactura.value, __FechaHastaFactura.set, None, None)


    _ElementMap = {
        __NumeroMeses.name() : __NumeroMeses,
        __FechaDesdeFactura.name() : __FechaDesdeFactura,
        __FechaHastaFactura.name() : __FechaHastaFactura
    }
    _AttributeMap = {
        
    }



# Complex type TipoLimiteIntervaloLectura with content type ELEMENT_ONLY
class TipoLimiteIntervaloLectura (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoLimiteIntervaloLectura')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Lectura uses Python identifier Lectura
    __Lectura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Lectura'), 'Lectura', '__httplocalhostelegibilidad_TipoLimiteIntervaloLectura_httplocalhostelegibilidadLectura', False)

    
    Lectura = property(__Lectura.value, __Lectura.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHora uses Python identifier FechaHora
    __FechaHora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHora'), 'FechaHora', '__httplocalhostelegibilidad_TipoLimiteIntervaloLectura_httplocalhostelegibilidadFechaHora', False)

    
    FechaHora = property(__FechaHora.value, __FechaHora.set, None, None)

    
    # Element {http://localhost/elegibilidad}Procedencia uses Python identifier Procedencia
    __Procedencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Procedencia'), 'Procedencia', '__httplocalhostelegibilidad_TipoLimiteIntervaloLectura_httplocalhostelegibilidadProcedencia', False)

    
    Procedencia = property(__Procedencia.value, __Procedencia.set, None, u'Tabla 44')


    _ElementMap = {
        __Lectura.name() : __Lectura,
        __FechaHora.name() : __FechaHora,
        __Procedencia.name() : __Procedencia
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'TipoLimiteIntervaloLectura', TipoLimiteIntervaloLectura)


# Complex type Cabecera with content type ELEMENT_ONLY
class Cabecera (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Cabecera')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}FechaSolicitud uses Python identifier FechaSolicitud
    __FechaSolicitud = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaSolicitud'), 'FechaSolicitud', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadFechaSolicitud', False)

    
    FechaSolicitud = property(__FechaSolicitud.value, __FechaSolicitud.set, None, None)

    
    # Element {http://localhost/elegibilidad}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Version'), 'Version', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadVersion', False)

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoREEEmpresaEmisora uses Python identifier CodigoREEEmpresaEmisora
    __CodigoREEEmpresaEmisora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoREEEmpresaEmisora'), 'CodigoREEEmpresaEmisora', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadCodigoREEEmpresaEmisora', False)

    
    CodigoREEEmpresaEmisora = property(__CodigoREEEmpresaEmisora.value, __CodigoREEEmpresaEmisora.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoDelProceso uses Python identifier CodigoDelProceso
    __CodigoDelProceso = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoDelProceso'), 'CodigoDelProceso', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadCodigoDelProceso', False)

    
    CodigoDelProceso = property(__CodigoDelProceso.value, __CodigoDelProceso.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoREEEmpresaDestino uses Python identifier CodigoREEEmpresaDestino
    __CodigoREEEmpresaDestino = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoREEEmpresaDestino'), 'CodigoREEEmpresaDestino', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadCodigoREEEmpresaDestino', False)

    
    CodigoREEEmpresaDestino = property(__CodigoREEEmpresaDestino.value, __CodigoREEEmpresaDestino.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoDeSolicitud uses Python identifier CodigoDeSolicitud
    __CodigoDeSolicitud = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoDeSolicitud'), 'CodigoDeSolicitud', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadCodigoDeSolicitud', False)

    
    CodigoDeSolicitud = property(__CodigoDeSolicitud.value, __CodigoDeSolicitud.set, None, None)

    
    # Element {http://localhost/elegibilidad}SecuencialDeSolicitud uses Python identifier SecuencialDeSolicitud
    __SecuencialDeSolicitud = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SecuencialDeSolicitud'), 'SecuencialDeSolicitud', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadSecuencialDeSolicitud', False)

    
    SecuencialDeSolicitud = property(__SecuencialDeSolicitud.value, __SecuencialDeSolicitud.set, None, None)

    
    # Element {http://localhost/elegibilidad}Codigo uses Python identifier Codigo
    __Codigo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Codigo'), 'Codigo', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadCodigo', False)

    
    Codigo = property(__Codigo.value, __Codigo.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoDePaso uses Python identifier CodigoDePaso
    __CodigoDePaso = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoDePaso'), 'CodigoDePaso', '__httplocalhostelegibilidad_Cabecera_httplocalhostelegibilidadCodigoDePaso', False)

    
    CodigoDePaso = property(__CodigoDePaso.value, __CodigoDePaso.set, None, None)


    _ElementMap = {
        __FechaSolicitud.name() : __FechaSolicitud,
        __Version.name() : __Version,
        __CodigoREEEmpresaEmisora.name() : __CodigoREEEmpresaEmisora,
        __CodigoDelProceso.name() : __CodigoDelProceso,
        __CodigoREEEmpresaDestino.name() : __CodigoREEEmpresaDestino,
        __CodigoDeSolicitud.name() : __CodigoDeSolicitud,
        __SecuencialDeSolicitud.name() : __SecuencialDeSolicitud,
        __Codigo.name() : __Codigo,
        __CodigoDePaso.name() : __CodigoDePaso
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Cabecera', Cabecera)


# Complex type EnergiasAFacturar with content type ELEMENT_ONLY
class EnergiasAFacturar (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EnergiasAFacturar')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}EnergiaAFacturar uses Python identifier EnergiaAFacturar
    __EnergiaAFacturar = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EnergiaAFacturar'), 'EnergiaAFacturar', '__httplocalhostelegibilidad_EnergiasAFacturar_httplocalhostelegibilidadEnergiaAFacturar', True)

    
    EnergiaAFacturar = property(__EnergiaAFacturar.value, __EnergiaAFacturar.set, None, None)


    _ElementMap = {
        __EnergiaAFacturar.name() : __EnergiaAFacturar
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'EnergiasAFacturar', EnergiasAFacturar)


# Complex type NombreCliente with content type ELEMENT_ONLY
class NombreCliente (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NombreCliente')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}SegundoApellido uses Python identifier SegundoApellido
    __SegundoApellido = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SegundoApellido'), 'SegundoApellido', '__httplocalhostelegibilidad_NombreCliente_httplocalhostelegibilidadSegundoApellido', False)

    
    SegundoApellido = property(__SegundoApellido.value, __SegundoApellido.set, None, None)

    
    # Element {http://localhost/elegibilidad}NombreDePila uses Python identifier NombreDePila
    __NombreDePila = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NombreDePila'), 'NombreDePila', '__httplocalhostelegibilidad_NombreCliente_httplocalhostelegibilidadNombreDePila', False)

    
    NombreDePila = property(__NombreDePila.value, __NombreDePila.set, None, None)

    
    # Element {http://localhost/elegibilidad}RazonSocial uses Python identifier RazonSocial
    __RazonSocial = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RazonSocial'), 'RazonSocial', '__httplocalhostelegibilidad_NombreCliente_httplocalhostelegibilidadRazonSocial', False)

    
    RazonSocial = property(__RazonSocial.value, __RazonSocial.set, None, None)

    
    # Element {http://localhost/elegibilidad}PrimerApellido uses Python identifier PrimerApellido
    __PrimerApellido = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrimerApellido'), 'PrimerApellido', '__httplocalhostelegibilidad_NombreCliente_httplocalhostelegibilidadPrimerApellido', False)

    
    PrimerApellido = property(__PrimerApellido.value, __PrimerApellido.set, None, None)


    _ElementMap = {
        __SegundoApellido.name() : __SegundoApellido,
        __NombreDePila.name() : __NombreDePila,
        __RazonSocial.name() : __RazonSocial,
        __PrimerApellido.name() : __PrimerApellido
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'NombreCliente', NombreCliente)


# Complex type CTD_ANON_4 with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}IVAIGICReducido uses Python identifier IVAIGICReducido
    __IVAIGICReducido = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IVAIGICReducido'), 'IVAIGICReducido', '__httplocalhostelegibilidad_CTD_ANON_4_httplocalhostelegibilidadIVAIGICReducido', False)

    
    IVAIGICReducido = property(__IVAIGICReducido.value, __IVAIGICReducido.set, None, None)

    
    # Element {http://localhost/elegibilidad}DatosGeneralesOtrasFacturas uses Python identifier DatosGeneralesOtrasFacturas
    __DatosGeneralesOtrasFacturas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesOtrasFacturas'), 'DatosGeneralesOtrasFacturas', '__httplocalhostelegibilidad_CTD_ANON_4_httplocalhostelegibilidadDatosGeneralesOtrasFacturas', False)

    
    DatosGeneralesOtrasFacturas = property(__DatosGeneralesOtrasFacturas.value, __DatosGeneralesOtrasFacturas.set, None, None)

    
    # Element {http://localhost/elegibilidad}Concepto uses Python identifier Concepto
    __Concepto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Concepto'), 'Concepto', '__httplocalhostelegibilidad_CTD_ANON_4_httplocalhostelegibilidadConcepto', True)

    
    Concepto = property(__Concepto.value, __Concepto.set, None, None)

    
    # Element {http://localhost/elegibilidad}IVA uses Python identifier IVA
    __IVA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IVA'), 'IVA', '__httplocalhostelegibilidad_CTD_ANON_4_httplocalhostelegibilidadIVA', False)

    
    IVA = property(__IVA.value, __IVA.set, None, None)


    _ElementMap = {
        __IVAIGICReducido.name() : __IVAIGICReducido,
        __DatosGeneralesOtrasFacturas.name() : __DatosGeneralesOtrasFacturas,
        __Concepto.name() : __Concepto,
        __IVA.name() : __IVA
    }
    _AttributeMap = {
        
    }



# Complex type DireccionCorrespondencia with content type ELEMENT_ONLY
class DireccionCorrespondencia (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Direccion uses Python identifier Direccion
    __Direccion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Direccion'), 'Direccion', '__httplocalhostelegibilidad_DireccionCorrespondencia_httplocalhostelegibilidadDireccion', False)

    
    Direccion = property(__Direccion.value, __Direccion.set, None, None)

    
    # Element {http://localhost/elegibilidad}Indicador uses Python identifier Indicador
    __Indicador = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Indicador'), 'Indicador', '__httplocalhostelegibilidad_DireccionCorrespondencia_httplocalhostelegibilidadIndicador', False)

    
    Indicador = property(__Indicador.value, __Indicador.set, None, None)


    _ElementMap = {
        __Direccion.name() : __Direccion,
        __Indicador.name() : __Indicador
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DireccionCorrespondencia', DireccionCorrespondencia)


# Complex type TipoDatosGeneralesFactura with content type ELEMENT_ONLY
class TipoDatosGeneralesFactura (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoDatosGeneralesFactura')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTotalFactura uses Python identifier ImporteTotalFactura
    __ImporteTotalFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalFactura'), 'ImporteTotalFactura', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadImporteTotalFactura', False)

    
    ImporteTotalFactura = property(__ImporteTotalFactura.value, __ImporteTotalFactura.set, None, None)

    
    # Element {http://localhost/elegibilidad}NumeroFacturaRectificada uses Python identifier NumeroFacturaRectificada
    __NumeroFacturaRectificada = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroFacturaRectificada'), 'NumeroFacturaRectificada', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadNumeroFacturaRectificada', False)

    
    NumeroFacturaRectificada = property(__NumeroFacturaRectificada.value, __NumeroFacturaRectificada.set, None, u'N\xfamero de factura a la que rectifica.')

    
    # Element {http://localhost/elegibilidad}TipoMoneda uses Python identifier TipoMoneda
    __TipoMoneda = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoMoneda'), 'TipoMoneda', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadTipoMoneda', False)

    
    TipoMoneda = property(__TipoMoneda.value, __TipoMoneda.set, None, u'Tabla 104 (01-Pesetas, 02-Euros)')

    
    # Element {http://localhost/elegibilidad}FechaFactura uses Python identifier FechaFactura
    __FechaFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaFactura'), 'FechaFactura', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadFechaFactura', False)

    
    FechaFactura = property(__FechaFactura.value, __FechaFactura.set, None, u'Fecha oficial de la factura (albar\xe1n, en su caso)')

    
    # Element {http://localhost/elegibilidad}SaldoFactura uses Python identifier SaldoFactura
    __SaldoFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SaldoFactura'), 'SaldoFactura', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadSaldoFactura', False)

    
    SaldoFactura = property(__SaldoFactura.value, __SaldoFactura.set, None, u'Para los casos de rectificaciones')

    
    # Element {http://localhost/elegibilidad}Observaciones uses Python identifier Observaciones
    __Observaciones = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Observaciones'), 'Observaciones', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadObservaciones', False)

    
    Observaciones = property(__Observaciones.value, __Observaciones.set, None, u'Comentarios a la factura, como p.e. nro. Expte anormalidad ')

    
    # Element {http://localhost/elegibilidad}NumeroFactura uses Python identifier NumeroFactura
    __NumeroFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroFactura'), 'NumeroFactura', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadNumeroFactura', False)

    
    NumeroFactura = property(__NumeroFactura.value, __NumeroFactura.set, None, u'N\xfamero de la factura (albar\xe1n, en su caso)')

    
    # Element {http://localhost/elegibilidad}SaldoCobro uses Python identifier SaldoCobro
    __SaldoCobro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SaldoCobro'), 'SaldoCobro', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadSaldoCobro', False)

    
    SaldoCobro = property(__SaldoCobro.value, __SaldoCobro.set, None, u' Saldo cobro ')

    
    # Element {http://localhost/elegibilidad}CodigoFiscalFactura uses Python identifier CodigoFiscalFactura
    __CodigoFiscalFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoFiscalFactura'), 'CodigoFiscalFactura', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadCodigoFiscalFactura', False)

    
    CodigoFiscalFactura = property(__CodigoFiscalFactura.value, __CodigoFiscalFactura.set, None, u'N\xfamero de IVA')

    
    # Element {http://localhost/elegibilidad}TipoFactura uses Python identifier TipoFactura
    __TipoFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoFactura'), 'TipoFactura', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadTipoFactura', False)

    
    TipoFactura = property(__TipoFactura.value, __TipoFactura.set, None, u'Tabla 101 (Normal, fraude...)')

    
    # Element {http://localhost/elegibilidad}CIFEmisora uses Python identifier CIFEmisora
    __CIFEmisora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CIFEmisora'), 'CIFEmisora', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadCIFEmisora', False)

    
    CIFEmisora = property(__CIFEmisora.value, __CIFEmisora.set, None, None)

    
    # Element {http://localhost/elegibilidad}IndicativoFacturaRectificadora uses Python identifier IndicativoFacturaRectificadora
    __IndicativoFacturaRectificadora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndicativoFacturaRectificadora'), 'IndicativoFacturaRectificadora', '__httplocalhostelegibilidad_TipoDatosGeneralesFactura_httplocalhostelegibilidadIndicativoFacturaRectificadora', False)

    
    IndicativoFacturaRectificadora = property(__IndicativoFacturaRectificadora.value, __IndicativoFacturaRectificadora.set, None, u'Tabla 102 (N-Normal, R-Rectificadora , A-Anuladora, B-Anuladora con sustituyente)')


    _ElementMap = {
        __ImporteTotalFactura.name() : __ImporteTotalFactura,
        __NumeroFacturaRectificada.name() : __NumeroFacturaRectificada,
        __TipoMoneda.name() : __TipoMoneda,
        __FechaFactura.name() : __FechaFactura,
        __SaldoFactura.name() : __SaldoFactura,
        __Observaciones.name() : __Observaciones,
        __NumeroFactura.name() : __NumeroFactura,
        __SaldoCobro.name() : __SaldoCobro,
        __CodigoFiscalFactura.name() : __CodigoFiscalFactura,
        __TipoFactura.name() : __TipoFactura,
        __CIFEmisora.name() : __CIFEmisora,
        __IndicativoFacturaRectificadora.name() : __IndicativoFacturaRectificadora
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'TipoDatosGeneralesFactura', TipoDatosGeneralesFactura)


# Complex type ContactoConDireccion with content type ELEMENT_ONLY
class ContactoConDireccion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContactoConDireccion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}NombreDePila uses Python identifier NombreDePila
    __NombreDePila = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NombreDePila'), 'NombreDePila', '__httplocalhostelegibilidad_ContactoConDireccion_httplocalhostelegibilidadNombreDePila', False)

    
    NombreDePila = property(__NombreDePila.value, __NombreDePila.set, None, None)

    
    # Element {http://localhost/elegibilidad}PrimerApellido uses Python identifier PrimerApellido
    __PrimerApellido = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrimerApellido'), 'PrimerApellido', '__httplocalhostelegibilidad_ContactoConDireccion_httplocalhostelegibilidadPrimerApellido', False)

    
    PrimerApellido = property(__PrimerApellido.value, __PrimerApellido.set, None, None)

    
    # Element {http://localhost/elegibilidad}SegundoApellido uses Python identifier SegundoApellido
    __SegundoApellido = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SegundoApellido'), 'SegundoApellido', '__httplocalhostelegibilidad_ContactoConDireccion_httplocalhostelegibilidadSegundoApellido', False)

    
    SegundoApellido = property(__SegundoApellido.value, __SegundoApellido.set, None, None)

    
    # Element {http://localhost/elegibilidad}Telefono uses Python identifier Telefono
    __Telefono = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), 'Telefono', '__httplocalhostelegibilidad_ContactoConDireccion_httplocalhostelegibilidadTelefono', False)

    
    Telefono = property(__Telefono.value, __Telefono.set, None, None)

    
    # Element {http://localhost/elegibilidad}IndicadorTipoDireccion uses Python identifier IndicadorTipoDireccion
    __IndicadorTipoDireccion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndicadorTipoDireccion'), 'IndicadorTipoDireccion', '__httplocalhostelegibilidad_ContactoConDireccion_httplocalhostelegibilidadIndicadorTipoDireccion', False)

    
    IndicadorTipoDireccion = property(__IndicadorTipoDireccion.value, __IndicadorTipoDireccion.set, None, None)

    
    # Element {http://localhost/elegibilidad}Direccion uses Python identifier Direccion
    __Direccion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Direccion'), 'Direccion', '__httplocalhostelegibilidad_ContactoConDireccion_httplocalhostelegibilidadDireccion', False)

    
    Direccion = property(__Direccion.value, __Direccion.set, None, None)


    _ElementMap = {
        __NombreDePila.name() : __NombreDePila,
        __PrimerApellido.name() : __PrimerApellido,
        __SegundoApellido.name() : __SegundoApellido,
        __Telefono.name() : __Telefono,
        __IndicadorTipoDireccion.name() : __IndicadorTipoDireccion,
        __Direccion.name() : __Direccion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ContactoConDireccion', ContactoConDireccion)


# Complex type Contacto with content type ELEMENT_ONLY
class Contacto (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Contacto')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Telefono uses Python identifier Telefono
    __Telefono = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), 'Telefono', '__httplocalhostelegibilidad_Contacto_httplocalhostelegibilidadTelefono', False)

    
    Telefono = property(__Telefono.value, __Telefono.set, None, None)

    
    # Element {http://localhost/elegibilidad}Nombre uses Python identifier Nombre
    __Nombre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), 'Nombre', '__httplocalhostelegibilidad_Contacto_httplocalhostelegibilidadNombre', False)

    
    Nombre = property(__Nombre.value, __Nombre.set, None, None)


    _ElementMap = {
        __Telefono.name() : __Telefono,
        __Nombre.name() : __Nombre
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Contacto', Contacto)


# Complex type CTD_ANON_5 with content type SIMPLE
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = ExcesoPotFact
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is ExcesoPotFact
    
    # Attribute periodo uses Python identifier periodo
    __periodo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'periodo'), 'periodo', '__httplocalhostelegibilidad_CTD_ANON_5_periodo', pyxb.binding.datatypes.integer, required=True)
    
    periodo = property(__periodo.value, __periodo.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __periodo.name() : __periodo
    }



# Complex type MedidasAparato with content type ELEMENT_ONLY
class MedidasAparato (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MedidasAparato')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Medida uses Python identifier Medida
    __Medida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Medida'), 'Medida', '__httplocalhostelegibilidad_MedidasAparato_httplocalhostelegibilidadMedida', True)

    
    Medida = property(__Medida.value, __Medida.set, None, None)


    _ElementMap = {
        __Medida.name() : __Medida
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'MedidasAparato', MedidasAparato)


# Complex type CondicionesContractuales with content type ELEMENT_ONLY
class CondicionesContractuales (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PotenciasMaximas uses Python identifier PotenciasMaximas
    __PotenciasMaximas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciasMaximas'), 'PotenciasMaximas', '__httplocalhostelegibilidad_CondicionesContractuales_httplocalhostelegibilidadPotenciasMaximas', False)

    
    PotenciasMaximas = property(__PotenciasMaximas.value, __PotenciasMaximas.set, None, None)

    
    # Element {http://localhost/elegibilidad}TarifaATR uses Python identifier TarifaATR
    __TarifaATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR'), 'TarifaATR', '__httplocalhostelegibilidad_CondicionesContractuales_httplocalhostelegibilidadTarifaATR', False)

    
    TarifaATR = property(__TarifaATR.value, __TarifaATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}PotenciasContratadas uses Python identifier PotenciasContratadas
    __PotenciasContratadas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas'), 'PotenciasContratadas', '__httplocalhostelegibilidad_CondicionesContractuales_httplocalhostelegibilidadPotenciasContratadas', False)

    
    PotenciasContratadas = property(__PotenciasContratadas.value, __PotenciasContratadas.set, None, None)


    _ElementMap = {
        __PotenciasMaximas.name() : __PotenciasMaximas,
        __TarifaATR.name() : __TarifaATR,
        __PotenciasContratadas.name() : __PotenciasContratadas
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CondicionesContractuales', CondicionesContractuales)


# Complex type Aparatos with content type ELEMENT_ONLY
class Aparatos (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aparatos')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Aparato uses Python identifier Aparato
    __Aparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Aparato'), 'Aparato', '__httplocalhostelegibilidad_Aparatos_httplocalhostelegibilidadAparato', True)

    
    Aparato = property(__Aparato.value, __Aparato.set, None, None)


    _ElementMap = {
        __Aparato.name() : __Aparato
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Aparatos', Aparatos)


# Complex type ImportesTerminoPotencia with content type ELEMENT_ONLY
class ImportesTerminoPotencia (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoPotencia')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTerminoPotencia uses Python identifier ImporteTerminoPotencia
    __ImporteTerminoPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTerminoPotencia'), 'ImporteTerminoPotencia', '__httplocalhostelegibilidad_ImportesTerminoPotencia_httplocalhostelegibilidadImporteTerminoPotencia', True)

    
    ImporteTerminoPotencia = property(__ImporteTerminoPotencia.value, __ImporteTerminoPotencia.set, None, None)


    _ElementMap = {
        __ImporteTerminoPotencia.name() : __ImporteTerminoPotencia
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ImportesTerminoPotencia', ImportesTerminoPotencia)


# Complex type CTD_ANON_6 with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ValorExcesoPotencia uses Python identifier ValorExcesoPotencia
    __ValorExcesoPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ValorExcesoPotencia'), 'ValorExcesoPotencia', '__httplocalhostelegibilidad_CTD_ANON_6_httplocalhostelegibilidadValorExcesoPotencia', False)

    
    ValorExcesoPotencia = property(__ValorExcesoPotencia.value, __ValorExcesoPotencia.set, None, u'En Watios')


    _ElementMap = {
        __ValorExcesoPotencia.name() : __ValorExcesoPotencia
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_7 with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Importe uses Python identifier Importe
    __Importe = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Importe'), 'Importe', '__httplocalhostelegibilidad_CTD_ANON_7_httplocalhostelegibilidadImporte', False)

    
    Importe = property(__Importe.value, __Importe.set, None, None)

    
    # Element {http://localhost/elegibilidad}BaseImponible uses Python identifier BaseImponible
    __BaseImponible = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BaseImponible'), 'BaseImponible', '__httplocalhostelegibilidad_CTD_ANON_7_httplocalhostelegibilidadBaseImponible', False)

    
    BaseImponible = property(__BaseImponible.value, __BaseImponible.set, None, None)

    
    # Element {http://localhost/elegibilidad}Coeficiente uses Python identifier Coeficiente
    __Coeficiente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Coeficiente'), 'Coeficiente', '__httplocalhostelegibilidad_CTD_ANON_7_httplocalhostelegibilidadCoeficiente', False)

    
    Coeficiente = property(__Coeficiente.value, __Coeficiente.set, None, None)

    
    # Element {http://localhost/elegibilidad}Porcentaje uses Python identifier Porcentaje
    __Porcentaje = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Porcentaje'), 'Porcentaje', '__httplocalhostelegibilidad_CTD_ANON_7_httplocalhostelegibilidadPorcentaje', False)

    
    Porcentaje = property(__Porcentaje.value, __Porcentaje.set, None, None)


    _ElementMap = {
        __Importe.name() : __Importe,
        __BaseImponible.name() : __BaseImponible,
        __Coeficiente.name() : __Coeficiente,
        __Porcentaje.name() : __Porcentaje
    }
    _AttributeMap = {
        
    }



# Complex type TelefonoInternacional with content type ELEMENT_ONLY
class TelefonoInternacional (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TelefonoInternacional')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Numero uses Python identifier Numero
    __Numero = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Numero'), 'Numero', '__httplocalhostelegibilidad_TelefonoInternacional_httplocalhostelegibilidadNumero', False)

    
    Numero = property(__Numero.value, __Numero.set, None, None)

    
    # Element {http://localhost/elegibilidad}PrefijoPais uses Python identifier PrefijoPais
    __PrefijoPais = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrefijoPais'), 'PrefijoPais', '__httplocalhostelegibilidad_TelefonoInternacional_httplocalhostelegibilidadPrefijoPais', False)

    
    PrefijoPais = property(__PrefijoPais.value, __PrefijoPais.set, None, None)


    _ElementMap = {
        __Numero.name() : __Numero,
        __PrefijoPais.name() : __PrefijoPais
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'TelefonoInternacional', TelefonoInternacional)


# Complex type RegistroValAnomalias with content type ELEMENT_ONLY
class RegistroValAnomalias (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RegistroValAnomalias')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Energias uses Python identifier Energias
    __Energias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Energias'), 'Energias', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadEnergias', False)

    
    Energias = property(__Energias.value, __Energias.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaDesdeHistorico uses Python identifier FechaDesdeHistorico
    __FechaDesdeHistorico = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeHistorico'), 'FechaDesdeHistorico', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadFechaDesdeHistorico', False)

    
    FechaDesdeHistorico = property(__FechaDesdeHistorico.value, __FechaDesdeHistorico.set, None, None)

    
    # Element {http://localhost/elegibilidad}Reactivas uses Python identifier Reactivas
    __Reactivas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reactivas'), 'Reactivas', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadReactivas', False)

    
    Reactivas = property(__Reactivas.value, __Reactivas.set, None, None)

    
    # Element {http://localhost/elegibilidad}InicioRefacturacion uses Python identifier InicioRefacturacion
    __InicioRefacturacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InicioRefacturacion'), 'InicioRefacturacion', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadInicioRefacturacion', False)

    
    InicioRefacturacion = property(__InicioRefacturacion.value, __InicioRefacturacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}FinRefacturacion uses Python identifier FinRefacturacion
    __FinRefacturacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FinRefacturacion'), 'FinRefacturacion', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadFinRefacturacion', False)

    
    FinRefacturacion = property(__FinRefacturacion.value, __FinRefacturacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}OtrosConceptos uses Python identifier OtrosConceptos
    __OtrosConceptos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OtrosConceptos'), 'OtrosConceptos', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadOtrosConceptos', False)

    
    OtrosConceptos = property(__OtrosConceptos.value, __OtrosConceptos.set, None, None)

    
    # Element {http://localhost/elegibilidad}Importes uses Python identifier Importes
    __Importes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Importes'), 'Importes', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadImportes', False)

    
    Importes = property(__Importes.value, __Importes.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHastaHistorico uses Python identifier FechaHastaHistorico
    __FechaHastaHistorico = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaHistorico'), 'FechaHastaHistorico', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadFechaHastaHistorico', False)

    
    FechaHastaHistorico = property(__FechaHastaHistorico.value, __FechaHastaHistorico.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoTarifa uses Python identifier CodigoTarifa
    __CodigoTarifa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoTarifa'), 'CodigoTarifa', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadCodigoTarifa', False)

    
    CodigoTarifa = property(__CodigoTarifa.value, __CodigoTarifa.set, None, None)

    
    # Element {http://localhost/elegibilidad}ExcesosPotencia uses Python identifier ExcesosPotencia
    __ExcesosPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExcesosPotencia'), 'ExcesosPotencia', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadExcesosPotencia', False)

    
    ExcesosPotencia = property(__ExcesosPotencia.value, __ExcesosPotencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Potencias uses Python identifier Potencias
    __Potencias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Potencias'), 'Potencias', '__httplocalhostelegibilidad_RegistroValAnomalias_httplocalhostelegibilidadPotencias', False)

    
    Potencias = property(__Potencias.value, __Potencias.set, None, None)


    _ElementMap = {
        __Energias.name() : __Energias,
        __FechaDesdeHistorico.name() : __FechaDesdeHistorico,
        __Reactivas.name() : __Reactivas,
        __InicioRefacturacion.name() : __InicioRefacturacion,
        __FinRefacturacion.name() : __FinRefacturacion,
        __OtrosConceptos.name() : __OtrosConceptos,
        __Importes.name() : __Importes,
        __FechaHastaHistorico.name() : __FechaHastaHistorico,
        __CodigoTarifa.name() : __CodigoTarifa,
        __ExcesosPotencia.name() : __ExcesosPotencia,
        __Potencias.name() : __Potencias
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'RegistroValAnomalias', RegistroValAnomalias)


# Complex type Potencias with content type ELEMENT_ONLY
class Potencias (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Potencias')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Potencia uses Python identifier Potencia
    __Potencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Potencia'), 'Potencia', '__httplocalhostelegibilidad_Potencias_httplocalhostelegibilidadPotencia', True)

    
    Potencia = property(__Potencia.value, __Potencia.set, None, None)


    _ElementMap = {
        __Potencia.name() : __Potencia
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Potencias', Potencias)


# Complex type CTD_ANON_8 with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Aparato uses Python identifier Aparato
    __Aparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Aparato'), 'Aparato', '__httplocalhostelegibilidad_CTD_ANON_8_httplocalhostelegibilidadAparato', True)

    
    Aparato = property(__Aparato.value, __Aparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodUnificadoPuntoSuministro uses Python identifier CodUnificadoPuntoSuministro
    __CodUnificadoPuntoSuministro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodUnificadoPuntoSuministro'), 'CodUnificadoPuntoSuministro', '__httplocalhostelegibilidad_CTD_ANON_8_httplocalhostelegibilidadCodUnificadoPuntoSuministro', False)

    
    CodUnificadoPuntoSuministro = property(__CodUnificadoPuntoSuministro.value, __CodUnificadoPuntoSuministro.set, None, None)


    _ElementMap = {
        __Aparato.name() : __Aparato,
        __CodUnificadoPuntoSuministro.name() : __CodUnificadoPuntoSuministro
    }
    _AttributeMap = {
        
    }



# Complex type CondicionesContractuales2n with content type ELEMENT_ONLY
class CondicionesContractuales2n (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales2n')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PotenciasContratadas uses Python identifier PotenciasContratadas
    __PotenciasContratadas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas'), 'PotenciasContratadas', '__httplocalhostelegibilidad_CondicionesContractuales2n_httplocalhostelegibilidadPotenciasContratadas', False)

    
    PotenciasContratadas = property(__PotenciasContratadas.value, __PotenciasContratadas.set, None, None)

    
    # Element {http://localhost/elegibilidad}TarifaATR uses Python identifier TarifaATR
    __TarifaATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR'), 'TarifaATR', '__httplocalhostelegibilidad_CondicionesContractuales2n_httplocalhostelegibilidadTarifaATR', False)

    
    TarifaATR = property(__TarifaATR.value, __TarifaATR.set, None, None)


    _ElementMap = {
        __PotenciasContratadas.name() : __PotenciasContratadas,
        __TarifaATR.name() : __TarifaATR
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CondicionesContractuales2n', CondicionesContractuales2n)


# Complex type CTD_ANON_9 with content type SIMPLE
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = Importe
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is Importe

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type CuentaBancaria with content type ELEMENT_ONLY
class CuentaBancaria (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Cuenta uses Python identifier Cuenta
    __Cuenta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cuenta'), 'Cuenta', '__httplocalhostelegibilidad_CuentaBancaria_httplocalhostelegibilidadCuenta', False)

    
    Cuenta = property(__Cuenta.value, __Cuenta.set, None, None)

    
    # Element {http://localhost/elegibilidad}Banco uses Python identifier Banco
    __Banco = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Banco'), 'Banco', '__httplocalhostelegibilidad_CuentaBancaria_httplocalhostelegibilidadBanco', False)

    
    Banco = property(__Banco.value, __Banco.set, None, None)

    
    # Element {http://localhost/elegibilidad}Sucursal uses Python identifier Sucursal
    __Sucursal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Sucursal'), 'Sucursal', '__httplocalhostelegibilidad_CuentaBancaria_httplocalhostelegibilidadSucursal', False)

    
    Sucursal = property(__Sucursal.value, __Sucursal.set, None, None)

    
    # Element {http://localhost/elegibilidad}DC uses Python identifier DC
    __DC = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DC'), 'DC', '__httplocalhostelegibilidad_CuentaBancaria_httplocalhostelegibilidadDC', False)

    
    DC = property(__DC.value, __DC.set, None, None)


    _ElementMap = {
        __Cuenta.name() : __Cuenta,
        __Banco.name() : __Banco,
        __Sucursal.name() : __Sucursal,
        __DC.name() : __DC
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CuentaBancaria', CuentaBancaria)


# Complex type CTD_ANON_10 with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Integrador uses Python identifier Integrador
    __Integrador = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Integrador'), 'Integrador', '__httplocalhostelegibilidad_CTD_ANON_10_httplocalhostelegibilidadIntegrador', True)

    
    Integrador = property(__Integrador.value, __Integrador.set, None, None)

    
    # Element {http://localhost/elegibilidad}Tipo uses Python identifier Tipo
    __Tipo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Tipo'), 'Tipo', '__httplocalhostelegibilidad_CTD_ANON_10_httplocalhostelegibilidadTipo', False)

    
    Tipo = property(__Tipo.value, __Tipo.set, None, u'Tabla 24')

    
    # Element {http://localhost/elegibilidad}Marca uses Python identifier Marca
    __Marca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Marca'), 'Marca', '__httplocalhostelegibilidad_CTD_ANON_10_httplocalhostelegibilidadMarca', False)

    
    Marca = property(__Marca.value, __Marca.set, None, u'Tabla 25')

    
    # Element {http://localhost/elegibilidad}CodigoDH uses Python identifier CodigoDH
    __CodigoDH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoDH'), 'CodigoDH', '__httplocalhostelegibilidad_CTD_ANON_10_httplocalhostelegibilidadCodigoDH', False)

    
    CodigoDH = property(__CodigoDH.value, __CodigoDH.set, None, u'Tabla 35')

    
    # Element {http://localhost/elegibilidad}NumeroSerie uses Python identifier NumeroSerie
    __NumeroSerie = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), 'NumeroSerie', '__httplocalhostelegibilidad_CTD_ANON_10_httplocalhostelegibilidadNumeroSerie', False)

    
    NumeroSerie = property(__NumeroSerie.value, __NumeroSerie.set, None, None)


    _ElementMap = {
        __Integrador.name() : __Integrador,
        __Tipo.name() : __Tipo,
        __Marca.name() : __Marca,
        __CodigoDH.name() : __CodigoDH,
        __NumeroSerie.name() : __NumeroSerie
    }
    _AttributeMap = {
        
    }



# Complex type LocalizacionPS with content type ELEMENT_ONLY
class LocalizacionPS (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LocalizacionPS')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Municipio uses Python identifier Municipio
    __Municipio = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), 'Municipio', '__httplocalhostelegibilidad_LocalizacionPS_httplocalhostelegibilidadMunicipio', False)

    
    Municipio = property(__Municipio.value, __Municipio.set, None, None)

    
    # Element {http://localhost/elegibilidad}Poblacion uses Python identifier Poblacion
    __Poblacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Poblacion'), 'Poblacion', '__httplocalhostelegibilidad_LocalizacionPS_httplocalhostelegibilidadPoblacion', False)

    
    Poblacion = property(__Poblacion.value, __Poblacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoVia uses Python identifier TipoVia
    __TipoVia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoVia'), 'TipoVia', '__httplocalhostelegibilidad_LocalizacionPS_httplocalhostelegibilidadTipoVia', False)

    
    TipoVia = property(__TipoVia.value, __TipoVia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Provincia uses Python identifier Provincia
    __Provincia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Provincia'), 'Provincia', '__httplocalhostelegibilidad_LocalizacionPS_httplocalhostelegibilidadProvincia', False)

    
    Provincia = property(__Provincia.value, __Provincia.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodPostal uses Python identifier CodPostal
    __CodPostal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodPostal'), 'CodPostal', '__httplocalhostelegibilidad_LocalizacionPS_httplocalhostelegibilidadCodPostal', False)

    
    CodPostal = property(__CodPostal.value, __CodPostal.set, None, None)

    
    # Element {http://localhost/elegibilidad}Pais uses Python identifier Pais
    __Pais = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Pais'), 'Pais', '__httplocalhostelegibilidad_LocalizacionPS_httplocalhostelegibilidadPais', False)

    
    Pais = property(__Pais.value, __Pais.set, None, None)


    _ElementMap = {
        __Municipio.name() : __Municipio,
        __Poblacion.name() : __Poblacion,
        __TipoVia.name() : __TipoVia,
        __Provincia.name() : __Provincia,
        __CodPostal.name() : __CodPostal,
        __Pais.name() : __Pais
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'LocalizacionPS', LocalizacionPS)


# Complex type CTD_ANON_11 with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTotalConcepto uses Python identifier ImporteTotalConcepto
    __ImporteTotalConcepto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalConcepto'), 'ImporteTotalConcepto', '__httplocalhostelegibilidad_CTD_ANON_11_httplocalhostelegibilidadImporteTotalConcepto', False)

    
    ImporteTotalConcepto = property(__ImporteTotalConcepto.value, __ImporteTotalConcepto.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoConcepto uses Python identifier TipoConcepto
    __TipoConcepto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoConcepto'), 'TipoConcepto', '__httplocalhostelegibilidad_CTD_ANON_11_httplocalhostelegibilidadTipoConcepto', False)

    
    TipoConcepto = property(__TipoConcepto.value, __TipoConcepto.set, None, u'Tabla 103')

    
    # Element {http://localhost/elegibilidad}UnidadesConcepto uses Python identifier UnidadesConcepto
    __UnidadesConcepto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'UnidadesConcepto'), 'UnidadesConcepto', '__httplocalhostelegibilidad_CTD_ANON_11_httplocalhostelegibilidadUnidadesConcepto', False)

    
    UnidadesConcepto = property(__UnidadesConcepto.value, __UnidadesConcepto.set, None, u'P.e., en contrataci\xf3n kW a contratar')

    
    # Element {http://localhost/elegibilidad}ImporteUnidadConcepto uses Python identifier ImporteUnidadConcepto
    __ImporteUnidadConcepto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteUnidadConcepto'), 'ImporteUnidadConcepto', '__httplocalhostelegibilidad_CTD_ANON_11_httplocalhostelegibilidadImporteUnidadConcepto', False)

    
    ImporteUnidadConcepto = property(__ImporteUnidadConcepto.value, __ImporteUnidadConcepto.set, None, u'P.e., precio en tarifa del kW contratado')


    _ElementMap = {
        __ImporteTotalConcepto.name() : __ImporteTotalConcepto,
        __TipoConcepto.name() : __TipoConcepto,
        __UnidadesConcepto.name() : __UnidadesConcepto,
        __ImporteUnidadConcepto.name() : __ImporteUnidadConcepto
    }
    _AttributeMap = {
        
    }



# Complex type ContratoConModificacion with content type ELEMENT_ONLY
class ContratoConModificacion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContratoConModificacion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}DireccionCorrespondencia uses Python identifier DireccionCorrespondencia
    __DireccionCorrespondencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), 'DireccionCorrespondencia', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadDireccionCorrespondencia', False)

    
    DireccionCorrespondencia = property(__DireccionCorrespondencia.value, __DireccionCorrespondencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Duracion uses Python identifier Duracion
    __Duracion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), 'Duracion', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadDuracion', False)

    
    Duracion = property(__Duracion.value, __Duracion.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoContratoATR uses Python identifier TipoContratoATR
    __TipoContratoATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), 'TipoContratoATR', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadTipoContratoATR', False)

    
    TipoContratoATR = property(__TipoContratoATR.value, __TipoContratoATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}ConsumoAnualEstimado uses Python identifier ConsumoAnualEstimado
    __ConsumoAnualEstimado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConsumoAnualEstimado'), 'ConsumoAnualEstimado', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadConsumoAnualEstimado', False)

    
    ConsumoAnualEstimado = property(__ConsumoAnualEstimado.value, __ConsumoAnualEstimado.set, None, None)

    
    # Element {http://localhost/elegibilidad}CondicionesContractuales uses Python identifier CondicionesContractuales
    __CondicionesContractuales = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales'), 'CondicionesContractuales', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadCondicionesContractuales', False)

    
    CondicionesContractuales = property(__CondicionesContractuales.value, __CondicionesContractuales.set, None, None)

    
    # Element {http://localhost/elegibilidad}Contacto uses Python identifier Contacto
    __Contacto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contacto'), 'Contacto', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadContacto', False)

    
    Contacto = property(__Contacto.value, __Contacto.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdContrato uses Python identifier IdContrato
    __IdContrato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), 'IdContrato', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadIdContrato', False)

    
    IdContrato = property(__IdContrato.value, __IdContrato.set, None, None)

    
    # Element {http://localhost/elegibilidad}CuentaBancaria uses Python identifier CuentaBancaria
    __CuentaBancaria = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), 'CuentaBancaria', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadCuentaBancaria', False)

    
    CuentaBancaria = property(__CuentaBancaria.value, __CuentaBancaria.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaFinalizacion uses Python identifier FechaFinalizacion
    __FechaFinalizacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), 'FechaFinalizacion', '__httplocalhostelegibilidad_ContratoConModificacion_httplocalhostelegibilidadFechaFinalizacion', False)

    
    FechaFinalizacion = property(__FechaFinalizacion.value, __FechaFinalizacion.set, None, None)


    _ElementMap = {
        __DireccionCorrespondencia.name() : __DireccionCorrespondencia,
        __Duracion.name() : __Duracion,
        __TipoContratoATR.name() : __TipoContratoATR,
        __ConsumoAnualEstimado.name() : __ConsumoAnualEstimado,
        __CondicionesContractuales.name() : __CondicionesContractuales,
        __Contacto.name() : __Contacto,
        __IdContrato.name() : __IdContrato,
        __CuentaBancaria.name() : __CuentaBancaria,
        __FechaFinalizacion.name() : __FechaFinalizacion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ContratoConModificacion', ContratoConModificacion)


# Complex type DatosReclamante with content type ELEMENT_ONLY
class DatosReclamante (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosReclamante')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Telefono uses Python identifier Telefono
    __Telefono = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), 'Telefono', '__httplocalhostelegibilidad_DatosReclamante_httplocalhostelegibilidadTelefono', False)

    
    Telefono = property(__Telefono.value, __Telefono.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdReclamante uses Python identifier IdReclamante
    __IdReclamante = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdReclamante'), 'IdReclamante', '__httplocalhostelegibilidad_DatosReclamante_httplocalhostelegibilidadIdReclamante', False)

    
    IdReclamante = property(__IdReclamante.value, __IdReclamante.set, None, None)

    
    # Element {http://localhost/elegibilidad}Fax uses Python identifier Fax
    __Fax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Fax'), 'Fax', '__httplocalhostelegibilidad_DatosReclamante_httplocalhostelegibilidadFax', False)

    
    Fax = property(__Fax.value, __Fax.set, None, None)

    
    # Element {http://localhost/elegibilidad}Nombre uses Python identifier Nombre
    __Nombre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), 'Nombre', '__httplocalhostelegibilidad_DatosReclamante_httplocalhostelegibilidadNombre', False)

    
    Nombre = property(__Nombre.value, __Nombre.set, None, None)


    _ElementMap = {
        __Telefono.name() : __Telefono,
        __IdReclamante.name() : __IdReclamante,
        __Fax.name() : __Fax,
        __Nombre.name() : __Nombre
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosReclamante', DatosReclamante)


# Complex type CTD_ANON_12 with content type SIMPLE
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = Potencia
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is Potencia
    
    # Attribute periodo uses Python identifier periodo
    __periodo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'periodo'), 'periodo', '__httplocalhostelegibilidad_CTD_ANON_12_periodo', pyxb.binding.datatypes.integer, required=True)
    
    periodo = property(__periodo.value, __periodo.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __periodo.name() : __periodo
    }



# Complex type ComentarioPM with content type ELEMENT_ONLY
class ComentarioPM (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComentarioPM')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Texto uses Python identifier Texto
    __Texto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Texto'), 'Texto', '__httplocalhostelegibilidad_ComentarioPM_httplocalhostelegibilidadTexto', False)

    
    Texto = property(__Texto.value, __Texto.set, None, None)


    _ElementMap = {
        __Texto.name() : __Texto
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ComentarioPM', ComentarioPM)


# Complex type CTD_ANON_13 with content type SIMPLE
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = ReactivaFact
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is ReactivaFact
    
    # Attribute periodo uses Python identifier periodo
    __periodo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'periodo'), 'periodo', '__httplocalhostelegibilidad_CTD_ANON_13_periodo', pyxb.binding.datatypes.integer, required=True)
    
    periodo = property(__periodo.value, __periodo.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __periodo.name() : __periodo
    }



# Complex type DatosAparatoNoICP with content type ELEMENT_ONLY
class DatosAparatoNoICP (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoNoICP')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}NumeroSerie uses Python identifier NumeroSerie
    __NumeroSerie = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), 'NumeroSerie', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadNumeroSerie', False)

    
    NumeroSerie = property(__NumeroSerie.value, __NumeroSerie.set, None, None)

    
    # Element {http://localhost/elegibilidad}FuncionAparato uses Python identifier FuncionAparato
    __FuncionAparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FuncionAparato'), 'FuncionAparato', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadFuncionAparato', False)

    
    FuncionAparato = property(__FuncionAparato.value, __FuncionAparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}NumIntegradores uses Python identifier NumIntegradores
    __NumIntegradores = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumIntegradores'), 'NumIntegradores', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadNumIntegradores', False)

    
    NumIntegradores = property(__NumIntegradores.value, __NumIntegradores.set, None, None)

    
    # Element {http://localhost/elegibilidad}ConstanteEnergia uses Python identifier ConstanteEnergia
    __ConstanteEnergia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConstanteEnergia'), 'ConstanteEnergia', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadConstanteEnergia', False)

    
    ConstanteEnergia = property(__ConstanteEnergia.value, __ConstanteEnergia.set, None, None)

    
    # Element {http://localhost/elegibilidad}ConstanteMaximetro uses Python identifier ConstanteMaximetro
    __ConstanteMaximetro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMaximetro'), 'ConstanteMaximetro', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadConstanteMaximetro', False)

    
    ConstanteMaximetro = property(__ConstanteMaximetro.value, __ConstanteMaximetro.set, None, None)

    
    # Element {http://localhost/elegibilidad}RuedasEnteras uses Python identifier RuedasEnteras
    __RuedasEnteras = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RuedasEnteras'), 'RuedasEnteras', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadRuedasEnteras', False)

    
    RuedasEnteras = property(__RuedasEnteras.value, __RuedasEnteras.set, None, None)

    
    # Element {http://localhost/elegibilidad}RuedasDecimales uses Python identifier RuedasDecimales
    __RuedasDecimales = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RuedasDecimales'), 'RuedasDecimales', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadRuedasDecimales', False)

    
    RuedasDecimales = property(__RuedasDecimales.value, __RuedasDecimales.set, None, None)

    
    # Element {http://localhost/elegibilidad}PeriodoFabricacion uses Python identifier PeriodoFabricacion
    __PeriodoFabricacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PeriodoFabricacion'), 'PeriodoFabricacion', '__httplocalhostelegibilidad_DatosAparatoNoICP_httplocalhostelegibilidadPeriodoFabricacion', False)

    
    PeriodoFabricacion = property(__PeriodoFabricacion.value, __PeriodoFabricacion.set, None, None)


    _ElementMap = {
        __NumeroSerie.name() : __NumeroSerie,
        __FuncionAparato.name() : __FuncionAparato,
        __NumIntegradores.name() : __NumIntegradores,
        __ConstanteEnergia.name() : __ConstanteEnergia,
        __ConstanteMaximetro.name() : __ConstanteMaximetro,
        __RuedasEnteras.name() : __RuedasEnteras,
        __RuedasDecimales.name() : __RuedasDecimales,
        __PeriodoFabricacion.name() : __PeriodoFabricacion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosAparatoNoICP', DatosAparatoNoICP)


# Complex type DatosReclamacion with content type ELEMENT_ONLY
class DatosReclamacion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosReclamacion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}TipoMovimientoSolicitud uses Python identifier TipoMovimientoSolicitud
    __TipoMovimientoSolicitud = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimientoSolicitud'), 'TipoMovimientoSolicitud', '__httplocalhostelegibilidad_DatosReclamacion_httplocalhostelegibilidadTipoMovimientoSolicitud', False)

    
    TipoMovimientoSolicitud = property(__TipoMovimientoSolicitud.value, __TipoMovimientoSolicitud.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoReclamacion uses Python identifier TipoReclamacion
    __TipoReclamacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoReclamacion'), 'TipoReclamacion', '__httplocalhostelegibilidad_DatosReclamacion_httplocalhostelegibilidadTipoReclamacion', False)

    
    TipoReclamacion = property(__TipoReclamacion.value, __TipoReclamacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaIncidencia uses Python identifier FechaIncidencia
    __FechaIncidencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaIncidencia'), 'FechaIncidencia', '__httplocalhostelegibilidad_DatosReclamacion_httplocalhostelegibilidadFechaIncidencia', False)

    
    FechaIncidencia = property(__FechaIncidencia.value, __FechaIncidencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Comentario uses Python identifier Comentario
    __Comentario = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Comentario'), 'Comentario', '__httplocalhostelegibilidad_DatosReclamacion_httplocalhostelegibilidadComentario', False)

    
    Comentario = property(__Comentario.value, __Comentario.set, None, None)

    
    # Element {http://localhost/elegibilidad}IndemnizacionSolicitada uses Python identifier IndemnizacionSolicitada
    __IndemnizacionSolicitada = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndemnizacionSolicitada'), 'IndemnizacionSolicitada', '__httplocalhostelegibilidad_DatosReclamacion_httplocalhostelegibilidadIndemnizacionSolicitada', False)

    
    IndemnizacionSolicitada = property(__IndemnizacionSolicitada.value, __IndemnizacionSolicitada.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaLimiteLegal uses Python identifier FechaLimiteLegal
    __FechaLimiteLegal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaLimiteLegal'), 'FechaLimiteLegal', '__httplocalhostelegibilidad_DatosReclamacion_httplocalhostelegibilidadFechaLimiteLegal', False)

    
    FechaLimiteLegal = property(__FechaLimiteLegal.value, __FechaLimiteLegal.set, None, None)


    _ElementMap = {
        __TipoMovimientoSolicitud.name() : __TipoMovimientoSolicitud,
        __TipoReclamacion.name() : __TipoReclamacion,
        __FechaIncidencia.name() : __FechaIncidencia,
        __Comentario.name() : __Comentario,
        __IndemnizacionSolicitada.name() : __IndemnizacionSolicitada,
        __FechaLimiteLegal.name() : __FechaLimiteLegal
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosReclamacion', DatosReclamacion)


# Complex type TipoDireccionSuministro with content type ELEMENT_ONLY
class TipoDireccionSuministro (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TipoDireccionSuministro')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}DirSuministro uses Python identifier DirSuministro
    __DirSuministro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DirSuministro'), 'DirSuministro', '__httplocalhostelegibilidad_TipoDireccionSuministro_httplocalhostelegibilidadDirSuministro', False)

    
    DirSuministro = property(__DirSuministro.value, __DirSuministro.set, None, None)

    
    # Element {http://localhost/elegibilidad}CUPS uses Python identifier CUPS
    __CUPS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CUPS'), 'CUPS', '__httplocalhostelegibilidad_TipoDireccionSuministro_httplocalhostelegibilidadCUPS', False)

    
    CUPS = property(__CUPS.value, __CUPS.set, None, None)

    
    # Element {http://localhost/elegibilidad}Municipio uses Python identifier Municipio
    __Municipio = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), 'Municipio', '__httplocalhostelegibilidad_TipoDireccionSuministro_httplocalhostelegibilidadMunicipio', False)

    
    Municipio = property(__Municipio.value, __Municipio.set, None, None)


    _ElementMap = {
        __DirSuministro.name() : __DirSuministro,
        __CUPS.name() : __CUPS,
        __Municipio.name() : __Municipio
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'TipoDireccionSuministro', TipoDireccionSuministro)


# Complex type DatosAceptacion with content type ELEMENT_ONLY
class DatosAceptacion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosAceptacion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}FechaUltimaLectura uses Python identifier FechaUltimaLectura
    __FechaUltimaLectura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaUltimaLectura'), 'FechaUltimaLectura', '__httplocalhostelegibilidad_DatosAceptacion_httplocalhostelegibilidadFechaUltimaLectura', False)

    
    FechaUltimaLectura = property(__FechaUltimaLectura.value, __FechaUltimaLectura.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaAceptacion uses Python identifier FechaAceptacion
    __FechaAceptacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaAceptacion'), 'FechaAceptacion', '__httplocalhostelegibilidad_DatosAceptacion_httplocalhostelegibilidadFechaAceptacion', False)

    
    FechaAceptacion = property(__FechaAceptacion.value, __FechaAceptacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}PotenciaActual uses Python identifier PotenciaActual
    __PotenciaActual = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciaActual'), 'PotenciaActual', '__httplocalhostelegibilidad_DatosAceptacion_httplocalhostelegibilidadPotenciaActual', False)

    
    PotenciaActual = property(__PotenciaActual.value, __PotenciaActual.set, None, None)

    
    # Element {http://localhost/elegibilidad}ActuacionCampo uses Python identifier ActuacionCampo
    __ActuacionCampo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ActuacionCampo'), 'ActuacionCampo', '__httplocalhostelegibilidad_DatosAceptacion_httplocalhostelegibilidadActuacionCampo', False)

    
    ActuacionCampo = property(__ActuacionCampo.value, __ActuacionCampo.set, None, None)


    _ElementMap = {
        __FechaUltimaLectura.name() : __FechaUltimaLectura,
        __FechaAceptacion.name() : __FechaAceptacion,
        __PotenciaActual.name() : __PotenciaActual,
        __ActuacionCampo.name() : __ActuacionCampo
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosAceptacion', DatosAceptacion)


# Complex type CTD_ANON_14 with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTotalEnergiaActiva uses Python identifier ImporteTotalEnergiaActiva
    __ImporteTotalEnergiaActiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalEnergiaActiva'), 'ImporteTotalEnergiaActiva', '__httplocalhostelegibilidad_CTD_ANON_14_httplocalhostelegibilidadImporteTotalEnergiaActiva', False)

    
    ImporteTotalEnergiaActiva = property(__ImporteTotalEnergiaActiva.value, __ImporteTotalEnergiaActiva.set, None, None)

    
    # Element {http://localhost/elegibilidad}TerminoEnergiaActiva uses Python identifier TerminoEnergiaActiva
    __TerminoEnergiaActiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TerminoEnergiaActiva'), 'TerminoEnergiaActiva', '__httplocalhostelegibilidad_CTD_ANON_14_httplocalhostelegibilidadTerminoEnergiaActiva', True)

    
    TerminoEnergiaActiva = property(__TerminoEnergiaActiva.value, __TerminoEnergiaActiva.set, None, None)


    _ElementMap = {
        __ImporteTotalEnergiaActiva.name() : __ImporteTotalEnergiaActiva,
        __TerminoEnergiaActiva.name() : __TerminoEnergiaActiva
    }
    _AttributeMap = {
        
    }



# Complex type Cliente with content type ELEMENT_ONLY
class Cliente (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Cliente')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Telefono uses Python identifier Telefono
    __Telefono = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), 'Telefono', '__httplocalhostelegibilidad_Cliente_httplocalhostelegibilidadTelefono', False)

    
    Telefono = property(__Telefono.value, __Telefono.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdCliente uses Python identifier IdCliente
    __IdCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), 'IdCliente', '__httplocalhostelegibilidad_Cliente_httplocalhostelegibilidadIdCliente', False)

    
    IdCliente = property(__IdCliente.value, __IdCliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}Nombre uses Python identifier Nombre
    __Nombre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), 'Nombre', '__httplocalhostelegibilidad_Cliente_httplocalhostelegibilidadNombre', False)

    
    Nombre = property(__Nombre.value, __Nombre.set, None, None)

    
    # Element {http://localhost/elegibilidad}Fax uses Python identifier Fax
    __Fax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Fax'), 'Fax', '__httplocalhostelegibilidad_Cliente_httplocalhostelegibilidadFax', False)

    
    Fax = property(__Fax.value, __Fax.set, None, None)


    _ElementMap = {
        __Telefono.name() : __Telefono,
        __IdCliente.name() : __IdCliente,
        __Nombre.name() : __Nombre,
        __Fax.name() : __Fax
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Cliente', Cliente)


# Complex type RegistrosValAnomalias with content type ELEMENT_ONLY
class RegistrosValAnomalias (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RegistrosValAnomalias')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}RegistroValAnomalias uses Python identifier RegistroValAnomalias
    __RegistroValAnomalias = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RegistroValAnomalias'), 'RegistroValAnomalias', '__httplocalhostelegibilidad_RegistrosValAnomalias_httplocalhostelegibilidadRegistroValAnomalias', True)

    
    RegistroValAnomalias = property(__RegistroValAnomalias.value, __RegistroValAnomalias.set, None, None)


    _ElementMap = {
        __RegistroValAnomalias.name() : __RegistroValAnomalias
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'RegistrosValAnomalias', RegistrosValAnomalias)


# Complex type Direccion with content type ELEMENT_ONLY
class Direccion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Direccion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Provincia uses Python identifier Provincia
    __Provincia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Provincia'), 'Provincia', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadProvincia', False)

    
    Provincia = property(__Provincia.value, __Provincia.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoAclaradorFinca uses Python identifier TipoAclaradorFinca
    __TipoAclaradorFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoAclaradorFinca'), 'TipoAclaradorFinca', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadTipoAclaradorFinca', False)

    
    TipoAclaradorFinca = property(__TipoAclaradorFinca.value, __TipoAclaradorFinca.set, None, None)

    
    # Element {http://localhost/elegibilidad}Municipio uses Python identifier Municipio
    __Municipio = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), 'Municipio', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadMunicipio', False)

    
    Municipio = property(__Municipio.value, __Municipio.set, None, None)

    
    # Element {http://localhost/elegibilidad}Piso uses Python identifier Piso
    __Piso = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Piso'), 'Piso', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadPiso', False)

    
    Piso = property(__Piso.value, __Piso.set, None, None)

    
    # Element {http://localhost/elegibilidad}Poblacion uses Python identifier Poblacion
    __Poblacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Poblacion'), 'Poblacion', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadPoblacion', False)

    
    Poblacion = property(__Poblacion.value, __Poblacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoVia uses Python identifier TipoVia
    __TipoVia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoVia'), 'TipoVia', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadTipoVia', False)

    
    TipoVia = property(__TipoVia.value, __TipoVia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Escalera uses Python identifier Escalera
    __Escalera = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Escalera'), 'Escalera', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadEscalera', False)

    
    Escalera = property(__Escalera.value, __Escalera.set, None, None)

    
    # Element {http://localhost/elegibilidad}AclaradorFinca uses Python identifier AclaradorFinca
    __AclaradorFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AclaradorFinca'), 'AclaradorFinca', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadAclaradorFinca', False)

    
    AclaradorFinca = property(__AclaradorFinca.value, __AclaradorFinca.set, None, None)

    
    # Element {http://localhost/elegibilidad}Puerta uses Python identifier Puerta
    __Puerta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Puerta'), 'Puerta', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadPuerta', False)

    
    Puerta = property(__Puerta.value, __Puerta.set, None, None)

    
    # Element {http://localhost/elegibilidad}Calle uses Python identifier Calle
    __Calle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Calle'), 'Calle', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadCalle', False)

    
    Calle = property(__Calle.value, __Calle.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodPostal uses Python identifier CodPostal
    __CodPostal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodPostal'), 'CodPostal', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadCodPostal', False)

    
    CodPostal = property(__CodPostal.value, __CodPostal.set, None, None)

    
    # Element {http://localhost/elegibilidad}NumeroFinca uses Python identifier NumeroFinca
    __NumeroFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroFinca'), 'NumeroFinca', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadNumeroFinca', False)

    
    NumeroFinca = property(__NumeroFinca.value, __NumeroFinca.set, None, None)

    
    # Element {http://localhost/elegibilidad}Pais uses Python identifier Pais
    __Pais = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Pais'), 'Pais', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadPais', False)

    
    Pais = property(__Pais.value, __Pais.set, None, None)

    
    # Element {http://localhost/elegibilidad}DuplicadorFinca uses Python identifier DuplicadorFinca
    __DuplicadorFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DuplicadorFinca'), 'DuplicadorFinca', '__httplocalhostelegibilidad_Direccion_httplocalhostelegibilidadDuplicadorFinca', False)

    
    DuplicadorFinca = property(__DuplicadorFinca.value, __DuplicadorFinca.set, None, None)


    _ElementMap = {
        __Provincia.name() : __Provincia,
        __TipoAclaradorFinca.name() : __TipoAclaradorFinca,
        __Municipio.name() : __Municipio,
        __Piso.name() : __Piso,
        __Poblacion.name() : __Poblacion,
        __TipoVia.name() : __TipoVia,
        __Escalera.name() : __Escalera,
        __AclaradorFinca.name() : __AclaradorFinca,
        __Puerta.name() : __Puerta,
        __Calle.name() : __Calle,
        __CodPostal.name() : __CodPostal,
        __NumeroFinca.name() : __NumeroFinca,
        __Pais.name() : __Pais,
        __DuplicadorFinca.name() : __DuplicadorFinca
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Direccion', Direccion)


# Complex type ClienteConDireccion with content type ELEMENT_ONLY
class ClienteConDireccion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClienteConDireccion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}IndicadorTipoDireccion uses Python identifier IndicadorTipoDireccion
    __IndicadorTipoDireccion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndicadorTipoDireccion'), 'IndicadorTipoDireccion', '__httplocalhostelegibilidad_ClienteConDireccion_httplocalhostelegibilidadIndicadorTipoDireccion', False)

    
    IndicadorTipoDireccion = property(__IndicadorTipoDireccion.value, __IndicadorTipoDireccion.set, None, None)

    
    # Element {http://localhost/elegibilidad}Direccion uses Python identifier Direccion
    __Direccion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Direccion'), 'Direccion', '__httplocalhostelegibilidad_ClienteConDireccion_httplocalhostelegibilidadDireccion', False)

    
    Direccion = property(__Direccion.value, __Direccion.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdCliente uses Python identifier IdCliente
    __IdCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), 'IdCliente', '__httplocalhostelegibilidad_ClienteConDireccion_httplocalhostelegibilidadIdCliente', False)

    
    IdCliente = property(__IdCliente.value, __IdCliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}Nombre uses Python identifier Nombre
    __Nombre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), 'Nombre', '__httplocalhostelegibilidad_ClienteConDireccion_httplocalhostelegibilidadNombre', False)

    
    Nombre = property(__Nombre.value, __Nombre.set, None, None)

    
    # Element {http://localhost/elegibilidad}Fax uses Python identifier Fax
    __Fax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Fax'), 'Fax', '__httplocalhostelegibilidad_ClienteConDireccion_httplocalhostelegibilidadFax', False)

    
    Fax = property(__Fax.value, __Fax.set, None, None)

    
    # Element {http://localhost/elegibilidad}Telefono uses Python identifier Telefono
    __Telefono = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), 'Telefono', '__httplocalhostelegibilidad_ClienteConDireccion_httplocalhostelegibilidadTelefono', False)

    
    Telefono = property(__Telefono.value, __Telefono.set, None, None)


    _ElementMap = {
        __IndicadorTipoDireccion.name() : __IndicadorTipoDireccion,
        __Direccion.name() : __Direccion,
        __IdCliente.name() : __IdCliente,
        __Nombre.name() : __Nombre,
        __Fax.name() : __Fax,
        __Telefono.name() : __Telefono
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ClienteConDireccion', ClienteConDireccion)


# Complex type DatosReclamacionFactura with content type ELEMENT_ONLY
class DatosReclamacionFactura (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosReclamacionFactura')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}CodAgrupacion uses Python identifier CodAgrupacion
    __CodAgrupacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodAgrupacion'), 'CodAgrupacion', '__httplocalhostelegibilidad_DatosReclamacionFactura_httplocalhostelegibilidadCodAgrupacion', False)

    
    CodAgrupacion = property(__CodAgrupacion.value, __CodAgrupacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodFiscalFactura uses Python identifier CodFiscalFactura
    __CodFiscalFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodFiscalFactura'), 'CodFiscalFactura', '__httplocalhostelegibilidad_DatosReclamacionFactura_httplocalhostelegibilidadCodFiscalFactura', False)

    
    CodFiscalFactura = property(__CodFiscalFactura.value, __CodFiscalFactura.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImporteFactReclamada uses Python identifier ImporteFactReclamada
    __ImporteFactReclamada = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteFactReclamada'), 'ImporteFactReclamada', '__httplocalhostelegibilidad_DatosReclamacionFactura_httplocalhostelegibilidadImporteFactReclamada', False)

    
    ImporteFactReclamada = property(__ImporteFactReclamada.value, __ImporteFactReclamada.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaFactura uses Python identifier FechaFactura
    __FechaFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaFactura'), 'FechaFactura', '__httplocalhostelegibilidad_DatosReclamacionFactura_httplocalhostelegibilidadFechaFactura', False)

    
    FechaFactura = property(__FechaFactura.value, __FechaFactura.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaDesdeFact uses Python identifier FechaDesdeFact
    __FechaDesdeFact = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeFact'), 'FechaDesdeFact', '__httplocalhostelegibilidad_DatosReclamacionFactura_httplocalhostelegibilidadFechaDesdeFact', False)

    
    FechaDesdeFact = property(__FechaDesdeFact.value, __FechaDesdeFact.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHastaFact uses Python identifier FechaHastaFact
    __FechaHastaFact = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaFact'), 'FechaHastaFact', '__httplocalhostelegibilidad_DatosReclamacionFactura_httplocalhostelegibilidadFechaHastaFact', False)

    
    FechaHastaFact = property(__FechaHastaFact.value, __FechaHastaFact.set, None, None)


    _ElementMap = {
        __CodAgrupacion.name() : __CodAgrupacion,
        __CodFiscalFactura.name() : __CodFiscalFactura,
        __ImporteFactReclamada.name() : __ImporteFactReclamada,
        __FechaFactura.name() : __FechaFactura,
        __FechaDesdeFact.name() : __FechaDesdeFact,
        __FechaHastaFact.name() : __FechaHastaFact
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosReclamacionFactura', DatosReclamacionFactura)


# Complex type CTD_ANON_15 with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTotalExcesos uses Python identifier ImporteTotalExcesos
    __ImporteTotalExcesos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalExcesos'), 'ImporteTotalExcesos', '__httplocalhostelegibilidad_CTD_ANON_15_httplocalhostelegibilidadImporteTotalExcesos', False)

    
    ImporteTotalExcesos = property(__ImporteTotalExcesos.value, __ImporteTotalExcesos.set, None, None)

    
    # Element {http://localhost/elegibilidad}Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_CTD_ANON_15_httplocalhostelegibilidadPeriodo', True)

    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)


    _ElementMap = {
        __ImporteTotalExcesos.name() : __ImporteTotalExcesos,
        __Periodo.name() : __Periodo
    }
    _AttributeMap = {
        
    }



# Complex type IdYNombreCliente with content type ELEMENT_ONLY
class IdYNombreCliente (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IdYNombreCliente')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Nombre uses Python identifier Nombre
    __Nombre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), 'Nombre', '__httplocalhostelegibilidad_IdYNombreCliente_httplocalhostelegibilidadNombre', False)

    
    Nombre = property(__Nombre.value, __Nombre.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdCliente uses Python identifier IdCliente
    __IdCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), 'IdCliente', '__httplocalhostelegibilidad_IdYNombreCliente_httplocalhostelegibilidadIdCliente', False)

    
    IdCliente = property(__IdCliente.value, __IdCliente.set, None, None)


    _ElementMap = {
        __Nombre.name() : __Nombre,
        __IdCliente.name() : __IdCliente
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'IdYNombreCliente', IdYNombreCliente)


# Complex type Contrato with content type ELEMENT_ONLY
class Contrato (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Contrato')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ConsumoAnualEstimado uses Python identifier ConsumoAnualEstimado
    __ConsumoAnualEstimado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConsumoAnualEstimado'), 'ConsumoAnualEstimado', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadConsumoAnualEstimado', False)

    
    ConsumoAnualEstimado = property(__ConsumoAnualEstimado.value, __ConsumoAnualEstimado.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdContrato uses Python identifier IdContrato
    __IdContrato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), 'IdContrato', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadIdContrato', False)

    
    IdContrato = property(__IdContrato.value, __IdContrato.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionCorrespondencia uses Python identifier DireccionCorrespondencia
    __DireccionCorrespondencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), 'DireccionCorrespondencia', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadDireccionCorrespondencia', False)

    
    DireccionCorrespondencia = property(__DireccionCorrespondencia.value, __DireccionCorrespondencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaFinalizacion uses Python identifier FechaFinalizacion
    __FechaFinalizacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), 'FechaFinalizacion', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadFechaFinalizacion', False)

    
    FechaFinalizacion = property(__FechaFinalizacion.value, __FechaFinalizacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}CuentaBancaria uses Python identifier CuentaBancaria
    __CuentaBancaria = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), 'CuentaBancaria', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadCuentaBancaria', False)

    
    CuentaBancaria = property(__CuentaBancaria.value, __CuentaBancaria.set, None, None)

    
    # Element {http://localhost/elegibilidad}Contacto uses Python identifier Contacto
    __Contacto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contacto'), 'Contacto', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadContacto', False)

    
    Contacto = property(__Contacto.value, __Contacto.set, None, None)

    
    # Element {http://localhost/elegibilidad}Duracion uses Python identifier Duracion
    __Duracion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), 'Duracion', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadDuracion', False)

    
    Duracion = property(__Duracion.value, __Duracion.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoContratoATR uses Python identifier TipoContratoATR
    __TipoContratoATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), 'TipoContratoATR', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadTipoContratoATR', False)

    
    TipoContratoATR = property(__TipoContratoATR.value, __TipoContratoATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}CondicionesContractuales uses Python identifier CondicionesContractuales
    __CondicionesContractuales = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales'), 'CondicionesContractuales', '__httplocalhostelegibilidad_Contrato_httplocalhostelegibilidadCondicionesContractuales', False)

    
    CondicionesContractuales = property(__CondicionesContractuales.value, __CondicionesContractuales.set, None, None)


    _ElementMap = {
        __ConsumoAnualEstimado.name() : __ConsumoAnualEstimado,
        __IdContrato.name() : __IdContrato,
        __DireccionCorrespondencia.name() : __DireccionCorrespondencia,
        __FechaFinalizacion.name() : __FechaFinalizacion,
        __CuentaBancaria.name() : __CuentaBancaria,
        __Contacto.name() : __Contacto,
        __Duracion.name() : __Duracion,
        __TipoContratoATR.name() : __TipoContratoATR,
        __CondicionesContractuales.name() : __CondicionesContractuales
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Contrato', Contrato)


# Complex type CTD_ANON_16 with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTotal uses Python identifier ImporteTotal
    __ImporteTotal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotal'), 'ImporteTotal', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadImporteTotal', False)

    
    ImporteTotal = property(__ImporteTotal.value, __ImporteTotal.set, None, u'Importe total de todas las facturas del XML')

    
    # Element {http://localhost/elegibilidad}SaldoTotalCobro uses Python identifier SaldoTotalCobro
    __SaldoTotalCobro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SaldoTotalCobro'), 'SaldoTotalCobro', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadSaldoTotalCobro', False)

    
    SaldoTotalCobro = property(__SaldoTotalCobro.value, __SaldoTotalCobro.set, None, u'Saldo total cobro del XML')

    
    # Element {http://localhost/elegibilidad}CuentaBancaria uses Python identifier CuentaBancaria
    __CuentaBancaria = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), 'CuentaBancaria', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadCuentaBancaria', False)

    
    CuentaBancaria = property(__CuentaBancaria.value, __CuentaBancaria.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaValor uses Python identifier FechaValor
    __FechaValor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaValor'), 'FechaValor', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadFechaValor', False)

    
    FechaValor = property(__FechaValor.value, __FechaValor.set, None, None)

    
    # Element {http://localhost/elegibilidad}SaldoTotalFacturacion uses Python identifier SaldoTotalFacturacion
    __SaldoTotalFacturacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SaldoTotalFacturacion'), 'SaldoTotalFacturacion', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadSaldoTotalFacturacion', False)

    
    SaldoTotalFacturacion = property(__SaldoTotalFacturacion.value, __SaldoTotalFacturacion.set, None, u'Saldo total de todas las facturas del xml')

    
    # Element {http://localhost/elegibilidad}FechaLimitePago uses Python identifier FechaLimitePago
    __FechaLimitePago = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaLimitePago'), 'FechaLimitePago', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadFechaLimitePago', False)

    
    FechaLimitePago = property(__FechaLimitePago.value, __FechaLimitePago.set, None, u'Fecha teorica de pago ')

    
    # Element {http://localhost/elegibilidad}TipoMoneda uses Python identifier TipoMoneda
    __TipoMoneda = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoMoneda'), 'TipoMoneda', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadTipoMoneda', False)

    
    TipoMoneda = property(__TipoMoneda.value, __TipoMoneda.set, None, u'Tabla 104 (01-Pesetas, 02-Euros)')

    
    # Element {http://localhost/elegibilidad}IdRemesa uses Python identifier IdRemesa
    __IdRemesa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdRemesa'), 'IdRemesa', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadIdRemesa', False)

    
    IdRemesa = property(__IdRemesa.value, __IdRemesa.set, None, u'identificacion remesa o agrupaci\xf3n')

    
    # Element {http://localhost/elegibilidad}TotalRecibos uses Python identifier TotalRecibos
    __TotalRecibos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TotalRecibos'), 'TotalRecibos', '__httplocalhostelegibilidad_CTD_ANON_16_httplocalhostelegibilidadTotalRecibos', False)

    
    TotalRecibos = property(__TotalRecibos.value, __TotalRecibos.set, None, u'Numero recibos del XML')


    _ElementMap = {
        __ImporteTotal.name() : __ImporteTotal,
        __SaldoTotalCobro.name() : __SaldoTotalCobro,
        __CuentaBancaria.name() : __CuentaBancaria,
        __FechaValor.name() : __FechaValor,
        __SaldoTotalFacturacion.name() : __SaldoTotalFacturacion,
        __FechaLimitePago.name() : __FechaLimitePago,
        __TipoMoneda.name() : __TipoMoneda,
        __IdRemesa.name() : __IdRemesa,
        __TotalRecibos.name() : __TotalRecibos
    }
    _AttributeMap = {
        
    }



# Complex type DatosAutolecturas with content type ELEMENT_ONLY
class DatosAutolecturas (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosAutolecturas')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_DatosAutolecturas_httplocalhostelegibilidadPeriodo', False)

    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)

    
    # Element {http://localhost/elegibilidad}Procedencia uses Python identifier Procedencia
    __Procedencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Procedencia'), 'Procedencia', '__httplocalhostelegibilidad_DatosAutolecturas_httplocalhostelegibilidadProcedencia', False)

    
    Procedencia = property(__Procedencia.value, __Procedencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}MagnitudMedida uses Python identifier MagnitudMedida
    __MagnitudMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MagnitudMedida'), 'MagnitudMedida', '__httplocalhostelegibilidad_DatosAutolecturas_httplocalhostelegibilidadMagnitudMedida', False)

    
    MagnitudMedida = property(__MagnitudMedida.value, __MagnitudMedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoDH uses Python identifier TipoDH
    __TipoDH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoDH'), 'TipoDH', '__httplocalhostelegibilidad_DatosAutolecturas_httplocalhostelegibilidadTipoDH', False)

    
    TipoDH = property(__TipoDH.value, __TipoDH.set, None, None)

    
    # Element {http://localhost/elegibilidad}Aparato uses Python identifier Aparato
    __Aparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Aparato'), 'Aparato', '__httplocalhostelegibilidad_DatosAutolecturas_httplocalhostelegibilidadAparato', False)

    
    Aparato = property(__Aparato.value, __Aparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}LecturaPropuesta uses Python identifier LecturaPropuesta
    __LecturaPropuesta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LecturaPropuesta'), 'LecturaPropuesta', '__httplocalhostelegibilidad_DatosAutolecturas_httplocalhostelegibilidadLecturaPropuesta', False)

    
    LecturaPropuesta = property(__LecturaPropuesta.value, __LecturaPropuesta.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaLectura uses Python identifier FechaLectura
    __FechaLectura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaLectura'), 'FechaLectura', '__httplocalhostelegibilidad_DatosAutolecturas_httplocalhostelegibilidadFechaLectura', False)

    
    FechaLectura = property(__FechaLectura.value, __FechaLectura.set, None, None)


    _ElementMap = {
        __Periodo.name() : __Periodo,
        __Procedencia.name() : __Procedencia,
        __MagnitudMedida.name() : __MagnitudMedida,
        __TipoDH.name() : __TipoDH,
        __Aparato.name() : __Aparato,
        __LecturaPropuesta.name() : __LecturaPropuesta,
        __FechaLectura.name() : __FechaLectura
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosAutolecturas', DatosAutolecturas)


# Complex type CTD_ANON_17 with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}DatosFacturaATR uses Python identifier DatosFacturaATR
    __DatosFacturaATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatosFacturaATR'), 'DatosFacturaATR', '__httplocalhostelegibilidad_CTD_ANON_17_httplocalhostelegibilidadDatosFacturaATR', False)

    
    DatosFacturaATR = property(__DatosFacturaATR.value, __DatosFacturaATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionSuministro uses Python identifier DireccionSuministro
    __DireccionSuministro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionSuministro'), 'DireccionSuministro', '__httplocalhostelegibilidad_CTD_ANON_17_httplocalhostelegibilidadDireccionSuministro', False)

    
    DireccionSuministro = property(__DireccionSuministro.value, __DireccionSuministro.set, None, None)

    
    # Element {http://localhost/elegibilidad}Cliente uses Python identifier Cliente
    __Cliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cliente'), 'Cliente', '__httplocalhostelegibilidad_CTD_ANON_17_httplocalhostelegibilidadCliente', False)

    
    Cliente = property(__Cliente.value, __Cliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}DatosGeneralesFactura uses Python identifier DatosGeneralesFactura
    __DatosGeneralesFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFactura'), 'DatosGeneralesFactura', '__httplocalhostelegibilidad_CTD_ANON_17_httplocalhostelegibilidadDatosGeneralesFactura', False)

    
    DatosGeneralesFactura = property(__DatosGeneralesFactura.value, __DatosGeneralesFactura.set, None, None)

    
    # Element {http://localhost/elegibilidad}Contrato uses Python identifier Contrato
    __Contrato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contrato'), 'Contrato', '__httplocalhostelegibilidad_CTD_ANON_17_httplocalhostelegibilidadContrato', False)

    
    Contrato = property(__Contrato.value, __Contrato.set, None, None)


    _ElementMap = {
        __DatosFacturaATR.name() : __DatosFacturaATR,
        __DireccionSuministro.name() : __DireccionSuministro,
        __Cliente.name() : __Cliente,
        __DatosGeneralesFactura.name() : __DatosGeneralesFactura,
        __Contrato.name() : __Contrato
    }
    _AttributeMap = {
        
    }



# Complex type CondicionesContractualesC with content type ELEMENT_ONLY
class CondicionesContractualesC (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractualesC')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PotenciasMaximas uses Python identifier PotenciasMaximas
    __PotenciasMaximas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciasMaximas'), 'PotenciasMaximas', '__httplocalhostelegibilidad_CondicionesContractualesC_httplocalhostelegibilidadPotenciasMaximas', False)

    
    PotenciasMaximas = property(__PotenciasMaximas.value, __PotenciasMaximas.set, None, None)

    
    # Element {http://localhost/elegibilidad}TarifaATR uses Python identifier TarifaATR
    __TarifaATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR'), 'TarifaATR', '__httplocalhostelegibilidad_CondicionesContractualesC_httplocalhostelegibilidadTarifaATR', False)

    
    TarifaATR = property(__TarifaATR.value, __TarifaATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}PotenciasContratadas uses Python identifier PotenciasContratadas
    __PotenciasContratadas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas'), 'PotenciasContratadas', '__httplocalhostelegibilidad_CondicionesContractualesC_httplocalhostelegibilidadPotenciasContratadas', False)

    
    PotenciasContratadas = property(__PotenciasContratadas.value, __PotenciasContratadas.set, None, None)

    
    # Element {http://localhost/elegibilidad}MarcaMedidaBTConPerdidas uses Python identifier MarcaMedidaBTConPerdidas
    __MarcaMedidaBTConPerdidas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MarcaMedidaBTConPerdidas'), 'MarcaMedidaBTConPerdidas', '__httplocalhostelegibilidad_CondicionesContractualesC_httplocalhostelegibilidadMarcaMedidaBTConPerdidas', False)

    
    MarcaMedidaBTConPerdidas = property(__MarcaMedidaBTConPerdidas.value, __MarcaMedidaBTConPerdidas.set, None, None)

    
    # Element {http://localhost/elegibilidad}KVAsTrafo uses Python identifier KVAsTrafo
    __KVAsTrafo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'KVAsTrafo'), 'KVAsTrafo', '__httplocalhostelegibilidad_CondicionesContractualesC_httplocalhostelegibilidadKVAsTrafo', False)

    
    KVAsTrafo = property(__KVAsTrafo.value, __KVAsTrafo.set, None, None)

    
    # Element {http://localhost/elegibilidad}PorcentajePerdidasPactadas uses Python identifier PorcentajePerdidasPactadas
    __PorcentajePerdidasPactadas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PorcentajePerdidasPactadas'), 'PorcentajePerdidasPactadas', '__httplocalhostelegibilidad_CondicionesContractualesC_httplocalhostelegibilidadPorcentajePerdidasPactadas', False)

    
    PorcentajePerdidasPactadas = property(__PorcentajePerdidasPactadas.value, __PorcentajePerdidasPactadas.set, None, None)


    _ElementMap = {
        __PotenciasMaximas.name() : __PotenciasMaximas,
        __TarifaATR.name() : __TarifaATR,
        __PotenciasContratadas.name() : __PotenciasContratadas,
        __MarcaMedidaBTConPerdidas.name() : __MarcaMedidaBTConPerdidas,
        __KVAsTrafo.name() : __KVAsTrafo,
        __PorcentajePerdidasPactadas.name() : __PorcentajePerdidasPactadas
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CondicionesContractualesC', CondicionesContractualesC)


# Complex type CTD_ANON_18 with content type SIMPLE
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = Importe
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is Importe

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type DatosAparatoICP with content type ELEMENT_ONLY
class DatosAparatoICP (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoICP')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}NumIntegradores uses Python identifier NumIntegradores
    __NumIntegradores = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumIntegradores'), 'NumIntegradores', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadNumIntegradores', False)

    
    NumIntegradores = property(__NumIntegradores.value, __NumIntegradores.set, None, None)

    
    # Element {http://localhost/elegibilidad}PeriodoFabricacion uses Python identifier PeriodoFabricacion
    __PeriodoFabricacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PeriodoFabricacion'), 'PeriodoFabricacion', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadPeriodoFabricacion', False)

    
    PeriodoFabricacion = property(__PeriodoFabricacion.value, __PeriodoFabricacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}NumeroSerie uses Python identifier NumeroSerie
    __NumeroSerie = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), 'NumeroSerie', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadNumeroSerie', False)

    
    NumeroSerie = property(__NumeroSerie.value, __NumeroSerie.set, None, None)

    
    # Element {http://localhost/elegibilidad}FuncionAparato uses Python identifier FuncionAparato
    __FuncionAparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FuncionAparato'), 'FuncionAparato', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadFuncionAparato', False)

    
    FuncionAparato = property(__FuncionAparato.value, __FuncionAparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}RuedasDecimales uses Python identifier RuedasDecimales
    __RuedasDecimales = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RuedasDecimales'), 'RuedasDecimales', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadRuedasDecimales', False)

    
    RuedasDecimales = property(__RuedasDecimales.value, __RuedasDecimales.set, None, None)

    
    # Element {http://localhost/elegibilidad}ConstanteEnergia uses Python identifier ConstanteEnergia
    __ConstanteEnergia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConstanteEnergia'), 'ConstanteEnergia', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadConstanteEnergia', False)

    
    ConstanteEnergia = property(__ConstanteEnergia.value, __ConstanteEnergia.set, None, None)

    
    # Element {http://localhost/elegibilidad}ConstanteMaximetro uses Python identifier ConstanteMaximetro
    __ConstanteMaximetro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMaximetro'), 'ConstanteMaximetro', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadConstanteMaximetro', False)

    
    ConstanteMaximetro = property(__ConstanteMaximetro.value, __ConstanteMaximetro.set, None, None)

    
    # Element {http://localhost/elegibilidad}RuedasEnteras uses Python identifier RuedasEnteras
    __RuedasEnteras = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RuedasEnteras'), 'RuedasEnteras', '__httplocalhostelegibilidad_DatosAparatoICP_httplocalhostelegibilidadRuedasEnteras', False)

    
    RuedasEnteras = property(__RuedasEnteras.value, __RuedasEnteras.set, None, None)


    _ElementMap = {
        __NumIntegradores.name() : __NumIntegradores,
        __PeriodoFabricacion.name() : __PeriodoFabricacion,
        __NumeroSerie.name() : __NumeroSerie,
        __FuncionAparato.name() : __FuncionAparato,
        __RuedasDecimales.name() : __RuedasDecimales,
        __ConstanteEnergia.name() : __ConstanteEnergia,
        __ConstanteMaximetro.name() : __ConstanteMaximetro,
        __RuedasEnteras.name() : __RuedasEnteras
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosAparatoICP', DatosAparatoICP)


# Complex type ImportesOtrosConceptos with content type ELEMENT_ONLY
class ImportesOtrosConceptos (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ImportesOtrosConceptos')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteOtrosConceptos uses Python identifier ImporteOtrosConceptos
    __ImporteOtrosConceptos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteOtrosConceptos'), 'ImporteOtrosConceptos', '__httplocalhostelegibilidad_ImportesOtrosConceptos_httplocalhostelegibilidadImporteOtrosConceptos', True)

    
    ImporteOtrosConceptos = property(__ImporteOtrosConceptos.value, __ImporteOtrosConceptos.set, None, None)


    _ElementMap = {
        __ImporteOtrosConceptos.name() : __ImporteOtrosConceptos
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ImportesOtrosConceptos', ImportesOtrosConceptos)


# Complex type CTD_ANON_19 with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Anomalia uses Python identifier Anomalia
    __Anomalia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Anomalia'), 'Anomalia', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadAnomalia', False)

    
    Anomalia = property(__Anomalia.value, __Anomalia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Ajuste uses Python identifier Ajuste
    __Ajuste = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Ajuste'), 'Ajuste', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadAjuste', False)

    
    Ajuste = property(__Ajuste.value, __Ajuste.set, None, None)

    
    # Element {http://localhost/elegibilidad}NumeroRuedasDecimales uses Python identifier NumeroRuedasDecimales
    __NumeroRuedasDecimales = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroRuedasDecimales'), 'NumeroRuedasDecimales', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadNumeroRuedasDecimales', False)

    
    NumeroRuedasDecimales = property(__NumeroRuedasDecimales.value, __NumeroRuedasDecimales.set, None, None)

    
    # Element {http://localhost/elegibilidad}Magnitud uses Python identifier Magnitud
    __Magnitud = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Magnitud'), 'Magnitud', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadMagnitud', False)

    
    Magnitud = property(__Magnitud.value, __Magnitud.set, None, u'Tabla 43')

    
    # Element {http://localhost/elegibilidad}ConsumoCalculado uses Python identifier ConsumoCalculado
    __ConsumoCalculado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConsumoCalculado'), 'ConsumoCalculado', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadConsumoCalculado', False)

    
    ConsumoCalculado = property(__ConsumoCalculado.value, __ConsumoCalculado.set, None, u'Consumo')

    
    # Element {http://localhost/elegibilidad}NumeroRuedasEnteras uses Python identifier NumeroRuedasEnteras
    __NumeroRuedasEnteras = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroRuedasEnteras'), 'NumeroRuedasEnteras', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadNumeroRuedasEnteras', False)

    
    NumeroRuedasEnteras = property(__NumeroRuedasEnteras.value, __NumeroRuedasEnteras.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHoraMaximetro uses Python identifier FechaHoraMaximetro
    __FechaHoraMaximetro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHoraMaximetro'), 'FechaHoraMaximetro', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadFechaHoraMaximetro', False)

    
    FechaHoraMaximetro = property(__FechaHoraMaximetro.value, __FechaHoraMaximetro.set, None, None)

    
    # Element {http://localhost/elegibilidad}LecturaDesde uses Python identifier LecturaDesde
    __LecturaDesde = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LecturaDesde'), 'LecturaDesde', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadLecturaDesde', False)

    
    LecturaDesde = property(__LecturaDesde.value, __LecturaDesde.set, None, u'Lectura anterior ventana de facturaci\xf3n')

    
    # Element {http://localhost/elegibilidad}ConstanteMultiplicadora uses Python identifier ConstanteMultiplicadora
    __ConstanteMultiplicadora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMultiplicadora'), 'ConstanteMultiplicadora', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadConstanteMultiplicadora', False)

    
    ConstanteMultiplicadora = property(__ConstanteMultiplicadora.value, __ConstanteMultiplicadora.set, None, u'Coeficiente de multiplicaci\xf3n del equipo')

    
    # Element {http://localhost/elegibilidad}CodigoPeriodo uses Python identifier CodigoPeriodo
    __CodigoPeriodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoPeriodo'), 'CodigoPeriodo', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadCodigoPeriodo', False)

    
    CodigoPeriodo = property(__CodigoPeriodo.value, __CodigoPeriodo.set, None, u'Tabla 42')

    
    # Element {http://localhost/elegibilidad}LecturaHasta uses Python identifier LecturaHasta
    __LecturaHasta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LecturaHasta'), 'LecturaHasta', '__httplocalhostelegibilidad_CTD_ANON_19_httplocalhostelegibilidadLecturaHasta', False)

    
    LecturaHasta = property(__LecturaHasta.value, __LecturaHasta.set, None, u'Valor actual de la ventana de facturaci\xf3n')


    _ElementMap = {
        __Anomalia.name() : __Anomalia,
        __Ajuste.name() : __Ajuste,
        __NumeroRuedasDecimales.name() : __NumeroRuedasDecimales,
        __Magnitud.name() : __Magnitud,
        __ConsumoCalculado.name() : __ConsumoCalculado,
        __NumeroRuedasEnteras.name() : __NumeroRuedasEnteras,
        __FechaHoraMaximetro.name() : __FechaHoraMaximetro,
        __LecturaDesde.name() : __LecturaDesde,
        __ConstanteMultiplicadora.name() : __ConstanteMultiplicadora,
        __CodigoPeriodo.name() : __CodigoPeriodo,
        __LecturaHasta.name() : __LecturaHasta
    }
    _AttributeMap = {
        
    }



# Complex type MedidaC2 with content type ELEMENT_ONLY
class MedidaC2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MedidaC2')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}EquipoInstaladoCliente uses Python identifier EquipoInstaladoCliente
    __EquipoInstaladoCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente'), 'EquipoInstaladoCliente', '__httplocalhostelegibilidad_MedidaC2_httplocalhostelegibilidadEquipoInstaladoCliente', False)

    
    EquipoInstaladoCliente = property(__EquipoInstaladoCliente.value, __EquipoInstaladoCliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoEquipoMedida uses Python identifier TipoEquipoMedida
    __TipoEquipoMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), 'TipoEquipoMedida', '__httplocalhostelegibilidad_MedidaC2_httplocalhostelegibilidadTipoEquipoMedida', False)

    
    TipoEquipoMedida = property(__TipoEquipoMedida.value, __TipoEquipoMedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}ModelosAparato uses Python identifier ModelosAparato
    __ModelosAparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato'), 'ModelosAparato', '__httplocalhostelegibilidad_MedidaC2_httplocalhostelegibilidadModelosAparato', False)

    
    ModelosAparato = property(__ModelosAparato.value, __ModelosAparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}ICPAportadoInstalado uses Python identifier ICPAportadoInstalado
    __ICPAportadoInstalado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado'), 'ICPAportadoInstalado', '__httplocalhostelegibilidad_MedidaC2_httplocalhostelegibilidadICPAportadoInstalado', False)

    
    ICPAportadoInstalado = property(__ICPAportadoInstalado.value, __ICPAportadoInstalado.set, None, None)

    
    # Element {http://localhost/elegibilidad}ICPInstalacion uses Python identifier ICPInstalacion
    __ICPInstalacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion'), 'ICPInstalacion', '__httplocalhostelegibilidad_MedidaC2_httplocalhostelegibilidadICPInstalacion', False)

    
    ICPInstalacion = property(__ICPInstalacion.value, __ICPInstalacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}EquipoAportadoCliente uses Python identifier EquipoAportadoCliente
    __EquipoAportadoCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente'), 'EquipoAportadoCliente', '__httplocalhostelegibilidad_MedidaC2_httplocalhostelegibilidadEquipoAportadoCliente', False)

    
    EquipoAportadoCliente = property(__EquipoAportadoCliente.value, __EquipoAportadoCliente.set, None, None)


    _ElementMap = {
        __EquipoInstaladoCliente.name() : __EquipoInstaladoCliente,
        __TipoEquipoMedida.name() : __TipoEquipoMedida,
        __ModelosAparato.name() : __ModelosAparato,
        __ICPAportadoInstalado.name() : __ICPAportadoInstalado,
        __ICPInstalacion.name() : __ICPInstalacion,
        __EquipoAportadoCliente.name() : __EquipoAportadoCliente
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'MedidaC2', MedidaC2)


# Complex type CTD_ANON_20 with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PrecioEnergia uses Python identifier PrecioEnergia
    __PrecioEnergia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PrecioEnergia'), 'PrecioEnergia', '__httplocalhostelegibilidad_CTD_ANON_20_httplocalhostelegibilidadPrecioEnergia', False)

    
    PrecioEnergia = property(__PrecioEnergia.value, __PrecioEnergia.set, None, None)

    
    # Element {http://localhost/elegibilidad}ValorEnergiaActiva uses Python identifier ValorEnergiaActiva
    __ValorEnergiaActiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ValorEnergiaActiva'), 'ValorEnergiaActiva', '__httplocalhostelegibilidad_CTD_ANON_20_httplocalhostelegibilidadValorEnergiaActiva', False)

    
    ValorEnergiaActiva = property(__ValorEnergiaActiva.value, __ValorEnergiaActiva.set, None, u'En Kwh')


    _ElementMap = {
        __PrecioEnergia.name() : __PrecioEnergia,
        __ValorEnergiaActiva.name() : __ValorEnergiaActiva
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_21 with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_CTD_ANON_21_httplocalhostelegibilidadPeriodo', True)

    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaDesde uses Python identifier FechaDesde
    __FechaDesde = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde'), 'FechaDesde', '__httplocalhostelegibilidad_CTD_ANON_21_httplocalhostelegibilidadFechaDesde', False)

    
    FechaDesde = property(__FechaDesde.value, __FechaDesde.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHasta uses Python identifier FechaHasta
    __FechaHasta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta'), 'FechaHasta', '__httplocalhostelegibilidad_CTD_ANON_21_httplocalhostelegibilidadFechaHasta', False)

    
    FechaHasta = property(__FechaHasta.value, __FechaHasta.set, None, None)


    _ElementMap = {
        __Periodo.name() : __Periodo,
        __FechaDesde.name() : __FechaDesde,
        __FechaHasta.name() : __FechaHasta
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_22 with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_CTD_ANON_22_httplocalhostelegibilidadPeriodo', False)

    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoFacturacion uses Python identifier TipoFacturacion
    __TipoFacturacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoFacturacion'), 'TipoFacturacion', '__httplocalhostelegibilidad_CTD_ANON_22_httplocalhostelegibilidadTipoFacturacion', False)

    
    TipoFacturacion = property(__TipoFacturacion.value, __TipoFacturacion.set, None, u'Tabla 105 (1-Regular (Periodo completo); 2-Irregular (Periodo incompleto))')

    
    # Element {http://localhost/elegibilidad}FechaBOE uses Python identifier FechaBOE
    __FechaBOE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaBOE'), 'FechaBOE', '__httplocalhostelegibilidad_CTD_ANON_22_httplocalhostelegibilidadFechaBOE', False)

    
    FechaBOE = property(__FechaBOE.value, __FechaBOE.set, None, None)

    
    # Element {http://localhost/elegibilidad}IndAltamedidoenBaja uses Python identifier IndAltamedidoenBaja
    __IndAltamedidoenBaja = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IndAltamedidoenBaja'), 'IndAltamedidoenBaja', '__httplocalhostelegibilidad_CTD_ANON_22_httplocalhostelegibilidadIndAltamedidoenBaja', False)

    
    IndAltamedidoenBaja = property(__IndAltamedidoenBaja.value, __IndAltamedidoenBaja.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoTarifa uses Python identifier CodigoTarifa
    __CodigoTarifa = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoTarifa'), 'CodigoTarifa', '__httplocalhostelegibilidad_CTD_ANON_22_httplocalhostelegibilidadCodigoTarifa', False)

    
    CodigoTarifa = property(__CodigoTarifa.value, __CodigoTarifa.set, None, u'Tabla 107')


    _ElementMap = {
        __Periodo.name() : __Periodo,
        __TipoFacturacion.name() : __TipoFacturacion,
        __FechaBOE.name() : __FechaBOE,
        __IndAltamedidoenBaja.name() : __IndAltamedidoenBaja,
        __CodigoTarifa.name() : __CodigoTarifa
    }
    _AttributeMap = {
        
    }



# Complex type DatosAPM with content type ELEMENT_ONLY
class DatosAPM (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosAPM')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}FechaCaducidadApm uses Python identifier FechaCaducidadApm
    __FechaCaducidadApm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaCaducidadApm'), 'FechaCaducidadApm', '__httplocalhostelegibilidad_DatosAPM_httplocalhostelegibilidadFechaCaducidadApm', False)

    
    FechaCaducidadApm = property(__FechaCaducidadApm.value, __FechaCaducidadApm.set, None, None)

    
    # Element {http://localhost/elegibilidad}ApmAportado uses Python identifier ApmAportado
    __ApmAportado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ApmAportado'), 'ApmAportado', '__httplocalhostelegibilidad_DatosAPM_httplocalhostelegibilidadApmAportado', False)

    
    ApmAportado = property(__ApmAportado.value, __ApmAportado.set, None, None)

    
    # Element {http://localhost/elegibilidad}PotenciaInstAT uses Python identifier PotenciaInstAT
    __PotenciaInstAT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciaInstAT'), 'PotenciaInstAT', '__httplocalhostelegibilidad_DatosAPM_httplocalhostelegibilidadPotenciaInstAT', False)

    
    PotenciaInstAT = property(__PotenciaInstAT.value, __PotenciaInstAT.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaEmisionApm uses Python identifier FechaEmisionApm
    __FechaEmisionApm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaEmisionApm'), 'FechaEmisionApm', '__httplocalhostelegibilidad_DatosAPM_httplocalhostelegibilidadFechaEmisionApm', False)

    
    FechaEmisionApm = property(__FechaEmisionApm.value, __FechaEmisionApm.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoApm uses Python identifier CodigoApm
    __CodigoApm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoApm'), 'CodigoApm', '__httplocalhostelegibilidad_DatosAPM_httplocalhostelegibilidadCodigoApm', False)

    
    CodigoApm = property(__CodigoApm.value, __CodigoApm.set, None, None)


    _ElementMap = {
        __FechaCaducidadApm.name() : __FechaCaducidadApm,
        __ApmAportado.name() : __ApmAportado,
        __PotenciaInstAT.name() : __PotenciaInstAT,
        __FechaEmisionApm.name() : __FechaEmisionApm,
        __CodigoApm.name() : __CodigoApm
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosAPM', DatosAPM)


# Complex type CTD_ANON_23 with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Cabecera uses Python identifier Cabecera
    __Cabecera = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cabecera'), 'Cabecera', '__httplocalhostelegibilidad_CTD_ANON_23_httplocalhostelegibilidadCabecera', False)

    
    Cabecera = property(__Cabecera.value, __Cabecera.set, None, None)

    
    # Element {http://localhost/elegibilidad}Facturas uses Python identifier Facturas
    __Facturas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Facturas'), 'Facturas', '__httplocalhostelegibilidad_CTD_ANON_23_httplocalhostelegibilidadFacturas', False)

    
    Facturas = property(__Facturas.value, __Facturas.set, None, None)

    
    # Element {http://localhost/elegibilidad}OtrosDatosFactura uses Python identifier OtrosDatosFactura
    __OtrosDatosFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OtrosDatosFactura'), 'OtrosDatosFactura', '__httplocalhostelegibilidad_CTD_ANON_23_httplocalhostelegibilidadOtrosDatosFactura', False)

    
    OtrosDatosFactura = property(__OtrosDatosFactura.value, __OtrosDatosFactura.set, None, None)

    
    # Attribute Firmar uses Python identifier Firmar
    __Firmar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Firmar'), 'Firmar', '__httplocalhostelegibilidad_CTD_ANON_23_Firmar', pyxb.binding.datatypes.string)
    
    Firmar = property(__Firmar.value, __Firmar.set, None, None)

    
    # Attribute AgenteSolicitante uses Python identifier AgenteSolicitante
    __AgenteSolicitante = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AgenteSolicitante'), 'AgenteSolicitante', '__httplocalhostelegibilidad_CTD_ANON_23_AgenteSolicitante', Agente, required=True)
    
    AgenteSolicitante = property(__AgenteSolicitante.value, __AgenteSolicitante.set, None, None)

    _HasWildcardElement = True

    _ElementMap = {
        __Cabecera.name() : __Cabecera,
        __Facturas.name() : __Facturas,
        __OtrosDatosFactura.name() : __OtrosDatosFactura
    }
    _AttributeMap = {
        __Firmar.name() : __Firmar,
        __AgenteSolicitante.name() : __AgenteSolicitante
    }



# Complex type ContratoPasoMRAMLTarifa2SinCambios with content type ELEMENT_ONLY
class ContratoPasoMRAMLTarifa2SinCambios (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContratoPasoMRAMLTarifa2SinCambios')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}IdContrato uses Python identifier IdContrato
    __IdContrato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), 'IdContrato', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2SinCambios_httplocalhostelegibilidadIdContrato', False)

    
    IdContrato = property(__IdContrato.value, __IdContrato.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoContratoATR uses Python identifier TipoContratoATR
    __TipoContratoATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), 'TipoContratoATR', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2SinCambios_httplocalhostelegibilidadTipoContratoATR', False)

    
    TipoContratoATR = property(__TipoContratoATR.value, __TipoContratoATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionCorrespondencia uses Python identifier DireccionCorrespondencia
    __DireccionCorrespondencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), 'DireccionCorrespondencia', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2SinCambios_httplocalhostelegibilidadDireccionCorrespondencia', False)

    
    DireccionCorrespondencia = property(__DireccionCorrespondencia.value, __DireccionCorrespondencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}CuentaBancaria uses Python identifier CuentaBancaria
    __CuentaBancaria = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), 'CuentaBancaria', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2SinCambios_httplocalhostelegibilidadCuentaBancaria', False)

    
    CuentaBancaria = property(__CuentaBancaria.value, __CuentaBancaria.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaFinalizacion uses Python identifier FechaFinalizacion
    __FechaFinalizacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), 'FechaFinalizacion', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2SinCambios_httplocalhostelegibilidadFechaFinalizacion', False)

    
    FechaFinalizacion = property(__FechaFinalizacion.value, __FechaFinalizacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}Duracion uses Python identifier Duracion
    __Duracion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), 'Duracion', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2SinCambios_httplocalhostelegibilidadDuracion', False)

    
    Duracion = property(__Duracion.value, __Duracion.set, None, None)


    _ElementMap = {
        __IdContrato.name() : __IdContrato,
        __TipoContratoATR.name() : __TipoContratoATR,
        __DireccionCorrespondencia.name() : __DireccionCorrespondencia,
        __CuentaBancaria.name() : __CuentaBancaria,
        __FechaFinalizacion.name() : __FechaFinalizacion,
        __Duracion.name() : __Duracion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ContratoPasoMRAMLTarifa2SinCambios', ContratoPasoMRAMLTarifa2SinCambios)


# Complex type Medida with content type ELEMENT_ONLY
class Medida (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Medida')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}TipoEquipoMedida uses Python identifier TipoEquipoMedida
    __TipoEquipoMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), 'TipoEquipoMedida', '__httplocalhostelegibilidad_Medida_httplocalhostelegibilidadTipoEquipoMedida', False)

    
    TipoEquipoMedida = property(__TipoEquipoMedida.value, __TipoEquipoMedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}ModelosAparato uses Python identifier ModelosAparato
    __ModelosAparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato'), 'ModelosAparato', '__httplocalhostelegibilidad_Medida_httplocalhostelegibilidadModelosAparato', False)

    
    ModelosAparato = property(__ModelosAparato.value, __ModelosAparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}EquipoInstaladoCliente uses Python identifier EquipoInstaladoCliente
    __EquipoInstaladoCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente'), 'EquipoInstaladoCliente', '__httplocalhostelegibilidad_Medida_httplocalhostelegibilidadEquipoInstaladoCliente', False)

    
    EquipoInstaladoCliente = property(__EquipoInstaladoCliente.value, __EquipoInstaladoCliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}ICPAportadoInstalado uses Python identifier ICPAportadoInstalado
    __ICPAportadoInstalado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado'), 'ICPAportadoInstalado', '__httplocalhostelegibilidad_Medida_httplocalhostelegibilidadICPAportadoInstalado', False)

    
    ICPAportadoInstalado = property(__ICPAportadoInstalado.value, __ICPAportadoInstalado.set, None, None)

    
    # Element {http://localhost/elegibilidad}ICPInstalacion uses Python identifier ICPInstalacion
    __ICPInstalacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion'), 'ICPInstalacion', '__httplocalhostelegibilidad_Medida_httplocalhostelegibilidadICPInstalacion', False)

    
    ICPInstalacion = property(__ICPInstalacion.value, __ICPInstalacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}EquipoAportadoCliente uses Python identifier EquipoAportadoCliente
    __EquipoAportadoCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente'), 'EquipoAportadoCliente', '__httplocalhostelegibilidad_Medida_httplocalhostelegibilidadEquipoAportadoCliente', False)

    
    EquipoAportadoCliente = property(__EquipoAportadoCliente.value, __EquipoAportadoCliente.set, None, None)


    _ElementMap = {
        __TipoEquipoMedida.name() : __TipoEquipoMedida,
        __ModelosAparato.name() : __ModelosAparato,
        __EquipoInstaladoCliente.name() : __EquipoInstaladoCliente,
        __ICPAportadoInstalado.name() : __ICPAportadoInstalado,
        __ICPInstalacion.name() : __ICPInstalacion,
        __EquipoAportadoCliente.name() : __EquipoAportadoCliente
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Medida', Medida)


# Complex type CTD_ANON_24 with content type SIMPLE
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = TipoConcepto
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is TipoConcepto

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type DatosCIE with content type ELEMENT_ONLY
class DatosCIE (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DatosCIE')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}FechaEmisionCie uses Python identifier FechaEmisionCie
    __FechaEmisionCie = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaEmisionCie'), 'FechaEmisionCie', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadFechaEmisionCie', False)

    
    FechaEmisionCie = property(__FechaEmisionCie.value, __FechaEmisionCie.set, None, None)

    
    # Element {http://localhost/elegibilidad}CieAportado uses Python identifier CieAportado
    __CieAportado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CieAportado'), 'CieAportado', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadCieAportado', False)

    
    CieAportado = property(__CieAportado.value, __CieAportado.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaCaducidadCie uses Python identifier FechaCaducidadCie
    __FechaCaducidadCie = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaCaducidadCie'), 'FechaCaducidadCie', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadFechaCaducidadCie', False)

    
    FechaCaducidadCie = property(__FechaCaducidadCie.value, __FechaCaducidadCie.set, None, None)

    
    # Element {http://localhost/elegibilidad}SeccionCable uses Python identifier SeccionCable
    __SeccionCable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SeccionCable'), 'SeccionCable', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadSeccionCable', False)

    
    SeccionCable = property(__SeccionCable.value, __SeccionCable.set, None, None)

    
    # Element {http://localhost/elegibilidad}NifInstalador uses Python identifier NifInstalador
    __NifInstalador = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NifInstalador'), 'NifInstalador', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadNifInstalador', False)

    
    NifInstalador = property(__NifInstalador.value, __NifInstalador.set, None, None)

    
    # Element {http://localhost/elegibilidad}CieElectronico uses Python identifier CieElectronico
    __CieElectronico = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CieElectronico'), 'CieElectronico', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadCieElectronico', False)

    
    CieElectronico = property(__CieElectronico.value, __CieElectronico.set, None, None)

    
    # Element {http://localhost/elegibilidad}TensionSuministro uses Python identifier TensionSuministro
    __TensionSuministro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TensionSuministro'), 'TensionSuministro', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadTensionSuministro', False)

    
    TensionSuministro = property(__TensionSuministro.value, __TensionSuministro.set, None, None)

    
    # Element {http://localhost/elegibilidad}NombreInstalador uses Python identifier NombreInstalador
    __NombreInstalador = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NombreInstalador'), 'NombreInstalador', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadNombreInstalador', False)

    
    NombreInstalador = property(__NombreInstalador.value, __NombreInstalador.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoSuministro uses Python identifier TipoSuministro
    __TipoSuministro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoSuministro'), 'TipoSuministro', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadTipoSuministro', False)

    
    TipoSuministro = property(__TipoSuministro.value, __TipoSuministro.set, None, None)

    
    # Element {http://localhost/elegibilidad}SelloElectronico uses Python identifier SelloElectronico
    __SelloElectronico = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SelloElectronico'), 'SelloElectronico', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadSelloElectronico', False)

    
    SelloElectronico = property(__SelloElectronico.value, __SelloElectronico.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoCie uses Python identifier CodigoCie
    __CodigoCie = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoCie'), 'CodigoCie', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadCodigoCie', False)

    
    CodigoCie = property(__CodigoCie.value, __CodigoCie.set, None, None)

    
    # Element {http://localhost/elegibilidad}SensibilidadDif uses Python identifier SensibilidadDif
    __SensibilidadDif = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SensibilidadDif'), 'SensibilidadDif', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadSensibilidadDif', False)

    
    SensibilidadDif = property(__SensibilidadDif.value, __SensibilidadDif.set, None, None)

    
    # Element {http://localhost/elegibilidad}PotenciaInstBT uses Python identifier PotenciaInstBT
    __PotenciaInstBT = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciaInstBT'), 'PotenciaInstBT', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadPotenciaInstBT', False)

    
    PotenciaInstBT = property(__PotenciaInstBT.value, __PotenciaInstBT.set, None, None)

    
    # Element {http://localhost/elegibilidad}InstensidadDif uses Python identifier InstensidadDif
    __InstensidadDif = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'InstensidadDif'), 'InstensidadDif', '__httplocalhostelegibilidad_DatosCIE_httplocalhostelegibilidadInstensidadDif', False)

    
    InstensidadDif = property(__InstensidadDif.value, __InstensidadDif.set, None, None)


    _ElementMap = {
        __FechaEmisionCie.name() : __FechaEmisionCie,
        __CieAportado.name() : __CieAportado,
        __FechaCaducidadCie.name() : __FechaCaducidadCie,
        __SeccionCable.name() : __SeccionCable,
        __NifInstalador.name() : __NifInstalador,
        __CieElectronico.name() : __CieElectronico,
        __TensionSuministro.name() : __TensionSuministro,
        __NombreInstalador.name() : __NombreInstalador,
        __TipoSuministro.name() : __TipoSuministro,
        __SelloElectronico.name() : __SelloElectronico,
        __CodigoCie.name() : __CodigoCie,
        __SensibilidadDif.name() : __SensibilidadDif,
        __PotenciaInstBT.name() : __PotenciaInstBT,
        __InstensidadDif.name() : __InstensidadDif
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DatosCIE', DatosCIE)


# Complex type Importes with content type ELEMENT_ONLY
class Importes (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Importes')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImportesOtrosConceptos uses Python identifier ImportesOtrosConceptos
    __ImportesOtrosConceptos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImportesOtrosConceptos'), 'ImportesOtrosConceptos', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImportesOtrosConceptos', False)

    
    ImportesOtrosConceptos = property(__ImportesOtrosConceptos.value, __ImportesOtrosConceptos.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImportesTerminoPotencia uses Python identifier ImportesTerminoPotencia
    __ImportesTerminoPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoPotencia'), 'ImportesTerminoPotencia', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImportesTerminoPotencia', False)

    
    ImportesTerminoPotencia = property(__ImportesTerminoPotencia.value, __ImportesTerminoPotencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}IVA uses Python identifier IVA
    __IVA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IVA'), 'IVA', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadIVA', False)

    
    IVA = property(__IVA.value, __IVA.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImporteTotal uses Python identifier ImporteTotal
    __ImporteTotal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotal'), 'ImporteTotal', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImporteTotal', False)

    
    ImporteTotal = property(__ImporteTotal.value, __ImporteTotal.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImpuestoElectrico uses Python identifier ImpuestoElectrico
    __ImpuestoElectrico = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImpuestoElectrico'), 'ImpuestoElectrico', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImpuestoElectrico', False)

    
    ImpuestoElectrico = property(__ImpuestoElectrico.value, __ImpuestoElectrico.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImporteReactiva uses Python identifier ImporteReactiva
    __ImporteReactiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteReactiva'), 'ImporteReactiva', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImporteReactiva', False)

    
    ImporteReactiva = property(__ImporteReactiva.value, __ImporteReactiva.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImporteExcesoPotencia uses Python identifier ImporteExcesoPotencia
    __ImporteExcesoPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteExcesoPotencia'), 'ImporteExcesoPotencia', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImporteExcesoPotencia', False)

    
    ImporteExcesoPotencia = property(__ImporteExcesoPotencia.value, __ImporteExcesoPotencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImportesTerminoEnergia uses Python identifier ImportesTerminoEnergia
    __ImportesTerminoEnergia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoEnergia'), 'ImportesTerminoEnergia', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImportesTerminoEnergia', False)

    
    ImportesTerminoEnergia = property(__ImportesTerminoEnergia.value, __ImportesTerminoEnergia.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImporteAlquileres uses Python identifier ImporteAlquileres
    __ImporteAlquileres = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteAlquileres'), 'ImporteAlquileres', '__httplocalhostelegibilidad_Importes_httplocalhostelegibilidadImporteAlquileres', False)

    
    ImporteAlquileres = property(__ImporteAlquileres.value, __ImporteAlquileres.set, None, None)


    _ElementMap = {
        __ImportesOtrosConceptos.name() : __ImportesOtrosConceptos,
        __ImportesTerminoPotencia.name() : __ImportesTerminoPotencia,
        __IVA.name() : __IVA,
        __ImporteTotal.name() : __ImporteTotal,
        __ImpuestoElectrico.name() : __ImpuestoElectrico,
        __ImporteReactiva.name() : __ImporteReactiva,
        __ImporteExcesoPotencia.name() : __ImporteExcesoPotencia,
        __ImportesTerminoEnergia.name() : __ImportesTerminoEnergia,
        __ImporteAlquileres.name() : __ImporteAlquileres
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Importes', Importes)


# Complex type PuntoDeMedida with content type ELEMENT_ONLY
class PuntoDeMedida (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PuntoDeMedida')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}TelefonoTelemedida uses Python identifier TelefonoTelemedida
    __TelefonoTelemedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TelefonoTelemedida'), 'TelefonoTelemedida', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadTelefonoTelemedida', False)

    
    TelefonoTelemedida = property(__TelefonoTelemedida.value, __TelefonoTelemedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaVigor uses Python identifier FechaVigor
    __FechaVigor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaVigor'), 'FechaVigor', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadFechaVigor', False)

    
    FechaVigor = property(__FechaVigor.value, __FechaVigor.set, None, None)

    
    # Element {http://localhost/elegibilidad}ClaveAcceso uses Python identifier ClaveAcceso
    __ClaveAcceso = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ClaveAcceso'), 'ClaveAcceso', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadClaveAcceso', False)

    
    ClaveAcceso = property(__ClaveAcceso.value, __ClaveAcceso.set, None, None)

    
    # Element {http://localhost/elegibilidad}TensionPM uses Python identifier TensionPM
    __TensionPM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TensionPM'), 'TensionPM', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadTensionPM', False)

    
    TensionPM = property(__TensionPM.value, __TensionPM.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodPMPrincipal uses Python identifier CodPMPrincipal
    __CodPMPrincipal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodPMPrincipal'), 'CodPMPrincipal', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadCodPMPrincipal', False)

    
    CodPMPrincipal = property(__CodPMPrincipal.value, __CodPMPrincipal.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaAlta uses Python identifier FechaAlta
    __FechaAlta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaAlta'), 'FechaAlta', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadFechaAlta', False)

    
    FechaAlta = property(__FechaAlta.value, __FechaAlta.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaBaja uses Python identifier FechaBaja
    __FechaBaja = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaBaja'), 'FechaBaja', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadFechaBaja', False)

    
    FechaBaja = property(__FechaBaja.value, __FechaBaja.set, None, None)

    
    # Element {http://localhost/elegibilidad}PasswordPM uses Python identifier PasswordPM
    __PasswordPM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PasswordPM'), 'PasswordPM', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadPasswordPM', False)

    
    PasswordPM = property(__PasswordPM.value, __PasswordPM.set, None, None)

    
    # Element {http://localhost/elegibilidad}ComentariosPM uses Python identifier ComentariosPM
    __ComentariosPM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComentariosPM'), 'ComentariosPM', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadComentariosPM', False)

    
    ComentariosPM = property(__ComentariosPM.value, __ComentariosPM.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodPM uses Python identifier CodPM
    __CodPM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodPM'), 'CodPM', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadCodPM', False)

    
    CodPM = property(__CodPM.value, __CodPM.set, None, None)

    
    # Element {http://localhost/elegibilidad}Aparatos uses Python identifier Aparatos
    __Aparatos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Aparatos'), 'Aparatos', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadAparatos', False)

    
    Aparatos = property(__Aparatos.value, __Aparatos.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoMovimiento uses Python identifier TipoMovimiento
    __TipoMovimiento = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimiento'), 'TipoMovimiento', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadTipoMovimiento', False)

    
    TipoMovimiento = property(__TipoMovimiento.value, __TipoMovimiento.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodREE uses Python identifier CodREE
    __CodREE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodREE'), 'CodREE', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadCodREE', False)

    
    CodREE = property(__CodREE.value, __CodREE.set, None, None)

    
    # Element {http://localhost/elegibilidad}CUPS uses Python identifier CUPS
    __CUPS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CUPS'), 'CUPS', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadCUPS', False)

    
    CUPS = property(__CUPS.value, __CUPS.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoPM uses Python identifier TipoPM
    __TipoPM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoPM'), 'TipoPM', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadTipoPM', False)

    
    TipoPM = property(__TipoPM.value, __TipoPM.set, None, None)

    
    # Element {http://localhost/elegibilidad}EstadoTelefono uses Python identifier EstadoTelefono
    __EstadoTelefono = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EstadoTelefono'), 'EstadoTelefono', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadEstadoTelefono', False)

    
    EstadoTelefono = property(__EstadoTelefono.value, __EstadoTelefono.set, None, None)

    
    # Element {http://localhost/elegibilidad}ModoLectura uses Python identifier ModoLectura
    __ModoLectura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModoLectura'), 'ModoLectura', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadModoLectura', False)

    
    ModoLectura = property(__ModoLectura.value, __ModoLectura.set, None, None)

    
    # Element {http://localhost/elegibilidad}EstadoPM uses Python identifier EstadoPM
    __EstadoPM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EstadoPM'), 'EstadoPM', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadEstadoPM', False)

    
    EstadoPM = property(__EstadoPM.value, __EstadoPM.set, None, None)

    
    # Element {http://localhost/elegibilidad}Funcion uses Python identifier Funcion
    __Funcion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Funcion'), 'Funcion', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadFuncion', False)

    
    Funcion = property(__Funcion.value, __Funcion.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionEnlace uses Python identifier DireccionEnlace
    __DireccionEnlace = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionEnlace'), 'DireccionEnlace', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadDireccionEnlace', False)

    
    DireccionEnlace = property(__DireccionEnlace.value, __DireccionEnlace.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionPuntoMedida uses Python identifier DireccionPuntoMedida
    __DireccionPuntoMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionPuntoMedida'), 'DireccionPuntoMedida', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadDireccionPuntoMedida', False)

    
    DireccionPuntoMedida = property(__DireccionPuntoMedida.value, __DireccionPuntoMedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}NumLinea uses Python identifier NumLinea
    __NumLinea = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumLinea'), 'NumLinea', '__httplocalhostelegibilidad_PuntoDeMedida_httplocalhostelegibilidadNumLinea', False)

    
    NumLinea = property(__NumLinea.value, __NumLinea.set, None, None)


    _ElementMap = {
        __TelefonoTelemedida.name() : __TelefonoTelemedida,
        __FechaVigor.name() : __FechaVigor,
        __ClaveAcceso.name() : __ClaveAcceso,
        __TensionPM.name() : __TensionPM,
        __CodPMPrincipal.name() : __CodPMPrincipal,
        __FechaAlta.name() : __FechaAlta,
        __FechaBaja.name() : __FechaBaja,
        __PasswordPM.name() : __PasswordPM,
        __ComentariosPM.name() : __ComentariosPM,
        __CodPM.name() : __CodPM,
        __Aparatos.name() : __Aparatos,
        __TipoMovimiento.name() : __TipoMovimiento,
        __CodREE.name() : __CodREE,
        __CUPS.name() : __CUPS,
        __TipoPM.name() : __TipoPM,
        __EstadoTelefono.name() : __EstadoTelefono,
        __ModoLectura.name() : __ModoLectura,
        __EstadoPM.name() : __EstadoPM,
        __Funcion.name() : __Funcion,
        __DireccionEnlace.name() : __DireccionEnlace,
        __DireccionPuntoMedida.name() : __DireccionPuntoMedida,
        __NumLinea.name() : __NumLinea
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'PuntoDeMedida', PuntoDeMedida)


# Complex type CTD_ANON_25 with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTotalTerminoPotencia uses Python identifier ImporteTotalTerminoPotencia
    __ImporteTotalTerminoPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalTerminoPotencia'), 'ImporteTotalTerminoPotencia', '__httplocalhostelegibilidad_CTD_ANON_25_httplocalhostelegibilidadImporteTotalTerminoPotencia', False)

    
    ImporteTotalTerminoPotencia = property(__ImporteTotalTerminoPotencia.value, __ImporteTotalTerminoPotencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}TerminoPotencia uses Python identifier TerminoPotencia
    __TerminoPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TerminoPotencia'), 'TerminoPotencia', '__httplocalhostelegibilidad_CTD_ANON_25_httplocalhostelegibilidadTerminoPotencia', True)

    
    TerminoPotencia = property(__TerminoPotencia.value, __TerminoPotencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}PenalizacionNoICP uses Python identifier PenalizacionNoICP
    __PenalizacionNoICP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PenalizacionNoICP'), 'PenalizacionNoICP', '__httplocalhostelegibilidad_CTD_ANON_25_httplocalhostelegibilidadPenalizacionNoICP', False)

    
    PenalizacionNoICP = property(__PenalizacionNoICP.value, __PenalizacionNoICP.set, None, None)


    _ElementMap = {
        __ImporteTotalTerminoPotencia.name() : __ImporteTotalTerminoPotencia,
        __TerminoPotencia.name() : __TerminoPotencia,
        __PenalizacionNoICP.name() : __PenalizacionNoICP
    }
    _AttributeMap = {
        
    }



# Complex type Comentarios with content type ELEMENT_ONLY
class Comentarios (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Comentarios')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Comentario uses Python identifier Comentario
    __Comentario = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Comentario'), 'Comentario', '__httplocalhostelegibilidad_Comentarios_httplocalhostelegibilidadComentario', True)

    
    Comentario = property(__Comentario.value, __Comentario.set, None, None)


    _ElementMap = {
        __Comentario.name() : __Comentario
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Comentarios', Comentarios)


# Complex type Comentario with content type ELEMENT_ONLY
class Comentario (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Comentario')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Hora uses Python identifier Hora
    __Hora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Hora'), 'Hora', '__httplocalhostelegibilidad_Comentario_httplocalhostelegibilidadHora', False)

    
    Hora = property(__Hora.value, __Hora.set, None, None)

    
    # Element {http://localhost/elegibilidad}Texto uses Python identifier Texto
    __Texto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Texto'), 'Texto', '__httplocalhostelegibilidad_Comentario_httplocalhostelegibilidadTexto', False)

    
    Texto = property(__Texto.value, __Texto.set, None, None)

    
    # Element {http://localhost/elegibilidad}Fecha uses Python identifier Fecha
    __Fecha = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Fecha'), 'Fecha', '__httplocalhostelegibilidad_Comentario_httplocalhostelegibilidadFecha', False)

    
    Fecha = property(__Fecha.value, __Fecha.set, None, None)


    _ElementMap = {
        __Hora.name() : __Hora,
        __Texto.name() : __Texto,
        __Fecha.name() : __Fecha
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Comentario', Comentario)


# Complex type PotenciasAFacturar with content type ELEMENT_ONLY
class PotenciasAFacturar (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PotenciasAFacturar')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PotenciaAFacturar uses Python identifier PotenciaAFacturar
    __PotenciaAFacturar = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PotenciaAFacturar'), 'PotenciaAFacturar', '__httplocalhostelegibilidad_PotenciasAFacturar_httplocalhostelegibilidadPotenciaAFacturar', True)

    
    PotenciaAFacturar = property(__PotenciaAFacturar.value, __PotenciaAFacturar.set, None, None)


    _ElementMap = {
        __PotenciaAFacturar.name() : __PotenciaAFacturar
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'PotenciasAFacturar', PotenciasAFacturar)


# Complex type CTD_ANON_26 with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}AjustePorIntegrador uses Python identifier AjustePorIntegrador
    __AjustePorIntegrador = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AjustePorIntegrador'), 'AjustePorIntegrador', '__httplocalhostelegibilidad_CTD_ANON_26_httplocalhostelegibilidadAjustePorIntegrador', False)

    
    AjustePorIntegrador = property(__AjustePorIntegrador.value, __AjustePorIntegrador.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodigoMotivoAjuste uses Python identifier CodigoMotivoAjuste
    __CodigoMotivoAjuste = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodigoMotivoAjuste'), 'CodigoMotivoAjuste', '__httplocalhostelegibilidad_CTD_ANON_26_httplocalhostelegibilidadCodigoMotivoAjuste', False)

    
    CodigoMotivoAjuste = property(__CodigoMotivoAjuste.value, __CodigoMotivoAjuste.set, None, u'Tabla 106')


    _ElementMap = {
        __AjustePorIntegrador.name() : __AjustePorIntegrador,
        __CodigoMotivoAjuste.name() : __CodigoMotivoAjuste
    }
    _AttributeMap = {
        
    }



# Complex type ContratoPasoMRAMLTarifa2ConCambios with content type ELEMENT_ONLY
class ContratoPasoMRAMLTarifa2ConCambios (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContratoPasoMRAMLTarifa2ConCambios')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Duracion uses Python identifier Duracion
    __Duracion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), 'Duracion', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadDuracion', False)

    
    Duracion = property(__Duracion.value, __Duracion.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoContratoATR uses Python identifier TipoContratoATR
    __TipoContratoATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), 'TipoContratoATR', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadTipoContratoATR', False)

    
    TipoContratoATR = property(__TipoContratoATR.value, __TipoContratoATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}CondicionesContractuales2n uses Python identifier CondicionesContractuales2n
    __CondicionesContractuales2n = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales2n'), 'CondicionesContractuales2n', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadCondicionesContractuales2n', False)

    
    CondicionesContractuales2n = property(__CondicionesContractuales2n.value, __CondicionesContractuales2n.set, None, None)

    
    # Element {http://localhost/elegibilidad}Contacto uses Python identifier Contacto
    __Contacto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contacto'), 'Contacto', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadContacto', False)

    
    Contacto = property(__Contacto.value, __Contacto.set, None, None)

    
    # Element {http://localhost/elegibilidad}CuentaBancaria uses Python identifier CuentaBancaria
    __CuentaBancaria = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), 'CuentaBancaria', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadCuentaBancaria', False)

    
    CuentaBancaria = property(__CuentaBancaria.value, __CuentaBancaria.set, None, None)

    
    # Element {http://localhost/elegibilidad}IdContrato uses Python identifier IdContrato
    __IdContrato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), 'IdContrato', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadIdContrato', False)

    
    IdContrato = property(__IdContrato.value, __IdContrato.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionCorrespondencia uses Python identifier DireccionCorrespondencia
    __DireccionCorrespondencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), 'DireccionCorrespondencia', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadDireccionCorrespondencia', False)

    
    DireccionCorrespondencia = property(__DireccionCorrespondencia.value, __DireccionCorrespondencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaFinalizacion uses Python identifier FechaFinalizacion
    __FechaFinalizacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), 'FechaFinalizacion', '__httplocalhostelegibilidad_ContratoPasoMRAMLTarifa2ConCambios_httplocalhostelegibilidadFechaFinalizacion', False)

    
    FechaFinalizacion = property(__FechaFinalizacion.value, __FechaFinalizacion.set, None, None)


    _ElementMap = {
        __Duracion.name() : __Duracion,
        __TipoContratoATR.name() : __TipoContratoATR,
        __CondicionesContractuales2n.name() : __CondicionesContractuales2n,
        __Contacto.name() : __Contacto,
        __CuentaBancaria.name() : __CuentaBancaria,
        __IdContrato.name() : __IdContrato,
        __DireccionCorrespondencia.name() : __DireccionCorrespondencia,
        __FechaFinalizacion.name() : __FechaFinalizacion
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ContratoPasoMRAMLTarifa2ConCambios', ContratoPasoMRAMLTarifa2ConCambios)


# Complex type DireccionSinCodPostal with content type ELEMENT_ONLY
class DireccionSinCodPostal (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DireccionSinCodPostal')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Piso uses Python identifier Piso
    __Piso = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Piso'), 'Piso', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadPiso', False)

    
    Piso = property(__Piso.value, __Piso.set, None, None)

    
    # Element {http://localhost/elegibilidad}Poblacion uses Python identifier Poblacion
    __Poblacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Poblacion'), 'Poblacion', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadPoblacion', False)

    
    Poblacion = property(__Poblacion.value, __Poblacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}Municipio uses Python identifier Municipio
    __Municipio = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), 'Municipio', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadMunicipio', False)

    
    Municipio = property(__Municipio.value, __Municipio.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoAclaradorFinca uses Python identifier TipoAclaradorFinca
    __TipoAclaradorFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoAclaradorFinca'), 'TipoAclaradorFinca', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadTipoAclaradorFinca', False)

    
    TipoAclaradorFinca = property(__TipoAclaradorFinca.value, __TipoAclaradorFinca.set, None, None)

    
    # Element {http://localhost/elegibilidad}Pais uses Python identifier Pais
    __Pais = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Pais'), 'Pais', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadPais', False)

    
    Pais = property(__Pais.value, __Pais.set, None, None)

    
    # Element {http://localhost/elegibilidad}AclaradorFinca uses Python identifier AclaradorFinca
    __AclaradorFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AclaradorFinca'), 'AclaradorFinca', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadAclaradorFinca', False)

    
    AclaradorFinca = property(__AclaradorFinca.value, __AclaradorFinca.set, None, None)

    
    # Element {http://localhost/elegibilidad}Calle uses Python identifier Calle
    __Calle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Calle'), 'Calle', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadCalle', False)

    
    Calle = property(__Calle.value, __Calle.set, None, None)

    
    # Element {http://localhost/elegibilidad}Provincia uses Python identifier Provincia
    __Provincia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Provincia'), 'Provincia', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadProvincia', False)

    
    Provincia = property(__Provincia.value, __Provincia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Puerta uses Python identifier Puerta
    __Puerta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Puerta'), 'Puerta', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadPuerta', False)

    
    Puerta = property(__Puerta.value, __Puerta.set, None, None)

    
    # Element {http://localhost/elegibilidad}NumeroFinca uses Python identifier NumeroFinca
    __NumeroFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroFinca'), 'NumeroFinca', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadNumeroFinca', False)

    
    NumeroFinca = property(__NumeroFinca.value, __NumeroFinca.set, None, None)

    
    # Element {http://localhost/elegibilidad}DuplicadorFinca uses Python identifier DuplicadorFinca
    __DuplicadorFinca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DuplicadorFinca'), 'DuplicadorFinca', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadDuplicadorFinca', False)

    
    DuplicadorFinca = property(__DuplicadorFinca.value, __DuplicadorFinca.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoVia uses Python identifier TipoVia
    __TipoVia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoVia'), 'TipoVia', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadTipoVia', False)

    
    TipoVia = property(__TipoVia.value, __TipoVia.set, None, None)

    
    # Element {http://localhost/elegibilidad}Escalera uses Python identifier Escalera
    __Escalera = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Escalera'), 'Escalera', '__httplocalhostelegibilidad_DireccionSinCodPostal_httplocalhostelegibilidadEscalera', False)

    
    Escalera = property(__Escalera.value, __Escalera.set, None, None)


    _ElementMap = {
        __Piso.name() : __Piso,
        __Poblacion.name() : __Poblacion,
        __Municipio.name() : __Municipio,
        __TipoAclaradorFinca.name() : __TipoAclaradorFinca,
        __Pais.name() : __Pais,
        __AclaradorFinca.name() : __AclaradorFinca,
        __Calle.name() : __Calle,
        __Provincia.name() : __Provincia,
        __Puerta.name() : __Puerta,
        __NumeroFinca.name() : __NumeroFinca,
        __DuplicadorFinca.name() : __DuplicadorFinca,
        __TipoVia.name() : __TipoVia,
        __Escalera.name() : __Escalera
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'DireccionSinCodPostal', DireccionSinCodPostal)


# Complex type Aparato with content type ELEMENT_ONLY
class Aparato (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aparato')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}TipoEquipoMedida uses Python identifier TipoEquipoMedida
    __TipoEquipoMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), 'TipoEquipoMedida', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadTipoEquipoMedida', False)

    
    TipoEquipoMedida = property(__TipoEquipoMedida.value, __TipoEquipoMedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}DiscriminacionHorariaActiva uses Python identifier DiscriminacionHorariaActiva
    __DiscriminacionHorariaActiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DiscriminacionHorariaActiva'), 'DiscriminacionHorariaActiva', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadDiscriminacionHorariaActiva', False)

    
    DiscriminacionHorariaActiva = property(__DiscriminacionHorariaActiva.value, __DiscriminacionHorariaActiva.set, None, None)

    
    # Element {http://localhost/elegibilidad}Propietario uses Python identifier Propietario
    __Propietario = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Propietario'), 'Propietario', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadPropietario', False)

    
    Propietario = property(__Propietario.value, __Propietario.set, None, None)

    
    # Element {http://localhost/elegibilidad}DatosAparatoNoICP uses Python identifier DatosAparatoNoICP
    __DatosAparatoNoICP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoNoICP'), 'DatosAparatoNoICP', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadDatosAparatoNoICP', False)

    
    DatosAparatoNoICP = property(__DatosAparatoNoICP.value, __DatosAparatoNoICP.set, None, None)

    
    # Element {http://localhost/elegibilidad}ExtraccionLecturas uses Python identifier ExtraccionLecturas
    __ExtraccionLecturas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExtraccionLecturas'), 'ExtraccionLecturas', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadExtraccionLecturas', False)

    
    ExtraccionLecturas = property(__ExtraccionLecturas.value, __ExtraccionLecturas.set, None, None)

    
    # Element {http://localhost/elegibilidad}DatosAparatoICP uses Python identifier DatosAparatoICP
    __DatosAparatoICP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoICP'), 'DatosAparatoICP', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadDatosAparatoICP', False)

    
    DatosAparatoICP = property(__DatosAparatoICP.value, __DatosAparatoICP.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoPropiedadAparato uses Python identifier TipoPropiedadAparato
    __TipoPropiedadAparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoPropiedadAparato'), 'TipoPropiedadAparato', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadTipoPropiedadAparato', False)

    
    TipoPropiedadAparato = property(__TipoPropiedadAparato.value, __TipoPropiedadAparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}Medidas uses Python identifier Medidas
    __Medidas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Medidas'), 'Medidas', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadMedidas', False)

    
    Medidas = property(__Medidas.value, __Medidas.set, None, None)

    
    # Element {http://localhost/elegibilidad}DiscriminacionHorariaMaximas uses Python identifier DiscriminacionHorariaMaximas
    __DiscriminacionHorariaMaximas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DiscriminacionHorariaMaximas'), 'DiscriminacionHorariaMaximas', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadDiscriminacionHorariaMaximas', False)

    
    DiscriminacionHorariaMaximas = property(__DiscriminacionHorariaMaximas.value, __DiscriminacionHorariaMaximas.set, None, None)

    
    # Element {http://localhost/elegibilidad}Modelo uses Python identifier Modelo
    __Modelo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Modelo'), 'Modelo', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadModelo', False)

    
    Modelo = property(__Modelo.value, __Modelo.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodPrecinto uses Python identifier CodPrecinto
    __CodPrecinto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodPrecinto'), 'CodPrecinto', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadCodPrecinto', False)

    
    CodPrecinto = property(__CodPrecinto.value, __CodPrecinto.set, None, u'Codigo de precinto')

    
    # Element {http://localhost/elegibilidad}LecturaDirecta uses Python identifier LecturaDirecta
    __LecturaDirecta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LecturaDirecta'), 'LecturaDirecta', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadLecturaDirecta', False)

    
    LecturaDirecta = property(__LecturaDirecta.value, __LecturaDirecta.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoMovimiento uses Python identifier TipoMovimiento
    __TipoMovimiento = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimiento'), 'TipoMovimiento', '__httplocalhostelegibilidad_Aparato_httplocalhostelegibilidadTipoMovimiento', False)

    
    TipoMovimiento = property(__TipoMovimiento.value, __TipoMovimiento.set, None, None)


    _ElementMap = {
        __TipoEquipoMedida.name() : __TipoEquipoMedida,
        __DiscriminacionHorariaActiva.name() : __DiscriminacionHorariaActiva,
        __Propietario.name() : __Propietario,
        __DatosAparatoNoICP.name() : __DatosAparatoNoICP,
        __ExtraccionLecturas.name() : __ExtraccionLecturas,
        __DatosAparatoICP.name() : __DatosAparatoICP,
        __TipoPropiedadAparato.name() : __TipoPropiedadAparato,
        __Medidas.name() : __Medidas,
        __DiscriminacionHorariaMaximas.name() : __DiscriminacionHorariaMaximas,
        __Modelo.name() : __Modelo,
        __CodPrecinto.name() : __CodPrecinto,
        __LecturaDirecta.name() : __LecturaDirecta,
        __TipoMovimiento.name() : __TipoMovimiento
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Aparato', Aparato)


# Complex type Anomalias with content type ELEMENT_ONLY
class Anomalias (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Anomalias')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Anomalia uses Python identifier Anomalia
    __Anomalia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Anomalia'), 'Anomalia', '__httplocalhostelegibilidad_Anomalias_httplocalhostelegibilidadAnomalia', True)

    
    Anomalia = property(__Anomalia.value, __Anomalia.set, None, None)


    _ElementMap = {
        __Anomalia.name() : __Anomalia
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Anomalias', Anomalias)


# Complex type RegistrosDocs with content type ELEMENT_ONLY
class RegistrosDocs (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RegistrosDocs')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}RegistroDoc uses Python identifier RegistroDoc
    __RegistroDoc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RegistroDoc'), 'RegistroDoc', '__httplocalhostelegibilidad_RegistrosDocs_httplocalhostelegibilidadRegistroDoc', True)

    
    RegistroDoc = property(__RegistroDoc.value, __RegistroDoc.set, None, None)


    _ElementMap = {
        __RegistroDoc.name() : __RegistroDoc
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'RegistrosDocs', RegistrosDocs)


# Complex type ModelosAparato with content type ELEMENT_ONLY
class ModelosAparato (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ModeloAparato uses Python identifier ModeloAparato
    __ModeloAparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModeloAparato'), 'ModeloAparato', '__httplocalhostelegibilidad_ModelosAparato_httplocalhostelegibilidadModeloAparato', True)

    
    ModeloAparato = property(__ModeloAparato.value, __ModeloAparato.set, None, None)


    _ElementMap = {
        __ModeloAparato.name() : __ModeloAparato
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ModelosAparato', ModelosAparato)


# Complex type MedidaResto with content type ELEMENT_ONLY
class MedidaResto (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MedidaResto')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ModelosAparato uses Python identifier ModelosAparato
    __ModelosAparato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato'), 'ModelosAparato', '__httplocalhostelegibilidad_MedidaResto_httplocalhostelegibilidadModelosAparato', False)

    
    ModelosAparato = property(__ModelosAparato.value, __ModelosAparato.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoEquipoMedida uses Python identifier TipoEquipoMedida
    __TipoEquipoMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), 'TipoEquipoMedida', '__httplocalhostelegibilidad_MedidaResto_httplocalhostelegibilidadTipoEquipoMedida', False)

    
    TipoEquipoMedida = property(__TipoEquipoMedida.value, __TipoEquipoMedida.set, None, None)

    
    # Element {http://localhost/elegibilidad}ICPAportadoInstalado uses Python identifier ICPAportadoInstalado
    __ICPAportadoInstalado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado'), 'ICPAportadoInstalado', '__httplocalhostelegibilidad_MedidaResto_httplocalhostelegibilidadICPAportadoInstalado', False)

    
    ICPAportadoInstalado = property(__ICPAportadoInstalado.value, __ICPAportadoInstalado.set, None, None)

    
    # Element {http://localhost/elegibilidad}ICPInstalacion uses Python identifier ICPInstalacion
    __ICPInstalacion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion'), 'ICPInstalacion', '__httplocalhostelegibilidad_MedidaResto_httplocalhostelegibilidadICPInstalacion', False)

    
    ICPInstalacion = property(__ICPInstalacion.value, __ICPInstalacion.set, None, None)

    
    # Element {http://localhost/elegibilidad}EquipoAportadoCliente uses Python identifier EquipoAportadoCliente
    __EquipoAportadoCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente'), 'EquipoAportadoCliente', '__httplocalhostelegibilidad_MedidaResto_httplocalhostelegibilidadEquipoAportadoCliente', False)

    
    EquipoAportadoCliente = property(__EquipoAportadoCliente.value, __EquipoAportadoCliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}EquipoInstaladoCliente uses Python identifier EquipoInstaladoCliente
    __EquipoInstaladoCliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente'), 'EquipoInstaladoCliente', '__httplocalhostelegibilidad_MedidaResto_httplocalhostelegibilidadEquipoInstaladoCliente', False)

    
    EquipoInstaladoCliente = property(__EquipoInstaladoCliente.value, __EquipoInstaladoCliente.set, None, None)


    _ElementMap = {
        __ModelosAparato.name() : __ModelosAparato,
        __TipoEquipoMedida.name() : __TipoEquipoMedida,
        __ICPAportadoInstalado.name() : __ICPAportadoInstalado,
        __ICPInstalacion.name() : __ICPInstalacion,
        __EquipoAportadoCliente.name() : __EquipoAportadoCliente,
        __EquipoInstaladoCliente.name() : __EquipoInstaladoCliente
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'MedidaResto', MedidaResto)


# Complex type OtrosConceptos with content type ELEMENT_ONLY
class OtrosConceptos (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OtrosConceptos')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Concepto uses Python identifier Concepto
    __Concepto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Concepto'), 'Concepto', '__httplocalhostelegibilidad_OtrosConceptos_httplocalhostelegibilidadConcepto', True)

    
    Concepto = property(__Concepto.value, __Concepto.set, None, None)


    _ElementMap = {
        __Concepto.name() : __Concepto
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'OtrosConceptos', OtrosConceptos)


# Complex type RegistroAutolecturas with content type ELEMENT_ONLY
class RegistroAutolecturas (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RegistroAutolecturas')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Autolecturas uses Python identifier Autolecturas
    __Autolecturas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Autolecturas'), 'Autolecturas', '__httplocalhostelegibilidad_RegistroAutolecturas_httplocalhostelegibilidadAutolecturas', True)

    
    Autolecturas = property(__Autolecturas.value, __Autolecturas.set, None, None)


    _ElementMap = {
        __Autolecturas.name() : __Autolecturas
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'RegistroAutolecturas', RegistroAutolecturas)


# Complex type ModeloAparato with content type ELEMENT_ONLY
class ModeloAparato (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModeloAparato')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ModeloMarca uses Python identifier ModeloMarca
    __ModeloMarca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModeloMarca'), 'ModeloMarca', '__httplocalhostelegibilidad_ModeloAparato_httplocalhostelegibilidadModeloMarca', False)

    
    ModeloMarca = property(__ModeloMarca.value, __ModeloMarca.set, None, None)

    
    # Element {http://localhost/elegibilidad}Tipo uses Python identifier Tipo
    __Tipo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Tipo'), 'Tipo', '__httplocalhostelegibilidad_ModeloAparato_httplocalhostelegibilidadTipo', False)

    
    Tipo = property(__Tipo.value, __Tipo.set, None, u'Tabla 24')

    
    # Element {http://localhost/elegibilidad}Marca uses Python identifier Marca
    __Marca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Marca'), 'Marca', '__httplocalhostelegibilidad_ModeloAparato_httplocalhostelegibilidadMarca', False)

    
    Marca = property(__Marca.value, __Marca.set, None, u'Tabla 25')


    _ElementMap = {
        __ModeloMarca.name() : __ModeloMarca,
        __Tipo.name() : __Tipo,
        __Marca.name() : __Marca
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ModeloAparato', ModeloAparato)


# Complex type CTD_ANON_27 with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ConceptoIVA uses Python identifier ConceptoIVA
    __ConceptoIVA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConceptoIVA'), 'ConceptoIVA', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadConceptoIVA', True)

    
    ConceptoIVA = property(__ConceptoIVA.value, __ConceptoIVA.set, None, u'Para facturar conceptos excepcionales que solo lleven aplicado IVA.')

    
    # Element {http://localhost/elegibilidad}EnergiaReactiva uses Python identifier EnergiaReactiva
    __EnergiaReactiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EnergiaReactiva'), 'EnergiaReactiva', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadEnergiaReactiva', False)

    
    EnergiaReactiva = property(__EnergiaReactiva.value, __EnergiaReactiva.set, None, None)

    
    # Element {http://localhost/elegibilidad}EnergiaActiva uses Python identifier EnergiaActiva
    __EnergiaActiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EnergiaActiva'), 'EnergiaActiva', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadEnergiaActiva', False)

    
    EnergiaActiva = property(__EnergiaActiva.value, __EnergiaActiva.set, None, None)

    
    # Element {http://localhost/elegibilidad}IVA uses Python identifier IVA
    __IVA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IVA'), 'IVA', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadIVA', False)

    
    IVA = property(__IVA.value, __IVA.set, None, None)

    
    # Element {http://localhost/elegibilidad}ImporteIntereses uses Python identifier ImporteIntereses
    __ImporteIntereses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteIntereses'), 'ImporteIntereses', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadImporteIntereses', False)

    
    ImporteIntereses = property(__ImporteIntereses.value, __ImporteIntereses.set, None, u'En los casos que se incluyan intereses de demora')

    
    # Element {http://localhost/elegibilidad}Medidas uses Python identifier Medidas
    __Medidas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Medidas'), 'Medidas', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadMedidas', True)

    
    Medidas = property(__Medidas.value, __Medidas.set, None, None)

    
    # Element {http://localhost/elegibilidad}IVAIGICReducido uses Python identifier IVAIGICReducido
    __IVAIGICReducido = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'IVAIGICReducido'), 'IVAIGICReducido', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadIVAIGICReducido', False)

    
    IVAIGICReducido = property(__IVAIGICReducido.value, __IVAIGICReducido.set, None, None)

    
    # Element {http://localhost/elegibilidad}ExcesoPotencia uses Python identifier ExcesoPotencia
    __ExcesoPotencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExcesoPotencia'), 'ExcesoPotencia', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadExcesoPotencia', False)

    
    ExcesoPotencia = property(__ExcesoPotencia.value, __ExcesoPotencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}DatosGeneralesFacturaATR uses Python identifier DatosGeneralesFacturaATR
    __DatosGeneralesFacturaATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFacturaATR'), 'DatosGeneralesFacturaATR', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadDatosGeneralesFacturaATR', False)

    
    DatosGeneralesFacturaATR = property(__DatosGeneralesFacturaATR.value, __DatosGeneralesFacturaATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}Potencia uses Python identifier Potencia
    __Potencia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Potencia'), 'Potencia', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadPotencia', False)

    
    Potencia = property(__Potencia.value, __Potencia.set, None, None)

    
    # Element {http://localhost/elegibilidad}ConceptoIEIVA uses Python identifier ConceptoIEIVA
    __ConceptoIEIVA = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ConceptoIEIVA'), 'ConceptoIEIVA', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadConceptoIEIVA', True)

    
    ConceptoIEIVA = property(__ConceptoIEIVA.value, __ConceptoIEIVA.set, None, u'Para facturar conceptos excepcionales que lleven aplicado impuesto el\xe9ctrico e IVA.')

    
    # Element {http://localhost/elegibilidad}ImpuestoElectrico uses Python identifier ImpuestoElectrico
    __ImpuestoElectrico = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImpuestoElectrico'), 'ImpuestoElectrico', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadImpuestoElectrico', False)

    
    ImpuestoElectrico = property(__ImpuestoElectrico.value, __ImpuestoElectrico.set, None, None)

    
    # Element {http://localhost/elegibilidad}Alquileres uses Python identifier Alquileres
    __Alquileres = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Alquileres'), 'Alquileres', '__httplocalhostelegibilidad_CTD_ANON_27_httplocalhostelegibilidadAlquileres', False)

    
    Alquileres = property(__Alquileres.value, __Alquileres.set, None, None)


    _ElementMap = {
        __ConceptoIVA.name() : __ConceptoIVA,
        __EnergiaReactiva.name() : __EnergiaReactiva,
        __EnergiaActiva.name() : __EnergiaActiva,
        __IVA.name() : __IVA,
        __ImporteIntereses.name() : __ImporteIntereses,
        __Medidas.name() : __Medidas,
        __IVAIGICReducido.name() : __IVAIGICReducido,
        __ExcesoPotencia.name() : __ExcesoPotencia,
        __DatosGeneralesFacturaATR.name() : __DatosGeneralesFacturaATR,
        __Potencia.name() : __Potencia,
        __ConceptoIEIVA.name() : __ConceptoIEIVA,
        __ImpuestoElectrico.name() : __ImpuestoElectrico,
        __Alquileres.name() : __Alquileres
    }
    _AttributeMap = {
        
    }



# Complex type OtrosDatosFactura with content type ELEMENT_ONLY
class OtrosDatosFactura (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OtrosDatosFactura')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}DireccionDestino uses Python identifier DireccionDestino
    __DireccionDestino = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionDestino'), 'DireccionDestino', '__httplocalhostelegibilidad_OtrosDatosFactura_httplocalhostelegibilidadDireccionDestino', False)

    
    DireccionDestino = property(__DireccionDestino.value, __DireccionDestino.set, None, None)

    
    # Element {http://localhost/elegibilidad}SociedadMercantilEmisora uses Python identifier SociedadMercantilEmisora
    __SociedadMercantilEmisora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SociedadMercantilEmisora'), 'SociedadMercantilEmisora', '__httplocalhostelegibilidad_OtrosDatosFactura_httplocalhostelegibilidadSociedadMercantilEmisora', False)

    
    SociedadMercantilEmisora = property(__SociedadMercantilEmisora.value, __SociedadMercantilEmisora.set, None, None)

    
    # Element {http://localhost/elegibilidad}SociedadMercantilDestino uses Python identifier SociedadMercantilDestino
    __SociedadMercantilDestino = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'SociedadMercantilDestino'), 'SociedadMercantilDestino', '__httplocalhostelegibilidad_OtrosDatosFactura_httplocalhostelegibilidadSociedadMercantilDestino', False)

    
    SociedadMercantilDestino = property(__SociedadMercantilDestino.value, __SociedadMercantilDestino.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionEmisora uses Python identifier DireccionEmisora
    __DireccionEmisora = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionEmisora'), 'DireccionEmisora', '__httplocalhostelegibilidad_OtrosDatosFactura_httplocalhostelegibilidadDireccionEmisora', False)

    
    DireccionEmisora = property(__DireccionEmisora.value, __DireccionEmisora.set, None, None)


    _ElementMap = {
        __DireccionDestino.name() : __DireccionDestino,
        __SociedadMercantilEmisora.name() : __SociedadMercantilEmisora,
        __SociedadMercantilDestino.name() : __SociedadMercantilDestino,
        __DireccionEmisora.name() : __DireccionEmisora
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'OtrosDatosFactura', OtrosDatosFactura)


# Complex type CTD_ANON_28 with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_CTD_ANON_28_httplocalhostelegibilidadPeriodo', True)

    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaDesde uses Python identifier FechaDesde
    __FechaDesde = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde'), 'FechaDesde', '__httplocalhostelegibilidad_CTD_ANON_28_httplocalhostelegibilidadFechaDesde', False)

    
    FechaDesde = property(__FechaDesde.value, __FechaDesde.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHasta uses Python identifier FechaHasta
    __FechaHasta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta'), 'FechaHasta', '__httplocalhostelegibilidad_CTD_ANON_28_httplocalhostelegibilidadFechaHasta', False)

    
    FechaHasta = property(__FechaHasta.value, __FechaHasta.set, None, None)


    _ElementMap = {
        __Periodo.name() : __Periodo,
        __FechaDesde.name() : __FechaDesde,
        __FechaHasta.name() : __FechaHasta
    }
    _AttributeMap = {
        
    }



# Complex type RegistroDoc with content type ELEMENT_ONLY
class RegistroDoc (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RegistroDoc')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}DireccionUrl uses Python identifier DireccionUrl
    __DireccionUrl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionUrl'), 'DireccionUrl', '__httplocalhostelegibilidad_RegistroDoc_httplocalhostelegibilidadDireccionUrl', False)

    
    DireccionUrl = property(__DireccionUrl.value, __DireccionUrl.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoDocAportado uses Python identifier TipoDocAportado
    __TipoDocAportado = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoDocAportado'), 'TipoDocAportado', '__httplocalhostelegibilidad_RegistroDoc_httplocalhostelegibilidadTipoDocAportado', False)

    
    TipoDocAportado = property(__TipoDocAportado.value, __TipoDocAportado.set, None, None)


    _ElementMap = {
        __DireccionUrl.name() : __DireccionUrl,
        __TipoDocAportado.name() : __TipoDocAportado
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'RegistroDoc', RegistroDoc)


# Complex type CTD_ANON_29 with content type SIMPLE
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = EnergiaFact
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is EnergiaFact
    
    # Attribute periodo uses Python identifier periodo
    __periodo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'periodo'), 'periodo', '__httplocalhostelegibilidad_CTD_ANON_29_periodo', pyxb.binding.datatypes.integer, required=True)
    
    periodo = property(__periodo.value, __periodo.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __periodo.name() : __periodo
    }



# Complex type Anomalia with content type ELEMENT_ONLY
class Anomalia (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Anomalia')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Descripcion uses Python identifier Descripcion
    __Descripcion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Descripcion'), 'Descripcion', '__httplocalhostelegibilidad_Anomalia_httplocalhostelegibilidadDescripcion', False)

    
    Descripcion = property(__Descripcion.value, __Descripcion.set, None, None)

    
    # Element {http://localhost/elegibilidad}CodAnomalia uses Python identifier CodAnomalia
    __CodAnomalia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CodAnomalia'), 'CodAnomalia', '__httplocalhostelegibilidad_Anomalia_httplocalhostelegibilidadCodAnomalia', False)

    
    CodAnomalia = property(__CodAnomalia.value, __CodAnomalia.set, None, None)


    _ElementMap = {
        __Descripcion.name() : __Descripcion,
        __CodAnomalia.name() : __CodAnomalia
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Anomalia', Anomalia)


# Complex type ComentariosPM with content type ELEMENT_ONLY
class ComentariosPM (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComentariosPM')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ComentarioPM uses Python identifier ComentarioPM
    __ComentarioPM = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ComentarioPM'), 'ComentarioPM', '__httplocalhostelegibilidad_ComentariosPM_httplocalhostelegibilidadComentarioPM', True)

    
    ComentarioPM = property(__ComentarioPM.value, __ComentarioPM.set, None, None)


    _ElementMap = {
        __ComentarioPM.name() : __ComentarioPM
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ComentariosPM', ComentariosPM)


# Complex type Reclamante with content type ELEMENT_ONLY
class Reclamante (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Reclamante')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Reclamante uses Python identifier Reclamante
    __Reclamante = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Reclamante'), 'Reclamante', '__httplocalhostelegibilidad_Reclamante_httplocalhostelegibilidadReclamante', False)

    
    Reclamante = property(__Reclamante.value, __Reclamante.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoReclamante uses Python identifier TipoReclamante
    __TipoReclamante = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoReclamante'), 'TipoReclamante', '__httplocalhostelegibilidad_Reclamante_httplocalhostelegibilidadTipoReclamante', False)

    
    TipoReclamante = property(__TipoReclamante.value, __TipoReclamante.set, None, None)


    _ElementMap = {
        __Reclamante.name() : __Reclamante,
        __TipoReclamante.name() : __TipoReclamante
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Reclamante', Reclamante)


# Complex type CTD_ANON_30 with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ImporteTotalEnergiaReactiva uses Python identifier ImporteTotalEnergiaReactiva
    __ImporteTotalEnergiaReactiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalEnergiaReactiva'), 'ImporteTotalEnergiaReactiva', '__httplocalhostelegibilidad_CTD_ANON_30_httplocalhostelegibilidadImporteTotalEnergiaReactiva', False)

    
    ImporteTotalEnergiaReactiva = property(__ImporteTotalEnergiaReactiva.value, __ImporteTotalEnergiaReactiva.set, None, None)

    
    # Element {http://localhost/elegibilidad}TerminoEnergiaReactiva uses Python identifier TerminoEnergiaReactiva
    __TerminoEnergiaReactiva = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TerminoEnergiaReactiva'), 'TerminoEnergiaReactiva', '__httplocalhostelegibilidad_CTD_ANON_30_httplocalhostelegibilidadTerminoEnergiaReactiva', True)

    
    TerminoEnergiaReactiva = property(__TerminoEnergiaReactiva.value, __TerminoEnergiaReactiva.set, None, None)


    _ElementMap = {
        __ImporteTotalEnergiaReactiva.name() : __ImporteTotalEnergiaReactiva,
        __TerminoEnergiaReactiva.name() : __TerminoEnergiaReactiva
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_31 with content type SIMPLE
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = Importe
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is Importe

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_32 with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}FechaBOE uses Python identifier FechaBOE
    __FechaBOE = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaBOE'), 'FechaBOE', '__httplocalhostelegibilidad_CTD_ANON_32_httplocalhostelegibilidadFechaBOE', False)

    
    FechaBOE = property(__FechaBOE.value, __FechaBOE.set, None, None)

    
    # Element {http://localhost/elegibilidad}DireccionSuministro uses Python identifier DireccionSuministro
    __DireccionSuministro = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DireccionSuministro'), 'DireccionSuministro', '__httplocalhostelegibilidad_CTD_ANON_32_httplocalhostelegibilidadDireccionSuministro', False)

    
    DireccionSuministro = property(__DireccionSuministro.value, __DireccionSuministro.set, None, None)

    
    # Element {http://localhost/elegibilidad}Cliente uses Python identifier Cliente
    __Cliente = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Cliente'), 'Cliente', '__httplocalhostelegibilidad_CTD_ANON_32_httplocalhostelegibilidadCliente', False)

    
    Cliente = property(__Cliente.value, __Cliente.set, None, None)

    
    # Element {http://localhost/elegibilidad}Contrato uses Python identifier Contrato
    __Contrato = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Contrato'), 'Contrato', '__httplocalhostelegibilidad_CTD_ANON_32_httplocalhostelegibilidadContrato', False)

    
    Contrato = property(__Contrato.value, __Contrato.set, None, None)

    
    # Element {http://localhost/elegibilidad}DatosGeneralesFactura uses Python identifier DatosGeneralesFactura
    __DatosGeneralesFactura = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFactura'), 'DatosGeneralesFactura', '__httplocalhostelegibilidad_CTD_ANON_32_httplocalhostelegibilidadDatosGeneralesFactura', False)

    
    DatosGeneralesFactura = property(__DatosGeneralesFactura.value, __DatosGeneralesFactura.set, None, None)

    
    # Element {http://localhost/elegibilidad}LineaNegocio uses Python identifier LineaNegocio
    __LineaNegocio = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LineaNegocio'), 'LineaNegocio', '__httplocalhostelegibilidad_CTD_ANON_32_httplocalhostelegibilidadLineaNegocio', False)

    
    LineaNegocio = property(__LineaNegocio.value, __LineaNegocio.set, None, u'Tabla 5')


    _ElementMap = {
        __FechaBOE.name() : __FechaBOE,
        __DireccionSuministro.name() : __DireccionSuministro,
        __Cliente.name() : __Cliente,
        __Contrato.name() : __Contrato,
        __DatosGeneralesFactura.name() : __DatosGeneralesFactura,
        __LineaNegocio.name() : __LineaNegocio
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_33 with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}TextoAnomalia uses Python identifier TextoAnomalia
    __TextoAnomalia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TextoAnomalia'), 'TextoAnomalia', '__httplocalhostelegibilidad_CTD_ANON_33_httplocalhostelegibilidadTextoAnomalia', False)

    
    TextoAnomalia = property(__TextoAnomalia.value, __TextoAnomalia.set, None, None)

    
    # Element {http://localhost/elegibilidad}TipoAnomalia uses Python identifier TipoAnomalia
    __TipoAnomalia = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'TipoAnomalia'), 'TipoAnomalia', '__httplocalhostelegibilidad_CTD_ANON_33_httplocalhostelegibilidadTipoAnomalia', False)

    
    TipoAnomalia = property(__TipoAnomalia.value, __TipoAnomalia.set, None, u'Tabla 45')


    _ElementMap = {
        __TextoAnomalia.name() : __TextoAnomalia,
        __TipoAnomalia.name() : __TipoAnomalia
    }
    _AttributeMap = {
        
    }



# Complex type ExcesosPotAFacturar with content type ELEMENT_ONLY
class ExcesosPotAFacturar (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExcesosPotAFacturar')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}ExcesoPotAFacturar uses Python identifier ExcesoPotAFacturar
    __ExcesoPotAFacturar = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ExcesoPotAFacturar'), 'ExcesoPotAFacturar', '__httplocalhostelegibilidad_ExcesosPotAFacturar_httplocalhostelegibilidadExcesoPotAFacturar', True)

    
    ExcesoPotAFacturar = property(__ExcesoPotAFacturar.value, __ExcesoPotAFacturar.set, None, None)


    _ElementMap = {
        __ExcesoPotAFacturar.name() : __ExcesoPotAFacturar
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ExcesosPotAFacturar', ExcesosPotAFacturar)


# Complex type CTD_ANON_34 with content type SIMPLE
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = Potencia
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is Potencia
    
    # Attribute Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_CTD_ANON_34_Periodo', pyxb.binding.datatypes.integer, required=True)
    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __Periodo.name() : __Periodo
    }



# Complex type PuntosDeMedida with content type ELEMENT_ONLY
class PuntosDeMedida (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PuntosDeMedida')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}PuntoDeMedida uses Python identifier PuntoDeMedida
    __PuntoDeMedida = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PuntoDeMedida'), 'PuntoDeMedida', '__httplocalhostelegibilidad_PuntosDeMedida_httplocalhostelegibilidadPuntoDeMedida', True)

    
    PuntoDeMedida = property(__PuntoDeMedida.value, __PuntoDeMedida.set, None, None)


    _ElementMap = {
        __PuntoDeMedida.name() : __PuntoDeMedida
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'PuntosDeMedida', PuntosDeMedida)


# Complex type ModeloAparatoAutolecturas with content type ELEMENT_ONLY
class ModeloAparatoAutolecturas (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModeloAparatoAutolecturas')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}NumeroSerie uses Python identifier NumeroSerie
    __NumeroSerie = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), 'NumeroSerie', '__httplocalhostelegibilidad_ModeloAparatoAutolecturas_httplocalhostelegibilidadNumeroSerie', False)

    
    NumeroSerie = property(__NumeroSerie.value, __NumeroSerie.set, None, None)

    
    # Element {http://localhost/elegibilidad}Tipo uses Python identifier Tipo
    __Tipo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Tipo'), 'Tipo', '__httplocalhostelegibilidad_ModeloAparatoAutolecturas_httplocalhostelegibilidadTipo', False)

    
    Tipo = property(__Tipo.value, __Tipo.set, None, u'Tabla 24')

    
    # Element {http://localhost/elegibilidad}Marca uses Python identifier Marca
    __Marca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Marca'), 'Marca', '__httplocalhostelegibilidad_ModeloAparatoAutolecturas_httplocalhostelegibilidadMarca', False)

    
    Marca = property(__Marca.value, __Marca.set, None, u'Tabla 25')

    
    # Element {http://localhost/elegibilidad}ModeloMarca uses Python identifier ModeloMarca
    __ModeloMarca = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ModeloMarca'), 'ModeloMarca', '__httplocalhostelegibilidad_ModeloAparatoAutolecturas_httplocalhostelegibilidadModeloMarca', False)

    
    ModeloMarca = property(__ModeloMarca.value, __ModeloMarca.set, None, None)


    _ElementMap = {
        __NumeroSerie.name() : __NumeroSerie,
        __Tipo.name() : __Tipo,
        __Marca.name() : __Marca,
        __ModeloMarca.name() : __ModeloMarca
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'ModeloAparatoAutolecturas', ModeloAparatoAutolecturas)


# Complex type CTD_ANON_35 with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}Periodo uses Python identifier Periodo
    __Periodo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), 'Periodo', '__httplocalhostelegibilidad_CTD_ANON_35_httplocalhostelegibilidadPeriodo', True)

    
    Periodo = property(__Periodo.value, __Periodo.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaDesde uses Python identifier FechaDesde
    __FechaDesde = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde'), 'FechaDesde', '__httplocalhostelegibilidad_CTD_ANON_35_httplocalhostelegibilidadFechaDesde', False)

    
    FechaDesde = property(__FechaDesde.value, __FechaDesde.set, None, None)

    
    # Element {http://localhost/elegibilidad}FechaHasta uses Python identifier FechaHasta
    __FechaHasta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta'), 'FechaHasta', '__httplocalhostelegibilidad_CTD_ANON_35_httplocalhostelegibilidadFechaHasta', False)

    
    FechaHasta = property(__FechaHasta.value, __FechaHasta.set, None, None)


    _ElementMap = {
        __Periodo.name() : __Periodo,
        __FechaDesde.name() : __FechaDesde,
        __FechaHasta.name() : __FechaHasta
    }
    _AttributeMap = {
        
    }



# Complex type Facturas with content type ELEMENT_ONLY
class Facturas (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Facturas')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://localhost/elegibilidad}RegistroFin uses Python identifier RegistroFin
    __RegistroFin = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'RegistroFin'), 'RegistroFin', '__httplocalhostelegibilidad_Facturas_httplocalhostelegibilidadRegistroFin', False)

    
    RegistroFin = property(__RegistroFin.value, __RegistroFin.set, None, None)

    
    # Element {http://localhost/elegibilidad}FacturaATR uses Python identifier FacturaATR
    __FacturaATR = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FacturaATR'), 'FacturaATR', '__httplocalhostelegibilidad_Facturas_httplocalhostelegibilidadFacturaATR', True)

    
    FacturaATR = property(__FacturaATR.value, __FacturaATR.set, None, None)

    
    # Element {http://localhost/elegibilidad}OtrasFacturas uses Python identifier OtrasFacturas
    __OtrasFacturas = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OtrasFacturas'), 'OtrasFacturas', '__httplocalhostelegibilidad_Facturas_httplocalhostelegibilidadOtrasFacturas', True)

    
    OtrasFacturas = property(__OtrasFacturas.value, __OtrasFacturas.set, None, None)


    _ElementMap = {
        __RegistroFin.name() : __RegistroFin,
        __FacturaATR.name() : __FacturaATR,
        __OtrasFacturas.name() : __OtrasFacturas
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Facturas', Facturas)


MensajeFacturacion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MensajeFacturacion'), CTD_ANON_23)
Namespace.addCategoryObject('elementBinding', MensajeFacturacion.name().localName(), MensajeFacturacion)



IdCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identificador'), X9, scope=IdCliente))

IdCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoCIFNIF'), TipoIdentificador, scope=IdCliente, documentation=u'Tabla 6'))
IdCliente._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IdCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoCIFNIF')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(IdCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identificador')), min_occurs=1, max_occurs=1)
    )
IdCliente._ContentModel = pyxb.binding.content.ParticleModel(IdCliente._GroupModel, min_occurs=1, max_occurs=1)



MedidaAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TextoAnomalia'), X250, scope=MedidaAparato))

MedidaAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoDH'), TipoDH, scope=MedidaAparato))

MedidaAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Anomalia'), AnomaliaMedida, scope=MedidaAparato))

MedidaAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagnitudMedida'), MagnitudMedida, scope=MedidaAparato))

MedidaAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Procedencia'), Procedencia, scope=MedidaAparato))

MedidaAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), TipoCodigoPeriodoDH, scope=MedidaAparato))

MedidaAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LecturaAnterior'), DecimalS10V2, scope=MedidaAparato))
MedidaAparato._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(MedidaAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoDH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Periodo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagnitudMedida')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Procedencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LecturaAnterior')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Anomalia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TextoAnomalia')), min_occurs=0L, max_occurs=1)
    )
MedidaAparato._ContentModel = pyxb.binding.content.ParticleModel(MedidaAparato._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteFacturacionAlquileres'), STD_ANON_2, scope=CTD_ANON, documentation=u'Suma de alquileres de equipos asociados al CUPS.'))
CTD_ANON._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteFacturacionAlquileres')), min_occurs=1, max_occurs=1)
    )
CTD_ANON._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON._GroupModel, min_occurs=1, max_occurs=1)



IdContrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodContrato'), CodigoContrato, scope=IdContrato))
IdContrato._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IdContrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodContrato')), min_occurs=1, max_occurs=1)
    )
IdContrato._ContentModel = pyxb.binding.content.ParticleModel(IdContrato._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrecioPotencia'), STD_ANON, scope=CTD_ANON_))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciaContratada'), STD_ANON_43, scope=CTD_ANON_, documentation=u'En watios'))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciaAFacturar'), STD_ANON_11, scope=CTD_ANON_, documentation=u'Potencia a facturar calculada en funci\xf3n de la potencia contratada. En Watios'))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciaMaxDemandada'), STD_ANON_25, scope=CTD_ANON_, documentation=u' En watios'))
CTD_ANON_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciaContratada')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciaMaxDemandada')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciaAFacturar')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrecioPotencia')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_._GroupModel, min_occurs=1, max_occurs=1)



ClienteSinTelefono._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TitularContratoVsTitularPago'), Indicativo, scope=ClienteSinTelefono))

ClienteSinTelefono._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), IdCliente, scope=ClienteSinTelefono))

ClienteSinTelefono._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), NombreCliente, scope=ClienteSinTelefono))
ClienteSinTelefono._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ClienteSinTelefono._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ClienteSinTelefono._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nombre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ClienteSinTelefono._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TitularContratoVsTitularPago')), min_occurs=0L, max_occurs=1)
    )
ClienteSinTelefono._ContentModel = pyxb.binding.content.ParticleModel(ClienteSinTelefono._GroupModel, min_occurs=1, max_occurs=1)



TipoIVAIGIC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Importe'), STD_ANON_10, scope=TipoIVAIGIC, documentation=u'En Canarias se informar\xe1 IGIC; en el resto, IVA.'))

TipoIVAIGIC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseImponible'), STD_ANON_42, scope=TipoIVAIGIC, documentation=u'En Canarias se informar\xe1 IGIC; en el resto, IVA.'))

TipoIVAIGIC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Porcentaje'), STD_ANON_22, scope=TipoIVAIGIC, documentation=u'En Canarias se informar\xe1 IGIC; en el resto, IVA.'))
TipoIVAIGIC._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(TipoIVAIGIC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BaseImponible')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoIVAIGIC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Porcentaje')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoIVAIGIC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Importe')), min_occurs=1, max_occurs=1)
    )
TipoIVAIGIC._ContentModel = pyxb.binding.content.ParticleModel(TipoIVAIGIC._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrecioEnergiaReactiva'), STD_ANON_31, scope=CTD_ANON_2))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValorEnergiaReactiva'), STD_ANON_45, scope=CTD_ANON_2))
CTD_ANON_2._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValorEnergiaReactiva')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrecioEnergiaReactiva')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_2._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_2._GroupModel, min_occurs=1, max_occurs=1)



ReactivasAFacturar._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReactivaAFacturar'), CTD_ANON_13, scope=ReactivasAFacturar))
ReactivasAFacturar._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ReactivasAFacturar._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReactivaAFacturar')), min_occurs=1, max_occurs=6L)
    )
ReactivasAFacturar._ContentModel = pyxb.binding.content.ParticleModel(ReactivasAFacturar._GroupModel, min_occurs=1, max_occurs=1)



ImportesTerminoEnergia._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTerminoEnergia'), CTD_ANON_31, scope=ImportesTerminoEnergia))
ImportesTerminoEnergia._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ImportesTerminoEnergia._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTerminoEnergia')), min_occurs=1, max_occurs=6L)
    )
ImportesTerminoEnergia._ContentModel = pyxb.binding.content.ParticleModel(ImportesTerminoEnergia._GroupModel, min_occurs=1, max_occurs=1)



IdReclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identificador'), X9, scope=IdReclamante))

IdReclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoCIFNIF'), TipoIdentificador, scope=IdReclamante, documentation=u'Tabla 6'))
IdReclamante._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IdReclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoCIFNIF')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(IdReclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identificador')), min_occurs=1, max_occurs=1)
    )
IdReclamante._ContentModel = pyxb.binding.content.ParticleModel(IdReclamante._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroMeses'), STD_ANON_56, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeFactura'), pyxb.binding.datatypes.date, scope=CTD_ANON_3))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaFactura'), pyxb.binding.datatypes.date, scope=CTD_ANON_3))
CTD_ANON_3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroMeses')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_3._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_3._GroupModel, min_occurs=1, max_occurs=1)



TipoLimiteIntervaloLectura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Lectura'), STD_ANON_26, scope=TipoLimiteIntervaloLectura))

TipoLimiteIntervaloLectura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHora'), pyxb.binding.datatypes.dateTime, scope=TipoLimiteIntervaloLectura))

TipoLimiteIntervaloLectura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Procedencia'), Procedencia, scope=TipoLimiteIntervaloLectura, documentation=u'Tabla 44'))
TipoLimiteIntervaloLectura._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(TipoLimiteIntervaloLectura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHora')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoLimiteIntervaloLectura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Procedencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoLimiteIntervaloLectura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Lectura')), min_occurs=1, max_occurs=1)
    )
TipoLimiteIntervaloLectura._ContentModel = pyxb.binding.content.ParticleModel(TipoLimiteIntervaloLectura._GroupModel, min_occurs=1, max_occurs=1)



Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaSolicitud'), pyxb.binding.datatypes.dateTime, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Version'), Version, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoREEEmpresaEmisora'), Agente, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoDelProceso'), CodigoDelProceso, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoREEEmpresaDestino'), Agente, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoDeSolicitud'), CodigoDeSolicitud, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecuencialDeSolicitud'), SecuencialDeSolicitud, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Codigo'), Codigo, scope=Cabecera))

Cabecera._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoDePaso'), CodigoDePaso, scope=Cabecera))
Cabecera._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoREEEmpresaEmisora')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoREEEmpresaDestino')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoDelProceso')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoDePaso')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoDeSolicitud')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SecuencialDeSolicitud')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Codigo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaSolicitud')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cabecera._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Version')), min_occurs=1, max_occurs=1)
    )
Cabecera._ContentModel = pyxb.binding.content.ParticleModel(Cabecera._GroupModel, min_occurs=1, max_occurs=1)



EnergiasAFacturar._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EnergiaAFacturar'), CTD_ANON_29, scope=EnergiasAFacturar))
EnergiasAFacturar._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(EnergiasAFacturar._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EnergiaAFacturar')), min_occurs=1, max_occurs=6L)
    )
EnergiasAFacturar._ContentModel = pyxb.binding.content.ParticleModel(EnergiasAFacturar._GroupModel, min_occurs=1, max_occurs=1)



NombreCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SegundoApellido'), X45, scope=NombreCliente))

NombreCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NombreDePila'), X45, scope=NombreCliente))

NombreCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RazonSocial'), X45, scope=NombreCliente))

NombreCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrimerApellido'), X45, scope=NombreCliente))
NombreCliente._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NombreCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NombreDePila')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NombreCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrimerApellido')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NombreCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SegundoApellido')), min_occurs=0L, max_occurs=1)
    )
NombreCliente._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(NombreCliente._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NombreCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RazonSocial')), min_occurs=1, max_occurs=1)
    )
NombreCliente._ContentModel = pyxb.binding.content.ParticleModel(NombreCliente._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IVAIGICReducido'), TipoIVAIGIC, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesOtrasFacturas'), CTD_ANON_32, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Concepto'), CTD_ANON_11, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IVA'), TipoIVAIGIC, scope=CTD_ANON_4))
CTD_ANON_4._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesOtrasFacturas')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Concepto')), min_occurs=1, max_occurs=12L),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IVA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IVAIGICReducido')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_4._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel, min_occurs=1, max_occurs=1)



DireccionCorrespondencia._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Direccion'), Direccion, scope=DireccionCorrespondencia))

DireccionCorrespondencia._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Indicador'), STD_ANON_41, scope=DireccionCorrespondencia))
DireccionCorrespondencia._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DireccionCorrespondencia._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Indicador')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionCorrespondencia._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Direccion')), min_occurs=0L, max_occurs=1)
    )
DireccionCorrespondencia._ContentModel = pyxb.binding.content.ParticleModel(DireccionCorrespondencia._GroupModel, min_occurs=1, max_occurs=1)



TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalFactura'), STD_ANON_29, scope=TipoDatosGeneralesFactura))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroFacturaRectificada'), STD_ANON_51, scope=TipoDatosGeneralesFactura, documentation=u'N\xfamero de factura a la que rectifica.'))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoMoneda'), TipoMoneda, scope=TipoDatosGeneralesFactura, documentation=u'Tabla 104 (01-Pesetas, 02-Euros)'))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaFactura'), pyxb.binding.datatypes.date, scope=TipoDatosGeneralesFactura, documentation=u'Fecha oficial de la factura (albar\xe1n, en su caso)'))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SaldoFactura'), STD_ANON_28, scope=TipoDatosGeneralesFactura, documentation=u'Para los casos de rectificaciones'))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Observaciones'), STD_ANON_59, scope=TipoDatosGeneralesFactura, documentation=u'Comentarios a la factura, como p.e. nro. Expte anormalidad '))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroFactura'), STD_ANON_37, scope=TipoDatosGeneralesFactura, documentation=u'N\xfamero de la factura (albar\xe1n, en su caso)'))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SaldoCobro'), STD_ANON_12, scope=TipoDatosGeneralesFactura, documentation=u' Saldo cobro '))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoFiscalFactura'), STD_ANON_9, scope=TipoDatosGeneralesFactura, documentation=u'N\xfamero de IVA'))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoFactura'), TipoFactura, scope=TipoDatosGeneralesFactura, documentation=u'Tabla 101 (Normal, fraude...)'))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CIFEmisora'), STD_ANON_20, scope=TipoDatosGeneralesFactura))

TipoDatosGeneralesFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicativoFacturaRectificadora'), TipoFacturaRectificadora, scope=TipoDatosGeneralesFactura, documentation=u'Tabla 102 (N-Normal, R-Rectificadora , A-Anuladora, B-Anuladora con sustituyente)'))
TipoDatosGeneralesFactura._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicativoFacturaRectificadora')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroFacturaRectificada')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CIFEmisora')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoFiscalFactura')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observaciones')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SaldoFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SaldoCobro')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoMoneda')), min_occurs=1, max_occurs=1)
    )
TipoDatosGeneralesFactura._ContentModel = pyxb.binding.content.ParticleModel(TipoDatosGeneralesFactura._GroupModel, min_occurs=1, max_occurs=1)



ContactoConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NombreDePila'), X45, scope=ContactoConDireccion))

ContactoConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrimerApellido'), X45, scope=ContactoConDireccion))

ContactoConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SegundoApellido'), X45, scope=ContactoConDireccion))

ContactoConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), TelefonoInternacional, scope=ContactoConDireccion))

ContactoConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicadorTipoDireccion'), STD_ANON_38, scope=ContactoConDireccion))

ContactoConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Direccion'), Direccion, scope=ContactoConDireccion))
ContactoConDireccion._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ContactoConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NombreDePila')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContactoConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrimerApellido')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContactoConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SegundoApellido')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContactoConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telefono')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContactoConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicadorTipoDireccion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContactoConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Direccion')), min_occurs=0L, max_occurs=1)
    )
ContactoConDireccion._ContentModel = pyxb.binding.content.ParticleModel(ContactoConDireccion._GroupModel, min_occurs=1, max_occurs=1)



Contacto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), TelefonoInternacional, scope=Contacto))

Contacto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), NombreCliente, scope=Contacto))
Contacto._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Contacto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nombre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contacto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telefono')), min_occurs=1, max_occurs=1)
    )
Contacto._ContentModel = pyxb.binding.content.ParticleModel(Contacto._GroupModel, min_occurs=1, max_occurs=1)



MedidasAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Medida'), MedidaAparato, scope=MedidasAparato))
MedidasAparato._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(MedidasAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Medida')), min_occurs=1, max_occurs=None)
    )
MedidasAparato._ContentModel = pyxb.binding.content.ParticleModel(MedidasAparato._GroupModel, min_occurs=1, max_occurs=1)



CondicionesContractuales._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciasMaximas'), Potencias, scope=CondicionesContractuales))

CondicionesContractuales._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR'), Tarifa, scope=CondicionesContractuales))

CondicionesContractuales._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas'), Potencias, scope=CondicionesContractuales))
CondicionesContractuales._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CondicionesContractuales._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractuales._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractuales._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciasMaximas')), min_occurs=0L, max_occurs=1)
    )
CondicionesContractuales._ContentModel = pyxb.binding.content.ParticleModel(CondicionesContractuales._GroupModel, min_occurs=1, max_occurs=1)



Aparatos._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Aparato'), Aparato, scope=Aparatos))
Aparatos._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Aparatos._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Aparato')), min_occurs=1, max_occurs=40L)
    )
Aparatos._ContentModel = pyxb.binding.content.ParticleModel(Aparatos._GroupModel, min_occurs=1, max_occurs=1)



ImportesTerminoPotencia._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTerminoPotencia'), CTD_ANON_9, scope=ImportesTerminoPotencia))
ImportesTerminoPotencia._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ImportesTerminoPotencia._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTerminoPotencia')), min_occurs=1, max_occurs=6L)
    )
ImportesTerminoPotencia._ContentModel = pyxb.binding.content.ParticleModel(ImportesTerminoPotencia._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValorExcesoPotencia'), STD_ANON_53, scope=CTD_ANON_6, documentation=u'En Watios'))
CTD_ANON_6._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValorExcesoPotencia')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_6._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_6._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Importe'), STD_ANON_16, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BaseImponible'), STD_ANON_54, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Coeficiente'), STD_ANON_48, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Porcentaje'), STD_ANON_52, scope=CTD_ANON_7))
CTD_ANON_7._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BaseImponible')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Coeficiente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Porcentaje')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Importe')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_7._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_7._GroupModel, min_occurs=1, max_occurs=1)



TelefonoInternacional._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Numero'), Decimal9, scope=TelefonoInternacional))

TelefonoInternacional._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrefijoPais'), Decimal2, scope=TelefonoInternacional))
TelefonoInternacional._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(TelefonoInternacional._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrefijoPais')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TelefonoInternacional._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Numero')), min_occurs=1, max_occurs=1)
    )
TelefonoInternacional._ContentModel = pyxb.binding.content.ParticleModel(TelefonoInternacional._GroupModel, min_occurs=1, max_occurs=1)



RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Energias'), EnergiasAFacturar, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeHistorico'), pyxb.binding.datatypes.date, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reactivas'), ReactivasAFacturar, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InicioRefacturacion'), pyxb.binding.datatypes.date, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FinRefacturacion'), pyxb.binding.datatypes.date, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OtrosConceptos'), OtrosConceptos, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Importes'), Importes, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaHistorico'), pyxb.binding.datatypes.date, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoTarifa'), Tarifa, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExcesosPotencia'), ExcesosPotAFacturar, scope=RegistroValAnomalias))

RegistroValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Potencias'), PotenciasAFacturar, scope=RegistroValAnomalias))
RegistroValAnomalias._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InicioRefacturacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FinRefacturacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeHistorico')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaHistorico')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoTarifa')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Potencias')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Energias')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reactivas')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExcesosPotencia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OtrosConceptos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Importes')), min_occurs=0L, max_occurs=1)
    )
RegistroValAnomalias._ContentModel = pyxb.binding.content.ParticleModel(RegistroValAnomalias._GroupModel, min_occurs=1, max_occurs=1)



Potencias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Potencia'), CTD_ANON_34, scope=Potencias))
Potencias._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Potencias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Potencia')), min_occurs=1, max_occurs=10L)
    )
Potencias._ContentModel = pyxb.binding.content.ParticleModel(Potencias._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Aparato'), CTD_ANON_10, scope=CTD_ANON_8))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodUnificadoPuntoSuministro'), STD_ANON_50, scope=CTD_ANON_8))
CTD_ANON_8._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodUnificadoPuntoSuministro')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Aparato')), min_occurs=1, max_occurs=10L)
    )
CTD_ANON_8._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_8._GroupModel, min_occurs=1, max_occurs=1)



CondicionesContractuales2n._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas'), Potencias, scope=CondicionesContractuales2n))

CondicionesContractuales2n._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR'), Tarifa, scope=CondicionesContractuales2n))
CondicionesContractuales2n._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CondicionesContractuales2n._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractuales2n._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas')), min_occurs=1, max_occurs=1)
    )
CondicionesContractuales2n._ContentModel = pyxb.binding.content.ParticleModel(CondicionesContractuales2n._GroupModel, min_occurs=1, max_occurs=1)



CuentaBancaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cuenta'), Decimal10, scope=CuentaBancaria))

CuentaBancaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Banco'), Decimal4, scope=CuentaBancaria))

CuentaBancaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Sucursal'), Decimal4, scope=CuentaBancaria))

CuentaBancaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DC'), STD_ANON_47, scope=CuentaBancaria))
CuentaBancaria._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CuentaBancaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Banco')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CuentaBancaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Sucursal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CuentaBancaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DC')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CuentaBancaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cuenta')), min_occurs=1, max_occurs=1)
    )
CuentaBancaria._ContentModel = pyxb.binding.content.ParticleModel(CuentaBancaria._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Integrador'), CTD_ANON_19, scope=CTD_ANON_10))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Tipo'), TipoAparato, scope=CTD_ANON_10, documentation=u'Tabla 24'))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Marca'), MarcaAparato, scope=CTD_ANON_10, documentation=u'Tabla 25'))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoDH'), TipoDH, scope=CTD_ANON_10, documentation=u'Tabla 35'))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), STD_ANON_35, scope=CTD_ANON_10))
CTD_ANON_10._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Tipo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Marca')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoDH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Integrador')), min_occurs=1, max_occurs=100L)
    )
CTD_ANON_10._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_10._GroupModel, min_occurs=1, max_occurs=1)



LocalizacionPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), Decimal7, scope=LocalizacionPS))

LocalizacionPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Poblacion'), Decimal7, scope=LocalizacionPS))

LocalizacionPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoVia'), TipoVia, scope=LocalizacionPS))

LocalizacionPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Provincia'), Decimal2, scope=LocalizacionPS))

LocalizacionPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodPostal'), Decimal5, scope=LocalizacionPS))

LocalizacionPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Pais'), X25, scope=LocalizacionPS))
LocalizacionPS._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LocalizacionPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Pais')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalizacionPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Provincia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalizacionPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Municipio')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalizacionPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Poblacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalizacionPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoVia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalizacionPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodPostal')), min_occurs=0L, max_occurs=1)
    )
LocalizacionPS._ContentModel = pyxb.binding.content.ParticleModel(LocalizacionPS._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalConcepto'), STD_ANON_23, scope=CTD_ANON_11))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoConcepto'), TipoConcepto, scope=CTD_ANON_11, documentation=u'Tabla 103'))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UnidadesConcepto'), STD_ANON_55, scope=CTD_ANON_11, documentation=u'P.e., en contrataci\xf3n kW a contratar'))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteUnidadConcepto'), STD_ANON_8, scope=CTD_ANON_11, documentation=u'P.e., precio en tarifa del kW contratado'))
CTD_ANON_11._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoConcepto')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'UnidadesConcepto')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteUnidadConcepto')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalConcepto')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_11._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel, min_occurs=1, max_occurs=1)



ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), DireccionCorrespondencia, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), Decimal2, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), TipoContrato, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConsumoAnualEstimado'), Decimal13, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales'), CondicionesContractuales, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contacto'), Contacto, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), IdContrato, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), CuentaBancaria, scope=ContratoConModificacion))

ContratoConModificacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), pyxb.binding.datatypes.date, scope=ContratoConModificacion))
ContratoConModificacion._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Duracion')), min_occurs=1, max_occurs=1)
    )
ContratoConModificacion._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdContrato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConsumoAnualEstimado')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contacto')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoConModificacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria')), min_occurs=0L, max_occurs=1)
    )
ContratoConModificacion._ContentModel = pyxb.binding.content.ParticleModel(ContratoConModificacion._GroupModel, min_occurs=1, max_occurs=1)



DatosReclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), TelefonoInternacional, scope=DatosReclamante))

DatosReclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdReclamante'), IdReclamante, scope=DatosReclamante))

DatosReclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), TelefonoInternacional, scope=DatosReclamante))

DatosReclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), NombreCliente, scope=DatosReclamante))
DatosReclamante._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosReclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdReclamante')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nombre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fax')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telefono')), min_occurs=0L, max_occurs=1)
    )
DatosReclamante._ContentModel = pyxb.binding.content.ParticleModel(DatosReclamante._GroupModel, min_occurs=1, max_occurs=1)



ComentarioPM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Texto'), X120, scope=ComentarioPM))
ComentarioPM._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ComentarioPM._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Texto')), min_occurs=1, max_occurs=1)
    )
ComentarioPM._ContentModel = pyxb.binding.content.ParticleModel(ComentarioPM._GroupModel, min_occurs=1, max_occurs=1)



DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), X10, scope=DatosAparatoNoICP))

DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FuncionAparato'), FuncionAparato, scope=DatosAparatoNoICP))

DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumIntegradores'), Decimal2, scope=DatosAparatoNoICP))

DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConstanteEnergia'), DecimalS9V3, scope=DatosAparatoNoICP))

DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMaximetro'), DecimalS9V3, scope=DatosAparatoNoICP))

DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RuedasEnteras'), Decimal2, scope=DatosAparatoNoICP))

DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RuedasDecimales'), Decimal2, scope=DatosAparatoNoICP))

DatosAparatoNoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PeriodoFabricacion'), Decimal4, scope=DatosAparatoNoICP))
DatosAparatoNoICP._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PeriodoFabricacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FuncionAparato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumIntegradores')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConstanteEnergia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMaximetro')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RuedasEnteras')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoNoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RuedasDecimales')), min_occurs=1, max_occurs=1)
    )
DatosAparatoNoICP._ContentModel = pyxb.binding.content.ParticleModel(DatosAparatoNoICP._GroupModel, min_occurs=1, max_occurs=1)



DatosReclamacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimientoSolicitud'), IndicativoARO, scope=DatosReclamacion))

DatosReclamacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoReclamacion'), TipoReclamacion, scope=DatosReclamacion))

DatosReclamacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaIncidencia'), pyxb.binding.datatypes.date, scope=DatosReclamacion))

DatosReclamacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comentario'), X400, scope=DatosReclamacion))

DatosReclamacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndemnizacionSolicitada'), X13, scope=DatosReclamacion))

DatosReclamacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaLimiteLegal'), pyxb.binding.datatypes.date, scope=DatosReclamacion))
DatosReclamacion._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosReclamacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimientoSolicitud')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoReclamacion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaIncidencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comentario')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndemnizacionSolicitada')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaLimiteLegal')), min_occurs=0L, max_occurs=1)
    )
DatosReclamacion._ContentModel = pyxb.binding.content.ParticleModel(DatosReclamacion._GroupModel, min_occurs=1, max_occurs=1)



TipoDireccionSuministro._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DirSuministro'), STD_ANON_3, scope=TipoDireccionSuministro))

TipoDireccionSuministro._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CUPS'), CUPS, scope=TipoDireccionSuministro))

TipoDireccionSuministro._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), Decimal7, scope=TipoDireccionSuministro))
TipoDireccionSuministro._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(TipoDireccionSuministro._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CUPS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDireccionSuministro._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Municipio')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(TipoDireccionSuministro._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DirSuministro')), min_occurs=1, max_occurs=1)
    )
TipoDireccionSuministro._ContentModel = pyxb.binding.content.ParticleModel(TipoDireccionSuministro._GroupModel, min_occurs=1, max_occurs=1)



DatosAceptacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaUltimaLectura'), pyxb.binding.datatypes.date, scope=DatosAceptacion))

DatosAceptacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaAceptacion'), pyxb.binding.datatypes.date, scope=DatosAceptacion))

DatosAceptacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciaActual'), Potencia, scope=DatosAceptacion))

DatosAceptacion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ActuacionCampo'), Indicativo, scope=DatosAceptacion))
DatosAceptacion._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosAceptacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaAceptacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAceptacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciaActual')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAceptacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ActuacionCampo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAceptacion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaUltimaLectura')), min_occurs=1, max_occurs=1)
    )
DatosAceptacion._ContentModel = pyxb.binding.content.ParticleModel(DatosAceptacion._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalEnergiaActiva'), STD_ANON_4, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TerminoEnergiaActiva'), CTD_ANON_35, scope=CTD_ANON_14))
CTD_ANON_14._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TerminoEnergiaActiva')), min_occurs=1, max_occurs=8L),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalEnergiaActiva')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_14._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel, min_occurs=1, max_occurs=1)



Cliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), TelefonoInternacional, scope=Cliente))

Cliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), IdCliente, scope=Cliente))

Cliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), NombreCliente, scope=Cliente))

Cliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), TelefonoInternacional, scope=Cliente))
Cliente._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nombre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fax')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telefono')), min_occurs=0L, max_occurs=1)
    )
Cliente._ContentModel = pyxb.binding.content.ParticleModel(Cliente._GroupModel, min_occurs=1, max_occurs=1)



RegistrosValAnomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistroValAnomalias'), RegistroValAnomalias, scope=RegistrosValAnomalias))
RegistrosValAnomalias._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RegistrosValAnomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistroValAnomalias')), min_occurs=1, max_occurs=None)
    )
RegistrosValAnomalias._ContentModel = pyxb.binding.content.ParticleModel(RegistrosValAnomalias._GroupModel, min_occurs=1, max_occurs=1)



Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Provincia'), Decimal2, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoAclaradorFinca'), TipoAclaradorFinca, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), Decimal7, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Piso'), Piso, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Poblacion'), Decimal7, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoVia'), TipoVia, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Escalera'), Escalera, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AclaradorFinca'), X40, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Puerta'), Puerta, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Calle'), X30, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodPostal'), Decimal5, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroFinca'), X5, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Pais'), X25, scope=Direccion))

Direccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DuplicadorFinca'), X3, scope=Direccion))
Direccion._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Pais')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Provincia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Municipio')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Poblacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoVia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodPostal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Calle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroFinca')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DuplicadorFinca')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Escalera')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Piso')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Puerta')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoAclaradorFinca')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Direccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AclaradorFinca')), min_occurs=0L, max_occurs=1)
    )
Direccion._ContentModel = pyxb.binding.content.ParticleModel(Direccion._GroupModel, min_occurs=1, max_occurs=1)



ClienteConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicadorTipoDireccion'), STD_ANON_44, scope=ClienteConDireccion))

ClienteConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Direccion'), Direccion, scope=ClienteConDireccion))

ClienteConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), IdCliente, scope=ClienteConDireccion))

ClienteConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), NombreCliente, scope=ClienteConDireccion))

ClienteConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), TelefonoInternacional, scope=ClienteConDireccion))

ClienteConDireccion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telefono'), TelefonoInternacional, scope=ClienteConDireccion))
ClienteConDireccion._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ClienteConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ClienteConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nombre')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ClienteConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fax')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ClienteConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telefono')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ClienteConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicadorTipoDireccion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ClienteConDireccion._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Direccion')), min_occurs=0L, max_occurs=1)
    )
ClienteConDireccion._ContentModel = pyxb.binding.content.ParticleModel(ClienteConDireccion._GroupModel, min_occurs=1, max_occurs=1)



DatosReclamacionFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodAgrupacion'), X20, scope=DatosReclamacionFactura))

DatosReclamacionFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodFiscalFactura'), X30, scope=DatosReclamacionFactura))

DatosReclamacionFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteFactReclamada'), X15, scope=DatosReclamacionFactura))

DatosReclamacionFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaFactura'), pyxb.binding.datatypes.date, scope=DatosReclamacionFactura))

DatosReclamacionFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeFact'), pyxb.binding.datatypes.date, scope=DatosReclamacionFactura))

DatosReclamacionFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaFact'), pyxb.binding.datatypes.date, scope=DatosReclamacionFactura))
DatosReclamacionFactura._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosReclamacionFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodFiscalFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacionFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteFactReclamada')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacionFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodAgrupacion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacionFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacionFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaDesdeFact')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosReclamacionFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHastaFact')), min_occurs=0L, max_occurs=1)
    )
DatosReclamacionFactura._ContentModel = pyxb.binding.content.ParticleModel(DatosReclamacionFactura._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalExcesos'), STD_ANON_36, scope=CTD_ANON_15))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), CTD_ANON_6, scope=CTD_ANON_15))
CTD_ANON_15._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Periodo')), min_occurs=1, max_occurs=10L),
    pyxb.binding.content.ParticleModel(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalExcesos')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_15._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_15._GroupModel, min_occurs=1, max_occurs=1)



IdYNombreCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nombre'), NombreCliente, scope=IdYNombreCliente))

IdYNombreCliente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdCliente'), IdCliente, scope=IdYNombreCliente))
IdYNombreCliente._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IdYNombreCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(IdYNombreCliente._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nombre')), min_occurs=1, max_occurs=1)
    )
IdYNombreCliente._ContentModel = pyxb.binding.content.ParticleModel(IdYNombreCliente._GroupModel, min_occurs=1, max_occurs=1)



Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConsumoAnualEstimado'), Decimal13, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), IdContrato, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), DireccionCorrespondencia, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), pyxb.binding.datatypes.date, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), CuentaBancaria, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contacto'), Contacto, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), Decimal2, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), TipoContrato, scope=Contrato))

Contrato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales'), CondicionesContractuales, scope=Contrato))
Contrato._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Duracion')), min_occurs=1, max_occurs=1)
    )
Contrato._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdContrato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConsumoAnualEstimado')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contacto')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Contrato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria')), min_occurs=0L, max_occurs=1)
    )
Contrato._ContentModel = pyxb.binding.content.ParticleModel(Contrato._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotal'), STD_ANON_40, scope=CTD_ANON_16, documentation=u'Importe total de todas las facturas del XML'))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SaldoTotalCobro'), STD_ANON_13, scope=CTD_ANON_16, documentation=u'Saldo total cobro del XML'))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), CuentaBancaria, scope=CTD_ANON_16))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaValor'), pyxb.binding.datatypes.date, scope=CTD_ANON_16))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SaldoTotalFacturacion'), STD_ANON_27, scope=CTD_ANON_16, documentation=u'Saldo total de todas las facturas del xml'))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaLimitePago'), pyxb.binding.datatypes.date, scope=CTD_ANON_16, documentation=u'Fecha teorica de pago '))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoMoneda'), TipoMoneda, scope=CTD_ANON_16, documentation=u'Tabla 104 (01-Pesetas, 02-Euros)'))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdRemesa'), STD_ANON_33, scope=CTD_ANON_16, documentation=u'identificacion remesa o agrupaci\xf3n'))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TotalRecibos'), STD_ANON_24, scope=CTD_ANON_16, documentation=u'Numero recibos del XML'))
CTD_ANON_16._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SaldoTotalFacturacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SaldoTotalCobro')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TotalRecibos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoMoneda')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaValor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaLimitePago')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdRemesa')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_16._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_16._GroupModel, min_occurs=1, max_occurs=1)



DatosAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), TipoCodigoPeriodoDH, scope=DatosAutolecturas))

DatosAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Procedencia'), Procedencia, scope=DatosAutolecturas))

DatosAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MagnitudMedida'), MagnitudMedida, scope=DatosAutolecturas))

DatosAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoDH'), TipoDH, scope=DatosAutolecturas))

DatosAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Aparato'), ModeloAparatoAutolecturas, scope=DatosAutolecturas))

DatosAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LecturaPropuesta'), DecimalS10V2, scope=DatosAutolecturas))

DatosAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaLectura'), pyxb.binding.datatypes.date, scope=DatosAutolecturas))
DatosAutolecturas._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoDH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Periodo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MagnitudMedida')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Aparato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Procedencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LecturaPropuesta')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaLectura')), min_occurs=1, max_occurs=1)
    )
DatosAutolecturas._ContentModel = pyxb.binding.content.ParticleModel(DatosAutolecturas._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatosFacturaATR'), CTD_ANON_22, scope=CTD_ANON_17))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionSuministro'), TipoDireccionSuministro, scope=CTD_ANON_17))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cliente'), IdCliente, scope=CTD_ANON_17))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFactura'), TipoDatosGeneralesFactura, scope=CTD_ANON_17))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contrato'), CodigoContrato, scope=CTD_ANON_17))
CTD_ANON_17._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionSuministro')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contrato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatosFacturaATR')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_17._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_17._GroupModel, min_occurs=1, max_occurs=1)



CondicionesContractualesC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciasMaximas'), Potencias, scope=CondicionesContractualesC))

CondicionesContractualesC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR'), Tarifa, scope=CondicionesContractualesC))

CondicionesContractualesC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas'), Potencias, scope=CondicionesContractualesC))

CondicionesContractualesC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MarcaMedidaBTConPerdidas'), X2, scope=CondicionesContractualesC))

CondicionesContractualesC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KVAsTrafo'), Potencia, scope=CondicionesContractualesC))

CondicionesContractualesC._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PorcentajePerdidasPactadas'), X6, scope=CondicionesContractualesC))
CondicionesContractualesC._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CondicionesContractualesC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TarifaATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractualesC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciasContratadas')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractualesC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciasMaximas')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractualesC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MarcaMedidaBTConPerdidas')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractualesC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'KVAsTrafo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CondicionesContractualesC._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PorcentajePerdidasPactadas')), min_occurs=0L, max_occurs=1)
    )
CondicionesContractualesC._ContentModel = pyxb.binding.content.ParticleModel(CondicionesContractualesC._GroupModel, min_occurs=1, max_occurs=1)



DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumIntegradores'), Decimal2, scope=DatosAparatoICP))

DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PeriodoFabricacion'), Decimal4, scope=DatosAparatoICP))

DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), X10, scope=DatosAparatoICP))

DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FuncionAparato'), FuncionAparato, scope=DatosAparatoICP))

DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RuedasDecimales'), Decimal2, scope=DatosAparatoICP))

DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConstanteEnergia'), DecimalS9V3, scope=DatosAparatoICP))

DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMaximetro'), DecimalS9V3, scope=DatosAparatoICP))

DatosAparatoICP._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RuedasEnteras'), Decimal2, scope=DatosAparatoICP))
DatosAparatoICP._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PeriodoFabricacion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FuncionAparato')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumIntegradores')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConstanteEnergia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMaximetro')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RuedasEnteras')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAparatoICP._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RuedasDecimales')), min_occurs=0L, max_occurs=1)
    )
DatosAparatoICP._ContentModel = pyxb.binding.content.ParticleModel(DatosAparatoICP._GroupModel, min_occurs=1, max_occurs=1)



ImportesOtrosConceptos._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteOtrosConceptos'), CTD_ANON_18, scope=ImportesOtrosConceptos))
ImportesOtrosConceptos._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ImportesOtrosConceptos._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteOtrosConceptos')), min_occurs=1, max_occurs=3L)
    )
ImportesOtrosConceptos._ContentModel = pyxb.binding.content.ParticleModel(ImportesOtrosConceptos._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Anomalia'), CTD_ANON_33, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Ajuste'), CTD_ANON_26, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroRuedasDecimales'), STD_ANON_7, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Magnitud'), MagnitudMedida, scope=CTD_ANON_19, documentation=u'Tabla 43'))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConsumoCalculado'), STD_ANON_19, scope=CTD_ANON_19, documentation=u'Consumo'))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroRuedasEnteras'), STD_ANON_18, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHoraMaximetro'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LecturaDesde'), TipoLimiteIntervaloLectura, scope=CTD_ANON_19, documentation=u'Lectura anterior ventana de facturaci\xf3n'))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMultiplicadora'), STD_ANON_34, scope=CTD_ANON_19, documentation=u'Coeficiente de multiplicaci\xf3n del equipo'))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoPeriodo'), TipoCodigoPeriodoDH, scope=CTD_ANON_19, documentation=u'Tabla 42'))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LecturaHasta'), TipoLimiteIntervaloLectura, scope=CTD_ANON_19, documentation=u'Valor actual de la ventana de facturaci\xf3n'))
CTD_ANON_19._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Magnitud')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoPeriodo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConstanteMultiplicadora')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroRuedasEnteras')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroRuedasDecimales')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConsumoCalculado')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LecturaDesde')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LecturaHasta')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Ajuste')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Anomalia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHoraMaximetro')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_19._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_19._GroupModel, min_occurs=1, max_occurs=1)



MedidaC2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente'), IndicativoYCD, scope=MedidaC2))

MedidaC2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), TiposEquipoMedida, scope=MedidaC2))

MedidaC2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato'), ModelosAparato, scope=MedidaC2))

MedidaC2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado'), IndicativoNCD, scope=MedidaC2))

MedidaC2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion'), IndicativoYCD, scope=MedidaC2))

MedidaC2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente'), IndicativoNCD, scope=MedidaC2))
MedidaC2._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(MedidaC2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaC2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaC2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaC2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaC2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaC2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato')), min_occurs=1, max_occurs=1)
    )
MedidaC2._ContentModel = pyxb.binding.content.ParticleModel(MedidaC2._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PrecioEnergia'), STD_ANON_14, scope=CTD_ANON_20))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValorEnergiaActiva'), STD_ANON_30, scope=CTD_ANON_20, documentation=u'En Kwh'))
CTD_ANON_20._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValorEnergiaActiva')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PrecioEnergia')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_20._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_20._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), CTD_ANON_2, scope=CTD_ANON_21))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde'), pyxb.binding.datatypes.date, scope=CTD_ANON_21))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta'), pyxb.binding.datatypes.date, scope=CTD_ANON_21))
CTD_ANON_21._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Periodo')), min_occurs=1, max_occurs=10L)
    )
CTD_ANON_21._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_21._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), CTD_ANON_3, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoFacturacion'), TipoFacturacionATR, scope=CTD_ANON_22, documentation=u'Tabla 105 (1-Regular (Periodo completo); 2-Irregular (Periodo incompleto))'))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaBOE'), pyxb.binding.datatypes.date, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndAltamedidoenBaja'), Indicativo, scope=CTD_ANON_22))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoTarifa'), TarifaATR, scope=CTD_ANON_22, documentation=u'Tabla 107'))
CTD_ANON_22._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoFacturacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaBOE')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoTarifa')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndAltamedidoenBaja')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Periodo')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_22._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_22._GroupModel, min_occurs=1, max_occurs=1)



DatosAPM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaCaducidadApm'), pyxb.binding.datatypes.date, scope=DatosAPM))

DatosAPM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ApmAportado'), Indicativo, scope=DatosAPM))

DatosAPM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciaInstAT'), Potencia, scope=DatosAPM))

DatosAPM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaEmisionApm'), pyxb.binding.datatypes.date, scope=DatosAPM))

DatosAPM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoApm'), X20, scope=DatosAPM))
DatosAPM._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosAPM._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ApmAportado')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAPM._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoApm')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAPM._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciaInstAT')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAPM._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaEmisionApm')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosAPM._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaCaducidadApm')), min_occurs=0L, max_occurs=1)
    )
DatosAPM._ContentModel = pyxb.binding.content.ParticleModel(DatosAPM._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cabecera'), Cabecera, scope=CTD_ANON_23))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Facturas'), Facturas, scope=CTD_ANON_23))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OtrosDatosFactura'), OtrosDatosFactura, scope=CTD_ANON_23))
CTD_ANON_23._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cabecera')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Facturas')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OtrosDatosFactura')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_23._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_23._GroupModel, min_occurs=1, max_occurs=1)



ContratoPasoMRAMLTarifa2SinCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), IdContrato, scope=ContratoPasoMRAMLTarifa2SinCambios))

ContratoPasoMRAMLTarifa2SinCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), TipoContrato, scope=ContratoPasoMRAMLTarifa2SinCambios))

ContratoPasoMRAMLTarifa2SinCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), DireccionCorrespondencia, scope=ContratoPasoMRAMLTarifa2SinCambios))

ContratoPasoMRAMLTarifa2SinCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), CuentaBancaria, scope=ContratoPasoMRAMLTarifa2SinCambios))

ContratoPasoMRAMLTarifa2SinCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), pyxb.binding.datatypes.date, scope=ContratoPasoMRAMLTarifa2SinCambios))

ContratoPasoMRAMLTarifa2SinCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), Decimal2, scope=ContratoPasoMRAMLTarifa2SinCambios))
ContratoPasoMRAMLTarifa2SinCambios._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Duracion')), min_occurs=1, max_occurs=1)
    )
ContratoPasoMRAMLTarifa2SinCambios._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdContrato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria')), min_occurs=0L, max_occurs=1)
    )
ContratoPasoMRAMLTarifa2SinCambios._ContentModel = pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2SinCambios._GroupModel, min_occurs=1, max_occurs=1)



Medida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), TiposEquipoMedida, scope=Medida))

Medida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato'), ModelosAparato, scope=Medida))

Medida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente'), IndicativoYCD, scope=Medida))

Medida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado'), IndicativoNCD, scope=Medida))

Medida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion'), IndicativoYCD, scope=Medida))

Medida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente'), IndicativoNCD, scope=Medida))
Medida._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Medida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Medida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Medida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Medida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Medida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Medida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato')), min_occurs=1, max_occurs=1)
    )
Medida._ContentModel = pyxb.binding.content.ParticleModel(Medida._GroupModel, min_occurs=1, max_occurs=1)



DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaEmisionCie'), pyxb.binding.datatypes.date, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CieAportado'), Indicativo, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaCaducidadCie'), pyxb.binding.datatypes.date, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SeccionCable'), X2, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NifInstalador'), X9, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CieElectronico'), Indicativo, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TensionSuministro'), X5, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NombreInstalador'), X45, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoSuministro'), TiposSuministro, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SelloElectronico'), X30, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoCie'), X11, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SensibilidadDif'), X2, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciaInstBT'), Potencia, scope=DatosCIE))

DatosCIE._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InstensidadDif'), X2, scope=DatosCIE))
DatosCIE._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CieAportado')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CieElectronico')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoCie')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SelloElectronico')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciaInstBT')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaEmisionCie')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaCaducidadCie')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NifInstalador')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NombreInstalador')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TensionSuministro')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'InstensidadDif')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SensibilidadDif')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SeccionCable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DatosCIE._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoSuministro')), min_occurs=0L, max_occurs=1)
    )
DatosCIE._ContentModel = pyxb.binding.content.ParticleModel(DatosCIE._GroupModel, min_occurs=1, max_occurs=1)



Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImportesOtrosConceptos'), ImportesOtrosConceptos, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoPotencia'), ImportesTerminoPotencia, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IVA'), Importe, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotal'), Importe, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImpuestoElectrico'), Importe, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteReactiva'), Importe, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteExcesoPotencia'), Importe, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoEnergia'), ImportesTerminoEnergia, scope=Importes))

Importes._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteAlquileres'), Importe, scope=Importes))
Importes._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoPotencia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImportesTerminoEnergia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteReactiva')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteExcesoPotencia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteAlquileres')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImportesOtrosConceptos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImpuestoElectrico')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IVA')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Importes._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotal')), min_occurs=0L, max_occurs=1)
    )
Importes._ContentModel = pyxb.binding.content.ParticleModel(Importes._GroupModel, min_occurs=1, max_occurs=1)



PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TelefonoTelemedida'), Decimal9, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaVigor'), pyxb.binding.datatypes.date, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaveAcceso'), X10, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TensionPM'), Decimal9, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodPMPrincipal'), CodPM, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaAlta'), pyxb.binding.datatypes.date, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaBaja'), pyxb.binding.datatypes.date, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PasswordPM'), X10, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComentariosPM'), ComentariosPM, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodPM'), CodPM, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Aparatos'), Aparatos, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimiento'), AltaBajaModificacion, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodREE'), X8, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CUPS'), CUPS, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoPM'), TipoPM, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EstadoTelefono'), EstadoTelefono, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModoLectura'), ModoLecturaPM, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EstadoPM'), EstadoPM, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Funcion'), FuncionPM, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionEnlace'), X10, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionPuntoMedida'), X10, scope=PuntoDeMedida))

PuntoDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumLinea'), Decimal2, scope=PuntoDeMedida))
PuntoDeMedida._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodPM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimiento')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodREE')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CUPS')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoPM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodPMPrincipal')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModoLectura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EstadoPM')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Funcion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionEnlace')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionPuntoMedida')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumLinea')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TelefonoTelemedida')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EstadoTelefono')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaveAcceso')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TensionPM')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaVigor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaAlta')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaBaja')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PasswordPM')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Aparatos')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PuntoDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComentariosPM')), min_occurs=0L, max_occurs=1)
    )
PuntoDeMedida._ContentModel = pyxb.binding.content.ParticleModel(PuntoDeMedida._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalTerminoPotencia'), STD_ANON_39, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TerminoPotencia'), CTD_ANON_28, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PenalizacionNoICP'), Indicativo, scope=CTD_ANON_25))
CTD_ANON_25._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TerminoPotencia')), min_occurs=1, max_occurs=8L),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PenalizacionNoICP')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalTerminoPotencia')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_25._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_25._GroupModel, min_occurs=1, max_occurs=1)



Comentarios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comentario'), Comentario, scope=Comentarios))
Comentarios._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Comentarios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comentario')), min_occurs=0L, max_occurs=50L)
    )
Comentarios._ContentModel = pyxb.binding.content.ParticleModel(Comentarios._GroupModel, min_occurs=1, max_occurs=1)



Comentario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hora'), pyxb.binding.datatypes.time, scope=Comentario))

Comentario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Texto'), X120, scope=Comentario))

Comentario._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fecha'), pyxb.binding.datatypes.date, scope=Comentario))
Comentario._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Comentario._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Texto')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Comentario._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fecha')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Comentario._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hora')), min_occurs=1, max_occurs=1)
    )
Comentario._ContentModel = pyxb.binding.content.ParticleModel(Comentario._GroupModel, min_occurs=1, max_occurs=1)



PotenciasAFacturar._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PotenciaAFacturar'), CTD_ANON_12, scope=PotenciasAFacturar))
PotenciasAFacturar._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PotenciasAFacturar._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PotenciaAFacturar')), min_occurs=1, max_occurs=6L)
    )
PotenciasAFacturar._ContentModel = pyxb.binding.content.ParticleModel(PotenciasAFacturar._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AjustePorIntegrador'), STD_ANON_5, scope=CTD_ANON_26))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodigoMotivoAjuste'), TipoMotivoAjuste, scope=CTD_ANON_26, documentation=u'Tabla 106'))
CTD_ANON_26._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodigoMotivoAjuste')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AjustePorIntegrador')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_26._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_26._GroupModel, min_occurs=1, max_occurs=1)



ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Duracion'), Decimal2, scope=ContratoPasoMRAMLTarifa2ConCambios))

ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR'), TipoContrato, scope=ContratoPasoMRAMLTarifa2ConCambios))

ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales2n'), CondicionesContractuales2n, scope=ContratoPasoMRAMLTarifa2ConCambios))

ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contacto'), Contacto, scope=ContratoPasoMRAMLTarifa2ConCambios))

ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria'), CuentaBancaria, scope=ContratoPasoMRAMLTarifa2ConCambios))

ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdContrato'), IdContrato, scope=ContratoPasoMRAMLTarifa2ConCambios))

ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia'), DireccionCorrespondencia, scope=ContratoPasoMRAMLTarifa2ConCambios))

ContratoPasoMRAMLTarifa2ConCambios._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion'), pyxb.binding.datatypes.date, scope=ContratoPasoMRAMLTarifa2ConCambios))
ContratoPasoMRAMLTarifa2ConCambios._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaFinalizacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Duracion')), min_occurs=1, max_occurs=1)
    )
ContratoPasoMRAMLTarifa2ConCambios._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IdContrato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoContratoATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CondicionesContractuales2n')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contacto')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionCorrespondencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CuentaBancaria')), min_occurs=0L, max_occurs=1)
    )
ContratoPasoMRAMLTarifa2ConCambios._ContentModel = pyxb.binding.content.ParticleModel(ContratoPasoMRAMLTarifa2ConCambios._GroupModel, min_occurs=1, max_occurs=1)



DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Piso'), Piso, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Poblacion'), Decimal7, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Municipio'), Decimal7, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoAclaradorFinca'), TipoAclaradorFinca, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Pais'), X25, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AclaradorFinca'), X40, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Calle'), X30, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Provincia'), Decimal2, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Puerta'), Puerta, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroFinca'), X5, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DuplicadorFinca'), X3, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoVia'), TipoVia, scope=DireccionSinCodPostal))

DireccionSinCodPostal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Escalera'), Escalera, scope=DireccionSinCodPostal))
DireccionSinCodPostal._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Pais')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Provincia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Municipio')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Poblacion')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoVia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Calle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroFinca')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DuplicadorFinca')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Escalera')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Piso')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Puerta')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoAclaradorFinca')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DireccionSinCodPostal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AclaradorFinca')), min_occurs=0L, max_occurs=1)
    )
DireccionSinCodPostal._ContentModel = pyxb.binding.content.ParticleModel(DireccionSinCodPostal._GroupModel, min_occurs=1, max_occurs=1)



Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), TiposEquipoMedida, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DiscriminacionHorariaActiva'), TipoDHActiva, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Propietario'), X20, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoNoICP'), DatosAparatoNoICP, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExtraccionLecturas'), Indicativo, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoICP'), DatosAparatoICP, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoPropiedadAparato'), TipoPropiedadAparato, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Medidas'), MedidasAparato, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DiscriminacionHorariaMaximas'), TipoDHMaximas, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Modelo'), ModeloAparato, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodPrecinto'), STD_ANON_17, scope=Aparato, documentation=u'Codigo de precinto'))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LecturaDirecta'), Indicativo, scope=Aparato))

Aparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimiento'), TipoMovimiento, scope=Aparato))
Aparato._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoNoICP')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatosAparatoICP')), min_occurs=1, max_occurs=1)
    )
Aparato._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Modelo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoMovimiento')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoPropiedadAparato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Propietario')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExtraccionLecturas')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DiscriminacionHorariaActiva')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DiscriminacionHorariaMaximas')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LecturaDirecta')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodPrecinto')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Aparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Medidas')), min_occurs=0L, max_occurs=1)
    )
Aparato._ContentModel = pyxb.binding.content.ParticleModel(Aparato._GroupModel, min_occurs=1, max_occurs=1)



Anomalias._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Anomalia'), Anomalia, scope=Anomalias))
Anomalias._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Anomalias._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Anomalia')), min_occurs=1, max_occurs=5L)
    )
Anomalias._ContentModel = pyxb.binding.content.ParticleModel(Anomalias._GroupModel, min_occurs=1, max_occurs=1)



RegistrosDocs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistroDoc'), RegistroDoc, scope=RegistrosDocs))
RegistrosDocs._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RegistrosDocs._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistroDoc')), min_occurs=0L, max_occurs=50L)
    )
RegistrosDocs._ContentModel = pyxb.binding.content.ParticleModel(RegistrosDocs._GroupModel, min_occurs=1, max_occurs=1)



ModelosAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModeloAparato'), ModeloAparato, scope=ModelosAparato))
ModelosAparato._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ModelosAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModeloAparato')), min_occurs=0L, max_occurs=50L)
    )
ModelosAparato._ContentModel = pyxb.binding.content.ParticleModel(ModelosAparato._GroupModel, min_occurs=1, max_occurs=1)



MedidaResto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato'), ModelosAparato, scope=MedidaResto))

MedidaResto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida'), TiposEquipoMedida, scope=MedidaResto))

MedidaResto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado'), IndicativoNCD, scope=MedidaResto))

MedidaResto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion'), IndicativoYCD, scope=MedidaResto))

MedidaResto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente'), IndicativoNCD, scope=MedidaResto))

MedidaResto._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente'), IndicativoYCD, scope=MedidaResto))
MedidaResto._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(MedidaResto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ICPAportadoInstalado')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaResto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ICPInstalacion')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaResto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EquipoAportadoCliente')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaResto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EquipoInstaladoCliente')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaResto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoEquipoMedida')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(MedidaResto._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModelosAparato')), min_occurs=1, max_occurs=1)
    )
MedidaResto._ContentModel = pyxb.binding.content.ParticleModel(MedidaResto._GroupModel, min_occurs=1, max_occurs=1)



OtrosConceptos._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Concepto'), CTD_ANON_24, scope=OtrosConceptos))
OtrosConceptos._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OtrosConceptos._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Concepto')), min_occurs=1, max_occurs=3L)
    )
OtrosConceptos._ContentModel = pyxb.binding.content.ParticleModel(OtrosConceptos._GroupModel, min_occurs=1, max_occurs=1)



RegistroAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Autolecturas'), DatosAutolecturas, scope=RegistroAutolecturas))
RegistroAutolecturas._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RegistroAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Autolecturas')), min_occurs=0L, max_occurs=50L)
    )
RegistroAutolecturas._ContentModel = pyxb.binding.content.ParticleModel(RegistroAutolecturas._GroupModel, min_occurs=1, max_occurs=1)



ModeloAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModeloMarca'), X30, scope=ModeloAparato))

ModeloAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Tipo'), TipoAparato, scope=ModeloAparato, documentation=u'Tabla 24'))

ModeloAparato._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Marca'), MarcaAparato, scope=ModeloAparato, documentation=u'Tabla 25'))
ModeloAparato._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ModeloAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Tipo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ModeloAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Marca')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ModeloAparato._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModeloMarca')), min_occurs=0L, max_occurs=1)
    )
ModeloAparato._ContentModel = pyxb.binding.content.ParticleModel(ModeloAparato._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConceptoIVA'), STD_ANON_15, scope=CTD_ANON_27, documentation=u'Para facturar conceptos excepcionales que solo lleven aplicado IVA.'))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EnergiaReactiva'), CTD_ANON_30, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EnergiaActiva'), CTD_ANON_14, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IVA'), TipoIVAIGIC, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteIntereses'), STD_ANON_49, scope=CTD_ANON_27, documentation=u'En los casos que se incluyan intereses de demora'))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Medidas'), CTD_ANON_8, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IVAIGICReducido'), TipoIVAIGIC, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExcesoPotencia'), CTD_ANON_15, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFacturaATR'), CTD_ANON_17, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Potencia'), CTD_ANON_25, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConceptoIEIVA'), STD_ANON_60, scope=CTD_ANON_27, documentation=u'Para facturar conceptos excepcionales que lleven aplicado impuesto el\xe9ctrico e IVA.'))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImpuestoElectrico'), CTD_ANON_7, scope=CTD_ANON_27))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Alquileres'), CTD_ANON, scope=CTD_ANON_27))
CTD_ANON_27._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFacturaATR')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Potencia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExcesoPotencia')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EnergiaActiva')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EnergiaReactiva')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImpuestoElectrico')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Alquileres')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteIntereses')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConceptoIEIVA')), min_occurs=0L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConceptoIVA')), min_occurs=0L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IVA')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IVAIGICReducido')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Medidas')), min_occurs=0L, max_occurs=10L)
    )
CTD_ANON_27._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_27._GroupModel, min_occurs=1, max_occurs=1)



OtrosDatosFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionDestino'), STD_ANON_32, scope=OtrosDatosFactura))

OtrosDatosFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SociedadMercantilEmisora'), STD_ANON_6, scope=OtrosDatosFactura))

OtrosDatosFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SociedadMercantilDestino'), STD_ANON_58, scope=OtrosDatosFactura))

OtrosDatosFactura._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionEmisora'), STD_ANON_46, scope=OtrosDatosFactura))
OtrosDatosFactura._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OtrosDatosFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SociedadMercantilEmisora')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OtrosDatosFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SociedadMercantilDestino')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OtrosDatosFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionEmisora')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(OtrosDatosFactura._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionDestino')), min_occurs=1, max_occurs=1)
    )
OtrosDatosFactura._ContentModel = pyxb.binding.content.ParticleModel(OtrosDatosFactura._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), CTD_ANON_, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde'), pyxb.binding.datatypes.date, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta'), pyxb.binding.datatypes.date, scope=CTD_ANON_28))
CTD_ANON_28._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Periodo')), min_occurs=1, max_occurs=10L)
    )
CTD_ANON_28._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_28._GroupModel, min_occurs=1, max_occurs=1)



RegistroDoc._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionUrl'), X255, scope=RegistroDoc))

RegistroDoc._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoDocAportado'), TiposDocumentacion, scope=RegistroDoc))
RegistroDoc._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RegistroDoc._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoDocAportado')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RegistroDoc._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionUrl')), min_occurs=0L, max_occurs=1)
    )
RegistroDoc._ContentModel = pyxb.binding.content.ParticleModel(RegistroDoc._GroupModel, min_occurs=1, max_occurs=1)



Anomalia._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Descripcion'), X45, scope=Anomalia))

Anomalia._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CodAnomalia'), TipoAnomalia, scope=Anomalia))
Anomalia._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Anomalia._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CodAnomalia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Anomalia._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Descripcion')), min_occurs=1, max_occurs=1)
    )
Anomalia._ContentModel = pyxb.binding.content.ParticleModel(Anomalia._GroupModel, min_occurs=1, max_occurs=1)



ComentariosPM._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComentarioPM'), ComentarioPM, scope=ComentariosPM))
ComentariosPM._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ComentariosPM._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComentarioPM')), min_occurs=0L, max_occurs=10L)
    )
ComentariosPM._ContentModel = pyxb.binding.content.ParticleModel(ComentariosPM._GroupModel, min_occurs=1, max_occurs=1)



Reclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reclamante'), DatosReclamante, scope=Reclamante))

Reclamante._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoReclamante'), TipoReclamante, scope=Reclamante))
Reclamante._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Reclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoReclamante')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Reclamante._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reclamante')), min_occurs=0L, max_occurs=1)
    )
Reclamante._ContentModel = pyxb.binding.content.ParticleModel(Reclamante._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalEnergiaReactiva'), STD_ANON_21, scope=CTD_ANON_30))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TerminoEnergiaReactiva'), CTD_ANON_21, scope=CTD_ANON_30))
CTD_ANON_30._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TerminoEnergiaReactiva')), min_occurs=1, max_occurs=8L),
    pyxb.binding.content.ParticleModel(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ImporteTotalEnergiaReactiva')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_30._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_30._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaBOE'), pyxb.binding.datatypes.date, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DireccionSuministro'), TipoDireccionSuministro, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Cliente'), IdCliente, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contrato'), CodigoContrato, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFactura'), TipoDatosGeneralesFactura, scope=CTD_ANON_32))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LineaNegocio'), STD_ANON_57, scope=CTD_ANON_32, documentation=u'Tabla 5'))
CTD_ANON_32._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DireccionSuministro')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Cliente')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contrato')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DatosGeneralesFactura')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LineaNegocio')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaBOE')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_32._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_32._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TextoAnomalia'), STD_ANON_, scope=CTD_ANON_33))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TipoAnomalia'), AnomaliaMedida, scope=CTD_ANON_33, documentation=u'Tabla 45'))
CTD_ANON_33._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TipoAnomalia')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TextoAnomalia')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_33._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_33._GroupModel, min_occurs=1, max_occurs=1)



ExcesosPotAFacturar._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExcesoPotAFacturar'), CTD_ANON_5, scope=ExcesosPotAFacturar))
ExcesosPotAFacturar._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ExcesosPotAFacturar._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExcesoPotAFacturar')), min_occurs=1, max_occurs=6L)
    )
ExcesosPotAFacturar._ContentModel = pyxb.binding.content.ParticleModel(ExcesosPotAFacturar._GroupModel, min_occurs=1, max_occurs=1)



PuntosDeMedida._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PuntoDeMedida'), PuntoDeMedida, scope=PuntosDeMedida))
PuntosDeMedida._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PuntosDeMedida._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PuntoDeMedida')), min_occurs=1, max_occurs=10L)
    )
PuntosDeMedida._ContentModel = pyxb.binding.content.ParticleModel(PuntosDeMedida._GroupModel, min_occurs=1, max_occurs=1)



ModeloAparatoAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie'), X10, scope=ModeloAparatoAutolecturas))

ModeloAparatoAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Tipo'), TipoAparato, scope=ModeloAparatoAutolecturas, documentation=u'Tabla 24'))

ModeloAparatoAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Marca'), MarcaAparato, scope=ModeloAparatoAutolecturas, documentation=u'Tabla 25'))

ModeloAparatoAutolecturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModeloMarca'), X30, scope=ModeloAparatoAutolecturas))
ModeloAparatoAutolecturas._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ModeloAparatoAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Tipo')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ModeloAparatoAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Marca')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ModeloAparatoAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ModeloMarca')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ModeloAparatoAutolecturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NumeroSerie')), min_occurs=1, max_occurs=1)
    )
ModeloAparatoAutolecturas._ContentModel = pyxb.binding.content.ParticleModel(ModeloAparatoAutolecturas._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Periodo'), CTD_ANON_20, scope=CTD_ANON_35))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde'), pyxb.binding.datatypes.date, scope=CTD_ANON_35))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta'), pyxb.binding.datatypes.date, scope=CTD_ANON_35))
CTD_ANON_35._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaDesde')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FechaHasta')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Periodo')), min_occurs=1, max_occurs=10L)
    )
CTD_ANON_35._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_35._GroupModel, min_occurs=1, max_occurs=1)



Facturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistroFin'), CTD_ANON_16, scope=Facturas))

Facturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FacturaATR'), CTD_ANON_27, scope=Facturas))

Facturas._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OtrasFacturas'), CTD_ANON_4, scope=Facturas))
Facturas._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Facturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FacturaATR')), min_occurs=0L, max_occurs=1000L),
    pyxb.binding.content.ParticleModel(Facturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OtrasFacturas')), min_occurs=0L, max_occurs=1000L),
    pyxb.binding.content.ParticleModel(Facturas._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistroFin')), min_occurs=1, max_occurs=1)
    )
Facturas._ContentModel = pyxb.binding.content.ParticleModel(Facturas._GroupModel, min_occurs=1, max_occurs=1)
