from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (QWidget,
                                QPushButton,
                                QHBoxLayout,
                                QCheckBox,
                                QLabel
                            )

from models import TaskStatus

class QTask(QWidget):
    def __init__( self, id, title, description, status, removeFn, change_statusFn, select_taskFn, parent=None):
        super(QTask, self).__init__(parent)

        self.statusChBox = QCheckBox()
        self.statusChBox.setMaximumSize(QSize(25, 20))
        self.statusChBox.setChecked(status == TaskStatus.DONE)
        self.statusChBox.setToolTip("Mark as Completed")
        self.statusChBox.toggled.connect(lambda checked: change_statusFn(id, TaskStatus.DONE if checked else TaskStatus.PENDING))

        self.titleLb = QLabel(title)
        self.titleLb.setMaximumSize(QSize(550, 20))
        self.titleLb.setToolTip(description if description != "" else title)
        self.titleLb.setStyleSheet("QLabel::hover" "{" "font-weight: 600!important;" "}")

        self.removeButton = QPushButton('Remove')
        self.removeButton.setMaximumSize(QSize(60, 42))
        self.removeButton.pressed.connect(lambda: removeFn(id))
        self.removeButton.setToolTip("Remove task")
        self.removeButton.setStyleSheet("background-color: #e7f3fe;" "color: #2784ff;" "font-weight: 600;" "border-radius: 5px;" "font-size: 10px")
        self.removeButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.editButton = QPushButton('Edit')
        self.editButton.setMaximumSize(QSize(60, 42))
        self.editButton.pressed.connect(lambda: select_taskFn(id, title, description, status))
        self.editButton.setToolTip("Edit task")
        self.editButton.setStyleSheet("background-color: #e7f3fe;" "color: #2784ff;" "font-weight: 600;" "border-radius: 5px;" "font-size: 10px")
        self.editButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        layout = QHBoxLayout()



        layout.addWidget(self.statusChBox)
        layout.addWidget(self.titleLb)
        layout.addWidget(self.removeButton)
        layout.addWidget(self.editButton)

        self.setLayout(layout)
