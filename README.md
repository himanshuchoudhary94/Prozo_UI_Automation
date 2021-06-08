# Prozo Task

**Abstract**

The goal of this project was to make automation framework for automation of 2 scenarios (Login & Create New Item Form Fill)

**Background**

Website Tested
1. https://swms.prozo.com/auth/login

**Test Cases:**

All the below test cases are according to the criteria mentioned in the task.

Following are the test cases that are implemented in the automation script:

1. **Functional Automation Testing of Domain, Login & Traversal to Create New Task** 
* Tests whether the website opened is correct or not
* Tests whether domain entry point is passed for positive test scenario
* Tests whether correct login password is accepted as positive test scenario
* Tests traversal to create new Item page


2. **Functional Automation Testing of Login Scenario**
* Tests whether empty form is saved or not
* Tests whether alphabetical submission of weight saves the form
* Tests whether alphabetical submission of length saves the form
* Tests whether alphabetical submission of breadth saves the form
* Tests whether alphabetical submission of height saves the form

**Environment**
* Language- Python
* Framework - Pytest
* Model - Selenium Python automation
* Report - pytest-html

**Pre requisites:** Test System should have python 3.6.2+ on it

**Steps to run automation script -**
1. Go to Automation Project https://github.com/himanshuchoudhary94/Prozo_UI_Automation.git
2. Clone it
3. cd projectname/
4. pip install -r requirements.txt
3. Install all the tools mentioned in requirements.txt
4. Run file start_test.bat 
5. HTML Report is generated in the same project in 'reports' Folder along with logs after running start_test.bat

**HTML Report**

HTML report contains all the test cases with their status .You can check the sample report in the same repo.  

**Further Scope**

For Login, few more scenarios that could be covered:
1. After Password reset, old Password should not work, new one should work fine
2. Password should be masked; it must not reveal characters 
3. Password must be stored in DB in encrypted format
4. Blank username and Blank password  should not work
5. SQL injection attacks & XSS should be verified for login
6. Negative test cases for login ID and Password

**Load Testing Assignment**
Locust Script with user behaviour is created and test result need to be compiled.
There is confusion in the problem statement. I'll try to connect and resolve
