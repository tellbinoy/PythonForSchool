import matplotlib.pyplot as plt, mpld3
import numpy as np


def barChartMaker(no = 0, itemNames=[], itemPrices=[] ):

    print('no is ',no)
    print('itemNames is ', itemNames)
    print('itemPrices is ', itemPrices)

    #N is The number of items that you want to show on your graph
    N = no
    ind = np.arange(N) #this will create an array of N items [0,1,..N]
    print('123 ind is ',ind)

    #set the x label
    plt.xlabel('Item', fontsize=24)

    #set the y label
    plt.ylabel('Final Price after GST', fontsize=24)

    #Set the labels of the products
    #itemList = ['G1', 'G2', 'G3','G4']
    itemList = itemNames
    plt.xticks(ind, itemList)
    #plt.xticks([0.5,1.5,2.5], itemList)

    #Set the price of the corresponding product
    #priceList = [3,1,4,2]
    priceList = itemPrices
    #print('priceList is ### ',priceList )
    #print('ind is ### ', ind)
    plt.bar(ind,priceList, width = 0.2)
    mpld3.show()
    return True