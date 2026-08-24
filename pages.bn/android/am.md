# am

> অ্যান্ড্রয়েড অ্যাক্টিভিটি ম্যানেজার।
> আরও তথ্য পাবেন: <https://developer.android.com/tools/adb#am>।

- নির্দিষ্ট কম্পোনেন্ট এবং প্যাকেজ নাম দিয়ে অ্যাক্টিভিটি শুরু করুন:

`am start -n {{com.android.settings/.Settings}}`

- একটি ইনটেন্ট অ্যাকশন শুরু করুন এবং এতে ডেটা পাঠান:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- নির্দিষ্ট অ্যাকশন এবং ক্যাটাগরির সাথে মেলে এমন একটি অ্যাক্টিভিটি শুরু করুন:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- একটি ইনটেন্টকে URI-তে রূপান্তর করুন:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
