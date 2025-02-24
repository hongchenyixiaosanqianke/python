

from locust import HttpUser,TaskSet,task
# userTask继承了taskSet，表示该类包含的任务是模拟用户的一系列操作
class Usertask(TaskSet):
    token=''

    @task(1)
    def login(self):
        url='http://10.59.9.14:7003/api/public/login'
        data={"username":"17829189973","password":"123456"}
        res=self.client.post(url=url,json=data)
        tokens=res.json()['data']['token']
        Usertask.token="Bearer"+tokens
        print(res.json)

    @task(1)
    def liebiao(self):
        url='http://10.59.9.14:7003/api/second?page=1&type=0&sort=1'
        self.client.get(url=url)

    @task(1)
    def xiangqing(self):
        url='http://10.59.9.14:7003/api/second/view?id=11'
        self.client.get(url=url)

    @task(1)
    def queren(self):
        url='http://10.59.9.14:7003/api/order/confirm?id=11&type=second&sku_id=&num=1&shipping_type=1'
        tou={'auth-token':Usertask.token}
        self.client.get(url=url,headers=tou)

    @task(1)
    def payment(self):
        url='http://10.59.9.14:7003/api/order/create'
        data={"id":"11","type":"second","address_id":3,"store_id":1,"shipping_type":1,"bonus_id":"0","payment":"balance","remarks":"","source":1,"url":"http://10.59.9.14:7003/wap/pages/cart/confirm?id=11&sku_id=&num=1&type=second","sku_id":"","num":"1"}
        tou={'auth-token':Usertask.token}
        self.client.post(url=url,json=data,headers=tou)

# user 类继承自 HttpUser，表示一个用户，包含了运行任务的相关配置。
class user(HttpUser):
    # 该用户类将执行 Usertask 中定义的所有任务。
    tasks=[Usertask]
    host = "10.59.9.14:7003"
    # 每个任务执行后，用户休眠的时间，单位是毫秒。
    max_wait = 2000
    min_wait = 1000

if __name__ == '__main__':
    import os

    os.system(r"locust -f D:\pythonfiles\Class2209aGrade5\2209A\work\zhuangao3\practice0214.py")

