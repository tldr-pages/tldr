# winget

> विंडोज़ पैकेज प्रबंधक।
> अधिक जानकारी: <https://learn.microsoft.com/windows/package-manager/winget>.

- एक पैकेज इनस्टॉल करें:

`winget install {{पैकेज}}`

- एक पैकेज निकालें (अनइंस्टॉल करें): (नोट: `uninstall` की जगह `remove` का भी इस्तेमाल किया जा सकता है):

`winget uninstall {{पैकेज}}`

- पैकेज के बारे में जानकारी प्रदर्शित करें:

`winget show {{पैकेज}}`

- पैकेज की खोज करें:

`winget search {{पैकेज}}`

- सभी पैकेज़ को नवीनतम संस्करणों में अपग्रेड करें:

`winget upgrade --all`

- `winget` के साथ प्रबंधित इन्सटाल्ड पैकेजों की सूची बनाएं:

`winget list --source winget`

- किसी फ़ाइल से पैकेज आयात करें, या स्थापित पैकेज़ को किसी फ़ाइल में निर्यात करें:

`winget {{import|export}} {{--import-file|--output}} {{फ़ाइल/का/पथ}}`

- विंगेट-पीकेजीएस(winget-pkgs) रिपॉजिटरी में पीआर(PR) सबमिट करने से पहले मैनिफ़ेस्ट को सत्यापित करें:

`winget validate {{प्रकट/का/पथ}}`
