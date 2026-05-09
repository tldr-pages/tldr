# dnf config-manager

> Fedora ভিত্তিক সিস্টেমে DNF কনফিগারেশন অপশন এবং রিপোজিটরি পরিচালনা করুন।
> `dnf` এর জন্য ডিফল্ট নয় তবে `dnf-plugins-core` এর মাধ্যমে সমর্থিত।
> আরও দেখুন: `dnf`।
> আরও তথ্য পাবেন: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>।

- একটি URL থেকে একটি রিপোজিটরি যোগ করুন (এবং চালু করুন):

`dnf config-manager --add-repo={{রিপোজিটরি_url}}`

- বর্তমান কনফিগারেশন ভ্যালু প্রিন্ট করুন:

`dnf config-manager --dump`

- একটি নির্দিষ্ট রিপোজিটরি চালু করুন:

`dnf config-manager {{[--enable|--set-enabled]}} {{রিপোজিটরি_ID}}`

- নির্দিষ্ট রিপোজিটরিগুলি নিষ্ক্রিয় করুন:

`dnf config-manager {{[--disable|--set-disabled]}} {{রিপোজিটরি_ID१ রিপোজিটরি_ID२ ...}}`

- একটি রিপোজিটরির জন্য একটি কনফিগারেশন অপশন সেট করুন:

`dnf config-manager --setopt={{অপশন}}={{মান}}`

- সাহায্য প্রদশর্ন:

`dnf config-manager --help-cmd`
