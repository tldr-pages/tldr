# cgcreate

> ایجاد cgroupها برای محدود کردن، اندازه‌گیری و کنترل منابع مصرفی فرایندها.
> انواع `cgroups` می‌توانند `memory`، `cpu`، `net_cls` و غیره باشند.
> اطلاعات بیشتر: <https://manned.org/cgcreate>.

- ایجاد یک گروه جدید با `-g`:

`cgcreate -g {{group_type}}:{{group_name}}`

- ایجاد یک گروه جدید با چند نوع cgroup با `-g`:

`cgcreate -g {{group_type1}},{{group_type2}}:{{group_name}}`

- ایجاد یک زیرگروه:

`mkdir /sys/fs/cgroup/{{group_type}}/{{group_name}}/{{subgroup_name}}`
