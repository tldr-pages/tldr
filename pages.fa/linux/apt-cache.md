# apt-cache

> ابزار پرس‌وجوی بسته‌های دبیان و اوبونتو.
> اطلاعات بیشتر: <https://manned.org/apt-cache>.

- جست‌وجوی یک بسته در منابع فعلی:

`apt-cache search {{query}}`

- نمایش اطلاعات یک بسته:

`apt-cache show {{package}}`

- نمایش وضعیت نصب و به‌روز بودن یک بسته:

`apt-cache policy {{package}}`

- نمایش وابستگی‌های یک بسته:

`apt-cache depends {{package}}`

- نمایش بسته‌هایی که به یک بستهٔ مشخص وابسته‌اند:

`apt-cache rdepends {{package}}`
