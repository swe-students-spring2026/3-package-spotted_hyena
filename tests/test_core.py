import pytest
import builtins
import sys
from procastinatrix.core import *

def test_motivation_returns_string():
    result = motivation()
    assert isinstance(result, str)

def test_motivation_returns_encouragement():
    result = motivation()
    assert result in ENCOURAGEMENTS

def test_instructions():
    result = instructions()
    assert isinstance(result, str)

# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
def test_fake_productivity_quick(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    result = fake_productivity()
    assert result in QUICK_ACTIVITIES

def test_fake_productivity_productive(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "2")
    result = fake_productivity()
    assert result in PRODUCTIVE_ACTIVITIES

def test_fake_productivity_creative(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "3")
    result = fake_productivity()
    assert result in CREATIVE_ACTIVITIES

def test_fake_productivity_social(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "4")
    result = fake_productivity()
    assert result in SOCIAL_ACTIVITIES

def test_fake_productivity_reset(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "5")
    result = fake_productivity()
    assert result in RESET_ACTIVITIES

#Function 2 Tests (Snack Recommender)
happy_sweet= ["cupcake", "ice cream", "bubble tea"]
stressed_sweet= ["brownie", "cookies", "chocolate bar"]
sleepy_sweet= ["banana bread", "pudding", "yogurt"]

happy_salty= ["popcorn", "pretzels", "fries"]
stressed_salty= ["chips", "nachos", "salted nuts"]
sleepy_salty= ["crackers", "toast", "rice cakes"]

@pytest.mark.parametrize("mood", ["happy", "stressed", "sleepy"])
def test_valid_moods_return_string(mood):
    result = recommend_snack(mood, 5)
    assert isinstance(result, str)

@pytest.mark.parametrize("sweet_tooth", [0, 1, 2, 3])
def test_low_sweet_tooth_returns_salty_for_happy(sweet_tooth):
    result= recommend_snack("happy", sweet_tooth)
    assert result in happy_salty

@pytest.mark.parametrize("sweet_tooth", [7, 8, 9, 10])
def test_high_sweet_tooth_returns_sweet_for_happy(sweet_tooth):
    result= recommend_snack("happy", sweet_tooth)
    assert result in happy_sweet

@pytest.mark.parametrize("sweet_tooth", [4, 5, 6])
def test_middle_sweet_tooth_returns_mixed_for_happy(sweet_tooth):
    result= recommend_snack("happy", sweet_tooth)
    assert result in happy_sweet + happy_salty

def test_stressed_low_returns_stressed_salty():
    result= recommend_snack("stressed", 2)
    assert result in stressed_salty

def test_stressed_high_returns_stressed_sweet():
    result= recommend_snack("stressed", 9)
    assert result in stressed_sweet

def test_sleepy_low_returns_sleepy_salty():
    result= recommend_snack("sleepy", 1)
    assert result in sleepy_salty

def test_sleepy_high_returns_sleepy_sweet():
    result= recommend_snack("sleepy", 10)
    assert result in sleepy_sweet

def test_edge_value_zero_is_allowed():
    result= recommend_snack("happy", 0)
    assert isinstance(result, str)

def test_invalid_sweet_tooth_above_range():
    with pytest.raises(ValueError):
        recommend_snack("happy", 11)


def test_invalid_sweet_tooth_below_range():
    with pytest.raises(ValueError):
        recommend_snack("happy", -1)

def test_invalid_mood_raises_error():
    with pytest.raises(ValueError):
        recommend_snack("angry", 5)

@pytest.mark.parametrize("deadline", range(1, 1442))
def test_valid_break_return_string(deadline):
    result = break_excuse(deadline)
    assert isinstance(result, str)

@pytest.mark.parametrize("deadline", range(1, 61))
def test_break_return_for_shortest_deadline(deadline):
    result = break_excuse(deadline)
    assert result == "You don't have time for a break, get to work!"

@pytest.mark.parametrize("deadline", range(61, 121))
def test_break_return_for_short_deadline(deadline):
    result = break_excuse(deadline)
    assert result == "You can take a 5-10 minute break, make sure to set a timer!"

@pytest.mark.parametrize("deadline", range(121, 241))
def test_break_return_for_medium_deadline(deadline):
    result = break_excuse(deadline)
    assert result == "You can take a 10-15 minute break, make sure to set a timer!"

@pytest.mark.parametrize("deadline", range(241, 481))
def test_break_return_for_long_deadline(deadline):
    result = break_excuse(deadline)
    assert result == "You can take a 20-30 minute break, make sure to set a timer!"

@pytest.mark.parametrize("deadline", range(481, 1441))
def test_break_return_for_longer_deadline(deadline):
    result = break_excuse(deadline)
    assert result == "No rush, take an hour long break, or a few 15 minute breaks."

@pytest.mark.parametrize("deadline", range(1441, 1450))
def test_break_return_for_longest_deadline(deadline):
    result = break_excuse(deadline)
    assert result == "It's not due until tomorrow, you have time, get back to it later!"
 
def test_edge_value_one():
    result = break_excuse(1)
    assert isinstance(result, str)

def test_edge_value_max():
    result = break_excuse(sys.maxsize)
    assert isinstance(result, str)

def test_invalid_deadline_below_range():
    with pytest.raises(ValueError):
        break_excuse(0)

# Function 4 Tests (Procrastination Plan)
def test_procrastination_plan_high_urgency_and_guilt():
    result = procrastination_plan("essay", 8, 8)
    assert result == "Open essay, review what needs to be done, and complete one small part to get started."

def test_procrastination_plan_high_urgency_only():
    result = procrastination_plan("project", 7, 3)
    assert result == "You should begin project soon. Consider taking a short reset, then start immediately."

def test_procrastination_plan_high_guilt_only():
    result = procrastination_plan("homework", 2, 9)
    assert result == "If homework is weighing on you, open it and make some visible progress, even if it is small."

def test_procrastination_plan_low_urgency_and_guilt():
    result = procrastination_plan("studying", 2, 2)
    assert result == "Set a clear start time for studying and commit to beginning when that time arrives."

def test_procrastination_plan_invalid_task():
    with pytest.raises(ValueError):
        procrastination_plan("", 5, 5)

def test_procrastination_plan_invalid_urgency():
    with pytest.raises(ValueError):
        procrastination_plan("essay", 11, 5)

def test_procrastination_plan_invalid_guilt():
    with pytest.raises(ValueError):
        procrastination_plan("essay", 5, -1)


# Function 5 Tests (Motivation Line)
def test_motivation_line_returns_string():
    result = motivation_line("chips", "your assignment")
    assert isinstance(result, str)

def test_motivation_line_expected_output():
    result = motivation_line("chips", "your assignment")
    assert result == "Complete your assignment, and you can reward yourself with chips."

def test_motivation_line_invalid_snack():
    with pytest.raises(ValueError):
        motivation_line("", "homework")

def test_motivation_line_invalid_task():
    with pytest.raises(ValueError):
        motivation_line("boba", "")


# Function 6 Tests (Return to Work Message)
def test_return_to_work_message_short_break():
    result = return_to_work_message("coding", 5)
    assert result == "Your break is complete. It is time to return to coding."

def test_return_to_work_message_medium_break():
    result = return_to_work_message("reading", 20)
    assert result == "You've had a long break. Get back to working on reading."

def test_return_to_work_message_long_break():
    result = return_to_work_message("your report", 45)
    assert result == "You have been away for a while. Get started with your report and move it forward."

def test_return_to_work_message_invalid_task():
    with pytest.raises(ValueError):
        return_to_work_message("", 10)

def test_return_to_work_message_invalid_break_length():
    with pytest.raises(ValueError):
        return_to_work_message("essay", -5)






