### Flask框架

#### 1. Flask簡介和url及視圖

##### 1.1 虛擬環境

- 虛擬環境和系統環境(全局環境)的區別
- 虛擬環境的必要性
- 虛擬環境的安裝步驟
  - 首先我們添加一個系統環境變量 [windows path : WORKON_HOME]
  - pip install pipenv
  - 進入到你的項目文件夾中 pipenv shell # 進入虛擬環境
  - 來到pycharm中設置虛擬環境

##### 1.2 Flask介紹和第一個Flask程序

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/') # 路由 : Url
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
```

##### 1.3 設置debug模式

######  1.3.1需要import config

- app.run(debug=True)
- app.config = True
- app.config.update(DEBUG=True)

##### 配置文件

- 寫死的方式︰app.config(DEBUG = True)
- app.config.update(DEBUG = True, SECRECT_KEY = xxxxx)
- 創建一個config.py文件
  - import config
  - app.config.from_object('config')
  - app.config.from_pyfile('config.py', silent=True)

##### 1.4 URL 和視圖
- 函數和URL的映射關系
- string : 默認的資料類型，接受沒有任何斜杠/的字串
- int: 整形
- float: 浮點型。
- path： 和string類似，但是可以傳遞斜杠/。
- uuid： uuid類型的字串。any：可以指定多種路徑
- / 分隔符
- ? 分隔符