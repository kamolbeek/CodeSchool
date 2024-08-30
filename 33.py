import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, 
QCheckBox, QFormLayout, QRadioButton, QLabel, QLineEdit, QSpinBox, QPushButton)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("So'rovnoma")
        self.setFixedSize(400, 500)
        form = QFormLayout()
        
        # Input fields
        self.name_label = QLabel("Name:")
        self.name = QLineEdit()
        self.name.setPlaceholderText("Write your name")
        form.addRow(self.name_label, self.name)
        
        self.surname_label = QLabel("Surname:")
        self.surname = QLineEdit()
        self.surname.setPlaceholderText("Write your surname")
        form.addRow(self.surname_label, self.surname)
        
        self.age_label = QLabel("Age:")
        self.age = QSpinBox()
        self.age.setValue(25)
        form.addRow(self.age_label, self.age)
        
        self.gender_label = QLabel("Gender: ")
        self.male = QRadioButton("Male")
        self.female = QRadioButton("Female")
        form.addRow(self.gender_label, self.male)
        form.addRow("", self.female)
        
        self.address_label = QLabel("Address:")
        self.address = QComboBox()
        self.address.addItems(["Tashkent", "Samarkand", "Bukhara", "Khorezm", "Shakhrisabz"])
        form.addRow(self.address_label, self.address)
        
        self.phone_label = QLabel("Phone number:")
        self.phone_number = QLineEdit()
        self.phone_number.setPlaceholderText("Write your phone number")
        form.addRow(self.phone_label, self.phone_number)
        
        self.major_label = QLabel("Faculty:")
        self.major = QLineEdit()
        self.major.setPlaceholderText("Write your faculty")
        form.addRow(self.major_label, self.major)
        
        self.course_label = QLabel("Course:")
        self.course = QComboBox()
        self.course.addItems(["1", "2", "3", "4"])
        form.addRow(self.course_label, self.course)
        
        self.check_label = QLabel("Confirmation:")
        self.check = QCheckBox("Confirm")
        form.addRow(self.check_label, self.check)
        
        # Save button
        self.save_button = QPushButton("Save")
        self.save_button.setFixedHeight(50)
        self.save_button.clicked.connect(self.save_data)
        form.addRow(self.save_button)

        # Output labels
        self.output_label = QLabel("")
        form.addRow(self.output_label)
        
        self.setLayout(form)
    
    def save_data(self):
        gender = "Male" if self.male.isChecked() else "Female"
        data = (
            f"Name: {self.name.text()}\n"
            f"Surname: {self.surname.text()}\n"
            f"Age: {self.age.value()}\n"
            f"Gender: {gender}\n"
            f"Address: {self.address.currentText()}\n"
            f"Phone number: {self.phone_number.text()}\n"
            f"Faculty: {self.major.text()}\n"
            f"Course: {self.course.currentText()}\n"
            f"Confirmation: {'Confirmed' if self.check.isChecked() else 'Not Confirmed'}"
        )
        self.output_label.setText(data)

# Create application
app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())