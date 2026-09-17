# clear

> 清除終端機畫面。
> 更多資訊：<https://manned.org/clear>。

- 清除畫面：

`clear`

- 清除畫面，但保留終端機的捲動緩衝區（相當於在 Bash 中按下 `<Ctrl l>`）：

`clear -x`

- 指定要清除的終端機類型（預設為環境變數 `$TERM` 的值）：

`clear -T {{終端機類型}}`

- 顯示 `clear` 所使用的 `ncurses` 版本：

`clear -V`
