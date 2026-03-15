from pawpal_system import Task, Pet

def test_task_completion():
    # Verify that calling mark_complete() actually changes the task's status.
    task = Task(description="Morning Walk", duration_minutes=30, priority="High")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True

def test_task_addition():
    # Verify that adding a task to a Pet increases that pet's task count.
    pet = Pet(name="Mochi", species="Dog")
    assert len(pet.tasks) == 0
    
    new_task = Task(description="Drink Water", duration_minutes=5, priority="High")
    pet.add_task(new_task)
    
    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Drink Water"
