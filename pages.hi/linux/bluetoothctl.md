# bluetoothctl

> ब्लूटूथ उपकरणों का प्रबंधन करें।
> अधिक जानकारी: <https://bitbucket.org/serkanp/bluetoothctl>.

- `bluetoothctl` शैल में प्रवेश करें:

`bluetoothctl`

- सभी ज्ञात उपकरणों की सूची दिखाएं:

`bluetoothctl devices`

- ब्लूटूथ नियंत्रक को चालने या बंद करें:

`bluetoothctl power {{on|off}}`

- किसी उपकरण के साथ जोड़ें:

`bluetoothctl pair {{mac_address}}`

- किसी उपकरण को हटाएं:

`bluetoothctl remove {{mac_address}}`

- एक जुड़े हुए उपकरण से कनेक्ट करें:

`bluetoothctl connect {{mac_address}}`

- एक जुड़े हुए उपकरण से डिसकनेक्ट करें:

`bluetoothctl disconnect {{mac_address}}`

- मदद दिखाएं:

`bluetoothctl help`
