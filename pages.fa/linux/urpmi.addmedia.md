# urpmi.addmedia

> افزودن رسانه در Mageia.
> توجه: مستندات Mageia واژه‌های رسانه و مخزن را مترادف به کار می‌برند.
> همچنین : `urpmi`, `urpmi.update`, `urpme`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> اطلاعات بیشتر: <https://man.linuxreviews.org/man8/urpmi.addmedia.8.html>.

- افزودن رسانه:

`sudo urpmi.addmedia {{medium}} {{ftp://ftp.site.com/path/to/Mageia/RPMS}}`

- افزودن رسانه از دیسک سخت (ابتدا `genhdlist2` را در دایرکتوری اجرا کنید):

`sudo urpmi.addmedia --distrib HD file://{{path/to/repo}}`

- افزودن رسانه‌های مهم از آینهٔ انتخاب‌شده:

`sudo urpmi.addmedia --distrib ftp://{{mirror_website}}/mirror/mageia/distrib/{{version}}/{{arch}}`

- انتخاب خودکار آینه‌ها از فهرست آینه‌ها:

`sudo urpmi.addmedia --distrib --mirrorlist {{mirrorlist}}`
