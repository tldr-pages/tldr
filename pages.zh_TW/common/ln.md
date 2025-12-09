# ln

> 建立指向檔案和目錄的連結。
> 更多資訊：<https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- 建立指向檔案或目錄的符號連結：

`ln {{[-s|--symbolic]}} /{{path/to/file_or_directory}} {{path/to/symlink}}`

- 覆寫現有的符號連結以指向其他檔案：

`ln {{[-sf|--symbolic --force]}} /{{path/to/new_file}} {{path/to/symlink}}`

- 建立指向檔案的硬連結：

`ln /{{path/to/file}} {{path/to/hardlink}}`
