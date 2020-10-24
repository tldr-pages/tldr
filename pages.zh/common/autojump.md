# autojump

> 快速跳转，访问次数最多的文件夹优先.
> 使用j、jc、jo作为别名.
> 详见: <https://github.com/wting/autojump>.

- 跳转到包含指定通配符的目录:

`j {{pattern}}`

- 跳转到包含指定通配符的目录的下一级:

`jc {{pattern}}`

- 使用系统文件管理器，打开指定的目录:

`jo {{pattern}}`

- 从autojump数据库中删除不存在的目录:

`j --purge`

- 展示autojump数据库数据:

`j -s`
