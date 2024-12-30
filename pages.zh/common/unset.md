# unset

> 移除 shell 变量或函数。
> 更多信息: <https://manned.org/unset>。

- 移除变量 `foo`，如果变量不存在，则移除函数 `foo`：

`unset {{foo}}`

- 移除变量 foo 和 bar：

`unset -v {{foo}} {{bar}}`

- 移除函数 my_func：

`unset -f {{my_func}}`