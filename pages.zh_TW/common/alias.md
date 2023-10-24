# alias

> 建立快捷鍵名稱 -- 取代命令字串的單字。
> 快捷鍵只會在現有的 shell 有效，除非在 shell 的設定檔中定義快捷鍵，例如：`~/.bashrc`.
> 更多資訊：<https://tldp.org/LDP/abs/html/aliases.html>.

- 列出所有快捷鍵：

`alias`

- 建立快捷鍵：

`alias {{快捷名稱}}="{{命令字串}}"`

- 查看與給定名稱有關的快捷鍵：

`alias {{快捷名稱}}`

- 移除快捷鍵：

`unalias {{快捷名稱}}`

- 將 `rm` 變成互動式指令：

`alias {{rm}}="{{rm --interactive}}"`

- 建立 `la` 作為 `ls --all` 的捷徑：

`alias {{la}}="{{ls --all}}"`
