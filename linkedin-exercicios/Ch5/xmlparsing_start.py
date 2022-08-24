#
# Example file for parsing and processing XML
#
import xml.dom.minidom


def main():

    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml")

    # print out the document node and the name of the first child tag
    print("doc.name      = ", doc.nodeName)
    print("doc.localName = ", doc.localName)
    print("doc.nodeType  = ", doc.nodeType)
    print("doc.attributes= ", doc.attributes)
    print("doc.firstChild= ", doc.firstChild)

    print("doc.firstChild.tagName = ", doc.firstChild.tagName)

    # get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print("numero de skills: %d" % skills.length)
    for skill in skills:
        print("skills.getAtrribute = ", skill.getAttribute("name"))

    # create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "Korn shell")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print("numero de skills agora: %d" % skills.length)
    for skill in skills:
        print("skills.getAtrribute = ", skill.getAttribute("name"))


if __name__ == "__main__":
    main()
