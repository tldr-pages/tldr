# settings

> Android OS সম্পর্কে তথ্য পান।
> আরও তথ্য পাবেন: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- `global` নামস্থানে সেটিংসের একটি তালিকা প্রদর্শন করুন:

`settings list {{গ্লোবাল}}`

- একটি নির্দিষ্ট সেটিং এর মান পান:

`settings get {{global}} {{airplane_mode_on}}`

- একটি সেটিং এর একটি নির্দিষ্ট মান সেট করুন:

`settings put {{system}} {{screen_brightness}} {{1..100}}`

- একটি নির্দিষ্ট সেটিং মুছুন:

`settings delete {{secure}} {{screensaver_enabled}}`
