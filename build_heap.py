# python3
import math  # Ar šīs bibliotēkas palīdzību es varu noapaļot skaitli.

def build_heap(data):
    data = [None] + data # es nevaru noteikt pareizo vecāku ja indeksācija sākas no 0 jo floor(2/2) = 1, bet vecāks
    #  ir 0. elements nevis 1. elements, tāpēc es pievienoju masīva sākumā tukšu elementu.

    i = len(data)-1
    swaps = []
    for i in range(i,1,-1):
      while i > 1: 
          if data[i] < data[math.floor(i/2)]:
            data[i],data[math.floor(i/2)] = data[math.floor(i/2)],data[i]
            swaps.append([(math.floor(i/2))-1, i-1])
            i = math.floor(i/2)
          else:
            i = math.floor(i/2)  
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():

    text = input()
    if "I" in text:
       n = int(input("input number of nodes: "))
       data = list(map(int, input().split()))
       assert len(data) == n
       swaps = build_heap(data)
       print(len(swaps))
       for i, j in swaps:
          print(i, j)
    elif "F" in text:
       nosaukums = input()
       fails = open("./tests/"+nosaukums)
       n = fails.readline()
       n = int(n)
       data = list(map(int, fails.readline().split()))
       assert len(data) == n
       swaps = build_heap(data)
       print(len(swaps))
       for i, j in swaps:
          print(i, j)
       fails.close
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    

    # checks if lenght of data is the same as the said lenght
   

    # calls function to assess the data 
    # and give back all swaps
   

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps


if __name__ == "__main__":
    main()
