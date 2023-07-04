import pytest
from app.main import *

def test_setup():
    assert app is not None
    assert api is not None
    assert cfg_port == 5000 # required to properly setup preceeding deployment step

    assert HelloWorld is not None

def test_endpoint():
    hw = HelloWorld()
    res = hw.get()
    assert res['data'] is not None
