## git 常用命令

| 命令名称                             | 作用                             |
| ------------------------------------ | -------------------------------- |
| git config --global user.name 用户名 | 设置用户签名 -- 首次配置需要设置 |
| git config --global user.email 邮箱  | 设置用户签名 -- 首次配置需要设置 |
| git init                             | 初始化本地库                     |
| git status                           | 查看本地库状态                   |
| git add 文件名                       | 添加到暂存区                     |
| git commit -m "日志信息" 文件名      | 提交到本地库                     |
| git reflog                           | 查看简化历史记录                 |
| git log                              | 查看详细历史记录                 |
| git reset -hard 版本号               | 版本穿梭                         |
| cat 文件名                           | 查看文件                         |


## git 分支操作

每个分支都是独立运行的，可以理解成副本，各个分支在开发过程中，如果某一个分支开发失败，不会对其他分支有任何影响。失败的 分支删除重新开始即可！
同时可以并行推进多个功能开发，提高效率，最后合并到主线

**分支的操作命令**

| 命令名称            | 作用                       |
| ------------------- | -------------------------- |
| git branch 分支名   | 创建分支                   |
| git branch -v       | 查看分支                   |
| git checkout 分支名 | 切换分支                   |
| git merge           | 把制定的分支合并到当前分支 |

**合并分支冲突解决**
冲突产生的原因: 合并分支时，两个分支在同一个文件的同一个位置有两套完全不同的修改。Git 无法替我们决定使用哪一个。必须人为决定新代码内容

编辑有冲突的文件，删除特殊符号，决定要使用的内容
特殊符号:<<<<<<< HEAD 当前分支的代码 ======= 合并过来的代码 >>>>>>> 分支名
自己手动修改代码，将多余的删除，然后提交暂存区，执行提交
