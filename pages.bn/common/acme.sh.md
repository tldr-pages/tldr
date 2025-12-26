# acme.sh

> এটি একটি শেল স্ক্রিপ্ট, যা ACME ক্লায়েন্ট প্রোটোকল বাস্তবায়ন করে, এটি `certbot`-এর একটি বিকল্প।
> আরও দেখুন: `acme.sh dns`।
> আরও তথ্য পাবেন: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>।

- webroot মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{webroot/এর/পাথ}}`

- পোর্ট ৮০ ব্যবহার করে standalone মোডে একাধিক ডোমেইনের জন্য একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- পোর্ট ৪৪৩ ব্যবহার করে standalone TLS মোডে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- কার্যকর (working) Nginx কনফিগারেশন ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- কার্যকর (working) Apache কনফিগারেশন ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- স্বয়ংক্রিয় DNS API মোড ব্যবহার করে একটি ওয়াইল্ডকার্ড (`*`) সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- নির্দিষ্ট লোকেশনে সার্টিফিকেট ফাইল ইনস্টল করুন (স্বয়ংক্রিয় সার্টিফিকেট নবায়নের জন্য উপকারী):

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{example.com.key/এর/পাথ}} --fullchain-file /{{example.com.cer/এর/পাথ}} --reloadcmd "{{systemctl force-reload nginx}}"`
