import pkgutil

# Pythonのインストールされたパッケージ一覧を取得
[print(module.name) for module in pkgutil.iter_modules()]
