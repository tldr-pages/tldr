# acme.sh --dns

> TLS সার্টিফিকেট ইস্যু করার জন্য DNS-01 চ্যালেঞ্জ ব্যবহার করুন।
> আরও তথ্য পেতে: <https://github.com/acmesh-official/acme.sh/wiki>.

- স্বয়ংক্রিয় DNS API মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns {{gnd_gd}} --domain {{example.com}}`

- স্বয়ংক্রিয় DNS API মোড ব্যবহার করে একটি উইল্ডকার্ড সার্টিফিকেট (যা একটি পূর্বনির্দেশিত চিহ্ন (*) দ্বারা চিহ্নিত) ইস্যু করুন:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- DNS অ্যালিয়াস মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- DNS রেকর্ড যোগ করার পর স্বয়ংক্রিয় Cloudflare/Google DNS পোলিং বন্ধ করে একটি সার্টিফিকেট ইস্যু করুন, সেকেন্ডে নির্দিষ্ট কাস্টম প্রতীক্ষার সময় স্পেসিফাই করে:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- ম্যানুয়াল DNS মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
