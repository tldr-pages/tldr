# choco outdated

> चॉकलेट के साथ पुराने पैकेजों की जांच करें।
> अधिक जानकारी: <https://chocolatey.org/docs/commands-outdated>।

- पुराने पैकेजों की तालिका प्रारूप में सूची प्रदर्शित करें:

`choco outdated`

- आउटपुट में पिन किए गए पैकेजों की अनदेखी करें:

`choco outdated --ignore-pinned`

- पैकेजों की जांच के लिए एक कस्टम स्रोत निर्दिष्ट करें:

`choco outdated --source {{स्रोत_url|उपनाम}}`

- प्रमाणीकरण के लिए एक उपयोगकर्ता नाम और पासवर्ड प्रदान करें:

`choco outdated --user {{उपयोगकर्ता_नाम}} --password {{पासवर्ड}}`
