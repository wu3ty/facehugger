"""
Unit tests for Flask app
"""
from app.main import app, api, HelloWorld, CFG_PORT, NewEndpoint

def test_setup():
    """
    Tests the setup of the API endpoint
    """    
    assert app is not None
    assert api is not None
    assert CFG_PORT == 5000 # required to properly setup preceeding deployment step

    assert HelloWorld is not None
    assert NewEndpoint is not None

def test_endpoint():
    """
    Tests the endpoint contract
    """    
    hello_world = HelloWorld()
    res = hello_world.get()
    assert res['data'] is not None
    t2 = NewEndpoint()
    res = t2.get()
    assert res['data'] is not None
