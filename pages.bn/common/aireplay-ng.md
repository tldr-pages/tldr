# aireplay-ng

> ওয়ায়ারলেস নেটওয়ার্কে প্যাকেট ইনজেক্ট করুন।
> `aireplay-ng` এর একটি অংশ।
> আরও জানতে: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- একটি এক্সেস পয়েন্টের MAC ঠিকানা, ক্লায়েন্টের MAC ঠিকানা এবং একটি ইন্টারফেস দেখে একটি নির্দিষ্ট সংখ্যক অপ্রাপ্ত প্যাকেট পাঠান:

`sudo aireplay-ng --deauth {{গণনা}} --bssid {{ap_mac}} --dmac {{client_mac}} {{ইন্টারফেস}}`
