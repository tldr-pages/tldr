# fuzzel

> 一个受 `rofi` 和 `dmenu` 启发的 Wayland 原生应用程序启动器和模糊查找器。
> 更多信息：<https://codeberg.org/dnkl/fuzzel>.

- 运行应用程序：

`fuzzel`

- 以 dmenu 模式运行 `fuzzel`：

`fuzzel {{[-d|--dmenu]}}`

- 显示 `ls` 命令输出的菜单：

`{{ls}} | fuzzel {{[-d|--dmenu]}}`

- 显示一个用换行符 (`\n`) 分隔的自定义项目菜单：

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel {{[-d|--dmenu]}}`

- 让用户在多个项目中选择，并将选中的项目保存到文件中：

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel {{[-d|--dmenu]}} > {{color.txt}}`

- 重置应用程序使用次数（默认缓存目录：`$XDG_CACHE_HOME/fuzzel`）：

`rm -v $HOME/.cache/fuzzel`

- 在特定的监视器上启动 `fuzzel`，参见 `wlr-randr` 或 `swaymsg -t get_outputs`：

`fuzzel {{[-o|--output]}} "{{DP-1}}"`

- 使用 `fuzzel` 进行在线搜索：

`fuzzel {{[-d|--dmenu]}} {{[-l|--lines]}} 0 --placeholder "{{输入您的搜索}}" | sed 's/^/\"/g;s/$/\"/g' | xargs firefox --search`