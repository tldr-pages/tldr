# aa-complain

> কোনো অ্যাপআর্মর (AppArmor) পলিসিকে কমপ্লেইন (complain) মোডে সেট করার জন্য ব্যবহৃত কমান্ড।
> আরও দেখুন: `aa-disable`, `aa-enforce`, `aa-status`।
> আরও তথ্য পাবেন: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>।

- কোনো প্রোফাইলকে কমপ্লেইন মোডে সেট করতে:

`sudo aa-complain {{প্রোফাইল১/এর/পাথ প্রোফাইল২/এর/পাথ ...}}`

- নির্দিষ্ট ডিরেক্টরির প্রোফাইলগুলোকে কমপ্লেইন মোডে সেট করতে:

`sudo aa-complain {{[-d|--dir]}} {{প্রোফাইল/গুলোর/পাথ}}`
