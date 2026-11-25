# mirrorselect

> انتخاب سریع‌ترین آینه‌های Gentoo و به‌روزرسانی `GENTOO_MIRRORS` در `/etc/portage/make.conf`.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Mirrorselect>.

- انتخاب تعاملی آینه‌های منبع از فهرست:

`sudo mirrorselect {{[-i|--interactive]}}`

- انتخاب تعاملی آینه‌ها از کشور مشخص:

`sudo mirrorselect {{[-i|--interactive]}} {{[-c|--country]}} "{{Germany}}"`

- انتخاب خودکار تعداد مشخصی از سریع‌ترین آینه‌ها:

`sudo mirrorselect {{[-s|--servers]}} {{3}}`

- انتخاب خودکار سریع‌ترین آینه‌ها با آزمون بارگیری دقیق‌تر:

`sudo mirrorselect {{[-D|--deep]}} {{[-s|--servers]}} {{3}}`

- در نظر گرفتن فقط آینه‌های HTTPS:

`sudo mirrorselect {{[-S|--https]}} {{[-s|--servers]}} {{3}}`

- چاپ آینه‌های انتخاب‌شده به‌جای نوشتن آن‌ها در `make.conf`:

`mirrorselect {{[-s|--servers]}} {{3}} {{[-o|--output]}}`

- انتخاب تعاملی آینهٔ rsync و افزودن آن به پیکربندی مخزن:

`mirrorselect {{[-i|--interactive]}} {{[-r|--rsync]}} {{[-o|--output]}} | sudo tee -a /etc/portage/repos.conf/gentoo.conf`
