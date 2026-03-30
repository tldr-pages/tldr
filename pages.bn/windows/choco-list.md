# choco list

> Chocolatey ব্যবহার করে প্যাকেজগুলোর একটি তালিকা দেখান।
> আরও তথ্য পাবেন: <https://docs.chocolatey.org/en-us/choco/commands/list/>।

- সবগুলো এভেলেভেল প্যাকেজ দেখান:

`choco list`

- লোকালভাবে ইনস্টল করা সব প্যাকেজ দেখান:

`choco list --local-only`

- লোকাল প্রোগ্রামসহ একটি তালিকা দেখান:

`choco list {{[-i|--include-programs]}}`

- শুধুমাত্র অনুমোদিত প্যাকেজ দেখান:

`choco list --approved-only`

- প্যাকেজ দেখার জন্য একটি কাস্টম সোর্স নির্দিষ্ট করুন:

`choco list {{[-s|--source]}} {{source_url|alias}}`

- অথেনটিকেশনের জন্য একটি ব্যবহারকারীর নাম এবং পাসওয়ার্ড দিন:

`choco list --user {{username}} --password {{password}}`
