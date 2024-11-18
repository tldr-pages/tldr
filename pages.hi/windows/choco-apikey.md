# choco apikey

> चॉकलेट के स्रोतों के लिए एपीआई की प्रबंधित करें।
> अधिक जानकारी: <https://chocolatey.org/docs/commands-apikey>।

- स्रोतों और उनके API चाबी की सूची दिखाएं:

`choco apikey`

- एक विशिष्ट स्रोत और उसके API चाबी को दिखाएं:

`choco apikey --source "{{स्रोत_URL}}"`

- एक स्रोत के लिए API चाबी सेट करें:

`choco apikey --source "{{स्रोत_URL}}" --key "{{api_चाबी}}"`

- एक स्रोत के लिए API चाबी हटाएं:

`choco apikey --source "{{स्रोत_URL}}" --remove`
