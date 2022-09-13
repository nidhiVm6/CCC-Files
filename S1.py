wood = int(input(""))
heights = input("")
widths = input("")
listHeight = []
listWidth = []
newHeight = 0
newWidth = 0
total = 0

for x in range(wood):
    newHeight, heights = heights.split(" ", 1)
    newHeight = int(newHeight)
    listHeight.append(newHeight)
heights = int(heights)
listHeight.append(heights)

for x in range(wood-1):
    newWidth, widths = widths.split(" ", 1)
    newWidth = int(newWidth)
    listWidth.append(newWidth)
widths = int(widths)
listWidth.append(widths)


def calc_area(h1, h2, w):

    if h1 <= h2:
        myArea = h1 * w
        myArea = myArea + ((h2-h1)*w/2)

    else:
        myArea = h2 * w
        myArea = myArea + ((h1-h2)*w/2)

    return myArea


for x in range(wood):

    total = total + calc_area(listHeight[x], listHeight[x+1], listWidth[x])

print(total)