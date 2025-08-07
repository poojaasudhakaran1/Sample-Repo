import sys
import base64          
b64_input = sys.stdin.read().strip()
decoded = base64.b64decode(b64_input).decode('utf8'))
print(decoded)