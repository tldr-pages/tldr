# curl

> PowerShell-এ এই কমান্ডটি `Invoke-WebRequest`-এর একটি উপনাম (alias) হতে পারে, যদি আসল `curl` প্রোগ্রামটি (<https://curl.se>) সঠিকভাবে ইনস্টল করা না থাকে।
> আরও তথ্য পাবেন: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>।

- আসল `curl` কমান্ডের ডকুমেন্টেশন দেখুন:

`tldr curl {{[-p|--platform]}} common`

- PowerShell-এর `Invoke-WebRequest` কমান্ডের ডকুমেন্টেশন দেখুন:

`tldr invoke-webrequest`

- `curl` সঠিকভাবে ইনস্টল আছে কিনা যাচাই করতে এর ভার্সন নম্বর প্রিন্ট করুন। যদি এই কমান্ডটিতে কোনো ত্রুটি দেখায়, তাহলে PowerShell এই কমান্ডটির পরিবর্তে `Invoke-WebRequest` ব্যবহার করে থাকতে পারে:

`curl --version`
