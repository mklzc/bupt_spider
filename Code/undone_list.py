import requests
import json
login_url = "https://auth.bupt.edu.cn/authserver/login"
user_data = {
    'username': '',
    'password': ''
}

session = requests.Session()
response = session.post(url=login_url, data=user_data)
if response.status_code == 200:
    print("登录成功")
else:
    print(f"登录失败，状态码：{response.status_code}")

resource_url = "https://apiucloud.bupt.edu.cn/ykt-site/site/student/undone?userId=1823312419857879130"

header = {
    'Blade-Auth': ''
}

response = session.get(url=resource_url, headers=header)

undone_json = json.loads(response.text)
undone_list = undone_json["data"]["undoneList"]

for task in undone_list:
    print("Activity Name:", task["activityName"])
    print("End Time:", task["endTime"])
    print("="*40)