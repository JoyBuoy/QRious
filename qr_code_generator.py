import pandas as pd
import qrcode
import os

# Read the Excel file
df = pd.read_excel('C:\\Users\\User\\OneDrive - University of Victoria\\Desktop\\qrious\\user_information.xlsx')

# Create a folder to save the QR codes
output_folder = 'C:\\Users\\User\\OneDrive - University of Victoria\\Desktop\\qrious\\qr_codes'
os.makedirs(output_folder, exist_ok=True)

# Generate QR codes for each entry
for index, row in df.iterrows():
    # Construct the data to encode in the QR code
    data = f"Thank you for finding me!\nI belong to:\nUser Name: {row['User Name']}\nEmail: {row['Email']}\nPhone: {row['Phone']}\n"


    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    qr_image.save(f"{output_folder}/qr_code_{index + 1}.png")

print("QR codes generated and saved successfully!")
