# mkdir

> ساخت پوشه ها و تنظیم مجوز آنها.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- ساخت پوشه مشخص:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- ساخت پوشه های مشخص به همراه پوشه های والد در صورت نیاز:

`mkdir {{[-p|--parents]}} {{path/to/directory1 path/to/directory2 ...}}`

- ساخت پوشه با مجوز های خاص:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`
