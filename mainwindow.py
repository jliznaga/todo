# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QPoint
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsDropShadowEffect)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from qtask import QTask

from models import Task, TaskStatus
from services import TasksService



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show_completed = False
        self.selected_task = None

        self.init_ui()
        self.set_styles()
        self.connect_slots()
        self.fetch_tasks()


    def init_ui(self):
        self.hideNewTaskWrapper()

    def set_styles(self):
        effect = QGraphicsDropShadowEffect(offset=QPoint(3, 3), blurRadius=50, color=QColor("#111"))

        self.setStyleSheet("background-color: #f7f9ff;" "color: rgba(32, 32, 32, 0.75);")
        self.ui.addTaskBtn.setStyleSheet("background-color: #2784ff;" "color: #fff;" "font-weight: 600;" "border-radius: 5px;")
        self.ui.addTaskBtn.setGraphicsEffect(effect)

        self.ui.frame.setStyleSheet("background-color: #fff;" "border-radius: 12px;")
        self.ui.frame.setGraphicsEffect(effect)
        self.ui.newTaskWrapper.setStyleSheet("background-color: #fff;")

        self.ui.scrollArea.setStyleSheet("background-color: #fff;" "border-radius: 12px;" "font-weight: 400;")
        self.ui.scrollArea.setGraphicsEffect(effect)

    def connect_slots(self):
        self.ui.addTaskBtn.pressed.connect(self.showNewTaskWrapper)
        self.ui.createTaskBtn.pressed.connect(self.save)
        self.ui.completedTaskChBx.toggled.connect(lambda checked: self.on_show_completed(checked))

    def showNewTaskWrapper(self):
        self.ui.newTaskWrapper.setVisible(True)
        self.ui.titleEdit.setStyleSheet("border: 2px solid rgb(217, 217, 217);" "border-radius: 4px;" "padding-left: 5px")
        self.ui.descEdit.setStyleSheet("border: 2px solid rgb(217, 217, 217);" "border-radius: 4px;" "padding-left: 5px")
        self.ui.createTaskBtn.setStyleSheet("background-color: #e7f3fe;" "color: #2784ff;" "font-size: 600;" "border-radius: 5px;")

        self.ui.titleEdit.setText("")
        self.ui.descEdit.setText("")
        self.selected_task = None

    def hideNewTaskWrapper(self):
        self.ui.newTaskWrapper.setVisible(False)

    def select_task(self, id, title, description, status):
        self.showNewTaskWrapper()
        self.ui.titleEdit.setText(title)
        self.ui.descEdit.setText(description)
        self.selected_task = (id, title, description, status)

    def update_report(self):
        tasks = TasksService().list()
        pending_task = [task for task in tasks if task[3] == TaskStatus.PENDING]

        self.ui.statusbar.showMessage(f"Pending tasks: {len(pending_task)}    Completed task: {len(tasks) - len(pending_task)}    Total: {len(tasks)} tasks")
        self.ui.statusbar.setStyleSheet("font-size: 12px")

    def fetch_tasks(self):
        while self.ui.formLayout.count() > 0:
            self.ui.formLayout.removeRow(0)

        tasks = TasksService().list()


        for task in tasks:
            if task[3] == TaskStatus.DONE and not self.show_completed:
                continue

            object_name = "taskWrapper-"+str(task[0])
            widget = QTask(task[0], task[1], task[2], task[3], self.remove, self.change_status, self.select_task)
            widget.setObjectName(object_name)

            setattr(self.ui, object_name, widget)
            self.ui.formLayout.addRow(widget)

        self.update_report()


    def save(self):
        title = self.ui.titleEdit.text()
        description = self.ui.descEdit.text()

        if title:
            if self.selected_task:
                TasksService().update(self.selected_task[0], title, description, self.selected_task[3])
                self.selected_task = None
            else:
                TasksService().create(Task(title, description))

            self.ui.titleEdit.setText("")
            self.ui.descEdit.setText("")

            self.fetch_tasks()
            self.hideNewTaskWrapper()

    def remove(self, task_id):
        TasksService().remove(task_id)
        self.fetch_tasks()

    def change_status(self, task_id, status):
        TasksService().change(task_id, status)

        if not self.show_completed and status == TaskStatus.DONE:
            getattr(self.ui, "taskWrapper-"+str(task_id)).setVisible(False)

        self.update_report()

    def on_show_completed(self, checked):
        self.show_completed = checked
        self.fetch_tasks()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
