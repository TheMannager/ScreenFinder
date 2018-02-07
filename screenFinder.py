from helperFunct import *


#main area
monitor_count = input('Enter number of monitors: ')
for x in range(1,monitor_count+1):
    print( (find_height(input("input size of monitor %d: " % x),input("input vertical resolution of monitor %d: " % x),input("input horizontal resolution of monitor %d: " % x))))
#print( round(find_height(27,1080,1920), 2))
