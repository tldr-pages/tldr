# tshark

> ابزار تحلیل بسته، نسخهٔ خط فرمان Wireshark.
> اطلاعات بیشتر: <https://tshark.dev/#sitemap-in-tshark---help>.

- پایش بسته‌ها از واسط پیش‌فرض:

`tshark`

- ضبط فقط بسته‌های مطابق فیلتر ضبط مشخص:

`tshark -f '{{udp port 53}}'`

- نمایش فقط بسته‌های مطابق فیلتر خروجی مشخص:

`tshark -Y '{{http.request.method == "GET"}}'`

- رمزگشایی پورت TCP با پروتکل مشخص (مانند HTTP):

`tshark -d tcp.port=={{8888}},{{http}}`

- تعیین قالب خروجی ضبط‌شده:

`tshark -T {{json|text|ps|...}}`

- انتخاب فیلدهای مشخص برای خروجی:

`tshark -T {{fields|ek|json|pdml}} -e {{http.request.method}} -e {{ip.src}}`

- نوشتن بستهٔ ضبط‌شده در فایل:

`tshark -w {{path/to/file}}`

- تحلیل بسته‌ها از فایل:

`tshark -r {{path/to/file.pcap}}`
