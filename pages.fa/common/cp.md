# cp

> کپی فایل ها و دایرکتوری ها.

- کپی فایل از مبدا به مقصد مشخص شده:

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- کپی فایل به دایرکتوری مشخص شده با حفظ نام فایل:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- کپی یک دایرکتوری به صورت کامل به مقصد جدید(اگر در مقصد دایرکتوری وجود داشت دایرکتوری مبدا در داخل دایرکتوری مقصد کپی می شود):

`cp -R {{path/to/source_directory}} {{path/to/target_directory}}`

- کپی یک دایرکتوری به صورت کامل با نمایش جزییات (نمایش فایل های کپی شده):

`cp -vR {{path/to/source_directory}} {{path/to/target_directory}}`

- به دایرکتوری مقصد در حالت تعاملی (قبل از باز نویسی تاییده توسط کاربر نیاز است) txt کپی کلیه فایل های با پسوند:

`cp -i {{*.txt}} {{path/to/target_directory}}`

- کپی لینک به مقصد بدون ارجاع به فایل اصلی

`cp -L {{link}} {{path/to/target_directory}}`
