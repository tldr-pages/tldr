# aa-disable

> অ্যাপআরমার এর নিরাপত্তা পলিসি নিষ্ক্রিয় করুন।
> আরও দেখুন: `aa-complain`, `aa-enforce`, `aa-status`।
> আরও তথ্য পাবেন: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>।

- প্রোফাইল নিষ্ক্রিয় করুন:

`sudo aa-disable {{পাথ/টু/প্রোফাইল১ পাথ/টু/প্রোফাইল২ ...}}`

- একটি ডিরেক্টরিতে প্রোফাইল নিষ্ক্রিয় করুন (সাধারণত `/etc/apparmor.d`):

`sudo aa-disable --dir {{পাথ/টু/প্রোফাইলগুচ্ছ}}`
