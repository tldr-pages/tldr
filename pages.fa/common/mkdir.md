# mkdir

> ساخت پوشه ها و تنظیم مجوز آنها.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/mkdir>.

- ساخت پوشه مشخص:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- ساخت پوشه های مشخص به همراه پوشه های والد در صورت نیاز:

`mkdir -p {{path/to/directory1 path/to/directory2 ...}}`

- ساخت پوشه با مجوز های خاص:

`mkdir -m {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`
