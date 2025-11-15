# unset

> 删除 Shell 变量或函数。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-unset>.

- 删除变量 `foo`，如果该变量不存在则删除函数 `foo`：

`unset {{foo}}`

- 删除变量 foo 和 bar：

`unset -v {{foo}} {{bar}}`

- 删除函数 my_func：

`unset -f {{my_func}}`
