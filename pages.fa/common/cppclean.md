# cppclean

> پیدا کردن کد های بدون استفاده در پروژه های سی پلاس پلاس.
> اطلاعات بیشتر: <https://github.com/myint/cppclean>.

- اجرا در پوشه ی پروژه:

`cppclean {{path/to/project}}`

- اجرا روی پروژه درحالی که هدرها در پوشه های `inc1/` و `inc2/` قرار دارند:

`cppclean {{path/to/project}} --include-path={{inc1}} --include-path={{inc2}}`

- اجرا روی فایل دلخواه مانند `main.cpp`:

`cppclean {{main.cpp}}`

- اجرا روی پوشه کنونی به استثنای پوشه "build":

`cppclean {{.}} --exclude={{build}}`
