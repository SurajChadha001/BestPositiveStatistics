def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)
x=18
y=12
gcd_value=gcd(x,y)
print(f"GCD of")