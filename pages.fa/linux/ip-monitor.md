# ip monitor

> پایش شبکه برای تغییرات وضعیت.
> اطلاعات بیشتر: <https://manned.org/ip-monitor>.

- پایش کل شبکه برای تغییرات وضعیت:

`ip {{[mo|monitor]}}`

- تعیین نوع مورد پایش:

`ip {{[mo|monitor]}} {{link|address|route|neigh|rule|maddress|...}}`

- بازپخش فایل رویداد (قابل تولید با `rtmon`):

`ip {{[mo|monitor]}} {{[f|file]}} {{path/to/file}}`
