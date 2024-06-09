#!/bin/bash

Help()
{
	echo "Build the TAMUS control standards catalog in Docusaurus using an OSCAL resolved catalog"
	echo
	echo "Syntax: build-docusaurus-catalog [Path to POM] [Path to Resolved Catalog XML Source] [Path to Docs Catalog]"
	echo
}

if ! [ -x "$(command -v mvn)" ]; then
  echo 'Error: Maven (mvn) is not in the PATH, is it installed?' >&2
  exit 1
fi

# This command runs the XSL transform to populate XML <insert> tags found in the OSCAL resolved catalog XML

mvn -f $1/pom.xml exec:java -Dexec.mainClass="net.sf.saxon.Transform" -Dexec.args="-xsl:oscal-populate-inserts.xsl -s:$2 -o:/tmp/catalog.xml"

# This command runs the Python script to generate the Markdown pages that form the catalog

python3 docusaurus-catalog.py --source=/tmp/catalog.xml --dest=$3

# This cleans up the temporary XML file created by step 1

rm /tmp/catalog.xml
