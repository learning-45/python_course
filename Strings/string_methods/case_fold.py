string_1 = "Strasse"
string_2 = "Straße"

a = string_1.lower()
b = string_2.lower()

print(f"{a} == {b}")

print(a == b)

c = string_1.casefold()
d = string_2.casefold()

print(f"{c} == {d}")

print(c == d)
