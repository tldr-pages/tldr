# findstr

> एक या एक से अधिक फाइलों में निर्दिष्ट टेक्स्ट खोजें।
> अधिक जानकारी: [https://learn.microsoft.com/windows-server/administration/windows-commands/findstr](https://learn.microsoft.com/windows-server/administration/windows-commands/findstr)।

- सभी फाइलों में एक या एक से अधिक स्ट्रिंग्स खोजें:

`findstr "{{string1 string2 ...}}" *`

- एक पाईप्ड कमांड के आउटपुट में एक या एक से अधिक स्ट्रिंग्स खोजें:

`{{dir}} | findstr "{{string1 string2 ...}}"`

- सभी फाइलों में पुनरावृत्तिपूर्वक एक या एक से अधिक स्ट्रिंग्स खोजें:

`findstr /s "{{string1 string2 ...}}" *`

- केस-इंसेंसिटिव सर्च का उपयोग करके स्ट्रिंग्स खोजें:

`findstr /i "{{string1 string2 ...}}" *`

- नियमित एक्सप्रेशंस का उपयोग करके सभी फाइलों में स्ट्रिंग्स खोजें:

`findstr /r "{{expression}}" *`

- सभी टेक्स्ट फाइलों में एक लिटरल स्ट्रिंग (जिसमें स्पेसेस शामिल हैं) खोजें:

`findstr /c:"{{string1 string2 ...}}" *.txt`

- प्रत्येक मेल खाने वाली लाइन के पहले लाइन नंबर दिखाएं:

`findstr /n "{{string1 string2 ...}}" *`

- केवल उन फाइलों के नाम दिखाएं जिनमें मैच पाया गया हो:

`findstr /m "{{string1 string2 ...}}" *`
