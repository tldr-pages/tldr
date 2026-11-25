# netplan

> ابزار پیکربندی شبکه با استفاده از YAML.
> اطلاعات بیشتر: <https://netplan.readthedocs.io/en/stable/cli/>.

- اعمال پیکربندی شبکه و پایدار کردن آن:

`sudo netplan apply`

- تولید فایل‌های پیکربندی backend:

`sudo netplan generate`

- پیکربندی واسط شبکه برای استفاده از DHCP:

`sudo netplan set ethernets.{{interface_name}}.dhcp4=true`

- آزمودن تغییرات پیکربندی بدون اعمال دائمی آن‌ها:

`sudo netplan try --timeout {{seconds}}`

- بازگشت به پیکربندی کاری قبلی پس از اعمال ناموفق:

`sudo netplan --debug apply`

- نمایش وضعیت پیکربندی فعلی netplan:

`netplan status`
