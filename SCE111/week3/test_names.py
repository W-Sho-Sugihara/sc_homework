import pytest
from names import make_full_name, extract_family_name, extract_given_name

def test_make_full_name():
    assert make_full_name("Joseph", "Smith") == "Smith; Joseph"

def test_extract_family_name():
    assert extract_family_name(make_full_name("Joseph", "Smith")) == "Smith"

def test_extract_given_name():
    assert extract_given_name(make_full_name("Joseph", "Smith")) == "Joseph"
    
pytest.main(["-v", "--tb=line", "-rN", __file__])
