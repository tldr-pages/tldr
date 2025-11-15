# btrfs

> लिनक्स के लिए कॉपी-ऑन-राइट (COW) सिद्धांत पर आधारित एक फ़ाइल सिस्टम।
> कुछ सब-कमांड जैसे `btrfs device`, उनका खुद का उपयोग दस्तावेज़न है।
> अधिक जानकारी: <https://btrfs.readthedocs.io/en/latest/btrfs.html>।

- उप-वॉल्यूम बनाएं:

`sudo btrfs subvolume create {{उप-वॉल्यूम/का/पथ}}`

- उप-वॉल्यूमों की सूची दिखाएं:

`sudo btrfs subvolume list {{माउंट_बिंदु/का/पथ}}`

- स्थान उपयोग सूचना दिखाएं:

`sudo btrfs filesystem df {{माउंट_बिंदु/का/पथ}}`

- कोटा सक्षम करें:

`sudo btrfs quota enable {{उप-वॉल्यूम/का/पथ}}`

- कोटा दिखाएं:

`sudo btrfs qgroup show {{उप-वॉल्यूम/का/पथ}}`
