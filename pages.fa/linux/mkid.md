# mkid

> ساخت پایگاه دادهٔ ID برای استفاده با `lid` و سایر ابزارهای idutils.
> اطلاعات بیشتر: <https://www.gnu.org/software/idutils/manual/idutils.html#mkid-invocation>.

- ساخت پایگاه دادهٔ ID برای دایرکتوری فعلی:

`mkid`

- ساخت پایگاه دادهٔ ID برای دایرکتوری‌های مشخص:

`mkid {{path/to/directory1 path/to/directory2 ...}}`

- ساخت پایگاه دادهٔ ID و ذخیره در فایل مشخص:

`mkid {{[-o|--output]}} {{path/to/database.id}}`

- گنجاندن فقط زبان‌های مشخص:

`mkid {{[-i|--include]}} "{{language1 language2 ...}}"`

- مستثنا کردن دایرکتوری‌های مشخص از نمایه‌سازی:

`mkid {{[-p|--prune]}} {{path/to/excluded_directory}}`

- نمایش آمار پس از ساخت پایگاه داده:

`mkid {{[-s|--statistics]}}`
