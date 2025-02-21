import sys
import os
import qrcode
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

# Function to create necessary folders
def create_qrg_folders():
    base_path = r"C:\QRG"
    subfolders = ["icons", "qr_generated"]

    # Create the base folder if it doesn't exist
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"Folder created: {base_path}")

    # Create subfolders
    for folder in subfolders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Subfolder created: {folder_path}")
        else:
            print(f"Subfolder already exists: {folder_path}")

# Ensure the folders exist before running the application
create_qrg_folders()

class QRGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 500, 600)
        
        # Updated paths
        self.save_path = r"C:\QRG\qr_generated"
        icon_path = r"C:\QRG\icons\qr-code.ico"

        # Set application icon if it exists
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.setup_ui()
        self.center()

    def setup_ui(self):
        self.setStyleSheet("background-color: #E5D0AC;")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Employee Name Input
        name_label = QLabel("Employee Name:")
        name_label.setStyleSheet("font-size: 14pt; color: #6D2323;")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter employee name")
        self.name_edit.setStyleSheet(
            "font-size: 12pt; padding: 5px; background-color: white; color: black; border: 1px solid #6D2323;"
        )
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)
        
        # Employee ID Input
        id_label = QLabel("Employee ID:")
        id_label.setStyleSheet("font-size: 14pt; color: #6D2323;")
        self.id_edit = QLineEdit()
        self.id_edit.setPlaceholderText("Enter employee ID")
        self.id_edit.setStyleSheet(
            "font-size: 12pt; padding: 5px; background-color: white; color: black; border: 1px solid #6D2323;"
        )
        layout.addWidget(id_label)
        layout.addWidget(self.id_edit)
        
        # Generate QR Code Button
        self.generate_button = QPushButton("Generate QR Code")
        self.generate_button.setStyleSheet("""
            QPushButton {
                font-size: 12pt;
                padding: 10px;
                background-color: #6D2323;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #8F3E3E;
            }
        """)
        self.generate_button.clicked.connect(self.generate_qr)
        layout.addWidget(self.generate_button)
        
        # Status Message Label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("font-size: 10pt; color: #6D2323;")
        layout.addWidget(self.status_label)
        
        # Label to Display the Generated QR Code
        self.qr_image_label = QLabel()
        self.qr_image_label.setFixedSize(300, 300)
        self.qr_image_label.setStyleSheet("border: 1px solid #6D2323; background-color: white;")
        layout.addWidget(self.qr_image_label, alignment=Qt.AlignCenter)
        
        central_widget.setLayout(layout)

    def generate_qr(self):
        name = self.name_edit.text().strip()
        emp_id = self.id_edit.text().strip()
        if not name or not emp_id:
            QMessageBox.warning(self, "Input Error", "Please enter both employee name and employee ID.")
            return
        
        # Create QR code from the employee's data
        data = f"name: {name}, id: {emp_id}"
        qr = qrcode.make(data)
        filename = f"{name}_{emp_id}.png"
        filepath = os.path.join(self.save_path, filename)
        qr.save(filepath)
        
        # Update status and display the QR code image
        self.status_label.setText(f"QR code saved at {filepath}")
        pixmap = QPixmap(filepath)
        pixmap = pixmap.scaled(self.qr_image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.qr_image_label.setPixmap(pixmap)
        
        # Reset the input fields after generating the QR code
        self.name_edit.clear()
        self.id_edit.clear()

    def center(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRGenerator()
    window.show()
    sys.exit(app.exec_())
