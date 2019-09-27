from lxml import etree
import argparse


def print_elems(elem, text=""):
    elem_contents = text + str(elem) + " " + str(elem.attrib) + " " + str(elem.text)
    elem_contents = elem_contents.replace("{}", "").replace("\n","")
    print(elem_contents)             # print element
    if len(elem.getchildren()) != 0:    # if they exist, print children
        for e in elem:
            print_elems(e, text + "\t")


# Arguments
parser = argparse.ArgumentParser(description="Validate XML files given a XSD")
parser.add_argument("--xsd", metavar="xsd", type=str, required=True)
parser.add_argument("--xml", metavar="xml", type=str, required=True)
args = vars(parser.parse_args())

# Load XSD file
xsd_root = etree.parse(args['xsd'])
xsd = etree.XMLSchema(xsd_root)

# Load XML file
xml_file = etree.parse(args['xml'])

# Validate XML file
print(xsd.validate(xml_file))

# Print XML file
#print(etree.tostring())
root = xml_file.getroot()
print_elems(root)

