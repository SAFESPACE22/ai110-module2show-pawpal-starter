from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    # 1. Create an Owner
    jordan = Owner(name="Jordan")

    # 2. Create at least two Pets
    mochi = Pet(name="Mochi", species="Dog")
    luna = Pet(name="Luna", species="Cat")

    # 3. Add pets to Owner
    jordan.add_pet(mochi)
    jordan.add_pet(luna)

    # 4. Add tasks out of order with times and one conflict
    mochi.add_task(Task(description="Evening Walk", duration_minutes=30, priority="High", due_time="18:00"))
    mochi.add_task(Task(description="Morning Walk", duration_minutes=30, priority="High", due_time="08:00"))
    mochi.add_task(Task(description="Feed Breakfast", duration_minutes=10, priority="High", due_time="07:30"))
    luna.add_task(Task(description="Clean Litterbox", duration_minutes=15, priority="Medium", due_time="08:00")) # Conflict with Morning Walk
    luna.add_task(Task(description="Play Time", duration_minutes=20, priority="Low")) # No time set

    # 5. Create Scheduler and print schedule
    scheduler = Scheduler(owner=jordan, daily_time_limit=60)
    print(f"--- Today's Schedule for {jordan.name}'s Pets ---")
    schedule = scheduler.generate_schedule()
    for item in schedule:
        print(item)

    # 6. Test recurrence
    print("\n--- Testing Recurrence ---")
    daily_task = Task(description="Daily Vitamin", duration_minutes=5, priority="High", frequency="daily")
    print(f"Original task: {daily_task.description}, Completed: {daily_task.completed}")
    new_task = daily_task.mark_complete()
    print(f"Original task marked complete. Completed: {daily_task.completed}")
    if new_task:
        print(f"New recurring task created: {new_task.description}, Completed: {new_task.completed}")


if __name__ == "__main__":
    main()
