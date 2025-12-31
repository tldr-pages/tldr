# ln

> این دستور برای ایجاد ارتباط(link) به فایل ها و پوشه ها(Directories) استفاده می شود.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>.

- ایجاد یک ارتباط نمادین (symbolic link) به یک فایل یا پوشه:

`ln {{[-s|--symbolic]}} {{/path/to/file_or_directory}} {{path/to/symlink}}`

- جایگزینی یک ارتباط نمادین موجود، برای اشاره به یک فایل متفاوت:

`ln {{[-sf|--symbolic --force]}} {{/path/to/new_file}} {{path/to/symlink}}`

- ایجاد یک لینک سخت (hard link) به یک فایل:

`ln {{/path/to/file}} {{path/to/hardlink}}`
