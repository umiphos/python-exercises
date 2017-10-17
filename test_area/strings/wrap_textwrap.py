import textwrap
def wrap(string, max_width):
    return textwrap.wrap(string, max_width)

wrapeated = wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)
for x in wrapeated:
    print x
print textwrap.fill('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)
