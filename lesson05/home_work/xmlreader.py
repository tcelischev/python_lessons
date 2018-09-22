import xml.etree.ElementTree as ET

tree = ET.parse('FrameworkList.xml')
root = tree.getroot()
for elem in root.iter():
    print(elem.tag, elem.attrib, " = ", elem.text)
    print()

