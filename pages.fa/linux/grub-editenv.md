# grub-editenv

> ویرایش متغیرهای محیطی GRUB.
> اطلاعات بیشتر: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- تنظیم ورودی پیش‌فرض راه‌اندازی (با فرض وجود داشتن ورودی):

`grub-editenv /boot/grub/grubenv set default={{Ubuntu}}`

- نمایش همهٔ متغیرهای محیطی GRUB:

`grub-editenv /boot/grub/grubenv list`

- بازنشانی متغیر `saved_entry` به حالت پیش‌فرض:

`grub-editenv /boot/grub/grubenv unset saved_entry`
