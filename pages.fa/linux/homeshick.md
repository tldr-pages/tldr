# homeshick

> همگام‌سازی فایل‌های پیکربندی نقطه‌ای با Git.
> همچنین ببینید: `chezmoi`, `stow`, `tuckr`, `vcsh`.
> اطلاعات بیشتر: <https://github.com/andsens/homeshick/wiki>.

- ایجاد یک castle جدید:

`homeshick generate {{castle_name}}`

- افزودن فایل به castle:

`homeshick track {{castle_name}} {{path/to/file}}`

- رفتن به یک castle:

`homeshick cd {{castle_name}}`

- رونوشت‌گیری از یک castle:

`homeshick clone {{github_username}}/{{repository_name}}`

- ایجاد پیوند نمادین برای همهٔ فایل‌های یک castle:

`homeshick link {{castle_name}}`
