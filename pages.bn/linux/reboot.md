# reboot

> মেশিনকে `reboot` করে
আরো তথ্যের জন্য: <https://manned.org/reboot.8>.

- তৎক্ষণাৎ রিবুট করে:

`reboot`

- সিস্টেমকে বন্ধ করে (পাওয়ার অফ এর বিকল্প):

`reboot --poweroff`

- সিস্টেমকে থামিয়ে দেয়:

`reboot --halt`

- Sysadmin এর সাথে যোগাযোগ না করেই তৎক্ষণাৎ রিবুট করে:

`reboot --force`

- সিস্টেমকে রিবুট না করেই wtmp শাটডাউন এন্ট্রি করে:

`reboot --wtmp-only`
