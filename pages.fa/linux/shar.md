# shar

> ایجاد بایگانی پوسته.
> اطلاعات بیشتر: <https://www.gnu.org/software/sharutils/manual/sharutils.html>.

- ایجاد اسکریپت پوسته که هنگام اجرا فایل‌های مشخص را از خود استخراج می‌کند:

`shar {{[-V|--vanilla-operation]}} {{path/to/file1 path/to/file2 ...}} >{{path/to/archive.sh}}`

- فشرده‌سازی فایل‌های بایگانی:

`shar {{[-C|--compactor]}} {{xz}} {{path/to/file1 path/to/file2 ...}} >{{path/to/archive.sh}}`

- در نظر گرفتن همهٔ فایل‌ها به‌صورت دودویی (یعنی اجرای `uuencode` روی همه):

`shar {{[-B|--uuencode]}} {{path/to/file1 path/to/file2 ...}} >{{path/to/archive.sh}}`

- در نظر گرفتن همهٔ فایل‌ها به‌صورت متنی (یعنی اجرا نکردن `uuencode` روی هیچ‌کدام):

`shar {{[-T|--text-files]}} {{path/to/file1 path/to/file2 ...}} >{{path/to/archive.sh}}`

- گنجاندن نام و علامت برش در توضیح سربرگ بایگانی:

`shar {{[-n|--archive-name]}} "{{My files}}" {{[-c|--cut-mark]}} {{path/to/file1 path/to/file2 ...}} >{{path/to/archive.sh}}`
