import random

class BackupTask:
    def __init__(self, task_id, status):
        self.task_id = task_id
        self.status = status

    def retry(self):
        self.status = "Completed" if random.choice([True, False]) else "Failed"

    def __str__(self):
        return f"Task {self.task_id}: {self.status}"

class BackupManagementAgent:
    def __init__(self, tasks):
        self.tasks = tasks

    def scan_and_retry_failed_backups(self):
        for task in self.tasks:
            if task.status == "Failed":
                print(f"Retrying {task.task_id}...")
                task.retry()

    def display_task_statuses(self):
        for task in self.tasks:
            print(task)

tasks = [BackupTask(task_id=i, status=random.choice(["Completed", "Failed"])) for i in range(1, 11)]

agent = BackupManagementAgent(tasks)

print("Initial Task Statuses:")
agent.display_task_statuses()

print("\nRetrying Failed Backups:")
agent.scan_and_retry_failed_backups()

print("\nUpdated Task Statuses:")
agent.display_task_statuses()
