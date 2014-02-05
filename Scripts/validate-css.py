#!/usr/bin/env python

import sys, os, subprocess, urllib
import xml.etree.ElementTree as ET


# Grab our path information
filePath = os.environ['EDITOR_PATH']
sugarPath = os.environ['EDITOR_SUGAR_PATH']
rootPath = os.environ['EDITOR_PROJECT_PATH']
if rootPath == '':
	rootPath = os.path.dirname(filePath)

# Compose and execute our JAR command
command = ['java', '-jar', 'css-validator.jar', '--profile=css3', '--output=soap12', 'file:' + filePath]
result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.path.join(sugarPath, 'ScriptLibraries'))
output, error = result.communicate()

# Strip out the first line of the output (command line output)
output = '\n'.join(output.splitlines(False)[1:])

# Create an ElementTree from our SOAP response
root = ET.fromstring(output)

# Map our "m:" namespace to its URI, and use standard "all children" prefix
prefix = './/{http://www.w3.org/2005/07/css-validator}'

# Function for finding error and warning information
def parseLineOutput(lists, targetTag):
	errorLists = []
	for list in lists:
		uri = list.findtext(prefix + 'uri').replace('file:', '', 1)
		issues = []
		# Parse through our errors and append them to the list
		for el in list.findall(targetTag):
			issues.append({
				'line': el.findtext(prefix + 'line'),
				'message': el.findtext(prefix + 'message').strip(' \t\n:')
			})
		# Now we have our error list, compile our dictionary
		errorLists.append({
			'uri': uri,
			'list': issues
		})
	return errorLists

# Find our errors and warnings
errorLists = root.findall(prefix + 'errorlist')
warningLists = root.findall(prefix + 'warninglist')

# Parse out our errors and warnings into lists
numErrors = root.findtext(prefix + 'errorcount')
if numErrors == None:
	numErrors = 0
else:
	numErrors = int(numErrors)
errors = []
if numErrors > 0:
	errors = parseLineOutput(errorLists, prefix + 'error')
else:
	numErrors = 0

numWarnings = root.findtext(prefix + 'warningcount')
if numWarnings is None:
	numWarnings = 0
else:
	numWarnings = int(numWarnings)
warnings = []
if numWarnings > 0:
	warnings = parseLineOutput(warningLists, prefix + 'warning')
else:
	numWarnings = 0

htmlOutput = '''<!DOCTYPE HTML>
<html lang="en-US">
<head>
	<meta charset="UTF-8">
	<title>CSS Validation Output</title>
	<link rel="stylesheet" href="Support/styles.css" />
</head>
<body><div id="page">
	<h1>Validation output for "'''

htmlOutput += os.path.basename(filePath) + '"</h1>\n'

htmlOutput += '<h2 class="errors"><strong>' + str(numErrors) + '</strong> errors</h2>\n'
if numErrors > 0:
	htmlOutput += '<ul>\n'
	outputPaths = True if len(errors) > 1 or len(warnings) > 1 else False
	for index, listing in enumerate(errors):
		if outputPaths is True:
			htmlOutput += '<li class="header">' + os.path.relpath(listing['uri'], rootPath) + '</li>'
		for error in listing['list']:
			htmlOutput += '<li><a href="x-espresso://open?filepath=' + urllib.quote(listing['uri']) + '&lines=' + error['line'] + '">Line ' + error['line'] + '</a>: ' + error['message'] + '</li>\n'
	htmlOutput += '</ul>\n'

htmlOutput += '<h2 class="warnings"><strong>' + str(numWarnings) + '</strong> warnings</h2>\n'
if numWarnings > 0:
	htmlOutput += '<ul>\n'
	outputPaths = True if len(errors) > 1 or len(warnings) > 1 else False
	for index, listing in enumerate(warnings):
		if outputPaths is True:
			htmlOutput += '<li class="header">' + os.path.relpath(listing['uri'], rootPath) + '</li>'
		for error in listing['list']:
			htmlOutput += '<li><a href="x-espresso://open?filepath=' + urllib.quote(listing['uri']) + '&lines=' + error['line'] + '">Line ' + error['line'] + '</a>: ' + error['message'] + '</li>\n'
	htmlOutput += '</ul>\n'

htmlOutput += '<div class="footer">Powered by the <a href="http://jigsaw.w3.org/css-validator/">W3C CSS Validation Service</a></div></div></body></html>'

# Debugging
#sys.stderr.write(ET.tostring(root))

# Output our HTML
sys.stdout.write(htmlOutput)