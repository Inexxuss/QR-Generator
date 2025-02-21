# QR Code Generator

## Description
This is a **QR Code Generator** built using **Python** and **PyQt5**. It allows users to generate QR codes based on an employee's name and ID, saving them automatically in a designated folder.

## Features
- User-friendly GUI built with **PyQt5**.
- Generates QR codes based on employee name and ID.
- Saves QR codes inside the `qr_generated` folder.
- Displays the generated QR code within the application.
- Ensures necessary folders (`C:\QRG`, `C:\QRG\icons`, `C:\QRG\qr_generated`) are created automatically.

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Required Libraries
Install the necessary dependencies by running:
```sh
pip install PyQt5 qrcode[pil] pillow
```

## Setup Instructions
1. **Download or clone** this repository.
2. Run the `QRGenerator.py` script.
3. The script will automatically create the required directories:
   - `C:\QRG` (Main Folder)
   - `C:\QRG\icons` (For storing icons)
   - `C:\QRG\qr_generated` (For storing generated QR codes)
4. **Important:**
   - Download an **icon file (`qr-code.ico`)** for the application.
   - Place the icon inside the `C:\QRG\icons` folder before running the program to ensure the app icon appears correctly.

## Usage
1. Enter the **Employee Name** and **Employee ID** in the provided fields.
2. Click the **"Generate QR Code"** button.
3. The QR code will be displayed and saved inside `C:\QRG\qr_generated`.

## Notes
- If the icon file is missing, the application will still work, but no custom icon will be displayed.
- Generated QR codes are saved in PNG format and named using `EmployeeName_EmployeeID.png`.

## License
This project is **open-source** and free to use.

## Author
Developed by **Tolentino Ian**.

