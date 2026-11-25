# limine

> راه‌انداز پیشرفته، قابل حمل و چندپروتکلی.
> همچنین : `limine-enroll-config`, `limine-entry-tool`, `limine-snapper-sync`.
> اطلاعات بیشتر: <https://codeberg.org/Limine/Limine>.

- نصب Limine روی دیسکی با پارتیشن‌بندی MBR:

`limine bios-install {{/dev/sdX}}`

- نصب Limine روی دیسکی با پارتیشن‌بندی GPT و پارتیشن راه‌اندازی BIOS مشخص:

`limine bios-install {{/dev/sdX}} {{partition_number}}`

- نصب Limine روی فایل تصویر دیسک:

`limine bios-install {{path/to/image.iso}}`

- نصب Limine برای سیستم‌های جدید UEFI (نیازمند بستهٔ `limine-entry-tool`):

`limine-install`

- به‌روزرسانی ورودی‌های راه‌اندازی پس از ارتقای هسته (نیازمند بستهٔ `limine-entry-tool`):

`limine-update`

- پویش سایر سیستم‌عامل‌ها برای افزودن به منوی راه‌اندازی (نیازمند بستهٔ `limine-entry-tool`):

`limine-scan`
