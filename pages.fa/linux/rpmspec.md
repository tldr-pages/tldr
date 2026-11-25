# rpmspec

> پرس‌وجوی فایل spec مربوط به RPM.
> اطلاعات بیشتر: <https://manned.org/rpmspec>.

- فهرست کردن بسته‌های دودویی که از فایل spec مربوط به RPM تولید خواهند شد:

`rpmspec --query {{path/to/rpm.spec}}`

- فهرست کردن همهٔ گزینه‌های `--queryformat`:

`rpmspec --querytags`

- دریافت اطلاعات خلاصهٔ بسته‌های دودویی تکی تولیدشده از فایل spec مربوط به RPM:

`rpmspec --query --queryformat "{{%{name}: %{summary}\n}}" {{path/to/rpm.spec}}`

- دریافت بستهٔ منبعی که از فایل spec مربوط به RPM تولید خواهد شد:

`rpmspec --query --srpm {{path/to/rpm.spec}}`

- تجزیهٔ فایل spec مربوط به RPM در `stdout`:

`rpmspec --parse {{path/to/rpm.spec}}`
