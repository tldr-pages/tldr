# eselect repository

> ماژول `eselect` برای پیکربندی مخازن ebuild برای Portage.
> پس از فعال کردن مخزن باید `emerge --sync repo_name` را برای دانلود ebuildها اجرا کنید.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- فهرست کردن همهٔ مخازن ebuild ثبت‌شده در <https://repos.gentoo.org>:

`eselect repository list`

- فهرست کردن مخازن فعال:

`eselect repository list -i`

- فعال کردن یک مخزن از فهرست با نام یا شمارهٔ آن از دستور `list`:

`eselect repository enable {{name|index}}`

- فعال کردن یک مخزن ثبت‌نشده:

`eselect repository add {{name}} {{rsync|git|mercurial|svn|...}} {{sync_uri}}`

- غیرفعال کردن مخازن بدون حذف محتویات آن‌ها:

`eselect repository disable {{repo1 repo2 ...}}`

- غیرفعال کردن مخازن و حذف محتویات آن‌ها:

`eselect repository remove {{repo1 repo2 ...}}`

- ایجاد و فعال کردن یک مخزن محلی:

`eselect repository create {{name}} {{path/to/repo}}`
