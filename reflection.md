# PawPal+ Project Reflection

## 1. System Design

**Core Actions:**
1. Represent pet care tasks (description, duration, priority).
2. Represent the pet and the owner (basic info and preferences).
3. Build a plan/schedule for a day that chooses and orders tasks based on constraints.

**a. Initial design**

My initial system design uses four main classes:
- **`Task`**: Represents individual activities with metadata (duration, priority).
- **`Pet`**: Groups tasks and stores basic pet info (name, species).
- **`Owner`**: Acts as a container for multiple pets.
- **`Scheduler`**: Contains the logic to sort and filter tasks based on the owner's available time.

The relationships are hierarchical: Owners have Pets, and Pets have Tasks. The Scheduler interacts with the Owner to pull all necessary data.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- **Simple Conflict Detection**: My scheduler currently detects conflicts based on exact start times (e.g., two tasks at 08:00) rather than checking for overlapping durations.
- **Why it's reasonable**: For a pet care app where tasks are often discrete and flexible, alerting the owner of a simultaneous start time is often enough to remind them to stagger the activities. A full-fledged overlap detection algorithm would add significant complexity that may be overkill for a simple daily planning tool.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI for brainstorming the initial classes, generating the Mermaid UML diagram, and scaffolding the Python code.
- **Prompts**: "Based on these core actions, what objects do I need?", "Generate a Mermaid.js class diagram," and "Translate this UML into Python Dataclasses."

**b. Judgment and verification**

- I did not accept the AI's first suggestion for the `Scheduler` logic. It originally proposed a very complex sorting algorithm that I simplified to focus on `due_time` to keep the UI clean and predictable.
- I verified the AI-generated code by running a manual `main.py` demo and automated `pytest` suites.

---

## 4. Testing and Verification

**a. What you tested**

- I tested task completion status, adding tasks to pets, and the sorting/conflict detection logic.
- **Importance**: These tests ensured that the core "brain" of PawPal+ works correctly before connecting it to the UI, preventing bugs from leaking into the user experience.

**b. Confidence**

- I am very confident in the current scheduler. It handles the defined constraints well.
- **Edge Cases**: I would test tasks that span past midnight or tasks with overlapping durations (not just start times) if I had more time.

---

## 5. Reflection

**a. What went well**

- I am most satisfied with the conflict detection logic. It provides immediate value to the user by highlighting scheduling errors.

**b. What you would improve**

- I would improve the UI to allow for better "explanation" of the schedule, perhaps with a timeline view.

**c. Key takeaway**

- Designing the system architecture *before* writing code makes the implementation much smoother and prevents major redesigns later. 

