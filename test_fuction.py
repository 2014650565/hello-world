from test_github import greet,add



def test_greet():
    assert greet("GitHub") == "Hello, GitHub! 合并两个分支的修改"


def test_add():
    assert add(1,2)==3
    assert add(-1,1)==0