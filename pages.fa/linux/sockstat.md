# sockstat

> فهرست کردن سوکت‌های باز Internet یا دامنهٔ UNIX.
> همچنین ببینید: `netstat`.
> اطلاعات بیشتر: <https://manned.org/sockstat>.

- نمایش اطلاعات سوکت‌های IPv4 و IPv6 برای سوکت‌های در حال گوش دادن و متصل:

`sockstat`

- نمایش اطلاعات سوکت‌های IPv4 یا IPv6 در حال گوش دادن روی پورت‌های مشخص با پروتکل مشخص:

`sockstat -{{4|6}} -l -R {{tcp|udp|raw|unix}} -p {{port1,port2...}}`

- نمایش سوکت‌های متصل و سوکت‌های Unix نیز:

`sockstat -cu`

- نمایش فقط سوکت‌های `process_id` یا فرایند مشخص:

`sockstat -P {{process_id|process_name}}`

- نمایش فقط سوکت‌های `user_id` یا کاربر مشخص:

`sockstat -U {{user_id|username}}`

- نمایش فقط سوکت‌های `group_id` یا گروه مشخص:

`sockstat -G {{group_id|group_name}}`
