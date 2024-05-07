import time
import requests


def test_function(prompt,history):
    # 发送POST请求
 
    url = "http://localhost:8888"  # API的地址
    data = {
        "prompt": prompt,
        "history": history,  # 历史对话，如果有的话，这里初始化为一个空列表
        "max_length": 2048,  # 最大生成长度
        "top_p": 0.7,  # Top-p采样参数
        "temperature": 0.95  # 温度参数
    }
    response = requests.post(url, json=data)
 
    # 解析响应
    if response.status_code == 200:
        answer = response.json()
        # print("Response:", answer["response"])
        # print("History:", answer["history"])
        # print("Status:", answer["status"])
        # print("Time:", answer["time"])
    else:
        print("Request failed:", response.text)

    return answer["response"],answer["history"]


history=[]
if __name__ == '__main__':
    
    while True:
        time_start = time.time()
        response ,history = test_function(input("Question:"),history)
        print('Answer:',response)
        time_end=time.time()
        print("测试时间"+str(time_end-time_start))