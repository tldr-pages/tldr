# choco install

> Chocolatey ব্যবহার করে এক বা একাধিক প্যাকেজ ইনস্টল করুন।
> আরও তথ্য পাবেন: <https://docs.chocolatey.org/en-us/choco/commands/install/>।

- এক বা একাধিক প্যাকেজ ইনস্টল করুন:

`choco install {{package1 package2 ...}}`

- একটি কাস্টম কনফিগারেশন ফাইল থেকে প্যাকেজ ইনস্টল করুন:

`choco install {{path\to\packages_file.config}}`

- একটি নির্দিষ্ট `.nuspec` বা `.nupkg` ফাইল ইনস্টল করুন:

`choco install {{path\to\file}}`

- একটি প্যাকেজের নির্দিষ্ট ভার্সন ইনস্টল করুন:

`choco install {{package}} --version {{version}}`

- একটি প্যাকেজের একাধিক ভার্সন ইনস্টল করার অনুমতি দিন:

`choco install {{package}} --allow-multiple`

- সব প্রম্পট স্বয়ংক্রিয়ভাবে নিশ্চিত করুন:

`choco install {{package}} --yes`

- প্যাকেজ গ্রহণের জন্য একটি কাস্টম সোর্স নির্দিষ্ট করুন:

`choco install {{package}} --source {{source_url|alias}}`

- অথেনটিকেশনের জন্য একটি ব্যবহারকারীর নাম এবং পাসওয়ার্ড দিন:

`choco install {{package}} --user {{username}} --password {{password}}`
