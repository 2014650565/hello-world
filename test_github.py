import requests


def test_get_token():
    sess=requests.session()
    resp=sess.post(url="http://43.133.227.52/api/login",json={"username":"tester","password":"123456"})
    assert resp.json()["code"]==0, f"登陆错误,返回码{resp.json()['code']}"

def test_get_products(get_headers):
    sess=requests.session()
    resp=sess.get(url="http://43.133.227.52/api/products",
                  headers=get_headers)
    assert resp.json()["code"]==0,f"获取商品列表错误,返回码{resp.json()['code']}"