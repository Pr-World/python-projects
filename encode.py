import os
print()
to_encode = input("What to encode? : ")
print("\n-=-=-=- Encoding -=-=-=-")
output = ""
warn=0
for b in to_encode:
	code = ord(b)
	if (code > 122 or code < 65) and code != 32:
		warn+=1
		print("WARNING: '{}' considered as invalid char".format(chr(code)))
		code = code
	elif code == 90:
		code = 65
	elif code == 122:
		code = 97
	elif code == 32:
		code = 32
	else:
		code+=1
	output+=chr(code)
if warn > 0:
	print("{} warnings detected".format(warn))
else:
	print("NO WARNINGS OR ERRORS DETECTED")
print("-=-=-=-=- Encoded -=-=-=-=-")
print("\nEncoded text: {}".format(output))