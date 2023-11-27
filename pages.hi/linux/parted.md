# parted

> एक पार्टीशन मैनिपुलेशन प्रोग्राम।
> देखें भी: `partprobe`.
> अधिक जानकारी: <https://www.gnu.org/software/parted/parted.html>।

- सभी ब्लॉक डिवाइस पर पार्टीशनों की सूची दिखाएं:

`sudo parted --list`

- निर्दिष्ट डिस्क के साथ इंटरैक्टिव मोड शुरू करें:

`sudo parted {{/dev/sdX}}`

- निर्दिष्ट लेबल-प्रकार का नया पार्टीशन टेबल बनाएं:

`sudo parted --script {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- इंटरैक्टिव मोड में पार्टीशन की जानकारी दिखाएं:

`print`

- इंटरैक्टिव मोड में डिस्क का चयन करें:

`select {{/dev/sdX}}`

- इंटरैक्टिव मोड में निर्दिष्ट फ़ाइल सिस्टम के साथ 16 जीबी का पार्टीशन बनाएं:

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- इंटरैक्टिव मोड में पार्टीशन का आकार बदलें:

`resizepart {{/dev/sdXN}} {{पार्टीशन की अंतिम स्थिति}}`

- इंटरैक्टिव मोड में एक पार्टीशन को हटाएं:

`rm {{/dev/sdXN}}`
