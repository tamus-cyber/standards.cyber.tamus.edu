import argparse, os, shutil, xml.etree.ElementTree as ET

def returnTitle(control):
	label = ""

	for prop in control.findall('{http://csrc.nist.gov/ns/oscal/1.0}prop'):
		if (prop.get('name') == "label" and prop.get('class') == None):
			label = prop.get('value')

		if (label == ""):
			for prop in control.findall('{http://csrc.nist.gov/ns/oscal/1.0}prop'):
				if (prop.get('name') == "label"):
					label = prop.get('value')
		
	title = control.find('{http://csrc.nist.gov/ns/oscal/1.0}title').text

	return {"label": label, "title": title}


def returnControl(control):
	title = returnTitle(control)

	string = "# %s %s {#%s}\n\n" % (title['label'], title['title'], control.find("{http://csrc.nist.gov/ns/oscal/1.0}prop[@name='sort-id']").attrib['value'])

	for prop in control.findall('{http://csrc.nist.gov/ns/oscal/1.0}prop'):
		if (prop.get('name') == "status" and prop.get('value') == "withdrawn"):
			string += "**_[Withdrawn]_**\n\n"
			
	for part in control.findall('{http://csrc.nist.gov/ns/oscal/1.0}part'):
		if (part.get('name') == "statement"):
			string += returnStatement(part)

	for enhancement in control.findall('{http://csrc.nist.gov/ns/oscal/1.0}control'):
		if (enhancement.get('class') == "SP800-53-enhancement"):
			string += returnEnhancement(enhancement)

	return string


def returnEnhancement(enhancement):
	title = returnTitle(enhancement)

	string = "## %s %s {#%s}\n\n" % (title['label'], title['title'], enhancement.find("{http://csrc.nist.gov/ns/oscal/1.0}prop[@name='sort-id']").attrib['value'])

	for part in enhancement.findall('{http://csrc.nist.gov/ns/oscal/1.0}part'):
		if (part.get('name') == "withdrawn-status"):
			string += ("%s\n\n" % (part.text))

		if (part.get('name') == "statement"):
			string += returnStatement(part)

	return string


def returnStatement(statement):
	i = 0

	string = ""

	for item in statement.iter('{http://csrc.nist.gov/ns/oscal/1.0}part'):
		if (item.get('name') == "item"):
			i =+ 1

			label = ""

			for prop in item.findall('{http://csrc.nist.gov/ns/oscal/1.0}prop'):
				if (prop.get('name') == "label"):
					label = prop.get('value') + " "

			p = item.find('{http://csrc.nist.gov/ns/oscal/1.0}p').text

			string += "%s%s\n\n" % (label, p)

	if (i == 0):
		string += "%s\n\n" % (statement.find('{http://csrc.nist.gov/ns/oscal/1.0}p').text)

	return string


parser = argparse.ArgumentParser(description='Parse an OSCAL catalog into a Docusaurus doc.')
parser.add_argument('--source', nargs=1, help='Path to OSCAL catalog source file')
args = parser.parse_args()

tree = ET.parse(args.source[0])
root = tree.getroot()

families = root.findall("{http://csrc.nist.gov/ns/oscal/1.0}group")

for family in families:

	if os.path.exists(family.get('id')) and os.path.isdir(family.get('id')):
		shutil.rmtree(family.get('id'))

	os.mkdir(family.get('id'))

	f = open(family.get('id') + "/index.md", "w")

	f.write("# %s - %s\n" % (family.get('id').upper(), family.find('{http://csrc.nist.gov/ns/oscal/1.0}title').text))

	f.close()

	for control in family.findall('{http://csrc.nist.gov/ns/oscal/1.0}control'):
		if (control.get('class') == "SP800-53"):
			for prop in control.findall('{http://csrc.nist.gov/ns/oscal/1.0}prop'):
				if (prop.get('name') == "sort-id"):
					sort_id = prop.get('value')

			f = open("%s/%s.md" % (family.get('id'), sort_id), "w")

			f.write(returnControl(control))

			f.close()