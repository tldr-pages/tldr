# pkg_info

> OpenBSD में पैकेजों के बारे में जानकारी देखें।
> देखें: `pkg_add`, `pkg_delete`।
> अधिक जानकारी: <https://man.openbsd.org/pkg_info>।

- पैकेज नाम का उपयोग करके पैकेज के लिए खोजें:

`pkg_info -Q {{पैकेज}}`

- `pkg_add -l` के साथ उपयोग के लिए स्थापित पैकेजों की सूची आउटपुट करें:

`pkg_info -mz`
