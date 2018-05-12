from django.http import HttpResponse
from django.shortcuts import render
from gstinfo import dataHandler
from gstinfo import barchartmaker

#@render_to('gstinfo:template_name.html')
#@login_required
def hello(request):
        html = "<html><body>The time is now.</body></html>"
	return HttpResponse(html)

def landing(request):
	print("Entered - Landing")
	question = 'To be or not to be'
	return render(request, 'landing.html', {'question': question})

def valueStat(request):
	print("Entered - readFile")

	#read the file
	fileGot = request.FILES["csv_file"]

	#Check if the file has a CSV extension, if not - send an error
	if not fileGot.name.endswith('.csv'):
		return render(request, '.html', {'message':'File is not a csv'})

	#prepare the dictionary to get the data
	valueInfo = dict(mean=0, min=0, max=0, std=0)
	valueInfo = dataHandler.describeValue(fileGot, valueInfo)
	print('valueInfo got is ',valueInfo)
	return render(request, 'ValueInfo.html', {'message':'Here is the details about the Value column of the CSV File', 'mean':valueInfo['mean']  ,'min':valueInfo['min'] ,'max':valueInfo['max'] ,'std':valueInfo['std'] })

def uploadData(request):
	print('Entered uploadData')
	fileGot = request.FILES["csv_file"]

	# Check if the file has a CSV extension, if not - send an error
	if not fileGot.name.endswith('.csv'):
		print('Exit - uploadData')
		return render(request, 'FileInfo.html', {'message': 'File is not a csv'})

	#Call the datahandler to upload the file
	status = dataHandler.uploadFile(fileGot)
	print('Exit - uploadData')
	return render(request, 'FileUpload.html'
				  )

def getItem(request):
	print('Entered getItem ')
	itemName = request.GET['itemName']
	print('ItemName got from the form is ',itemName)
	itemDetails = dataHandler.getItemDetail(itemName)
	print('Exit - getItem')
	return render(request, 'ItemDetail.html',
				  {'itemName':itemName,
				   'itemValue':itemDetails['value'],
				   'itemTaxRate':itemDetails['taxRate'],
				   'itemType': itemDetails['type'],
				   'itemPrice': itemDetails['price'],
				   'message':itemDetails['message']
				   }
				  )

def showGraph(request):
	print('Entered showGraph ')
	itemType = request.GET['itemType']
	itemDetails = dataHandler.countItemByType(itemType)

	#Call the graph with the item details if the list is > 0
	if itemDetails['size'] > 0:
		print(' Size is > 0 ')
		result = barchartmaker.barChartMaker(no=itemDetails['size'], itemNames=itemDetails['nameList'], itemPrices=itemDetails['priceList'])
		print('Exit - showGraph')
		render(request, 'FileUpload.html'
		   )
	else:
		print(' Size is 0 ')
		message = 'No items found'
		print('Exit - showGraph')
	return render(request, 'landing.html')

def downloadData(request):
	print('Entry - downloadData')
	dataHandler.downloadFile()
	print('Exit - downloadData')
	return render(request, 'FileDownload.html')



