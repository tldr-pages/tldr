# input

> একটি Android ডিভাইসে ইভেন্ট কোড বা টাচস্ক্রিন অঙ্গভঙ্গি পাঠান।
> এই কমান্ডটি শুধুমাত্র `adb shell` এর মাধ্যমে ব্যবহার করা যেতে পারে।
> আরও তথ্য: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>।

- একটি Android ডিভাইসে একটি একক অক্ষরের জন্য একটি ইভেন্ট কোড পাঠান:

`input keyevent {{event code}}`

- একটি অ্যান্ড্রয়েড ডিভাইসে একটি পাঠ্য পাঠান (`%s` স্পেস প্রতিনিধিত্ব করে):

`input text "{{লেখা}}"`

- একটি Android ডিভাইসে একটি একক ট্যাপ পাঠান:

`input tap {{x_pos}} {{y_pos}}`

- একটি Android ডিভাইসে একটি সোয়াইপ অঙ্গভঙ্গি পাঠান:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- একটি সোয়াইপ অঙ্গভঙ্গি ব্যবহার করে একটি Android ডিভাইসে একটি দীর্ঘ প্রেস পাঠান:

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duration_in_ms}}`
