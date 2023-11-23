# bootctl

> EFI फर्मवेयर बूट सेटिंग्स का नियंत्रण करें और बूट लोडर प्रबंधित करें।
> अधिक जानकारी: <https://manned.org/bootctl>।

- सिस्टम फर्मवेयर और बूटलोडर के बारे में जानकारी दिखाएं:

`bootctl status`

- सभी उपलब्ध बूटलोडर प्रविष्टियाँ दिखाएं:

`bootctl list`

- अगले बूट पर सिस्टम फर्मवेयर में बूट करने के लिए एक फ़्लैग सेट करें (`sudo systemctl reboot --firmware-setup` के समान):

`sudo bootctl reboot-to-firmware true`

- EFI सिस्टम पार्टीशन के पथ की निर्धारण करें (डिफ़ॉल्ट `/efi/`, `/boot/`, या `/boot/efi`):

`bootctl --esp-path={{/efi_system_partition/के/पथ/के/लिए}}`

- `systemd-boot` को EFI सिस्टम पार्टीशन में इंस्टॉल करें:

`sudo bootctl install`

- EFI सिस्टम पार्टीशन से `systemd-boot` के सभी स्थापित संस्करणों को हटाएं:

`sudo bootctl remove`
