# adb shell

> एंड्रॉइड डीबग ब्रिज शेल: एंड्रॉइड एमुलेटर इंस्टेंस या कनेक्टेड एंड्रॉइड डिवाइस पर रिमोट शेल कमांड चलाएं।
> अधिक जानकारी: <https://developer.android.com/studio/command-line/adb>।

- एम्यूलेटर या डिवाइस पर रिमोट इंटरैक्टिव शेल प्रारंभ करें:

`adb shell`

- एम्यूलेटर या डिवाइस से सभी गुण प्राप्त करें:

`adb shell getprop`

- सभी रनटाइम अनुमतियों को उनके डिफ़ॉल्ट पर वापस लाएं:

`adb shell pm reset-permissions`

- किसी एप्लिकेशन के लिए खतरनाक अनुमति रद्द करें:

`adb shell pm revoke {{पैकेज}} {{अनुमति}}`

- एक महत्वपूर्ण घटना को ट्रिगर करें:

`adb shell input keyevent {{कीकोड}}`

- किसी एमुलेटर या डिवाइस पर किसी एप्लिकेशन का डेटा साफ़ करें:

`adb shell pm clear {{पैकेज}}`

- एम्यूलेटर या डिवाइस पर एक गतिविधि प्रारंभ करें:

`adb shell am start -n {{पैकेज}}/{{गतिविधि}}`

- किसी एम्यूलेटर या डिवाइस पर घरेलू गतिविधि प्रारंभ करें:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
