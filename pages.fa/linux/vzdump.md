# vzdump

> ابزار پشتیبان‌گیری از ماشین‌های مجازی و کانتینرها.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- تهیهٔ نسخهٔ پشتیبان از ماشین مجازی مهمان در دایرکتوری پیش‌فرض (معمولاً `/var/lib/vz/dump/`) بدون snapshotها:

`vzdump {{vm_id}}`

- پشتیبان‌گیری از ماشین‌های مجازی مهمان با شناسه‌های ۱۰۱، ۱۰۲ و ۱۰۳:

`vzdump {{101 102 103}}`

- تهیهٔ نسخهٔ پشتیبان از ماشین مجازی مهمان با حالت مشخص:

`vzdump {{vm_id}} --mode {{suspend|snapshot}}`

- پشتیبان‌گیری از همهٔ سیستم‌های مهمان و ارسال ایمیل اعلان به کاربران root و admin:

`vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}`

- استفاده از حالت snapshot (بدون نیاز به توقف) و دایرکتوری غیربه‌پیش‌فرض برای پشتیبان:

`vzdump {{vm_id}} --dumpdir {{path/to/directory}} --mode {{snapshot}}`

- پشتیبان‌گیری از همهٔ ماشین‌های مجازی مهمان به‌جز شناسه‌های ۱۰۱ و ۱۰۲:

`vzdump --mode {{suspend}} --exclude {{101, 102}}`
