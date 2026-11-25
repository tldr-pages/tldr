# btrfs rescue

> تلاش برای بازیابی یک سیستم فایل btrfs آسیب‌دیده.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- بازسازی درخت فرادادهٔ سیستم فایل (بسیار کند):

`sudo btrfs {{[resc|rescue]}} {{[ch|chunk-recover]}} {{path/to/partition}}`

- رفع مشکلات مربوط به هم‌ترازی اندازهٔ دستگاه (برای مثال ناتوانی در سوار کردن سیستم فایل به دلیل عدم تطابق تعداد کل بایت‌های ابر‌بلوک):

`sudo btrfs {{[resc|rescue]}} {{[fix-de|fix-device-size]}} {{path/to/partition}}`

- بازیابی یک ابر‌بلوک خراب از نسخه‌های سالم (بازیابی ریشهٔ درخت سیستم فایل):

`sudo btrfs {{[resc|rescue]}} {{[s|super-recover]}} {{path/to/partition}}`

- بازیابی از تراکنش‌های قطع‌شده (مشکلات بازپخش گزارش را برطرف می‌کند):

`sudo btrfs {{[resc|rescue]}} {{[z|zero-log]}} {{path/to/partition}}`

- ایجاد دستگاه کنترلی `/dev/btrfs-control` هنگامی که `mknod` نصب نشده است:

`sudo btrfs {{[resc|rescue]}} {{[c|create-control-device]}}`
