# xdg-user-dirs-update

> 更新 XDG 用户目录。
> 更多信息：<https://manned.org/xdg-user-dirs-update>.

- 将 XDG 的 DESKTOP 目录更改为指定的目录（必须是绝对路径）：

`xdg-user-dirs-update --set DESKTOP "{{path/to/directory}}"`

- 将结果写入指定的干运行文件而不是 `user-dirs.dirs` 文件：

`xdg-user-dirs-update --dummy-output "{{path/to/dry_run_file}}" --set {{xdg_user_directory}} "{{path/to/directory}}"`
