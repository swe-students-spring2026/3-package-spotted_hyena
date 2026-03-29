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