# choco info

> चॉकलेट के साथ एक पैकेज के बारे में विस्तृत जानकारी प्रदर्शित करें।
> अधिक जानकारी: <https://chocolatey.org/docs/commands-info>।

- एक विशेष पैकेज पर जानकारी प्रदर्शित करें:

`choco info {{पैकेज}}`

- केवल एक स्थानीय पैकेज के लिए जानकारी प्रदर्शित करें:

`choco info {{पैकेज}} --local-only`

- पैकेजों की जानकारी प्राप्त करने के लिए एक कस्टम स्रोत निर्दिष्ट करें:

`choco info {{पैकेज}} --source {{स्रोत_यूआरएल|उपनाम}}`

- प्रमाणीकरण के लिए एक उपयोगकर्ता नाम और पासवर्ड प्रदान करें:

`choco info {{पैकेज}} --user {{उपयोगकर्ता_नाम}} --password {{पासवर्ड}}`
