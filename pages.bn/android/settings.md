# settings

> Android OS সম্পর্কে তথ্য পান।
> আরও তথ্য পাবেন: <https://web.archive.org/web/20240525010124/https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>।

- global নেমস্পেসের সেটিংসগুলোর তালিকা দেখুন:

`settings list {{গ্লোবাল}}`

- নির্দিষ্ট কোনো সেটিংসের মান বের করুন:

`settings get {{global}} {{airplane_mode_on}}`

- নির্দিষ্ট কোনো সেটিংসের মান সেট করুন:

`settings put {{system}} {{screen_brightness}} {{42}}`

- নির্দিষ্ট কোনো সেটিংস ডিলিট করুন:

`settings delete {{secure}} {{screensaver_enabled}}`
