# choco apikey

> चॉकलेट के स्रोतों के लिए एपीआई की प्रबंधित करें।
> अधिक जानकारी: <https://docs.chocolatey.org/en-us/create/commands/api-key/>।

- स्रोतों और उनके API चाबी की सूची दिखाएं:

`choco apikey`

- एक विशिष्ट स्रोत और उसके API चाबी को दिखाएं:

`choco apikey {{[-s|--source]}} "{{स्रोत_URL}}"`

- एक स्रोत के लिए API चाबी सेट करें:

`choco apikey {{[-s|--source]}} "{{स्रोत_URL}}" {{[-k|--api-key]}} "{{api_चाबी}}"`

- एक स्रोत के लिए API चाबी हटाएं:

`choco apikey {{[-s|--source]}} "{{स्रोत_URL}}" --remove`
