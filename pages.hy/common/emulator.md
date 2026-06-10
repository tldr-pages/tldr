# էմուլյատոր

> Կառավարեք Android-ի էմուլյատորները:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/studio/run/emulator-commandline>:.

- Սկսեք Android emulator սարքը.:

`emulator -avd {{name}}`

- Ցուցադրել վեբ-տեսախցիկները ձեր ծրագրավորման համակարգչի վրա, որոնք հասանելի են նմանակման համար.:

`emulator -avd {{name}} -webcam-list`

- Գործարկեք էմուլյատոր, որը վերացնում է դեմքի տեսախցիկի կարգավորումը (առջևի տեսախցիկի համար օգտագործեք `-camera-front`):

`emulator -avd {{name}} -camera-back {{none|emulated|webcamN}}`

- Սկսեք էմուլյատոր, ցանցի առավելագույն արագությամբ.:

`emulator -avd {{name}} -netspeed {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full}}`

- Սկսեք էմուլյատոր ցանցի հետաձգմամբ.:

`emulator -avd {{name}} -netdelay {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none}}`

- Սկսեք էմուլյատոր՝ կատարելով բոլոր TCP կապերը նշված HTTP/HTTPS վստահված անձի միջոցով (պորտի համարը պարտադիր է).:

`emulator -avd {{name}} -http-proxy {{http://example.com:80}}`

- Սկսեք էմուլյատորը տվյալ SD քարտի բաժանման պատկերի ֆայլով.:

`emulator -avd {{name}} -sdcard {{path/to/sdcard.img}}`

- Ցուցադրել օգնությունը.:

`emulator -help`
