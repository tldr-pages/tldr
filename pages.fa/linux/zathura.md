# zathura

> نمایش‌دهندهٔ حالتی اسناد شبیه Vim با خط فرمان یکپارچه.
> مطمئن شوید یک backend نصب شده است (poppler، PostScript یا DjVu).
> اطلاعات بیشتر: <https://pwmt.org/projects/zathura/>.

- باز کردن فایل:

`zathura {{path/to/file}}`

- پیمایش به چپ، بالا، پایین یا راست:

`{{<h>|<j>|<k>|<l>|<ArrowKeys>}}`

- چرخاندن:

`<r>`

- معکوس کردن رنگ‌ها:

`<Ctrl r>`

- جست‌وجوی متن با رشتهٔ مشخص:

`</>{{string}}`

- ایجاد یا حذف نشانک‌ها:

`<:>{{bmark|bdelete}} {{bookmark_name}}<Enter>`

- فهرست کردن نشانک‌ها:

`<:>blist<Enter>`

- دنبال کردن پیوندها:

`<f>{{link_number}}<Enter>`
