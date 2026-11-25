# Natural Selection 2

> شروع سرور بدون رابط گرافیکی Natural Selection 2.
> اطلاعات بیشتر: <https://naturalselection.fandom.com/wiki/Dedicated_Server>.

- شروع سرور با تنظیمات پیش‌فرض:

`{{path/to}}/server_linux`

- تعیین نام دلخواه سرور که در مرورگر سرورها نمایش داده می‌شود:

`{{path/to}}/server_linux -name '{{server_name}}'`

- تعیین پورت اتصال سرور:

`{{path/to}}/server_linux -port {{27015}}`

- تعیین حداکثر تعداد بازیکنان:

`{{path/to}}/server_linux -limit {{2..24}}`

- تعیین نقشهٔ اولیهٔ شروع سرور:

`{{path/to}}/server_linux -map {{ns2_summit}}`

- محدود کردن دسترسی به سرور با رمز عبور:

`{{path/to}}/server_linux -password {{password}}`

- شروع سرور با رابط مدیریت webui:

`{{path/to}}/server_linux -webadmin -webport {{8080}}`
