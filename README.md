# Week 7: Secure Authentication System

Student Name: Hana Fathima
Student ID: M01093595
Course: CST1510 - CW2 - Multi-Domain Intelligence Platform

## Project Description
This project is a command-line secure authentication system built using Python.
It allows users to register and log in securely using hashed passwords.

## Features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data storage

## Technical Implementation
- Hashing Algorithm: bcrypt
- Data Storage: Plain text file (`users.txt`)
- Password Security: One-way hashing, no plaintext password storage
- Username Validation: 3–20 alphanumeric characters
- Password Validation: 6–50 characters with uppercase letters and digits
