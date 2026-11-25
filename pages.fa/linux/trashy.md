# trashy

> جایگزینی برای `rm` و `trash-cli` نوشته‌شده با Rust.
> اطلاعات بیشتر: <https://github.com/oberblastmeister/trashy#usage>.

- انتقال فایل مشخص به سطل زباله:

`trash {{path/to/file}}`

- انتقال فایل‌های مشخص به سطل زباله:

`trash {{path/to/file1 path/to/file2 ...}}`

- فهرست کردن موارد سطل زباله:

`trash list`

- بازیابی فایل مشخص از سطل زباله:

`trash restore {{file}}`

- حذف فایل مشخص از سطل زباله:

`trash empty {{file}}`

- بازیابی همهٔ فایل‌ها از سطل زباله:

`trash restore --all`

- حذف همهٔ فایل‌ها از سطل زباله:

`trash empty --all`
