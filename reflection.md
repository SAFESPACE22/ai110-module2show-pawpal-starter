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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
