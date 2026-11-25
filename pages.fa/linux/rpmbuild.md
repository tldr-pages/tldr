# rpmbuild

> ابزار ساخت بستهٔ RPM.
> اطلاعات بیشتر: <https://manned.org/rpmbuild>.

- ساخت بسته‌های دودویی و منبع:

`rpmbuild -ba {{path/to/spec_file}}`

- ساخت بستهٔ دودویی بدون بستهٔ منبع:

`rpmbuild -bb {{path/to/spec_file}}`

- تعیین متغیرهای اضافی هنگام ساخت بسته:

`rpmbuild -bb {{path/to/spec_file}} --define "{{variable1}} {{value1}}" --define "{{variable2}} {{value2}}"`
