# virt-xml

> ویرایش فایل‌های XML دامنهٔ libvirt با گزینه‌های صریح خط فرمان.
> توجه: `domain` به نام، UUID یا شناسهٔ ماشین مجازی موجود اشاره دارد.
> همچنین ببینید: `virsh`.
> اطلاعات بیشتر: <https://github.com/virt-manager/virt-manager/blob/main/man/virt-xml.rst>.

- فهرست کردن همهٔ زیرگزینه‌های یک گزینهٔ مشخص:

`virt-xml --{{option}}=?`

- فهرست کردن همهٔ زیرگزینه‌های دیسک، شبکه و راه‌اندازی:

`virt-xml --disk=? --network=? --boot=?`

- ویرایش مقداری برای دامنهٔ مشخص:

`virt-xml {{domain}} --edit --{{option}} {{suboption}}={{new_value}}`

- تغییر توضیح دامنهٔ مشخص:

`virt-xml {{domain}} --edit --metadata description="{{new_description}}"`

- فعال یا غیرفعال کردن منوی دستگاه راه‌اندازی برای دامنهٔ مشخص:

`virt-xml {{domain}} --edit --boot bootmenu={{on|off}}`

- اتصال هاب USB میزبان به ماشین مجازی در حال اجرا (برای مشاهدهٔ دستگاه‌های USB و شناسه‌های آن‌ها `lsusb` را اجرا کنید):

`virt-xml {{domain}} --update --add-device --hostdev {{bus}}.{{device}}`
