# wget

> পাওয়ারশেলে, এই কমান্ডটি অরিজিনাল `wget` প্রোগ্রাম (<https://www.gnu.org/software/wget>) সঠিকভাবে ইনস্টল না থাকলে এটি `Invoke-WebRequest` এর এলিয়াস হতে পারে।
> আরও তথ্য পাবেন: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>।

- মৌলিক `wget` কমান্ডের জন্য নথি:

`tldr wget -p common`

- পাওয়ারশেলের `Invoke-WebRequest` কমান্ডের জন্য নথি:

`tldr invoke-webrequest`

- চেষ্টা করুন যে কি `wget` সঠিকভাবে ইনস্টল করা হয়েছে কিনা, এর সংস্করণ নম্বর প্রিন্ট করে। যদি এই কমান্ডটি একটি ত্রুটির মধ্যে মূল `Invoke-WebRequest` দিয়ে বদলে যায়, তবে:

`wget --version`
