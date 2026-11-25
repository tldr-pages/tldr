# virt-sysprep

> بازنشانی، حذف پیکربندی یا سفارشی‌سازی تصویر ماشین مجازی.
> این دستور را می‌توان روی ماشین مجازی یا مستقیماً روی تصویر دیسک آن استفاده کرد.
> توجه: ممکن است لازم باشد `--connect URI` را به دستورها بدهید یا URI را در `$XDG_CONFIG_HOME/libvirt/libvirt.conf` تنظیم کنید.
> اطلاعات بیشتر: <https://libguestfs.org/virt-sysprep.1.html>.

- فهرست کردن همهٔ عملیات پشتیبانی‌شده (عملیات فعال پیش‌فرض با ستاره مشخص شده‌اند):

`virt-sysprep --list-operations`

- اجرای فقط عملیات مشخص:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations {{operation1,operation2,...}}`

- حذف داده‌های حساس سیستم از تصویر ماشین مجازی (عملیات مشخص‌شده به‌عنوان پیش‌فرض):

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}}`

- شبیه‌سازی اجرای همهٔ عملیات فعال روی ماشین مجازی مشخص‌شده با نام:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} {{[-n|--dry-run]}}`

- بازنشانی تنظیمات شبکهٔ NetworkManager، نگاشت‌های پایدار MAC و نام میزبان برای جلوگیری از تداخل شبکه:

`sudo virt-sysprep {{[-d|--domain]}} {{vm_name}} --operations machine-id,net-hwaddr,net-hostname,net-nmconn,customize --hostname {{new_hostname}}`

- تنظیم رمز عبور root برای تصویر دیسک:

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --operations customize --root-password password:{{new_password}}`

- افزودن کاربر جدید با رمز عبور تعیین‌شده و اضافه کردن او به گروه sudo:

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --run-command 'useradd -m {{username}} && echo {{username}}:{{password}} | chpasswd && usermod -aG sudo {{username}}'`

- نصب بسته‌های مشخص روی تصویر دیسک (برای ارتقای همهٔ بسته‌های نصب‌شده به آخرین نسخه از `--update` استفاده کنید):

`sudo virt-sysprep {{[-a|--add]}} {{path/to/image.qcow2}} --operations customize --network --install {{package_name1,package_name2,...}}`
