README.MD

Overview of your solution 
This is a short description about the content of my project. 

Content
This proyect has two branches: test contains the tests of the repositories and manin contains all project .

Solution
The solution was developed in python and unit tests in Python Unittest.
For the solution, use two lists to enter the employees and a third list to save the same data between the first two lists.
A for loop was created that goes through list one and then an If statement is made that checks if there is an equal element in list two that belongs to list one, and that data is saved in a third list

How to run the program locally. 

You must first clone the repository on GITHUB or download the .py files.

Second, to run the exercise named Exer.PY, you must open it in a source code editor such as Visual Studio Code or if you have Python3 installed on your computer, double-click on the file Exer.PY.

Third, to perform the Unittest tests, you must perform them in the source code editor, Visual Studio Code.


Examples:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3