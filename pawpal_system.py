from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta
@dataclass
class Task:
    """Represents a single care activity with a description, duration, and priority."""
    description: str
    duration_minutes: int
    priority: str
    completed: bool = False
    due_time: Optional[str] = None  # Format: "HH:MM"
    frequency: Optional[str] = None  # e.g., "daily", "weekly"

    def mark_complete(self) -> Optional['Task']:
        """Marks the task as completed. Returns a new Task if recurring."""
        self.completed = True
        if self.frequency == "daily":
            return Task(
                description=self.description,
                duration_minutes=self.duration_minutes,
                priority=self.priority,
                due_time=self.due_time,
                frequency=self.frequency
            )
        return None

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
        
        # Phase 4: Sorting by time
        def get_time_key(task: Task):
            if task.due_time:
                try:
                    return datetime.strptime(task.due_time, "%H:%M")
                except ValueError:
                    return datetime.max
            return datetime.max
            
        pending_tasks = [t for t in all_tasks if not t.completed]
        sorted_tasks = sorted(pending_tasks, key=get_time_key)
        
        # Phase 4: Conflict detection
        conflicts = []
        time_slots = {}
        for task in sorted_tasks:
            if task.due_time:
                if task.due_time in time_slots:
                    conflicts.append(f"Conflict: '{task.description}' overlaps with '{time_slots[task.due_time].description}' at {task.due_time}")
                else:
                    time_slots[task.due_time] = task

        schedule = []
        if conflicts:
            schedule.append("⚠️ WARNING: Time conflicts detected!")
            for conflict in conflicts:
                schedule.append(f"  - {conflict}")
            schedule.append("")

        for task in sorted_tasks:
            status = "[ ]"
            time_str = f" @ {task.due_time}" if task.due_time else ""
            schedule.append(f"{status} {task.description}{time_str} ({task.duration_minutes} min, {task.priority} priority)")
            
        if not schedule:
            return ["No pending tasks scheduled!"]
            
        return schedule
