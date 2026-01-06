# Clear-History

> PowerShell সেশন কমান্ড হিস্ট্রি থেকে এন্ট্রি মুছে ফেলুন।
> নোট: `Clear-History`-এর উপনাম হিসাবে `clhy` ব্যবহার করা যেতে পারে।
> আরও তথ্য পাবেন: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/clear-history>।

- বর্তমান সেশন থেকে সমস্ত কমান্ড হিস্ট্রি পরিষ্কার করুন:

`Clear-History`

- নির্দিষ্ট নাম দ্বারা কমান্ড পরিষ্কার করুন:

`Clear-History -CommandLine "{{কমান্ড}}"`

- নাম দ্বারা একাধিক কমান্ড পরিষ্কার করুন:

`Clear-History -CommandLine {{"কমান্ড১", "কমান্ড২", ...}}`

- ID দ্বারা একটি নির্দিষ্ট হিস্ট্রি এন্ট্রি পরিষ্কার করুন:

`Clear-History -Id {{id_number}}`

- একাধিক ID পরিষ্কার করুন:

`Clear-History -Id {{id1, id2, ...}}`

- ID-এর একটি পরিসরের মধ্যে কমান্ড পরিষ্কার করুন:

`Clear-History -Id ({{start_id}}..{{end_id}})`

- কী মুছে ফেলা হবে সেটা দেখান:

`Clear-History -WhatIf`

- পরিষ্কার করার আগে নিশ্চিতকরণ জিজ্ঞাসা করুন:

`Clear-History -Confirm`
