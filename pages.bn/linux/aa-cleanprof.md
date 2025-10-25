# aa-cleanprof

> অ্যাপআর্মর (AppArmor) সিকিউরিটি প্রোফাইলগুলো থেকে অপ্রয়োজনীয় রুল (rule) সরিয়ে প্রোফাইল পরিষ্কার করার জন্য ব্যবহৃত কমান্ড।
> আরও তথ্য পাবেন: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>।

- কোনো প্রোফাইল পরিষ্কার করে অপ্রয়োজনীয় রুল সরাতে:

`sudo aa-cleanprof {{প্রোফাইলের_নাম}}`

- একাধিক প্রোফাইল একসাথে পরিষ্কার করতে:

`sudo aa-cleanprof {{প্রোফাইল1 প্রোফাইল2 ...}}`

- প্রোফাইলসমূহ যেই ডিরেক্টরিতে আছে তা নির্দিষ্ট করতে:

`sudo aa-cleanprof {{[-d|--dir]}} /{{path/to/profiles}} {{প্রোফাইলের_নাম}}`

- প্রম্পট (prompt) ছাড়াই নীরবে (silent mode) চালাতে:

`sudo aa-cleanprof {{[-s|--silent]}} {{প্রোফাইলের_নাম}}`

- পরিষ্কারের পর প্রোফাইল রিলোড হওয়া বন্ধ করতে:

`sudo aa-cleanprof --no-reload {{প্রোফাইলের_নাম}}`

- সহায়তা (help) প্রদর্শন করতে:

`aa-cleanprof {{[-h|--help]}}`
