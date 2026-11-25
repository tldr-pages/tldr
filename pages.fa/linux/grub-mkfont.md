# grub-mkfont

> تبدیل قالب‌های رایج فایل قلم به قالب PF2 مورد استفادهٔ GRUB.
> اطلاعات بیشتر: <https://manned.org/grub-mkfont>.

- تبدیل قلم به PF2:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{path/to/font.ttf}}`

- تبدیل قلم با اندازهٔ مشخص:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-s|--size]}} {{24}} {{path/to/font.ttf}}`

- تبدیل فقط نویسه‌های موجود در بازه‌های مشخص یونیکد:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-r|--range]}} {{0x20-0x7E,0xA0-0xFF}} {{path/to/font.ttf}}`

- تنظیم نام خانوادهٔ قلم خروجی:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-n|--name]}} "{{font_family_name}}" {{path/to/font.ttf}}`

- تبدیل قلم به ضخیم با اعمال اجباری hinting خودکار:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} {{[-b|--bold]}} {{[-a|--force-autohint]}} {{path/to/font.ttf}}`

- غیرفعال کردن hinting و نادیده گرفتن اندازه‌های bitmap جاسازی‌شده:

`grub-mkfont {{[-o|--output]}} {{path/to/output.pf2}} --no-hinting --no-bitmap {{path/to/font.ttf}}`
