import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class SimpleInterface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple Interface')
        self.setGeometry(0, 0, 480, 320)
        self.showMaximized()

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)  # Align elements vertically in the center
        layout.setSpacing(20)  # Set vertical spacing between elements

        # On/Off Button
        self.on_off_button = QPushButton('On')
        self.on_off_button.setCheckable(True)
        self.on_off_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px; border-radius: 5px; }"
                                         "QPushButton:checked { background-color: #f44336; }")
        self.on_off_button.clicked.connect(self.on_off_button_clicked)
        layout.addWidget(self.on_off_button, alignment=Qt.AlignHCenter)  # Align button in the center horizontally

        # Label for Brightness Slider
        brightness_label = QLabel('Brightness Slider')
        brightness_label.setAlignment(Qt.AlignHCenter)  # Align label text in the center horizontally
        layout.addWidget(brightness_label, alignment=Qt.AlignHCenter)  # Align label in the center horizontally

        # Brightness Slider
        self.brightness_slider = QSlider()
        self.brightness_slider.setOrientation(1)  # Vertical orientation
        layout.addWidget(self.brightness_slider, alignment=Qt.AlignHCenter)  # Align slider in the center horizontally

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("QTabWidget::pane { border: none; }"
                                "QTabBar::tab { background-color: #333; color: white; padding: 10px; }"
                                "QTabBar::tab:selected { background-color: #555; }")
        solid_tab = QWidget()
        gradient_tab = QWidget()
        rainbow_tab = QWidget()
        cycle_tab = QWidget()
        music_tab = QWidget()

        self.tabs.addTab(solid_tab, 'Solid')
        self.tabs.addTab(gradient_tab, 'Gradient')
        self.tabs.addTab(rainbow_tab, 'Rainbow')
        self.tabs.addTab(cycle_tab, 'Cycle')
        self.tabs.addTab(music_tab, 'Music')

        layout.addWidget(self.tabs, alignment=Qt.AlignHCenter)  # Align tabs in the center horizontally

        main_widget.setLayout(layout)
        main_widget.setStyleSheet("background-color: #222; color: white;")


    def on_off_button_clicked(self):
        if self.on_off_button.isChecked():
            self.on_off_button.setText('Off')
        else:
            self.on_off_button.setText('On')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleInterface()
    window.show()
    sys.exit(app.exec_())
