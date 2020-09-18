x=[]
for line in soup:
    line = line.decode().strip()
    lst = re.findall('[0-9]+', line)
    for number in lst:
        y=int(number)
        x.append(y)

print(sum(x))
