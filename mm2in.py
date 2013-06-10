#! /usr/bin/python

import sys
from optparse import OptionParser
import math

# Process command line arguments
usage = "usage: %prog <number of millimeters> *or* <options>"
parser = OptionParser(usage)
parser.add_option('-m', '--mm', action="store", type="int", dest="mm",
	help='millimeters')
parser.add_option('-c', '--cm', action="store", type="int", dest="cm",
	help='centimeters')
parser.add_option('-M', '--m', action="store", type="int", dest="m",
	help='meters')

mm = 0
valueFound = False
if (len(sys.argv) == 2):
	# Only one argument, assume it's millimeters
	try:
		mm += int(sys.argv[1]) # Ignore trailing options
		valueFound = True
	except:
		pass
elif (len(sys.argv) > 2):
	# More than one argument, use the OptionParser
	(options, args) = parser.parse_args()
	if (options.mm):
		mm = options.mm
	if (options.cm):
		mm += options.cm * 10
	if (options.m):
		mm += options.m * 1000
	if (mm > 0):
		valueFound = True

if (len(sys.argv) == 1 or not valueFound):
	parser.print_help()
	sys.exit()

MM_PER_INCH = 25.4
INCHES_PER_MILE = 63360
INCHES_PER_FEET = 12
INCHES_PER_INCH = 1
INCHES_PER_12 = 1/2.0
INCHES_PER_14 = 1/4.0
INCHES_PER_18 = 1/8.0
INCHES_PER_116 = 1/16.0

miles = 0
feet = 0
inches = 0
halfs = 0
quarters = 0
eighths = 0
sixteenths = 0

unaccountedInches = mm / MM_PER_INCH
totalInches = unaccountedInches

def factorOutUnit(inches, inchesPerUnit):
	miles = int(math.floor(inches / inchesPerUnit))
	inchesLeft = inches % inchesPerUnit
	return (miles, inchesLeft)

if (unaccountedInches > 0 and unaccountedInches >= INCHES_PER_MILE):
	(miles, unaccountedInches) = factorOutUnit(unaccountedInches, INCHES_PER_MILE)

if (unaccountedInches > 0 and unaccountedInches >= INCHES_PER_FEET):
	(feet, unaccountedInches) = factorOutUnit(unaccountedInches, INCHES_PER_FEET)

if (unaccountedInches > 0 and unaccountedInches >= INCHES_PER_INCH):
	(inches, unaccountedInches) = factorOutUnit(unaccountedInches, INCHES_PER_INCH)

if (unaccountedInches > 0 and unaccountedInches >= INCHES_PER_12):
	(halfs, unaccountedInches) = factorOutUnit(unaccountedInches, INCHES_PER_12)

if (unaccountedInches > 0 and unaccountedInches >= INCHES_PER_14):
	(quarters, unaccountedInches) = factorOutUnit(unaccountedInches, INCHES_PER_14)

if (unaccountedInches > 0 and unaccountedInches >= INCHES_PER_18):
	(eighths, unaccountedInches) = factorOutUnit(unaccountedInches, INCHES_PER_18)

if (unaccountedInches > 0 and unaccountedInches >= INCHES_PER_116):
	(sixteenths, unaccountedInches) = factorOutUnit(unaccountedInches, INCHES_PER_116)

fractions = ''
if (sixteenths > 0):
	fractions = '%d/16' % ((halfs * 8) + (quarters * 4) + (eighths * 2) + sixteenths)
elif (eighths > 0):
	fractions = '%d/8' % ((halfs * 4) + (quarters * 2) + eighths)
elif (quarters > 0):
	fractions = '%d/4' % ((halfs * 2) + quarters)
elif (halfs > 0):
	fractions = '%d/2' % halfs


# Prepare and print the answer
output = []
if (miles > 0):
	output.append('%d miles' % miles)
if (feet > 0):
	output.append('%d\'' % feet)
if (inches > 0):
	output.append('%d\"' % inches)
if (fractions != ''):
	output.append(fractions)
output.append(' (%d total inches)' % totalInches)

print ' '.join(output)