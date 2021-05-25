def intInput():
    index = int(input("Enter an index: "))
    return index


def getData( index ):
  data = [10,20,30,40,50]
  return data[index]

def printRes():
   print(getData(index))

while True:
    try:
        index = intInput()
        data     = getData( index )
        printRes()
        break
    except ValueError:
        print("index cannot be something else than an integer")
    except IndexError:
        print("an index value cannot be outside the list")
