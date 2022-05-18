import xml.etree.ElementTree as ET


def parse_xml_from_string():
    country_data_as_string = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""
    root = ET.fromstring(country_data_as_string)
    print(type(root))
    print(root[0][1].tag, root[0][1].text)
    for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)


def parse_xml_from_file():
    tree = ET.parse('country_data.xml')
    print(type(tree))
    root = tree.getroot()
    print(type(root))


if __name__ == '__main__':
    parse_xml_from_string()
    # parse_xml_from_file()
