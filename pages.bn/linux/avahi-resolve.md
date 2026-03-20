# avahi-resolve

> হোস্টনেম এবং IP এড্রেসের মধ্যে রূপান্তর করে।
> আরও তথ্য পাবেন: <https://manned.org/avahi-resolve>।

- একটি লোকাল সার্ভিসকে তার IPv4-এ রূপান্তর করুন:

`avahi-resolve -4 {{[-n|--name]}} {{service.local}}`

- বিস্তারিতভাবে একটি IP-কে হোস্টনেমে রূপান্তর করুন:

`avahi-resolve {{[-v|--verbose]}} {{[-a|--address]}} {{IP}}`
