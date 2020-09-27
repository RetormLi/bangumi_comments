# Bangumi用户已看评论打分备份
## 说明
- 本脚本可以用来备份bangumi.tv网站用户的历史番剧评论和分数。
- 在评论或者分数的修改后，重新运行脚本同步，不仅可以更新数据，还可以保存之前的历史数据，并保存对应的修改时间。
- 对应时间为脚本运行时的时间，而非实际修改的时间。
- 通过修改user_id可以读取任意Bangumi用户的评论和打分。

## 用法
- 需要电脑安装Python 3
- 打开comments_fetch.py（可使用记事本打开，不要双击打开）。

    在文件开头附近位置找到：

    ```python
    # Put your userid here
    user_id = 'xxxxxx'
    ```
  将用户id填入xxxxxx（id即打开用户时光机页面的网址https://bangumi.tv/anime/list/???/collect 里???处的字符串，
  或时光机页面用户名右侧的小字@???中???处的字符串）
  
  如对于用户retormli，应修改为：
    ```python
    # Put your userid here
    user_id = 'retormli'
    ```
- 在comments_fetch.py文件所在文件夹，运行如下指令：

    ```python comments_fetch.py```
    
    或
    
    ```python3 comments_fetch.py```

- 由于Bangumi网站访问较慢，提取一页评论大约需要1-5s的时间。
    
    在一切完成后，会输出：
    ```Everything is OK.```
- 备份文件会以json格式保存在```log/comments_userid.json```中，可以用记事本查看。

## 后记

由于每次Bangumi网站上不去时都担心自己的数据丢失，一直想做一个备份的小脚本。
当然也希望Bangumi永不倒闭(bgm38)

没想到真的开始动手的时候，遇见了很多初版代码里没想到的问题。最终修修补补改成了一个应该能用的版本。

当然现在的版本功能很少，只是实现了最初预想的最少功能需求。而且由于测试不足，很可能还有很多bug。对于建议或者问题，欢迎提出issue。

——@retormli
