# choco apikey

> चॉकलेट के स्रोतों के लिए एपीआई की प्रबंधित करें।
> अधिक जानकारी: <https://chocolatey.org/docs/commands-apikey>।

- स्रोतों और उनके एपीआई की की सूची दिखाएं:

`choco apikey`

- एक विशिष्ट स्रोत और उसके एपीआई की को दिखाएं:

`choco apikey --source "{{स्रोत_URL}}"`

- एक स्रोत के लिए एपीआई की सेट करें:

`choco apikey --source "{{स्रोत_URL}}" --key "{{api_key}}"`

- एक स्रोत के लिए एपीआई की हटाएं:

`choco apikey --source "{{स्रोत_URL}}" --remove`
