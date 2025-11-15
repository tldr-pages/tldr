# poweroff

> সিস্টেমের পাওয়ার বন্ধ করুন।
> আরও তথ্য পাবেন: <https://manned.org/poweroff>।

- সিস্টেমের পাওয়ার বন্ধ করুন:

`poweroff`

- সিস্টেম থামান (`halt` এর মতোই):

`poweroff --halt`

- সিস্টেম রিবুট করুন (`reboot` এর মতোই):

`poweroff --reboot`

- সিস্টেম ম্যানেজারকে না জানিয়েই অবিলম্বে শাট ডাউন করুন:

`poweroff {{[-f|--force]}}`

- সিস্টেম শাট ডাউন না করে wtmp শাটডাউন এন্ট্রি লিখুন:

`poweroff {{[-w|--wtmp-only]}}`
