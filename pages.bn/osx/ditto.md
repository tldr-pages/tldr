# ditto

> ফাইল এবং ডিরেক্টরি কপি করুন।
> আরও তথ্য পাবেন: <https://ss64.com/osx/ditto.html>.

- সোর্স ডিরেক্টরির বিষয়বস্তু দিয়ে  গন্তব্য ডিরেক্টরির বিষয়বস্তু ওভাররাইট করুন:

`ditto {{path/to/source}} {{path/to/destination}}`

- কপি করা প্রতিটি ফাইলের জন্য টার্মিনাল উইন্ডোতে একটি লাইন প্রিন্ট করুন:

`ditto -V {{path/to/source}} {{path/to/destination}}`

- মূল ফাইল এর পারমিশন বজায় রেখে একটি প্রদত্ত ফাইল বা ডিরেক্টরি কপি করুন:

`ditto -rsrc {{path/to/source}} {{path/to/destination}}`
