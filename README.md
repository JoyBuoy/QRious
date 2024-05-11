#  🔳 QRious
QRious is a Python script for generating QR codes from user information stored in an Excel file.

## Features

- Reads user information from an Excel file.
- Generates QR codes for each user.
- Customizes QR code content based on user information.
- Saves QR codes as PNG images.

## Requirements

- Python 3.x
- pandas
- qrcode
- openpyxl (required for reading Excel files)

## Installation

1. Clone the repository:

git clone https://github.com/JoyBuoy/QRious.git


2. Install the required Python libraries:

pip install pandas qrcode openpyxl

## Usage

1. Place your Excel file containing user information in the project directory.

2. Run the script:
python generate_qr_codes.py

3. QR codes will be generated for each user and saved in the `qr_codes` folder.

## Excel File Format

The Excel file should have the following columns:

- User Name
- Email
- Phone Number

## Acknowledgments

- This project was inspired by the need to efficiently generate QR codes for user information.
