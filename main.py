import requests
import os
from datetime import datetime

now = datetime.utcnow().strftime('%Y/%m/%d')

def sendTelegram(urls):
    text = f'''
    ▎ Github Actions | 刷步数 · 每日推送 {now}

    {urls}

    来自 [Github Action](https://github.com/tangwenlongNO1/mimotion/actions)'''
    
    data = {
      "chat": os.environ.get('TELEGRAM_CHAT'),
      "token": os.environ.get('TELEGRAM_TOKEN'),
      "text": text.replace('{{urls}}', "n".join(urls))
    }
    response = requests.post('https://api-wrap.simpread.pro/api/service/telegram', data=data)

    if response.status_code == 200:
        print('sendTelegram success', response)
    else:
        print('sendTelegram error', response)

    
urls = ["www.baidu.com"]
sendTelegram(urls)
