s = "FCIL{G00D_B0Y_M5G}"
for i in range(len(s)):
  c = (ord(s[i]) - i) ^ 20
  print(chr(c), end="")

print()
print(len(s))
s_ = "RVS]cV>=(B,1YF+2#x"
for i in range(len(s_)):
  c = (ord(s_[i]) ^ 20) + i
  print(chr(c), end="")

print()