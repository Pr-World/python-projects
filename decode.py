import os
print()
to_encode = input("What to decode? : ")
print("\n-=-=-=- Decoding -=-=-=-")
output = ""

for b in to_encode:
	code = ord(b)
	if (code > 122 or code < 65):
		code = code
	elif code == 65:
		code = 90
	elif code == 97:
		code = 122
	else:
		code-=1
	output+=chr(code)
print("NO ERRORS DETECTED")
print("-=-=-=-=- Decoded -=-=-=-=-")
print("\nDecoded text: {}".format(output))