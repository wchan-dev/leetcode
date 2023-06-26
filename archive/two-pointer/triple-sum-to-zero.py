#Given an array of unarr numbers, find all unique triplets in it that add up to zero.

#nput: [-3, 0, 1, 2, -1, 1, -2]
#Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
#Explanation: There are four unique triplets whose sum is equal to zero. smallest sum.'

#sortedArray: [-3,-2,-1,0,1,1,2]

def search_triplets(arr):
  arr.sort()

  triplets = []

  i = 0
  lp = i + 1
  rp = len(arr) - 1


  while i < len(arr) - 3:
    while lp < rp:
        sum = arr[lp] + arr[rp]
        target = arr[i]
        if target + sum == 0:
            triple = [arr[i],arr[lp],arr[rp]]
            triplets.append(triple)
            lp += 1
            rp -= 1
        elif target + sum > 0:
            if arr[rp - 1] == arr[rp]:
                while arr[rp - 1] == arr[rp]:
                    rp -= 1
            else:
                rp -= 1
        elif target + sum < 0:
            if arr[lp + 1] == arr[lp]:
                while arr[lp + 1] == arr[lp]:
                    lp += 1
            else:
                lp += 1
    if arr[i + 1] == arr[i]:
        while arr[i + 1] ==  arr[i]:
            i += 1
    else:
        i += 1
    lp = i + 1
    rp = len(arr) - 1
    

  return triplets



def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()

#[-3,-2,-1,0,1,2]