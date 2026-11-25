# kdialog

> نمایش پنجره‌های محاوره‌ای KDE از داخل اسکریپت‌های پوسته.
> اطلاعات بیشتر: <https://develop.kde.org/docs/administration/kdialog/>.

- باز کردن پنجرهٔ محاوره‌ای با پیام مشخص:

`kdialog --msgbox "{{message}}" "{{optional_detailed_message}}"`

- باز کردن پنجرهٔ پرسش با دکمه‌های `yes` و `no` که به‌ترتیب `0` و `1` برمی‌گردانند:

`kdialog --yesno "{{message}}"`

- باز کردن پنجرهٔ هشدار با دکمه‌های `yes`، `no` و `cancel` که به‌ترتیب `0`، `1` یا `2` برمی‌گردانند:

`kdialog --warningyesnocancel "{{message}}"`

- باز کردن پنجرهٔ ورود داده و چاپ ورودی در `stdout` با فشردن `OK`:

`kdialog --inputbox "{{message}}" "{{optional_default_text}}"`

- باز کردن پنجرهٔ درخواست رمز عبور مشخص و چاپ آن در `stdout`:

`kdialog --password "{{message}}"`

- باز کردن پنجرهٔ حاوی منوی کشویی مشخص و چاپ مورد انتخاب‌شده در `stdout`:

`kdialog --combobox "{{message}}" "{{item1}}" "{{item2}}" "{{...}}"`

- باز کردن پنجرهٔ انتخاب فایل و چاپ مسیر فایل انتخاب‌شده در `stdout`:

`kdialog --getopenfilename`

- باز کردن پنجرهٔ نوار پیشرفت و چاپ مرجع D-Bus برای ارتباط در `stdout`:

`kdialog --progressbar "{{message}}"`
