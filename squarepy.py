import time

# settings
width, height = 3, 3  # non square sums broken
start = 1
limit = 9
# init
square = [start for xy in range(width * height)]
# square = [1, 3, 4, 1, 5, 9, 6, 7, 2]
count = (width * height)
total = limit ** count
sums = [0 for ab in range(width + height + 2)]
debug = False


def left(s, amount):
    return s[:amount]


end_time = 0
start_time = time.perf_counter()

loc, iterations = 0, 0
while iterations < total:
    square[0] += 1
    iterations += 1
    if len(set(square)) == len(square):  # check if the square is unique
        x, y = 0, 0
        while x < width:  # columns
            while y < count:
                sums[x] += square[y]
                y += width
            x += 1
            y = x
        x, y = 0, 0
        while y < height:  # rows, ignore y redeclaration warning
            while x < width:
                sums[y + width] += square[x + (width * y)]
                x += 1
            y += 1
            x = 0
        x, y = 0, 0
        while y < height:  # diagonal right to left
            sums[width + height] += square[(width * (y + 1)) - (y + 1)]
            y += 1
        x, y = 0, 0
        while y < height:  # diagonal left to right
            sums[width + height + 1] += square[(width * y) + y]
            y += 1
        result = all(element == sums[0] for element in sums)  # check for a win
        # result = True  # remove
        if result:
            pry, prx = 0, 0  # square printing script --
            buff = ''
            while pry < height:
                while prx < width:
                    buff += str(square[prx + (pry * height)]) + ' '
                    prx += 1
                print(buff)
                pry += 1
                prx = 0
                buff = ''  # --
            print('n=' + str(sums[0]))
            print('')
            # break  # kill the program on win
        sums = [0 for ab in range(width + height + 2)]
    while loc < count:  # cascade the square
        if square[loc] >= limit:
            square[loc] = 1
            loc += 1
        else:
            if loc != 0:
                square[loc] += 1
            break
    loc = 0

end_time = time.perf_counter()
te = str(end_time - start_time).split('.')
print("Elapsed time: " + te[0] + "." + left(te[1], 2) + "s")
print('Finished with: ' + format(iterations, ",") + ' cycles')  # finished
te = str(iterations / end_time).split('.')
print(format(int(te[0]), ",") + ' cycles per second')
