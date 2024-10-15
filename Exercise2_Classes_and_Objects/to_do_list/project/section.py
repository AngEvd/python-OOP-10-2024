from project.task import Task


class Section:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = list()

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for t in self.tasks:
            if task_name == t.name:
                t.completed = True
                return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        removed_tasks = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self) -> str:
        result = f"Section {self.name}:"
        for t in self.tasks:
            result += f"\n{t.details()}"
        return result
