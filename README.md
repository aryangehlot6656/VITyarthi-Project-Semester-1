# VITyarthi-Project-Semester-1
 Eco-Route Emission Tracker
A beginner friendly python project that compares three travel routes using distance, traffic levels and vehicle type to calculate estimated carbon emissions and recommend the most eco friendly options.
1.	Project Title:
Eco-Route Emission Tracker: A Python Based Carbon Emission Comparison Tool.
2.	Overview of the Project:
The Eco-Route Emission Tracker is a Python application designed to help users identify the most environmentally friendly travel route based on distance, traffic levels, and vehicle type. The program calculates the estimated carbon emissions for three user-defined routes and recommends the route with the lowest environmental impact.
This project demonstrates real-world problem solving using basic Python concepts such as user input, functions, conditional logic, data validation, and simple computation.

3.	 Features:
a)	Vehicle Type Selection: Choose between CNG, Petrol, or Diesel.
b)	Route Comparison: Enter distance and traffic level for three routes.
c)	Carbon Emission Calculation: Automatically computes emissions using a simple formula.
d)	Traffic Multipliers: Low, Medium, and High traffic levels affect emissions.
e)	Intelligent Recommendation System: Suggests the most eco-friendly route. Includes tie-breaker logic when routes produce equal emissions.
f)	 Clean Summary Table: Displays all route details and emissions clearly.
g)	 Error Handling: Manages invalid inputs gracefully.

4.	Technologies / Tools Used:
Programming Language: Python 3
Libraries: No external libraries required (only built-in Python functions)
Environment: Works in any Python-compatible environment (VS Code, PyCharm, Jupyter, Terminal)

5.	Steps to Install & Run the Project

1.	 Install Python: Make sure Python 3.x is installed on your system. 
Download from: https://www.python.org/downloads/

2.	 Clone or Download the Repository:   https://github.com/aryangehlot6656/VITyarthi-Project-Semester-1.git

3.	 Run the Python Script: Navigate to the project folder and run: Code.py

4.	 Follow On-Screen Instructions:  The program will:
a)	Ask for vehicle type
b)	Ask for distance of Route A, B, C
c)	Ask for traffic levels
d)	Calculate carbon emissions
e)	Show the most eco-friendly route

6.	 Instructions for Testing:
To properly test the program:
 Test 1: Different Distances: Enter three routes with different distances and observe emission changes.
 Test 2: Different Traffic Levels: Try keeping distances same but changing traffic intensity to see the multiplier effect.
 Test 3: Vehicle Type Impact: Run the program three times, once each for CNG, Petrol, Diesel, to compare emissions.
Test 4: Tie-Breaker Handling: Enter identical distances and identical traffic for all three routes. The program must recommend the route with moderate distance + moderate traffic.
 Test 5: Invalid Inputs. Enter non-numeric values or invalid options to verify error handling.

