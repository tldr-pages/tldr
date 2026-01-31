# Get-History

> PowerShell কমান্ডের ইতিহাস প্রদর্শনের জন্য ব্যবহৃত হয়।
> নোট: এই কমান্ডটি শুধুমাত্র PowerShell এর মাধ্যমে ব্যবহার করা যেতে পারে।
> আরও তথ্য পাবেন: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-history>।

- আইডি সহ কমান্ডগুলোর ইতিহাসের তালিকা দেখুন:

`Get-History`

- আইডি ব্যবহার করে নির্দিষ্ট PowerShell হিস্ট্রি আইটেম পান:

`Get-History -Id {{id}}`

- শেষ `n` সংখ্যক কমান্ড প্রদর্শন করুন:

`Get-History -Count {{n}}`
