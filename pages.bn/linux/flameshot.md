# flameshot

> GUI সহ স্ক্রিনশট ইউটিলিটি।
> টেক্সট, শেইপ, কালার এবং imgur এর মতো বেসিক ইমেজ এডিটিং সাপোর্ট করে।
> আরও তথ্য পাবেন: <https://flameshot.org/docs/advanced/commandline-options/>।

- সম্পূর্ণ স্ক্রিনের স্ক্রিনশট নিতে:

`flameshot full`

- ইন্টারঅ্যাকটিভভাবে স্ক্রিনশট নিতে:

`flameshot gui`

- নির্দিষ্ট পাথে স্ক্রিনশট সেভ করতে:

`flameshot gui {{[-p|--path]}} {{পাথ/টু/ডিরেক্টরি}}`

- সরলীকৃত মোডে (simplified mode) ইন্টারঅ্যাকটিভভাবে স্ক্রিনশট নিতে:

`flameshot launcher`

- নির্দিষ্ট মনিটর থেকে স্ক্রিনশট নিতে:

`flameshot screen {{[-n|--number]}} {{2}}`

- স্ক্রিনশট নিয়ে `stdout`-এ প্রিন্ট করতে:

`flameshot gui {{[-r|--raw]}}`

- স্ক্রিনশট নিয়ে ক্লিপবোর্ডে কপি করতে:

`flameshot gui {{[-c|--clipboard]}}`

- নির্দিষ্ট বিলম্বসহ (মিলিসেকেন্ডে) স্ক্রিনশট নিতে:

`flameshot full {{[-d|--delay]}} {{5000}}`
