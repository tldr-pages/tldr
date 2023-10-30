# apache2ctl

> अपाचे HTTP वेब सर्वर का प्रबंधन करें।
> यह कमांड डेबियन आधारित ओएस के साथ आता है, आरएचईएल आधारित ओएस के लिए `httpd` देखें।
> अधिक जानकारी: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- अपाचे डेमॉन प्रारंभ करें. यदि संदेश पहले से चल रहा हो तो उसे फेंकें:

`sudo apache2ctl start`

- अपाचे डेमॉन बंद करो:

`sudo apache2ctl stop`

- अपाचे डेमॉन को पुनरारंभ करें:

`sudo apache2ctl restart`

- कॉन्फ़िगरेशन फ़ाइल के सिंटैक्स का परीक्षण करें:

`sudo apache2ctl -t`

- लोड किए गए मॉड्यूल की सूची बनाएं:

`sudo apache2ctl -M`
