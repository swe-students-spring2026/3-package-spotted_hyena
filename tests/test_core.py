import pytest
import builtins
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








