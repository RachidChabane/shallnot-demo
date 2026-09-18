import pytest

from password import is_acceptable


@pytest.mark.verifies("PWD-1~1")
def test_short_passwords_are_rejected():
    assert not is_acceptable("short", username="ada")


@pytest.mark.verifies("PWD-1~1")
def test_long_passwords_are_accepted():
    assert is_acceptable("correct horse battery", username="ada")


@pytest.mark.verifies("PWD-2~1")
def test_passwords_containing_the_username_are_rejected():
    assert not is_acceptable("ada-loves-long-passwords", username="ada")


@pytest.mark.verifies("PWD-2~1")
def test_the_username_is_matched_whatever_its_case():
    assert not is_acceptable("ADA-loves-long-passwords", username="ada")
