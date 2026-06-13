# aa-status

> বর্তমানে লোড করা AppArmor মডিউলগুলোর তালিকা দেখুন।
> আরও দেখুন: `aa-complain`, `aa-disable`, `aa-enforce`।
> আরও তথ্য পাবেন: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>।

- স্ট্যাটাস চেক করুন:

`sudo aa-status`

- JSON ফরম্যাটে স্ট্যাটাস প্রদর্শন করুন:

`sudo aa-status --json`

- সুন্দর JSON ফরম্যাটে স্ট্যাটাস প্রদর্শন করুন:

`sudo aa-status --pretty-json`

- লোড করা পলিসিগুলোর সংখ্যা প্রদর্শন করুন:

`sudo aa-status --profiled`

- লোড করা enforcing পলিসিগুলোর সংখ্যা প্রদর্শন করুন:

`sudo aa-status --enforced`

- লোড করা non-enforcing পলিসিগুলোর সংখ্যা প্রদর্শন করুন:

`sudo aa-status --complaining`

- লোড করা enforcing পলিসিগুলোর সংখ্যা প্রদর্শন করুন যা টাস্ক kill করে:

`sudo aa-status --kill`
