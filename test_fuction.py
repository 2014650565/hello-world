from test_github import greet,add
import requests


def test_greet():
    assert greet("GitHub") == "Hello, GitHub! 合并两个分支的修改"


def test_add():
    assert add(1,2)==3
    assert add(-1,1)==0




def test_health():
    resp=requests.request(url="http://43.133.227.52/api/health",method="GET")
    assert resp.json()["code"]==0