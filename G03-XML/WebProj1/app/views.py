from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import os
from lxml import etree
from lxml import builder
from WebProj1.settings import BASE_DIR

STATIC_PATH = os.path.join(BASE_DIR, "app", "static")
XML_PATH = os.path.join(STATIC_PATH, "xml")
COURSES_FILE_PATH = os.path.join(XML_PATH, "cursos.xml")
COURSES_XSD_FILE_PATH = os.path.join(XML_PATH, "curso.xsd")
COURSES_XSLT_FILE_PATH = os.path.join(XML_PATH, "cursos.xsl")


# Views
def index(request):
    return render(request, "default.html", {"content": "Hello World"})


def courses(request):
    """ Renders list of course names. Courses info is transformed into usable HTML using a XSLT file

        No arguments required

        :return: Webpage with list of courses
    """
    xml_file = etree.parse(COURSES_FILE_PATH)

    # Search for all courses in the XML File
    query = "//curso"
    courses = xml_file.xpath(query)

    # Create the list of the courses
    courses_dict = {}
    for course in courses:
        courses_dict[course.find('guid').text] = course.find('nome').text

    # Obtain XSLT
    xslt_file = etree.parse(COURSES_XSLT_FILE_PATH)
    transform = etree.XSLT(xslt_file)
    html = transform(xml_file)

    # Render Webpage
    context = {
        "courses": courses_dict,
        "content": html
    }

    return render(request, 'default.html', context)


def create_course(request):
    """ Renders a page to create a course. A course info is validated

        No arguments required

        :return: Webpage with to create a new course
    """

    # Render create a course page
    if 'name' not in request.POST:  # course has at least a name
        return render(request, 'create_course.html')

    # Obtain info to create course XML
    course_args = {k: v for k, v in request.POST.items() if v is not None and not (k in 'csrfmiddlewaretoken')}

    # Build course XML
    # won't work for more complex elements, such as departments (not considered in this example)
    # Create the root element
    course = etree.Element('course')

    # Add the subelements
    for course_arg in course_args:
        course_elem = etree.Element(course_arg)         #tag
        course_elem.text = course_args[course_arg]      #text
        course.append(course_elem)

    # Make a new document tree
    xml = etree.ElementTree(course)

    # Print xml
    root = xml.getroot()
    # print_elems(root)

    # Validate course XML
    valid_xml = is_xml_valid(xml, COURSES_XSD_FILE_PATH)

    if valid_xml:
        context = {
            "content": "Created XML successfully " + str(xml)
        }
    else:
        context = {
            "content": "Error creating course XML " + str(print_elems(root))
        }
    return render(request, 'default.html', context)


def is_xml_valid(xml, xsd):
    # Load XSD file
    xsd_root = etree.parse(xsd)
    xsd = etree.XMLSchema(xsd_root)

    # Validate XML file
    return xsd.validate(xml)


def print_elems(elem, text="", result=""):
    elem_contents = text + str(elem) + " " + str(elem.attrib) + " " + str(elem.text)
    elem_contents = elem_contents.replace("{}", "").replace("\n","")
    result += elem_contents             # print element
    if len(elem.getchildren()) != 0:    # if they exist, print children
        for e in elem:
            return result + print_elems(e, text + "\t")
    return result
