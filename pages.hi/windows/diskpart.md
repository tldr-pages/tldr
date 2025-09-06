# diskpart

> डिस्क, वॉल्यूम और विभाजन प्रबंधक।
> अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>।

- इसकी कमांड-लाइन दर्ज करने के लिए प्रशासनिक कमांड प्रॉम्प्ट में डिस्कपार्ट (diskpart) को स्वयं चलाएँ:

`diskpart`

- सभी डिस्क की सूची बनाएं:

`list disk`

- एक वॉल्यूम चुनें:

`select volume {{वॉल्यूम}}`

- चयनित वॉल्यूम के लिए एक ड्राइव अक्षर (letter) निर्दिष्ट करें:

`assign letter {{अक्षर}}`

- एक नया विभाजन बनाएँ:

`create partition primary`

- चयनित वॉल्यूम सक्रिय करें:

`active`

- डिस्कपार्ट (diskpart) से बाहर निकलें:

`exit`
