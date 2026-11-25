# sbctl

> مدیر کاربرپسند کلید Secure Boot.
> توجه: ثبت نکردن گواهی‌های Microsoft می‌تواند سیستم را از کار بیندازد. <https://github.com/Foxboron/sbctl/wiki/FAQ#option-rom> را ببینید.
> اطلاعات بیشتر: <https://github.com/Foxboron/sbctl#usage>.

- نمایش وضعیت فعلی Secure Boot:

`sbctl status`

- ایجاد کلیدهای دلخواه Secure Boot (به‌طور پیش‌فرض همه‌چیز در `/var/lib/sbctl` ذخیره می‌شود):

`sbctl create-keys`

- ثبت کلیدهای دلخواه Secure Boot و گواهی‌های فروشندهٔ UEFI مربوط به Microsoft:

`sbctl enroll-keys {{[-m|--microsoft]}}`

- اجرای خودکار `create-keys` و `enroll-keys` بر اساس تنظیمات `/etc/sbctl/sbctl.conf`:

`sbctl setup --setup`

- امضای فایل دودویی EFI با کلید ایجادشده و ذخیرهٔ فایل در پایگاه داده:

`sbctl sign {{[-s|--save]}} {{path/to/efi_binary}}`

- امضای مجدد همهٔ فایل‌های ذخیره‌شده:

`sbctl sign-all`

- بررسی امضا شدن همهٔ فایل‌های اجرایی EFI در پارتیشن سیستمی EFI:

`sbctl verify`
