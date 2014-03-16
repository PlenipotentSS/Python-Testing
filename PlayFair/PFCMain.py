"""
Main function for PLayFairCipher
"""
import sys
import getopt
from PlayFairCipher import *

def askStart(cipObj):
	var = raw_input("Decode or Encode?: ")
	if (var.lower() == "decode"):
		phrase = raw_input("Phrase to Decode? ")
		#Call PlayFairCipher decode method
		cipObj.decode(phrase)
	elif (var.lower() == "encode"):
		phrase = raw_input("Phrase to Encode? ")
		#Call PlaiFairCipher encode method
		cipObj.encode(phrase)

def runCipher(key):
	cipObj = PlayFairCipher(key)
	cipObj.createMatrix()
	askStart(cipObj)
	for i in range(0,5):
		var = raw_input(">>: ")
		if (var.lower() == "printmatrix"):
			#Call PlayFairCipher decode method
			cipObj.printMatrix()
		elif (var.lower() == "encode"):
			phrase = raw_input("Phrase to Encode? ")
			cipObj.encode(phrase)
		elif (var.lower() == "decode"):
			phrase = raw_input("Phrase to Decode? ")
			cipObj.decode(phrase)
		elif (var.lower() == "exit"):
			sys.exit(2)
		elif (var.lower() == 'new'):
			key = raw_input("New Key? ")
			cipObj.setKey(key)
			cipObj.createMatrix()
			askStart(cipObj)

def main(argv=sys.argv):
	# parse command line options	
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
	except getopt.error, msg:
		print msg
		print "for help use --help"
		sys.exit(2)
	# process options
	for o, a in opts:
		if o in ("-h", "--help"):
			print __doc__
			sys.exit(0)
	# process arguments
	runCipher(argv[1])

if __name__ == "__main__":
	sys.exit(main())
    

    
    