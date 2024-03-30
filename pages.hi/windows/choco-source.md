# choco source

> चॉकलेटी वाले पैकेजों के लिए स्रोत प्रबंधित करें।
> अधिक जानकारी: <https://chocolatey.org/docs/commands-source>।

- वर्तमान में उपलब्ध स्रोतों की सूची बनाएं:

`choco source list`

- एक नया पैकेज स्रोत जोड़ें:

`choco source add --name {{नाम}} --source {{यूआरएल}}`

- क्रेडेंशियल्स के साथ एक नया पैकेज स्रोत जोड़ें:

`choco source add --name {{नाम}} --source {{यूआरएल}} --user {{उपयोगकर्ता नाम}} --password {{पासवर्ड}}`

- क्लाइंट प्रमाणपत्र के साथ एक नया पैकेज स्रोत जोड़ें:

`choco source add --name {{नाम}} --source {{यूआरएल}} --cert {{प्रमाणपत्र_फ़ाइल\का\पथ}}`

- पैकेज स्रोत सक्षम करें:

`choco source enable --name {{नाम}}`

- पैकेज स्रोत को अक्षम करें:

`choco source disable --name {{नाम}}`

- पैकेज स्रोत हटाएँ:

`choco source remove --name {{नाम}}`
