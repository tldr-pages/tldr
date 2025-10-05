# asciiart

> চিত্রগুলিকে ASCII তে রূপান্তর করুন।
> আরও তথ্য পাবেন: <https://github.com/nodanaonlyzuul/asciiart>।

- ফাইল থেকে একটি ছবি পড়ুন এবং ASCII তে প্রিন্ট করুন:

`asciiart {{পাথ/টু/ইমেজ.jpg}}`

- একটি URL থেকে ছবি পড়ুন এবং ASCII তে প্রিন্ট করুন:

`asciiart {{www.example.com/image.jpg}}`

- আউটপুট প্রস্থ চয়ন করুন (পূর্বনির্ধারিত হলো 100):

`asciiart {{[-w|--width]}} {{50}} {{পাথ/টু/ইমেজ.jpg}}`

- **ASCII** আউটপুট রঙিন করুন:

`asciiart {{[-c|--color]}} {{পাথ/টু/ইমেজ.jpg}}`

- আউটপুট ফরম্যাট নির্ধারণ করুন (পূর্বনির্ধারিত ফরম্যাট হলো text):

`asciiart {{[-f|--format]}} {{text|html}} {{পাথ/টু/ইমেজ.jpg}}`

- ক্যারেক্টার ম্যাপ ইনভার্ট করুন:

`asciiart {{[-i|--invert-chars]}} {{পাথ/টু/ইমেজ.jpg}}`
