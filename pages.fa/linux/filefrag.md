# filefrag

> گزارش میزان احتمالی قطعه‌قطعه شدن یک فایل مشخص.
> اطلاعات بیشتر: <https://manned.org/filefrag>.

- نمایش گزارش برای یک یا چند فایل:

`filefrag {{path/to/file1 path/to/file2 ...}}`

- نمایش گزارش با اندازهٔ بلوک ۱۰۲۴ بایت:

`filefrag -k {{path/to/file}}`

- نمایش گزارش با اندازهٔ بلوک مشخص:

`filefrag -b{{1024|1K|1M|1G|...}} {{path/to/file}}`

- همگام‌سازی فایل پیش از درخواست نگاشت:

`filefrag -s {{path/to/file1 path/to/file2 ...}}`

- نمایش نگاشت ویژگی‌های گسترش‌یافته:

`filefrag -x {{path/to/file1 path/to/file2 ...}}`

- نمایش گزارش با اطلاعات مفصل:

`filefrag -v {{path/to/file1 path/to/file2 ...}}`
