# pridecat

> مانند cat اما رنگارنگ‌تر.
> اطلاعات بیشتر: <https://github.com/lunasorcery/pridecat#flags>.

- چاپ محتویات فایل در رنگ‌های پرچم افتخار در `stdout`:

`pridecat {{path/to/file}}`

- چاپ محتویات فایل در رنگ‌های پرچم ترنس:

`pridecat {{path/to/file}} {{[--trans|--transgender]}}`

- جابجایی متناوب بین پرچم‌های افتخار لزبین و دوجنس‌گرا:

`pridecat {{path/to/file}} --lesbian {{[--bi|--bisexual]}}`

- چاپ محتویات فایل با رنگ‌های پس‌زمینهٔ تغییرکرده:

`pridecat {{path/to/file}} {{[-b|--background]}}`

- فهرست کردن محتویات دایرکتوری با رنگ‌های پرچم افتخار:

`ls | pridecat --{{flag}}`
