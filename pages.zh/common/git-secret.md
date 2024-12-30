# git secret

> 在 Git 仓库中存储私密数据。使用 Bash 编写。
> 更多信息：<https://github.com/sobolevn/git-secret>。

- 在本地仓库中初始化 `git-secret`：

`git secret init`

- 授予当前 Git 用户的电子邮件访问权限：

`git secret tell -m`

- 通过电子邮件授予访问权限：

`git secret tell {{email}}`

- 撤销电子邮件的访问权限：

`git secret killperson {{email}}`

- 列出有权访问秘密的电子邮件：

`git secret whoknows`

- 注册一个秘密文件：

`git secret add {{path/to/file}}`

- 加密秘密：

`git secret hide`

- 解密秘密文件：

`git secret reveal`