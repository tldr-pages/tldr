# egrep

> এক্সটেন্ডেড `regex` দিয়ে ফাইলে প্যাটার্ন খুঁজুন।
> নোট: এটি `grep --extended-regexp`-এর একটি উপনাম (alias)।
> আরও তথ্য পাবেন: <https://manned.org/egrep>।

- এক বা একাধিক পুনরাবৃত্ত অক্ষর অনুসন্ধান করুন:

`egrep '{{a}}+' {{path/to/file}}`

- শূন্য বা একবার উপস্থিত অক্ষর অনুসন্ধান করুন (ঐচ্ছিক মিল):

`egrep '{{a}}?' {{path/to/file}}`

- কোনো অক্ষরের 10 বার পুনরাবৃত্তি অনুসন্ধান করুন:

`egrep '{{a}}{10}' {{path/to/file}}`

- তালিকাভুক্ত বিকল্পগুলোর যেকোনো একটি অনুসন্ধান করুন:

`egrep '({{cat}}|{{dog}}|{{mouse}})' {{path/to/file}}`

- স্ট্যান্ডার্ড character classes ব্যবহার করে অনুসন্ধান করুন (আরও তথ্য: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{path/to/file}}`
