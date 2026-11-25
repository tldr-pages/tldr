# logwatch

> خلاصه کردن گزارش‌های مختلف سرویس‌های رایج (مانند apache، pam_unix، sshd و غیره) در یک گزارش.
> اطلاعات بیشتر: <https://manned.org/logwatch>.

- تحلیل گزارش‌ها برای محدودهٔ تاریخ با سطح جزئیات مشخص:

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}`

- محدود کردن گزارش به اطلاعات سرویس انتخاب‌شده:

`logwatch --range {{all}} --service {{apache|pam_unix|...}}`
