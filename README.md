# CE305 Homework 1

## Student Information
- Name: [Your Name]
- Student ID: [Your Student ID]
- Course: CE305 - Computer Organization

---

## Overview
This project contains solutions for Homework #1. It includes:
1. Base conversion between different number systems with validation
2. Conversion of a floating decimal number into a 14-bit floating-point representation

---

## Question 1: Base Conversion

### Description
This program converts a number from any base to another base. It first checks if the input is valid. If any digit is greater than or equal to the base, the program returns an error message.

### Key Features
- Supports digits greater than 9 using hyphen format (e.g., `-16-`)
- Validates input before conversion
- Converts through base 10 as an intermediate step

### Example

Input: base_conv("123-45-6", 46, 23)
Output: -16-16-15-21-6


---

## Question 2: 14-bit Floating Point Model

### Description
This program converts a floating decimal number into a 14-bit binary representation.

### Format
- 1 bit: Sign (0 = positive, 1 = negative)
- 5 bits: Exponent (with bias)
- 8 bits: Significand (mantissa)

### Example

Input: floating_model(-26.625)
Output: 1_10101_11010101


---

## Project Structure

CE305_week1/
│
├── q1_base_conversion.py
├── q2_floating_model.py
├── main.py
├── README.md


---

## How to Run
1. Open the project folder in VS Code
2. Open the terminal
3. Run:

python main.py


---

## Notes
- Digits greater than or equal to 10 are enclosed in hyphens (e.g., `-16-`)
- Digits less than 10 are written normally
- The program validates all inputs before performing conversions