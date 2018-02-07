from helperFunct import *


#main area
monitor_count = input('Enter number of monitors: ')
for x in range(1,monitor_count+1):
    #ratio   = ( float(1920) / float(1080))
    #print ratio
    #print( float(27) / ((1 + ratio*ratio )**(1/2)))
    print( (find_height(input("input size of monitor %d: " % x),1080,1920)))
#print( round(find_height(27,1080,1920), 2))
