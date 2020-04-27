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

