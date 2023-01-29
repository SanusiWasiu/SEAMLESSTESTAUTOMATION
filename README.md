# SEAMLESSTESTAUTOMATION
This is an automation framework carried out with Selenium tool and Python programming language. This is inspired by a test by seamlessHR recruiting process. 
The Login.py file is a script to test valid log in to the given url while invalidlogin.py is a script to test an invalid login

## Steps to use this repository
1. Clone the repository
2. install selenium
3. Run on your IDE (Pycharm, VS Code)

## Question
Using selenium and any programming language of your choice, interact with the GUI of this website (https://the-internet.herokuapp.com/) and perform the following actions.

Question 1: Write a test script to test valid log in. 
Steps: 
1. Click “Form Authentication” 
2. Enter tomsmith for the username and SuperSecretPassword! for the password 
3. Assert the success message “You logged into a secure area!” 

Question 2: Write a test script for invalid log in 
Steps: 
1. Load url 
2. Click “Form Authentication” 
3. Enter thomas for the username and SecretPassword! for the password 
4. Assert the error message “Your username is invalid!”