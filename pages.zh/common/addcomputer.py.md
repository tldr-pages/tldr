# addcomputer.py

> 向域中添加一个计算机账户。
> 更多信息：<https://github.com/fortra/impacket>.

- 使用指定的名称和密码添加一台计算机：

`addcomputer.py -computer-name {{计算机名称$}} -computer-pass {{计算机密码}} {{域}}/{{用户名}}:{{密码}}`

- 仅为现有计算机设置一个新密码：

`addcomputer.py -no-add -computer-name {{计算机名称$}} -computer-pass {{计算机密码}} {{域}}/{{用户名}}:{{密码}}`

- 删除一个现有的计算机账户：

`addcomputer.py -delete -computer-name {{计算机名称$}} {{域}}/{{用户名}}:{{密码}}`

- 使用 Kerberos 身份验证添加计算机：

`addcomputer.py -k -no-pass {{域}}/{{用户名}}@{{主机名}}`

- 通过 LDAPS（端口 636）而不是 SAMR（端口 445）添加计算机：

`addcomputer.py -method LDAPS -port 636 {{域}}/{{用户名}}:{{密码}}`

- 当存在多个域控制器时，指定确切的域控制器：

`addcomputer.py -dc-host {{主机名}} {{域}}/{{用户名}}:{{密码}}`
