# 四川大学自动打卡项目

本项目仅限于学习交流，用于其他用途后果自负。请大家自行手动打卡，如果身体不适，请及时检查上报。

- ## 项目介绍

  项目抓取打卡后台地址，构建headers和模拟data数据，post提交。目前cookies仅需要携带"eai-sess"和"UUkey"参数便能提交成功。

- ## 使用方法

  1. 获取"eai-sess"和"UUkey"，方法：利用chrome等浏览器，直接抓取

     打开浏览器输入网址（进行操作前最好清除浏览器缓存的该网址的cookies，浏览器输入：chrome://settings/siteData， 搜索wfw，清除（若有的话））
     https://wfw.scu.edu.cn/ncov/wap/default/index
     按f12（如下图），点击network，然后清除历史，利用账号密码登录。

     ![image-20201224161233097](https://github.com/wangyufei2969/ScuDaKa/blob/main/image-20201224161233097.png)

     登录后会重定向到大家经常看到的微信打卡界面，点index，然后找到requests headers，再找里面的cookies，这个就是每个人的临时通行证，**复制这个，替换SaveData.py中headers里面的cookie（放在引号里面就行）**。

     ![image-20201224161636884](https://github.com/wangyufei2969/ScuDaKa/blob/main/image-20201224161636884.png)

  2. SaveData.py中"data"字典，字典每个字段都注释了对应的含义，请修改的时候，只修改需要的（'szxqmc'， 'address'，'area'， ），**不要乱修改，否则你会收到辅导员的问候电话**。*其他校区需要修改"geo_api_info",这个是调取高德api生成的，可以手动获取，方法如下*：

     ​		在获取cookies步骤的基础上，删除记录，并点击网页中“点击获取地理位置”，就会出来点击后的两个响应文件，便是获取的位置信息，将此信息替换掉"geo_api_info"的相应值。

     ![image-20201224164608825](https://github.com/wangyufei2969/ScuDaKa/blob/main/image-20201224164608825.png)

  3. 测试运行，部署定时运行：

     注释

     ```
     if timeNow == "08:30:10":
     ```

     反注释

     ```
     if True:
     ```

     运行代码，若出现下图，则表示身份认证成功，**但是提交的data不一定是准确的，所以一定不要乱改data字典。**

     ![image-20201224165625781](https://github.com/wangyufei2969/ScuDaKa/blob/main/image-20201224165625781.png)

     ## 若出现下图，则表示身份认证失败，需要重新检查cookies的获取以及准确性。

     ![image-20201224170043389](https://github.com/wangyufei2969/ScuDaKa/blob/main/image-20201224170043389.png)

     **身份认证无误，data修改完毕后，**

     反注释

     ```
     if timeNow == "08:30:10":
     ```

     修改你想运行自动打卡的时间，再注释

     ```
     if True:
     ```

     一切就绪。

     **关于定时运行：**

     不同平台的方法不同，推荐部署在Linux服务器，若你有管理员权限，可以使用'crontab'，若你没有权限，利用

     ```
     nohub python SaveData.py > SaveData.log 2>&1 &
     ```

## 其他

1. 由于试运行期短，还不知道cookies有效期，最理想的解决方法是：检测每次提交结果，失败时自动登录微服务平台再获取新cookies，更新cookies提交（若cookies持续时间短，我会考虑做）
2. 若打卡成功，当天微信不会收到微服务公众号的打卡提醒，若你有时间，可以结合微信二次开发，打卡后自动发微信消息给指定微信
3. 项目持续维护，欢迎大佬pull
4. 该项目为技术交流项目，若侵犯了您的利益，请与我联系

