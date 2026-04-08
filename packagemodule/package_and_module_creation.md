::page{title=" Hands-on Lab: Creating a Python Package"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="300" alt="cognitiveclass.ai logo">

## Creating a Python Package

 Estimated time needed: **30** minutes 

 

## Objectives

In this lab you will :

-   Create a module named basic
-   Add two functions to the module basic
-   Create a module named stats
-   Add two functions to the module stats
-   Create a python package named mymath
-   Verify that the package is working

::page{title="Lab"}

### Create Package

* On the window to the right, click on the **View** menu and select **Explorer** option, as shown in the image below.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/menu_explorer.png)

* Your IDE now should look like the image below.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/explorer_view.png)
* On the window to the right, click on the **File** menu and select **New Folder** option, as shown in the image below.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/menu_new_folder.png)
* Enter **mymath** and click OK as shown in the image below.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/new_folder_popup.png)

::page{title="Create the first module"}

* Create a python module named basic

Create a file named **basic.py**.

Copy and paste the below code into basic.py

```python
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2

def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2

def add(a, b):
    """
    This function returns the sum of given numbers
    """
    return a + b
```

You should see a screen like this now.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/basic_py_screenshot.png">

Save the file **basic.py**

::page{title="Create the second module"}

* Create a module named stats

Create a file named **stats.py** and copy and paste the below code into `stats.py`:

```python
def mean(numbers):
    """
    This function returns the mean of the given list of numbers.
    """
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    This function returns the median of the given list of numbers.
    """
    numbers.sort()

    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers) // 2]
        median2 = numbers[len(numbers) // 2 - 1]
        mymedian = (median1 + median2) / 2
    else:
        mymedian = numbers[len(numbers) // 2]

    return mymedian
```
You should see a screen like this now.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/statspy_screenshot.png">

Save the file **stats.py**
### Understanding the code

**`mean` function:** This function takes a list of numbers and returns their average. It uses Python's built-in `sum()` to add all values in the list and `len()` to get the count of elements, then divides the two to produce the mean.

**`median` function:** This function takes a list of numbers and returns the middle value. It begins by sorting the list in ascending order using `sort()`, since the median is position-dependent. It then checks whether the list has an even or odd number of elements. If the count is even, there is no single middle value, so it picks the two middle elements using index positions `len(numbers) // 2` and `len(numbers) // 2 - 1`, and returns their average. If the count is odd, there is a single middle element, and it is returned directly using index `len(numbers) // 2`.

::page{title="Create __init__.py"}

* Create the file `__init__.py`

Copy and paste the below code into `__init__.py`

```
from . import basic
from . import stats
```

Save the file `__init__.py`

Now your directory structure should look like

```
mymath
mymath/__init__.py
mymath/basic.py
mymath/stats.py
```

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/dir_structure.png)

You are done creating a package

::page{title="Verify the package"}

* On the window to the right, click on the **Terminal** menu and select **New Terminal** option, as shown in the image below.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/X_1sjVmIWemuP4ArDuDvVg/new-terminal.png)

* You will see a terminal open up on the bottom of the screen like the one in the image below.<br>
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/new_terminal.png)<br>
* At the terminal type **python3** to invoke python interpreter.
* Once the python interpreter is loaded.
* At the python prompt type **import mymath**
* If the above command runs without errors, it is an indication that the mymath package is successfully loaded.
* At the python prompt type **mymath.basic.add(3,4)**
* You should see an output *7* on the screen.
* At the python prompt type **mymath.stats.mean([3,4,5])**
* You should see an output *4.0* on the screen.
* Type **exit()** to quit python interpreter.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/package_testing.png)

::page{title="Practice Exercise"}

### Create a new module named geometry and add to the mymath package.

* Create a module name geometry
* Add a function named `area_of_rectangle` that takes length and breadth as input and returns the area of a rectangle.
* Add a function named `area_of_circle` that takes radius as input and returns the area of a circle.
* Modify the `__init__.py` to include this module.
* Import and test the function `area_of_circle` from python terminal.

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

<!---## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2020-11-25        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
| 2022-10-21 | 1.0 | Ratima | Updated Skill Network Logo screenshot|
|2026-03-24  |0.2   |Rajashree | Removed unnecessary inline comments from stats.py. Added a separate "Understanding the code" explanation. And corrected the stats file name error | --->

<h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>
 
 This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).


### Congratulations! You have completed this module. At this point, you know that: 

**1) The PEP8 guidelines for code readability include the following:**

* Four spaces for indentation

* Blank lines to separate functions and classes 

* Spaces around operators and after commas

**2) The PEP8 coding conventions for consistency and manageability include:**

* Add larger blocks of code inside functions

* Name functions and files using lowercase with underscores

* Name classes using CamelCase

* Name constants in capital letters with underscores separating words

**3) To ensure that your code adheres to the predefined style and standard without executing the code, you can use the Static code analysis method.**

**4) Unit testing is a method to validate if code units are operating as designed. You must test every unit before integration with the final codebase.**

**5) To create a package:**

* Create a folder with the package name

* Create an empty __init__.py file

* Create the required modules

* In the __init__.py file, add code to reference the modules needed in the package

**6) You can verify the package via the bash terminal in a Python shell.**