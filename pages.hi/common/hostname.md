# hostname

> सिस्टम का होस्टनेम प्रदर्शित या सेट करें।
> अधिक जानकारी: <https://www.man7.org/linux/man-pages/man1/hostname.1.html>.

- वर्तमान होस्टनेम दिखाएं:

`hostname`

- केवल मशीन का शॉर्ट होस्टनेम (डोमेन के बिना) दिखाएं:

`hostname --short`

- मशीन का डोमेन नाम दिखाएं:

`hostname --domain`

- नेटवर्क एड्रेस (IP पता) दिखाएं:

`hostname --ip-address`

- नया होस्टनेम सेट करें (सुपरयूज़र अधिकार आवश्यक):

`sudo hostname {{नया_होस्टनेम}}`
