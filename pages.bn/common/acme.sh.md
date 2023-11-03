# acme.sh

> ACME ক্লায়েন্ট প্রোটোকল প্রয়োজনীয় স্ক্রিপ্ট, certbot এর একটি বিকল্প।
> `acme.sh dns` দেখুন।
> আরও তথ্য পেতে: <https://github.com/acmesh-official/acme.sh>|

- ওয়েবরুট মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --domain {{example.com}} --webroot {{/পাথ/টু/ওয়েবরুট}}`

- পোর্ট ৮০ ব্যবহার করে স্ট্যান্ডঅলোন মোড ব্যবহার করে একটি মাল্টিপল ডোমেনের জন্য একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}`

- পোর্ট ৪৪৩ ব্যবহার করে স্ট্যান্ডঅলোন TLS মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --alpn --domain {{example.com}}`

- কাজকর্ম Nginx কনফিগারেশন ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --nginx --domain {{example.com}}`

- কাজকর্ম অ্যাপাচি কনফিগারেশন ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --apache --domain {{example.com}}`

- স্বয়ংক্রিয় DNS API মোড ব্যবহার করে একটি উইল্ডকার্ড (\*) সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns {{dns_cf}} --domain {{*.example.com}}`

- নির্দিষ্ট অবস্থানে সার্টিফিকেট ফাইল ইনস্টল করুন (স্বয়ংক্রিয় সার্টিফিকেট পুনরারম্ভের জন্য উপযুক্ত):

`acme.sh --install-cert -d {{example.com}} --key-file {{/পথ/থেকে/উদাহরণ.কম.কি}} --fullchain-file {{/পথ/থেকে/উদাহরণ.কম.সিআর}} --reloadcmd {{"systemctl force-reload nginx"}}`
