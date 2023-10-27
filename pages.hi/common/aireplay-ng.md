# aireplay-ng

> वायरलेस नेटवर्क में पैकेट इंजेक्ट करें। एयरक्रैक-एनजी का हिस्सा। 

> अधिक जानकारी: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- एक्सेस प्वाइंट के मैक पते, क्लाइंट के मैक पते और एक इंटरफ़ेस को देखते हुए एक विशिष्ट संख्या में असंबद्ध पैकेट भेजें:

` sudo aireplay-ng --deauth {{count}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}} `

