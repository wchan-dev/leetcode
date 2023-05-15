def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  leftPointer = 0
  rightPointer = len(arr) - 1
  count = len(arr) - 1
  while leftPointer < rightPointer:
    leftVal = arr[leftPointer] * arr[leftPointer]
    rightVal = arr[rightPointer] * arr[rightPointer]
    if max(leftVal,rightVal) == rightVal:
      squares[count] = rightVal
      count -= 1
      rightPointer -= 1
    elif max(leftVal, rightVal) == leftVal:
      squares[count] = leftVal
      count -= 1
      leftPointer += 1
  return squares



def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
