# btrfs

> लिनक्स के लिए कॉपी-ऑन-राइट (COW) सिद्धांत पर आधारित एक फ़ाइल सिस्टम।
> कुछ सब-कमांड जैसे `btrfs device`, उनका खुद का उपयोग दस्तावेज़न है।
> अधिक जानकारी: <https://btrfs.readthedocs.io/en/latest/btrfs.html>।

- उप-वॉल्यूम बनाएं:

`sudo btrfs subvolume create {{पथ/से/उप-वॉल्यूम}}`

- उप-वॉल्यूमों की सूची दिखाएं:

`sudo btrfs subvolume list {{पथ/से/माउंट_बिंदु}}`

- स्थान उपयोग सूचना दिखाएं:

`sudo btrfs filesystem df {{पथ/से/माउंट_बिंदु}}`

- कोटा सक्षम करें:

`sudo btrfs quota enable {{पथ/से/उप-वॉल्यूम}}`

- कोटा दिखाएं:

`sudo btrfs qgroup show {{पथ/से/उप-वॉल्यूम}}`
