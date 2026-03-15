from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a single care activity with a description, duration, and priority."""
    description: str
    duration_minutes: int
    priority: str
    completed: bool = False

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True

@dataclass
class Pet:
    """Stores pet details and a list of assigned tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Adds a task to this pet's schedule."""
        self.tasks.append(task)

@dataclass
class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Adds a pet to the owner's collection."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Retrieves all tasks for all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

class Scheduler:
    """The 'Brain' that retrieves, organizes, and manages tasks across pets."""
    def __init__(self, owner: Owner, daily_time_limit: int = 60):
        self.owner = owner
        self.daily_time_limit = daily_time_limit

    def generate_schedule(self) -> List[str]:
        """Retrieves and organizes tasks across all pets into a readable list."""
        all_tasks = self.owner.get_all_tasks()
        # For now, we just return them as a list of strings
        schedule = []
        for task in all_tasks:
            status = "[x]" if task.completed else "[ ]"
            schedule.append(f"{status} {task.description} ({task.duration_minutes} min, {task.priority} priority)")
        return schedule
