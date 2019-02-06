# Hexo Helper

**正在重构 QAQ**

## 二进制包

出于某些原因，暂时只会提供 macOS （理论资瓷 Linux ） 下的二进制安装包。

如果您要自行编译二进制安装包，可以参考以下方法：

1. 您需要安装 eel / pyyaml / PyInstaller 等一系列需要的第三方库
2. 在源代码所在目录运行
   ```shell
   python3 -m eel main.py web --onefile --noconsole
   ```
3. 等待运行完成后可在 `/dist` 目录找到您所需要的包