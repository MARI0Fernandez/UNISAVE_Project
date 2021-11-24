![Image](file:///Users/mariofernandezmenendez/Desktop/WhatsApp%20Image%202021-11-18%20at%2014.56.39.png)

# UNISAVE

**UNISAVE** is a program developed to help student to manage their budgets, among different categories of expenses.
Their budget is split in four predetermined categories (_University_, _Restaurants & Bars_, _Supermarket_ and _Leisure_), therefore they can 
observe where they are spending the most quantity of money and try to control it.

Our program allows the user to do  the following actions:
1. Obtain the user's QR code to pay.
2. See the user's budgets in each category.
3. Enter more money into a category, in case the user has spent all his money in a specific category.
4. See all the expenses the user has so far and observe two of the following graphs
   1. Expenses the user has had in order to compare the categories
   2. Total spent in each category


## Installation

To be able to run the program, make sure you have the following libraries installed:

+ **Python Programming Language**  
+ **Libraries**. In order to obtain a good performance of the program, you must make use of the following packages (last version):
  + cv2. Download library named `opencv-contrib-python` in python interpreter.
  + numpy. Install package named `numpy` in python interpreter.
  + qrcode.  Download library named `qrcode` in python interpreter.
  + csv. Make sure you already have the library `csv`.
  + pandas. Install package named `pandas` in python interpreter.
  + matplotlib. Download package named `matplotlib` in python interpreter.

Once we have the required libraries downloaded, open the file named "main_code_Unisave.py" and the dataset "infousers.csv".
As well, you should have the folder Images_QRcode open in the same project otherwise the following error will occur:

```
FileNotFoundError: [Errno2] No such file or directory './Images_QRcode/....png"
```

## Usage

Once the user enters the program, he will be asked to enter his NIF number in order to know if 
he is already in the program's system. In case the user is not in it, he will be asked to enter some
information so he can create an account.
* _User inputs_: NIF, Name, Surname, Degree, and Monthly budget.
* _Output_: main  page of the program.

Afterwards, the user will be in the main page of the program with the following actions:
* QRcode to pay.
* Visualize my budget for my categories.
* Earn some money into a category.
* Observe my expenses in a category.

By choosing an option, the user will be directed to different program windows, and whenever the user wants he can 
go back to the main page.

1. **QRcode to pay**. Our function, in this case, displays a customer qrcode of the user, which contains all his information, then he will have to close the page with the qrcode and return to the console, where he will have to input the expense. 

   * _User inputs_: Money spent and category where the user wants to put the expense.
   * _Output_: Message confirming the expense, it will ask if you want to run it again, if not, the user will return to the main page.


2. **Visualize my budget for my categories**. This function will show a table with the different category budgets.

    * _Output_: Table with the budgets and return to the main page.


3. **Earn some money into a category**. For this function, the user will be able to enter an  amount of money into a specific category. The program will show firstly a table with the budgets the user has, so he can see them.

    * _User inputs_: Amount of money to enter and in which category the user wants to put it.
    * _Outputs_: Table with the new budgets, a message confirming the deposit of money. The program will ask again if the user wants to enter more money, if not he will return to the main page.


4. **Observe my expenses in a category**. Our function will show the expenses the user has had and the total sum. As well, it suggests if the user wants to see graphs about his expenses.

    * _User inputs_: In the second part of the function, the program will require a yes or no answer.
    * _Outputs_: Expenses in  each category and the total sum of each. Then, it  will display one of the following charts:
      * Line chart with all the expenses of each category
      * Bar chart with the amount spent in the categories.


## Extra informartion 

In order to carry out the data storage it has been necessary to use Hash table, in order to structure the data and save them.
As well, we have implemented Object-Oriented Programming, so the program runs more dynamically. Through the different classes we create a main one, where all the methods are defined.

We have included some algorithms such as: Insertion, Deletion, Searching

Finally, the system already has a registered user with different expenses so that you can see how each of our functions works. You have to take this into account because the Images_QRcode folder has already the qrcode for this user.



##Credits
This project has been developed by:

Mario Fernández\
Álvaro García \
Emna Bouzguenda\
Juan Antonio Teixidor\
Victoria Sanchez\
German Medina


