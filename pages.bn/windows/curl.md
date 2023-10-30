# curl

> পাওয়ারশেলে, এই কমান্ডটি অরিজিনাল `curl` প্রোগ্রাম (<https://curl.se>) সঠিকভাবে ইনস্টল না থাকলে এটি `Invoke-WebRequest` এর এলিয়াস হতে পারে।
> আরও তথ্য পাবেন: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>।

- চেষ্টা করুন যে কি `curl` সঠিকভাবে ইনস্টল করা হয়েছে কিনা, এর সংস্করণ নম্বর প্রিন্ট করে। যদি এই কমান্ডটি একটি ত্রুটির মধ্যে মূল `Invoke-WebRequest` দিয়ে বদলে যায়, তবে:

`curl --version`

- মৌলিক `curl` কমান্ডের জন্য নথি:

`tldr curl -p common`

- `tldr` কমান্ড-লাইন ক্লায়েন্টের পুরোনো সংস্করণের জন্য `curl` কমান্ডের জন্য নথি:

`tldr curl -o common`

- পাওয়ারশেলের `Invoke-WebRequest` কমান্ডের জন্য নথি:

`tldr invoke-webrequest`
