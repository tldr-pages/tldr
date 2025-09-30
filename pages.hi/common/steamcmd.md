# steamcmd

> स्टीम क्लाइंट का एक कमांड-लाइन संस्करण।
> अधिक जानकारी: <https://manned.org/steamcmd>।

- एक एप्लिकेशन को गुमनाम रूप से स्थापित या अपडेट करें:

`steamcmd +login {{गुमनाम}} +app_update {{ऐप आईडी}} +quit`

- निर्दिष्ट क्रेडेंशियल का उपयोग करके एक एप्लिकेशन को स्थापित या अपडेट करें:

`steamcmd +login {{उपयोगकर्ता_नाम}} +app_update {{ऐप आईडी}} +quit`

- एक विशिष्ट प्लेटफॉर्म के लिए एक एप्लिकेशन स्थापित करें:

`steamcmd +@sSteamCmdForcePlatformType {{windows}} +login {{गुमनाम}} +app_update {{ऐप आईडी}} validate +quit`
