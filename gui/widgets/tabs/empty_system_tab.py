from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog

class EmptySystemsTab(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.systems_tab = QWidget()
        self.init_ui()

    def init_ui(self):
        systems_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()

        label = QLabel("The systems tab is empty. Click the button below to add a new tab or upload an excel file.")

        self.add_tab_button = QPushButton("Add")
        self.add_tab_button.setFixedWidth(100)
        self.upload_file_button = QPushButton("Upload")
        self.upload_file_button.setFixedWidth(100)

        buttons_layout.addWidget(self.add_tab_button)
        buttons_layout.addWidget(self.upload_file_button)
        buttons_layout.setAlignment(Qt.AlignCenter)

        systems_layout.addWidget(label)
        systems_layout.addLayout(buttons_layout)
        systems_layout.setAlignment(Qt.AlignCenter)

        self.systems_tab.setLayout(systems_layout)

    def connect_action_to_add_button(self, action):
        self.add_tab_button.clicked.connect(action)

    def connect_action_to_upload_button(self, action):
        self.upload_file_button.clicked.connect(action)
