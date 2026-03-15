from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    description: str
    duration_minutes: int
    priority: str
    completed: bool = False

    def mark_complete(self):
        """Method stub for marking a task as complete."""
        pass

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Method stub for adding a task to the pet."""
        pass

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Method stub for adding a pet to the owner."""
        pass

class Scheduler:
    def __init__(self, owner: Owner, daily_time_limit: int = 60):
        self.owner = owner
        self.daily_time_limit = daily_time_limit

    def generate_schedule(self):
        """Method stub for generating the daily schedule."""
        pass
