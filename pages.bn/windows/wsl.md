# wsl

> Windows Subsystem for Linux পরিচালনা করুন।
> আরও তথ্য পাবেন: <https://learn.microsoft.com/windows/wsl/reference>।

- একটি লিনাক্স shell শুরু করুন (ডিফল্ট ডিস্ট্রিবিউশন এ):

`wsl {{shell_command}}`

- একটি shell ব্যবহার না করে একটি লিনাক্স কমান্ড চালান:

`wsl {{[-e|--exec]}} {{command}} {{command_arguments}}`

- একটি নির্দিষ্ট ডিস্ট্রিবিউশন উল্লেখ করুন:

`wsl {{[-d|--distribution]}} {{distribution}} {{shell_command}}`

- ব্যবহারযোগ্য ডিস্ট্রিবিউশনগুলি তালিকা করুন:

`wsl {{[-l|--list]}}`

- একটি ডিস্ট্রিবিউশন `.tar` ফাইলে এক্সপোর্ট করুন:

`wsl --export {{distribution}} {{পাথ\টু\ডিস্ট্রো_ফাইল.tar}}`

- একটি `.tar` ফাইল থেকে ডিস্ট্রিবিউশন ইম্পোর্ট করুন:

`wsl --import {{distribution}} {{পাথ\টু\ইনস্টল_লোকেশন}} {{পাথ/টু/ডিস্ট্রো_ফাইল.tar}}`

- নির্দিষ্ট ডিস্ট্রিবিউশনের জন্য ব্যবহৃত wsl এর সংস্করণ পরিবর্তন করুন:

`wsl --set-version {{distribution}} {{version}}`

- Windows Subsystem for Linux বন্ধ করুন:

`wsl --shutdown`
