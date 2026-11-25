# quickemu

> ساخت و مدیریت سریع ماشین‌های مجازی دسکتاپ بهینه‌شده.
> توجه: هنگام کار با snapshotها ماشین مجازی باید متوقف باشد.
> همچنین : `quickget`.
> اطلاعات بیشتر: <https://github.com/quickemu-project/quickemu>.

- ایجاد و اجرای ماشین مجازی از فایل پیکربندی:

`quickemu --vm {{path/to/file.conf}}`

- ثبت نکردن هیچ تغییری در دیسک یا snapshot و نوشتن تغییرات در فایل‌های موقت:

`quickemu --status-quo --vm {{path/to/file.conf}}`

- شروع ماشین مجازی در حالت تمام‌صفحه (`<Ctrl Alt f>` برای خروج) و انتخاب backend نمایش (پیش‌فرض `sdl`):

`quickemu --fullscreen --display {{sdl|gtk|spice|spice-app|none}} --vm {{path/to/file.conf}}`

- انتخاب دستگاه صوتی مجازی برای شبیه‌سازی و ایجاد میانبر دسکتاپ:

`quickemu --sound-card {{intel-hda|ac97|es1370|sb16|none}} --shortcut --vm {{path/to/file.conf}}`

- ایجاد، بازیابی یا حذف snapshot:

`quickemu --snapshot {{create|apply|delete}} {{tag}} --vm {{path/to/file.conf}}`

- فهرست کردن snapshotهای موجود:

`quickemu --snapshot info --vm {{path/to/file.conf}}`

- حذف کل ماشین مجازی و پیکربندی آن:

`quickemu --delete-vm --vm {{path/to/file.conf}}`

- حذف تصویر دیسک ماشین مجازی و متغیرهای EFI:

`quickemu --delete-disk --vm {{path/to/file.conf}}`
