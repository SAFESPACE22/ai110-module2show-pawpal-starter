import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler
st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

# --- Step 2: Manage Application "Memory" ---
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name)

# Ensure there's a pet for this demo
if not st.session_state.owner.pets:
    initial_pet = Pet(name=pet_name, species=species)
    st.session_state.owner.add_pet(initial_pet)

# For this demo, we'll just work with the first pet
current_pet = st.session_state.owner.pets[0]

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

col4, col5 = st.columns(2)
with col4:
    due_time = st.text_input("Due Time (HH:MM)", value="08:00")
with col5:
    frequency = st.selectbox("Frequency", ["once", "daily"], index=0)

if st.button("Add task"):
    new_task = Task(
        description=task_title, 
        duration_minutes=int(duration), 
        priority=priority,
        due_time=due_time if due_time else None,
        frequency=frequency if frequency != "once" else None
    )
    current_pet.add_task(new_task)
    st.success(f"Added task: {task_title} for {current_pet.name}!")

if current_pet.tasks:
    st.write(f"Current tasks for {current_pet.name}:")
    # Display as a table for readability
    task_data = [
        {
            "Description": t.description, 
            "Time": t.due_time or "Not set",
            "Duration": t.duration_minutes, 
            "Priority": t.priority, 
            "Frequency": t.frequency or "Once",
            "Status": "Done" if t.completed else "Pending"
        }
        for t in current_pet.tasks
    ]
    st.table(task_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner=st.session_state.owner)
    schedule = scheduler.generate_schedule()
    
    st.header(f"Schedule for {st.session_state.owner.name}'s Pets")
    for item in schedule:
        if "WARNING" in item or "Conflict" in item:
            st.error(item)
        else:
            st.write(item)
