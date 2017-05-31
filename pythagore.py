# pythaGORE.py
# calculations with the Pythagorean theorem.

def check() {
  a = input('a = ')
  b = input('b = ')
  c = input('c = ')
  a = float(a)
  b = float(b)
  c = float(c)
  a = a**2
  b = b**2
  c = c**2
  a = eval(a)
  b = eval(b)
  c = eval(c)
  if a + b == c:
    print("This is a right triangle.")
  else:
    print("This is not a right triangle.")
}
