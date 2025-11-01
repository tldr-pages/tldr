# aa-decode

> অ্যাপআর্মর (AppArmor) অডিট লগগুলোকে মানুষের পড়ার উপযোগী (human-readable) ফরম্যাটে রূপান্তর করার জন্য ব্যবহৃত কমান্ড।
> আরও তথ্য পাবেন: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-decode.8>।

- কোনো হেক্স (hex) স্ট্রিং ডিকোড করতে:

`aa-decode {{হেক্স_স্ট্রিং}}`

- কোনো লগ ফাইল ডিকোড করতে:

`sudo aa-decode {{লগফাইল}}`

- `stdin` (যেমন রিডাইরেক্ট করা ফাইল) থেকে লগ ডিকোড করতে:

`sudo aa-decode - < {{লগফাইল}}`

- সহায়তা (help) প্রদর্শন করতে:

`aa-decode {{[-h|--help]}}`
