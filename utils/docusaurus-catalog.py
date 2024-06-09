import argparse, json, os, shutil, xml.etree.ElementTree as ET

custom_edit_url = "https://github.com/tamus-cyber/standards.cyber.tamus.edu/tree/main/content/tamus.edu/TAMUS_profile.xml"

intro_text = """Security and privacy control standards described in this control standards catalog have a well-defined
organization and structure. For ease of use in the security and privacy control selection and specification process,
controls are organized into families (listed in the navigation menu to the left). Each family contains controls that
are related to the specific topic of the family. A two-character identifier uniquely identifies each control family
(e.g., PS for Personnel Security). Security and privacy controls may involve aspects of policy, oversight, supervision,
manual processes, and automated mechanisms that are implemented by systems or actions by individuals."""

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
parser.add_argument('--dest', nargs=1, help='Path to Docs Catalog directory')
args = parser.parse_args()

tree = ET.parse(args.source[0])
root = tree.getroot()
catalog_dir = args.dest[0]

families = root.findall("{http://csrc.nist.gov/ns/oscal/1.0}group")

if os.path.exists("%s" % (catalog_dir)):
	shutil.rmtree("%s" % (catalog_dir))

os.mkdir("%s" % (catalog_dir))

f = open("%s/README.md" % (catalog_dir), "w")

f.write("---\ncustom_edit_url: null\nsidebar_position: 1\n---\n\n# Security Control Standards Catalog\n\n%s" % (intro_text))

f.close()

for family in families:

	os.mkdir("%s/%s" % (catalog_dir, family.get('id')))

	data = {
		"label": "%s - %s" % (family.get('id').upper(), family.find('{http://csrc.nist.gov/ns/oscal/1.0}title').text)
	}

	f = open("%s/%s/_category_.json" % (catalog_dir, family.get('id')), "w")

	f.write(json.dumps(data))

	#f.write("# %s - %s\n\n" % (family.get('id').upper(), family.find('{http://csrc.nist.gov/ns/oscal/1.0}title').text))

	#f.write("import DocCardList from '@theme/DocCardList';\n\n<DocCardList />")

	f.close()

	for control in family.findall('{http://csrc.nist.gov/ns/oscal/1.0}control'):
		if (control.get('class') == "SP800-53"):
			for prop in control.findall('{http://csrc.nist.gov/ns/oscal/1.0}prop'):
				if (prop.get('name') == "sort-id"):
					sort_id = prop.get('value')

			title = returnTitle(control)

			f = open("%s/%s/%s.md" % (catalog_dir, family.get('id'), sort_id), "w")

			f.write("---\ncustom_edit_url: %s\ntitle: %s %s\ndescription: \"\"\n---\n\n" % (custom_edit_url, title['label'], title['title']))

			f.write(returnControl(control))

			f.close()