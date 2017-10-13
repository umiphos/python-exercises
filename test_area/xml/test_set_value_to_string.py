from lxml import etree, objectify

xml_str= open('factura.xml').read()

document = objectify.XML(xml_str)
xpath_1 = '//cbc:ResponseCode'
xpath_2 = '//cbc:Description'

namespaces = {'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2', 'ar': 'urn:oasis:names:specification:ubl:schema:xsd:ApplicationResponse-2', 'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'}

response_code = document.xpath(xpath_1, namespaces=namespaces)[0]
description = document.xpath(xpath_2, namespaces=namespaces)[0]

import ipdb;ipdb.set_trace()
document.xpath(xpath_1, namespaces=namespaces)[0]._setText('9')
document.xpath(xpath_2, namespaces=namespaces)[0]._setText('this new text for description')

print response_code, document.xpath(xpath_1, namespaces=namespaces)[0]
print description, document.xpath(xpath_2, namespaces=namespaces)[0]
