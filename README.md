NJUPT 手机验证码发送工具 📱✨
该工具用于通过 Python 发送手机验证码，适用于 NJUPT（南京邮电大学）账号登录。📝

使用指南 🛠️
1. 安装依赖库 📦
首先，你需要确保安装了 requests 库，这是用于发送 HTTP 请求的库。如果尚未安装，可以通过以下命令安装：

bash
复制代码
pip install requests
✅ 安装完成后，继续下一步！

2. 下载 Python 脚本 📥
下载并保存 send_verification_code.py 脚本文件。确保将该文件存储在你希望运行的位置。🗂️

3. 修改账号信息 ✍️
在 send_verification_code.py 文件中，找到账号相关的设置。将文件中的 手机账号 修改为你自己的手机号码。📲

4. 运行脚本 🚀
打开 cmd（命令行终端），进入存放 send_verification_code.py 文件的目录。🌐

你可以使用 cd 命令来进入目录，例如：

bash
复制代码
cd 路径\到\send_verification_code.py
执行以下命令运行 Python 脚本：

bash
复制代码
python send_verification_code.py
如果成功，你将看到类似以下的输出信息：

bash
复制代码
服务器响应: jsonpReturn({"result":1,"msg":"验证码正下发，请注意查收！"});
成功 🎉
5. 获取验证码 📥
成功运行脚本后，你的手机会收到验证码信息。根据手机上收到的验证码，登录 NJUPT 系统。🔑

账号：使用你输入的手机号。
密码：使用手机接收到的验证码。
注意事项 ⚠️
请确保你输入的手机号是正确的。🔍
如果接收到的验证码没有及时到达，请稍等几分钟再次尝试。⏳
此工具仅适用于 NJUPT 的登录验证。
技术支持 💬
如果在使用过程中遇到问题，可以参考以下资源获取更多帮助：

Requests 文档 📚
Python 官方文档 🧑‍💻
这样，README 文件不仅更清晰，而且通过表情符号使得内容更加生动和友好。希望这能帮助用户更顺利地完成操作！🚀😊
