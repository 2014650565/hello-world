import pytest
import requests
@pytest.fixture(scope="session",autouse=True)
def get_headers():
    print("用例开始\n")
    yield {"Authorization":f"Bearer {requests.request(url="http://43.133.227.52/api/login",
                           method="post",
                           json={"username":"tester",
                                 "password":"123456"}).json()["token"]}"}
    print("\n用例结束")