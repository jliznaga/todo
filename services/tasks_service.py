# This Python file uses the following encoding: utf-8

from models import Task
from repositories import SQliteRepository


class TasksService:
    def __init__(self, repository: SQliteRepository = SQliteRepository()):
        self.repository = repository

    def list(self):
        return self.repository.get_all()

    def create(self, task: Task):
        return self.repository.add(task)

    def update(self, task_id: int, title: str, description: str, status: str):
        return self.repository.update(task_id, title, description, status)

    def change(self, task_id: int, status: str):
        return self.repository.change_status(task_id, status)

    def remove(self, task_id: int):
        return self.repository.delete(task_id)
