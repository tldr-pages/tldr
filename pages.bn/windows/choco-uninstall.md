# choco uninstall

> Chocolatey ব্যবহার করে প্যাকেজ আনইনস্টল করুন।
> আরও তথ্য পাবেন: <https://docs.chocolatey.org/en-us/choco/commands/uninstall/>।

- এক বা একাধিক প্যাকেজ আনইনস্টল করুন:

`choco uninstall {{প্যাকেজ১ প্যাকেজ२ ...}}`

- একটি প্যাকেজের নির্দিষ্ট ভার্সন আনইনস্টল করুন:

`choco uninstall {{প্যাকেজ}} --version {{version}}`

- সব প্রম্পট স্বয়ংক্রিয়ভাবে নিশ্চিত করুন:

`choco uninstall {{প্যাকেজ}} {{[-y|--yes]}}`

- আনইনস্টল করার সময় সব ডিপেন্ডেন্সি সরিয়ে ফেলুন:

`choco uninstall {{প্যাকেজ}} {{[-x|--remove-dependencies]}}`

- সব প্যাকেজ আনইনস্টল করুন:

`choco uninstall all`
