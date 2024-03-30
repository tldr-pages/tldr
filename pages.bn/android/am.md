# am

> অ্যান্ড্রয়েড অ্যাক্টিভিটি ম্যানেজার।
> আরও তথ্য পাবেন: <https://developer.android.com/tools/adb#am>।

- একটি নির্দিষ্ট কার্যকলাপ শুরু করুন:

`am start -n {{com.android.settings/.Settings}}`

- একটি কার্যকলাপ শুরু করুন এবং এতে ডেটা পাঠান:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- একটি নির্দিষ্ট কর্ম এবং বিভাগের সাথে মেলে এমন একটি কার্যকলাপ শুরু করুন:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- একটি উদ্দেশ্যকে একটি URI-তে রূপান্তর করুন:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
