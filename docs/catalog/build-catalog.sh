#!/bin/bash

Help()
{
	echo "Build the TAMUS catalog using OSCAL"
	echo
	echo "Syntax: build-catalog [PathToPOM] [XML Source] [XML Destination]"
	echo
}

mvn -f $1/pom.xml exec:java -Dexec.mainClass="net.sf.saxon.Transform" -Dexec.args="-xsl:oscal-populate-inserts.xsl -s:$2 -o:$3"

python3 generate-catalog.py --source=$3

#rm $3
