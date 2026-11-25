# cewl

> ابزار پیمایش URL برای ساخت فهرست واژه‌های شکستن رمز از محتوای وب.
> اطلاعات بیشتر: <https://digi.ninja/projects/cewl.php#usage>.

- ایجاد فایل فهرست واژه‌ها از URL مشخص تا عمق ۲ پیوند:

`cewl {{[-d|--depth]}} 2 {{[-w|--write]}} {{path/to/wordlist.txt}} {{url}}`

- چاپ فهرستی از واژه‌های حرفی‌عددی از URL مشخص با حداقل طول ۵ نویسه:

`cewl --with-numbers {{[-m|--min_word_length]}} 5 {{url}}`

- چاپ فهرست واژه‌ها از URL مشخص در حالت اشکال‌زدایی همراه با نشانی‌های رایانامه:

`cewl --debug {{[-e|--email]}} {{url}}`

- چاپ فهرست واژه‌ها از URL مشخص با احراز هویت HTTP از نوع Basic یا Digest:

`cewl --auth_type {{basic|digest}} --auth_user {{username}} --auth_pass {{password}} {{url}}`

- چاپ فهرست واژه‌ها از URL مشخص از طریق پراکسی:

`cewl --proxy_host {{host}} --proxy_port {{port}} {{url}}`
