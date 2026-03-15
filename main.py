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

    # 4. Add at least three Tasks with different times/priorities
    mochi.add_task(Task(description="Morning Walk", duration_minutes=30, priority="High"))
    mochi.add_task(Task(description="Feed Breakfast", duration_minutes=10, priority="High"))
    luna.add_task(Task(description="Clean Litterbox", duration_minutes=15, priority="Medium"))

    # 5. Create Scheduler and print schedule
    scheduler = Scheduler(owner=jordan, daily_time_limit=60)
    print(f"--- Today's Schedule for {jordan.name}'s Pets ---")
    schedule = scheduler.generate_schedule()
    for item in schedule:
        print(item)

if __name__ == "__main__":
    main()
