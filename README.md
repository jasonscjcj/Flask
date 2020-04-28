# Flask 框架

## 安裝

```
pip install pipenv
```

## 創建虛擬環境

```
pipenv shell	# 進入虛擬環境

pip install flask	# 在shell入面安裝flask

pip list	# 查看安裝了什麼

pipenv install --dev 框架名字	#記錄安裝了什麼到Pipfile

exit	# 離開虛擬環境

pipenv --rm	# 刪除虛擬環境，但不會刪除pipfile

```

## pipenv command

```
$ pipenv Usage: pipenv [OPTIONS] COMMAND [ARGS]...
Options: 
--where 顯示項目文件所在路徑
--venv 顯示虛擬環境實際文件所在路徑
--py 顯示虛擬環境Python解釋器所在路徑
--envs 顯示虛擬環境的選項變量
--rm 刪除虛擬環境
--bare 最小化輸出
--completion 完整輸出
--man 顯示幫助頁面
--three / --two 使用Python 3/2創建虛擬環境（注意本機已安裝的Python版本） 
--python TEXT 指定某個Python版本作為虛擬環境的安裝源
--site-packages 附帶安裝原Python解釋器中的第三方庫
--jumbotron An easter egg, effectively. 
--version 版本信息
-h, --help 幫助信息
```

## Pipfile

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple" #指定pip源
verify_ssl = true

[dev-packages]	# 開發環境

[packages]	# 生產環境

[requires]	# Python版本
python_version = "3.8"
```

# Debug Mode
## 方法1

```python
app.debug = True
app.run()
```
## 方法2

```python
app.run(debug=True)
```
## 方法3

```python
app.config.update(DEBUG=True)
```
## 方法4

```python
# 使用自定義config file，需要import config
# 4.1 通過模組字串
app.config.from_object(config)
# 4.2 通過模組物件
import config
app.config.from_object('config')
# 4.3
app.config.from_pyfile('config.py', silent=True)
# 4.4
app.config.from_pyfile('config.ini', silent=True)
```

開啟了Debug Mode的畫面

```
* Serving Flask app "firstFlask" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 202-551-615
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

# URL 與 視圖

```
string : 默認的資料類型，接受沒有任何斜杠/的字串
int: 整形
float: 浮點型。
path： 和string類似，但是可以傳遞斜杠/。
uuid： uuid類型的字串。any：可以指定多種路徑
```
