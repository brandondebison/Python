#!/usr/local/bin/python3
import xml.etree.ElementTree as etree 


tree = etree.parse('myfile.xml')

root = tree.getroot()

for node in root:
    elementName = node.tag
    elementAttribute = node.attrib

    for elementTag, elementTagValue in elementAttribute.items():
        print("\nType 1 = " + str(elementTag)+", Value 1 = "+str(elementTagValue))


    for item in node:
        itemAttribute = item.tag # This is the tag line in xml <author)
        itemValue = item.text # this is the text between tags
        print("\nType 2 = "+str(itemAttribute)+", Value 2 = " +str(itemValue))