# Python Package Exercise

![CI](https://github.com/swe-students-spring2026/3-package-spotted_hyena/actions/workflows/ci.yml/badge.svg)

Procastinatrix is a lighthearted Python package for procrastinators who still want to feel a little productive.

`procastinatrix` gives you:
- encouraging messages
- fake productive activity suggestions
- snack recommendations based on mood
- break suggestions based on your deadline
and other helpful messages to keep you focused and motivated.

## PyPI

Install from PyPI: https://pypi.org/project/procastinatrix/0.1.1/

```bash
pip install procastinatrix
```

## Importing the Package
 A developer can import the package using:
 ```python
import procastinatrix as lib
```

## Usage and Functions

### `instructions()`
Returns a short summary of the package functions

```python
lib.instructions()
```

### `motivation()`
Returns a random encouraging message

```python
lib.motivation()
```

### `fake_productivity()`
Prompts the user to choose a category and returns an activity in that category

```python
lib.fake_productivity()
```

### `recommend_snack(mood, sweet_level)`
Returns a snack based on mood and sweet level
- mood should be "happy", "stressed", or "sleepy"
- sweet_level should be between 0 and 10

```python
lib.recommend_snack("stressed", 8)
```

### `break_excuse(deadline)`
Suggests a break time based on deadline provided
- deadline: integer representing minutes until the deadline

```python
lib.break_excuse(120)
```

### `procrastination_plan(task, urgency, guilt_level)`
Returns a procrastination strategy based on urgency and guilt level
- task: non-empty string describing the task
- urgency: integer between 0 and 10
- guilt_level: integer between 0 and 10

```python
lib.procrastination_plan("essay", 7, 8)
```

### `reward(snack, task)`
Returns a reward message encouraging the user to complete a task.
- snack: string representing a reward (e.g., "boba")
- task: string describing the task

```python
lib.reward("boba", "essay")
```

### `return_to_work_message(task, break_length)`
Returns a message encouraging the user to return to work after a break.
- task: string describing the task
- break_length: integer representing minutes of the break

```python
lib.return_to_work_message("essay", 20)
```
### Example Program
A complete example program using all package functions is included here:

[`example.py`](./example.py)

Run it with:

```bash
python example.py
```
## Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/swe-students-spring2026/3-package-spotted_hyena.git
cd 3-package-spotted_hyena
```

### 2. Create and activate a virtual environment
On macOS and Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install pipenv build
pipenv install --dev
```

### 4. Run tests
```bash
pipenv run pytest
```

### 5. Build the package
```bash
pipenv run python -m build
```

## Running the Project
Run by importing the package or by running the example package

## Configuration
No configuration is required

## Team Members
- [hrehman1](https://github.com/hrehman1)
- [Sarah Randhawa](https://github.com/sarahrandhawa)
- [Abid](https://github.com/Abid2422)
- [sanabriageorge](https://github.com/sanabriageorge)