
#for x in range(1 , 11):
    #for y in range(1 , 11):
        #z = x*y

        #if z % 3 == 1:
            #print("O", end = "\t")
        #else:
            #print(z, end = "\t")
    #print()

for x in range(1 , 11):
    for y in range(1 , 11):


        if x*y % 2 == 0:
            print("E",end="\t")
        else:
            print(x*y, end = "\t")
    print()