# pkgctl diff

> مقایسهٔ فایل‌های بسته با حالت‌های مختلف.
> اطلاعات بیشتر: <https://manned.org/pkgctl-diff>.

- مقایسهٔ فایل‌های بسته در حالت تفاوت فهرست محتویات tar (پیش‌فرض):

`pkgctl diff {{[-l|--list]}} {{path/to/file|pkgname}}`

- مقایسهٔ فایل‌های بسته در حالت تفاوت diffoscope:

`pkgctl diff {{[-d|--diffoscope]}} {{path/to/file|pkgname}}`

- مقایسهٔ فایل‌های بسته در حالت تفاوت `.PKGINFO`:

`pkgctl diff {{[-p|--pkginfo]}} {{path/to/file|pkgname}}`

- مقایسهٔ فایل‌های بسته در حالت تفاوت `.BUILDINFO`:

`pkgctl diff {{[-b|--buildinfo]}} {{path/to/file|pkgname}}`
