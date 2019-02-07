# Hexo Helper

**正在重构 QAQ**

## 运行

如果您选择运行代码，需要安装 Python3 及 pyyaml / eel 等第三方库。
环境配置完成后，运行：
```shell
python3 main.py
```

如果您选择运行二进制包，直接运行即可。

需要注意的是，无论哪种方法，请确保对应目录下有 `config.yml` 文件，且 `config.yml` 文件里的 `hexo-path` 被正确配置，否则程序可能直接闪退。

e.g. `config.yml` 默认配置的路径对应了的场景。
```
- hexo # Hexo 所在目录
  - source
  - themes
  - _config.yml
  - hexo-helper
    - main.py    # 或二进制安装包
    - config.yml
```

成功运行后，请完成 `config.yml` 里的配置以供正常使用。

## 配置

* `hexo-path`
  按照上面所述的方法配置即可
* `command` 部分
  由于作者的电脑是 macOS ，所以只提供了 macOS 下的命令，且默认使用 VSCode 打开文件的。
  如果您是其他系统或想用其他软件打开，请自行修改。

## 二进制包

出于某些原因，暂时只会提供 macOS （理论资瓷 Linux ） 下的二进制安装包。

如果您要自行编译二进制安装包，可以参考以下方法：

1. 您需要安装 PyInstaller 和需要的第三方库
2. 在源代码所在目录运行
   ```shell
   python3 -m eel main.py web --onefile --noconsole
   ```
3. 等待运行完成后可在 `/dist` 目录找到您所需要的包