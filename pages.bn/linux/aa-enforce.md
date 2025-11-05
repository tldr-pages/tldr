# aa-enforce

> কোনো অ্যাপআর্মর (AppArmor) প্রোফাইলকে এনফোর্স (enforce) মোডে সেট করার জন্য ব্যবহৃত হয়।
> আরও দেখুন: `aa-complain`, `aa-disable`, `aa-status`।
> আরও তথ্য পাবেন: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>।

- নির্দিষ্ট প্রোফাইলকে এনফোর্স (enforce) মোডে চালু করতে:

`sudo aa-enforce {{[-d|--dir]}} {{প্রোফাইল/এর/পাথ}}`

- একাধিক প্রোফাইল এনফোর্স (enforce) মোডে চালু করতে:

`sudo aa-enforce {{প্রোফাইল/এর/পাথ1 প্রোফাইল/এর/পাথ2 ...}}`
