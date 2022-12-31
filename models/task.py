# This Python file uses the following encoding: utf-8
import enum

class TaskStatus(str, enum.Enum):
    PENDING = 'pending'
    DONE = 'done'


class Task:
    def __init__(self, title, description, status: TaskStatus = TaskStatus.PENDING):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return self.title
