# Rename-Item

> একটি আইটেমের নাম পরিবর্তন করার জন্য PowerShell কমান্ড।
> নোট: `ren` এবং `rni` উভয়ই `Rename-Item`-এর উপনাম হিসেবে ব্যবহার করা যেতে পারে।
> আরও তথ্য পাবেন: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/rename-item>।

- একটি ফাইলের নাম পরিবর্তন করুন:

`Rename-Item -Path "{{ফাইলের_পাথ}}" -NewName "{{নতুন_ফাইলের_নাম}}"`

- একটি ডিরেক্টরির নাম পরিবর্তন করুন:

`Rename-Item -Path "{{ডিরেক্টরির_পাথ}}" -NewName "{{নতুন_ডিরেক্টরির_নাম}}"`

- একটি ফাইলের নাম বদলে অন্য স্থানে রাখুন:

`Rename-Item -Path "{{ফাইলের_পাথ}}" -NewName "{{নতুন_ফাইলের_পাথ}}"`

- একটি ফাইলের নাম জোর করে পরিবর্তন করুন:

`Rename-Item -Path "{{ফাইলের_পাথ}}" -NewName "{{নতুন_ফাইলের_নাম}}" -Force`

- একটি ফাইলের নাম পরিবর্তনের আগে নিশ্চিতকরণ চাওয়ার জন্য অনুরোধ করুন:

`Rename-Item -Path "{{ফাইলের_পাথ}}" -NewName "{{নতুন_ফাইলের_নাম}}" {{[-Confirm|-cf]}}`
