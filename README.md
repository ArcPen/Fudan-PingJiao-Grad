# Fudan PingJiao Graduate

> “属于研究生自己的评教脚本”

1. 命令行下`pip3 install selenium`安装selenium，请使用4.x版本的selenium

   作者用的环境：python 3.10 + selenium 4.16

2. 在clone或者下载本项目获得work.py（python脚本）

3. 用文本编辑器打开work.py文件（如果是windows就右键-打开方式-记事本），在文件开头找到下面几行代码

   ```python
   username = ''
   password = ''
   sleep_time = 10 
   ```

   前两行引号内分别填入uis用户名和密码。第三行的参数表示填完一个问卷后等待多久提交，可以按需更改

4. 命令行中`python3 work.py`运行python脚本

5. 如果遇到问题的话，尝试下载对应浏览器的webdriver

   以下是chrome的浏览器webdriver下载地址，选择和自己chrome对应版本的chromedriver（可以再chrome浏览器网址栏中输入`chrome://version`查看，下载好了把里面的东西解压出来：

   * mac系统： 放在和work.py同一文件夹下
   * linux系统：在终端中进入解压出来的东西所在文件夹下，执行命令`sudo mv chromedriver /usr/local/chromedriver`
   * win系统：https://www.jianshu.com/p/28c0d1ed62f8

   [Chrome web driver](http://chromedriver.storage.googleapis.com/index.html)

6. 还有什么问题的话，欢迎提issue或者发邮件给我 shinkyre@outlook.com

7. 最后祝您，评教愉快
