# equery

> مشاهدهٔ اطلاعات بسته‌های Portage.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Equery>.

- فهرست کردن همهٔ بسته‌های نصب‌شده:

`equery list '*'`

- جست‌وجوی بسته‌های نصب‌شده در درخت Portage و overlayها:

`equery list -po {{package1 package2 ...}}`

- فهرست کردن همهٔ بسته‌هایی که به یک بستهٔ مشخص وابسته‌اند:

`equery depends {{package}}`

- فهرست کردن همهٔ بسته‌هایی که یک بستهٔ مشخص به آن‌ها وابسته است:

`equery depgraph {{package}}`

- فهرست کردن همهٔ فایل‌های نصب‌شده توسط یک بسته:

`equery files --tree {{package}}`
