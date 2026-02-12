# jira sprint

> Jira প্রজেক্ট বোর্ডে স্প্রিন্ট ম্যানেজ করুন।
> আরও তথ্য পাবেন: <https://github.com/ankitpokhrel/jira-cli#sprint>।

- একটি এক্সপ্লোরার ভিউতে স্প্রিন্ট এবং তাদের ইস্যু তালিকাভুক্ত করুন:

`jira sprint {{[ls|list]}}`

- বর্তমান স্প্রিন্ট থেকে ইস্যু তালিকাভুক্ত করুন:

`jira sprint {{[ls|list]}} --current`

- বর্তমান স্প্রিন্ট থেকে আমার কাছে বরাদ্দ করা ইস্যু তালিকাভুক্ত করুন:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- বর্তমান স্প্রিন্ট থেকে আমার কাছে বরাদ্দ করা হাই প্রায়োরিটিগুলো ইস্যু তালিকাভুক্ত করুন:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- একটি ইন্টার‌্যাকটিভ প্রম্পট ব্যবহার করে একটি স্প্রিন্টে ইস্যু যোগ করুন:

`jira sprint add`
