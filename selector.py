import re
import sys

text = open(sys.argv[1]).read()
emails = re.findall(r"[\w.-_]*@[\w._-]*\.\w{2,3}", text)

f = open(sys.argv[2], 'w')

for email  in emails:

	print >>f, email.replace(":", "")
