num = int(input("Number of your month:"))
def season_events(num):
        list1 = [[12 , 1 , 2], [3 , 4 , 5],
             [6 , 7 , 8], [9 , 10 , 11]]
        
        if num in list1[0]:
            print ("You were botn in Winter, White snow fell outside the window")
        elif num in list1[1]:
            print ("You were born in Spring, Birds sang beautiful songs")
        elif num in list1[2]:
            print ("You were born in Summer, The sun shone brighter than ever")
        elif num in list1[3]:
            print ("You were born in Autumn, The harvest was incredible")
        else:
            print ("You need to enter the real number of the month")


season_events(num)
