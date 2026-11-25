# mkhomedir_helper

> ایجاد دایرکتوری خانگی کاربر پس از ایجاد کاربر.
> اطلاعات بیشتر: <https://manned.org/mkhomedir_helper>.

- ایجاد دایرکتوری خانگی برای کاربر بر اساس `/etc/skel` با umask برابر 022:

`sudo mkhomedir_helper {{username}}`

- ایجاد دایرکتوری خانگی برای کاربر بر اساس `/etc/skel` با همهٔ مجوزها برای مالک (0) و مجوز خواندن برای گروه (3):

`sudo mkhomedir_helper {{username}} {{037}}`

- ایجاد دایرکتوری خانگی برای کاربر بر اساس اسکلت دلخواه:

`sudo mkhomedir_helper {{username}} {{umask}} {{path/to/skeleton_directory}}`
