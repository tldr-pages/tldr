# choco push

> একটি কম্পাইল করা NuGet প্যাকেজ (`.nupkg`) একটি প্যাকেজ ফিডে পাঠান।
> আরও তথ্য পাবেন: <https://docs.chocolatey.org/en-us/create/commands/push/>।

- নির্দিষ্ট ফিডে একটি কম্পাইল করা `.nupkg` পাঠান:

`choco push {{[-s|--source]}} {{https://push.chocolatey.org/}}`

- নির্দিষ্ট ফিডে সেকেন্ডে ঠিক করা টাইমআউটসহ (ডিফল্ট 2700) একটি কম্পাইল করা `.nupkg` পাঠান:

`choco push {{[-s|--source]}} {{https://push.chocolatey.org/}} {{[--timeout|--execution-timeout]}} {{500}}`
