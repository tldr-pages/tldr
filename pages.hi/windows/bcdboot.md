# bcdboot

> बूट फ़ाइलों को कॉन्फ़िगर या सुधारें।
> अधिक जानकारी: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>।

- स्रोत विंडोज़ फ़ोल्डर से BCD फ़ाइलों का उपयोग करके सिस्टम विभाजन को प्रारंभ करें:

`bcdboot {{C:\Windows}}`

- वर्बोज़(verbose[v]) मोड सक्षम करें:

`bcdboot {{C:\Windows}} /v`

- सिस्टम विभाजन का वॉल्यूम अक्षर निर्दिष्ट करें:

`bcdboot {{C:\Windows}} /s {{S:}}`

- कोई स्थान निर्दिष्ट करें:

`bcdboot {{C:\Windows}} /l {{en-us}}`

- बूट फ़ाइलों को निर्दिष्ट वॉल्यूम पर कॉपी करते समय फ़र्मवेयर प्रकार निर्दिष्ट करें:

`bcdboot {{C:\Windows}} /s {{S:}} /f {{UEFI|BIOS|ALL}}`
