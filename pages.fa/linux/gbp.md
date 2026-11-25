# gbp

> سامانه‌ای برای یکپارچه‌سازی سامانهٔ ساخت بستهٔ دبیان با Git.
> اطلاعات بیشتر: <https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>.

- تبدیل یک بستهٔ موجود دبیان به gbp:

`gbp import-dsc {{path/to/package.dsc}}`

- ساخت بسته در دایرکتوری فعلی با سازندهٔ پیش‌فرض (`debuild`):

`gbp buildpackage -jauto -us -uc`

- ساخت بسته در محیط `pbuilder` برای Debian Bullseye:

`DIST={{bullseye}} ARCH={{amd64}} gbp buildpackage -jauto -us -uc --git-builder={{git-pbuilder}}`

- تعیین بسته برای بارگذاری فقط منبع در فایل `.changes` (ببینید: <https://wiki.debian.org/SourceOnlyUpload>):

`gbp buildpackage -jauto -us -uc --changes-options={{-S}}`

- وارد کردن انتشار جدید بالادستی:

`gbp import-orig --pristine-tar {{path/to/package.tar.gz}}`
