# proctl

> 管理项目的许可证和语言，在模板许可证之间切换。
> 更多信息：<https://github.com/HeCodes2Much/proctl>。

- 列出可用的许可证：

`proctl {{-ll|-list-licenses}}`

- 列出可用的语言：

`proctl {{-lL|-list-languages}}`

- 在FZF菜单中选择许可证：

`proctl {{-pl|-pick-license}}`

- 在FZF菜单中选择语言：

`proctl {{-pL|-pick-language}}`

- 从当前项目中移除所有许可证：

`proctl {{-r|-remove-license}}`

- 创建一个新的许可证模板：

`proctl {{-t|-new-template}}`

- 从模板中删除许可证：

`proctl {{-R|-delete-license}} {{@license_name1 @license_name2 ...}}`

- 显示这个有用的命令列表：

`proctl {{-h|-help}}`