import pandas as pd
import matplotlib.pyplot as plt, mpld3
from gstinfo import taxinfo


def describeValue(fileGot, valueInfo):
    print('Entered dataHandler ')

    # Use pandas to get data from CSV into a dataframe named dataGot
    dataGot = pd.read_csv(fileGot, sep=',')

    # Get the mean, standard deviation, minimum and maximum of Value
    valueMean = dataGot["Value"].mean()
    valueMin = dataGot["Value"].min()
    valueMax = dataGot["Value"].max()
    valueStd = dataGot["Value"].std()
    print("Mean of Value ", valueMean)
    print("Minmum of Value ", valueMin)
    print("Maximum of Value ", valueMax)
    print("Standard Deviation of Value ", valueStd)

    #Assign them to the dictionary which was passed into the function and return it
    valueInfo['mean'] = valueMean
    valueInfo['min'] = valueMin
    valueInfo['max'] = valueMax
    valueInfo['std'] = valueStd

    return valueInfo

def uploadFile(fileGot):
    print('Entered uploadFile ')

    #Use pandas to get data from CSV into a dataframe named dataGot
    dataGot = pd.read_csv(fileGot, sep=',')

    # Get the dataFrame row by row and insert the value
    numberOfRecords = dataGot.__len__()
    print('numberReco ',numberOfRecords)

    for i in range(0, numberOfRecords):

        #Get a row of data from the dataframe
        rowData = dataGot.loc[i, :]

        #Separate each column from the row and insert it into the table
        taxinfo.insertToTable(rowData['Item'],rowData['Value'],rowData['Taxrate'],rowData['Type'])

    print('Data uploaded')

def showGraph():
    print('Entered - showGraph')
    plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    plt.plot([3, 1, 4, 1, 5], [1, 2, 3, 4, 5])
    plt.xlabel('xlabel', fontsize=18)
    plt.ylabel('ylabel', fontsize=18)

    mpld3.show()

def getItemDetail(itemName):
    itemInfo = taxinfo.selectItem(itemName)
    itemDetails = dict(name=None, value=None, taxRate=None, type=None, price=None, message='Item not Found')
    try:
        # I use primary key to get the row, so only one row will be returned. So get the 1st row's first element, second element etc
        itemName = itemInfo[0][0]
        itemValue = itemInfo[0][1]
        itemTaxRate = itemInfo[0][2]
        itemType = itemInfo[0][3]
        itemPrice = itemInfo[0][4]

        # Store the above fetched data into a dictionary and then return it
        itemDetails = dict(name=itemName, value=itemValue, taxRate=itemTaxRate, type=itemType, price=itemPrice, message='Item found' )

    except Exception as e:
        print('getItemDetail Failed: ',e)

    finally:
        return itemDetails

def countItemByType(itemType):
    itemInfo = taxinfo.countItemByType(itemType)

    #Im only interested in the name and price of product
    itemDetails = dict(nameList=None, priceList=None, message='Item not Found')

    itemNameList = []
    itemPriceList = []

    try:
      #Loop through the list of rows returned
      for i in itemInfo:
            #Fetch the item name and price through the loop
            currentItemName = i[0]
            currentItemPrice = i[4]
            print('currentItemName is ',  currentItemName)
            print('currentItemPrice is ', currentItemPrice)

            #Store the values in the corresponding lists
            itemNameList.append(currentItemName)
            itemPriceList.append(currentItemPrice)

    except Exception as e:
        print('countItemByType Failed: ', e)

    finally:
        itemDetails = dict(nameList=itemNameList, priceList=itemPriceList, size = itemNameList.__len__() ,message='Item/s Found')
        return itemDetails

def downloadFile():
    print('Entered downloadFile')
    dataToSend = taxinfo.selectAllData()
    fileToDownload = pd.DataFrame(dataToSend)
    fileToDownload.to_csv('Gst_Price_List.csv', sep=',', header=['Item','Value','Taxrate','Type','Price'], index= False)
    print('Exit downloadFile')
