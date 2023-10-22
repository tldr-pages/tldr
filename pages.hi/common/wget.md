# wget

> वेब से फ़ाइलें डाउनलोड करें।
> HTTP, HTTPS और FTP का समर्थन करता है।
> अधिक जानकारी: <https://www.gnu.org/software/wget>।

- किसी फ़ाइल में URL की अंतर्वस्तु डाउनलोड करें (इस मामले में "foo" नाम दिया गया है):

`wget {{https://example.com/foo}}`

- किसी फ़ाइल में URL की अंतर्वस्तु डाउनलोड करें (इस मामले में "bar" नाम दिया गया है):

`wget --output-document {{bar}} {{https://example.com/foo}}`

- अनुरोधों के बीच 3-सेकंड अंतराल के साथ एक एकल वेब पेज और उसके सभी संसाधन डाउनलोड करें (स्क्रिप्ट्स, स्टाइलशीट, चित्र, आदि।):

`wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}}`

- एक निर्देशिका और उसकी उप-निर्देशिकाओं में सभी सूचीबद्ध फ़ाइलें डाउनलोड करें (अंतर्निहित पृष्ठ तत्व डाउनलोड नहीं करता):

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- डाउनलोड की गति और कनेक्शन के पुन: प्रयास की संख्या सीमित करें:

`wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- मूल प्रमाणीकरण का उपयोग करके किसी HTTP सर्वर से फ़ाइल डाउनलोड करें (FTP के लिए भी काम करता है):

`wget --user={{उपयोगकर्ता_नाम}} --password={{पासवर्ड}} {{https://example.com}}`

- अधूरा डाउनलोड जारी रखें:

`wget --continue {{https://example.com}}`

- टेक्स्ट फ़ाइल में संग्रहीत सभी URL को एक विशिष्ट निर्देशिका में डाउनलोड करें:

`wget --directory-prefix {{निर्देशिका/का/पथ}} --input-file {{URLs.txt}}`
