https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04#creating-a-sample-project

http://dev.splunk.com/view/webframework-djangobindings/SP-CAAAEM5

https://docs.djangoproject.com/en/2.0/intro/tutorial03/

https://stackoverflow.com/questions/11956385/what-is-the-path-for-template-dirs-in-django-settings-py-when-using-virtualenv?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

https://stackoverflow.com/questions/11336548/django-taking-values-from-post-request?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

https://mpld3.github.io/quickstart.html



Design:

Use HTML only for showing the data and getting the data - Dont do any processing on the client
Use Controllers (view.py) to get the data from HTML and give the data to HTML
Best practice: Write separate python files to handle repetitive logic - call the functions in the view.py to make your code neat.



Requirements - install the following before running the code

Django (the web framework - MVC architecture )
pandas (the core dataframe engine)
mpld3 (helps you to visualize PyPlot graphs on browser)
mysql workbench (This will be the client for your mysql DB - Helps you write queries with GUI)
PyMySQL (Python DB driver for MySQL - without this, you cant talk to MySQL)
numpy (dependency for Pandas)
pyplot (For graphs)
SQLAlchemy (for simple DB interfacing)

Steps:

Get the basic framework up and running by going to the Project folder (/home/musigma/Programs/gstinfo  in my case), opening in terminal
and then typing 
python manage.py runserver 0.0.0.0:8000

The above line opens in the localhost at 8000 port


Define your URL mappings in the url.py file at (/home/musigma/Programs/gstinfo/gstinfo in my case)
url(r'^hello/', 'gstinfo.views.hello', name = 'hello')

The above URL mapping will point to a python file called "view" in the same folder, it will search for a method called hello and execute it


Define your templates in a separate folder called templates, put this templates folder in the folder containing manage.py
To make sure Django knows where your templates are, modify the TEMPLATE_DIRS in settings.py

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
         BASE_DIR+'/templates'
    )

For using a post, write a form in HTML and mark the method as post, append the / at the end of the action
pass the {% csrf_token %} in the form to prevent cross site referencing issues

This form hits a URL, django looks up at the URL mapping and then picks up a method in the view.py file.
In that method, get the form parameters that are posted by using requests object and the name of the parameter
name = request.POST.get("firstname")

When you render HTML from the view.py, use this
render(request, 'FileInfo.html', {'name':name})
The above thing renders a http response object, and passes parameters from the view.py to the HTML

In the HTMl use {{ keyName }} to display the data


After the above said stuff are done - lets create the DB in mySQL. Make sure you install mySQL and mySQL workbench on your system

Run the below SQL commands in the mySQL workbench's query window - check if the tables are getting created in the GUI.

CREATE DATABASE `gst` ;

CREATE TABLE `taxinfo` (
  `Item` varchar(45) NOT NULL,
  `Value` float DEFAULT NULL,
  `Taxrate` float DEFAULT NULL,
  `Type` varchar(45) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  PRIMARY KEY (`Item`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;






 
