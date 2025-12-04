# JustInvest Authentication & RBAC System

## Description

This project implements a simple authentication system with secure and industry standard password storage and hashing mechanisms. 
The password are hashed using SHA-256.

## Usage

1. Unzip the folder
2. cd into the directory
3. touch passwd.txt to create the password file in the directory
4. To run the system, run: python3 main.py
5. To run the tests, run: ./run_tests, while in the project directory
6. To log in to the system as an "Admin", change the role field of one of the user accounts in the password file to "Admin", restart the system, and login as that user
