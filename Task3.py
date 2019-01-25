s = input("Input a string")
d=l=m=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        m=m+1;

print("Letters", l)
print("Digits", d)
print("Words", m+1)