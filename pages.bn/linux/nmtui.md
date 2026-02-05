# nmtui

> NetworkManager নিয়ন্ত্রণের জন্য টেক্সট ইউজার ইন্টারফেস।
> নেভিগেট করতে `<ArrowKeys>` ব্যবহার করুন, একটি অপশন নির্বাচন করতে `<Enter>` ব্যবহার করুন।
> আরও দেখুন: `nmcli`।
> আরও তথ্য পাবেন: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>।

- ইউজার ইন্টারফেস খুলুন:

`nmtui`

- সক্রিয় বা নিষ্ক্রিয় করার অপশন সহ এভেলেভেল কানেকশনগুলোর তালিকা দেখুন:

`nmtui connect`

- একটি নির্দিষ্ট নেটওয়ার্কে সংযুক্ত হন:

`nmtui connect {{নাম|uuid|ডিভাইস|SSID}}`

- একটি নির্দিষ্ট নেটওয়ার্ক এডিট/এড/ডিলিট করুন:

`nmtui edit {{নাম|id}}`

- সিস্টেম হোস্টনেম সেট করুন:

`nmtui hostname`
