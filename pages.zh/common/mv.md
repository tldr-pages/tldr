# mv

> 移动或重命名文件和目录。
> 更多信息：<https://www.gnu.org/software/coreutils/mv>。

- 当目标不是已存在的目录时重命名文件或目录：

`mv {{path/to/source}} {{path/to/target}}`

- 将文件或目录移动到已存在的目录中：

`mv {{path/to/source}} {{path/to/existing_directory}}`

- 将多个文件移动到已存在的目录中，保持文件名不变：

`mv {{path/to/source1 path/to/source2 ...}} {{path/to/existing_directory}}`

- 在覆盖现有文件之前，不提示（[f]）确认：

`mv --force {{path/to/source}} {{path/to/target}}`

- 在覆盖现有文件之前，无论文件权限如何，交互式地提示确认 [i]：

`mv --interactive {{path/to/source}} {{path/to/target}}`

- 不在目标位置覆盖（[n]）现有文件：

`mv --no-clobber {{path/to/source}} {{path/to/target}}`

- 以 [v] 详细模式移动文件，显示已移动的文件：

`mv --verbose {{path/to/source}} {{path/to/target}}`

- 指定 [t] 目标目录，以便您可以使用外部工具收集可移动的文件：

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv --target-directory {{path/to/target_directory}}`