# iscsiadm

> مدیریت نشست‌ها، گره‌ها و کشف iSCSI.
> اطلاعات بیشتر: <https://manned.org/iscsiadm>.

- نمایش نشست‌های فعال iSCSI:

`sudo iscsiadm {{[-m|--mode]}} session`

- فهرست کردن همهٔ گره‌های شناخته‌شدهٔ iSCSI:

`sudo iscsiadm {{[-m|--mode]}} node`

- کشف مقصدهای iSCSI موجود در یک پورتال (بدون احراز هویت):

`sudo iscsiadm {{[-m|--mode]}} discovery {{[-t|--type]}} sendtargets {{[-p|--portal]}} {{ip_address}}`

- ورود به مقصد مشخص iSCSI بدون احراز هویت:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260 {{[-l|--login]}}`

- خروج از مقصد مشخص iSCSI:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260 {{[-u|--logout]}}`

- ایجاد گره iSCSI هنگامی که کشف مسدود است (برای احراز هویت CHAP):

`sudo iscsiadm {{[-m|--mode]}} node {{[-o|--op]}} new {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260`

- پیکربندی احراز هویت CHAP برای مقصد iSCSI:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_address}}:3260 {{[-o|--op]}} update {{[-n|--name]}} node.session.auth.authmethod {{[-v|--value]}} CHAP`
