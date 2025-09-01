from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QMenu
)
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction

import sys

class MainWindow(QMainWindow):
  def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

class OtherWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setMouseTracking(True)
    self.label = QLabel("Click in this window")
    self.label.setMouseTracking(True)
    self.setCentralWidget(self.label)

  def contextMenuEvent(self, event):
    context = QMenu(self)
    context.addAction(QAction("test 1", self))
    context.addAction(QAction("test 2", self))
    context.addAction(QAction("test 3", self))
    context.exec(event.globalPos())

  def mouseMoveEvent(self, event):
    self.label.setText("mouseMoveEvent")

  def mousePressEvent(self, event):
    self.label.setText("mousePressEvent")

  def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

  def mouseDoubleClickEvent(self, e):
    self.label.setText("mouseDoubleClickEvent")


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
# window = MainWindow()
window = MainWindow()
window.show()

# Start the event loop.
app.exec()