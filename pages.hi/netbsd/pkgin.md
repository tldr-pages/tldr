# pkgin

> NetBSD पर `pkgsrc` बाइनरी पैकेज प्रबंधित करें।
> अधिक जानकारी: <https://pkgin.net/#usage>।

- एक पैकेज स्थापित करें:

`pkgin install {{पैकेज}}`

- एक पैकेज और उसकी निर्भरताएँ हटाएँ:

`pkgin remove {{पैकेज}}`

- सभी पैकेज को उन्नत करें:

`pkgin full-upgrade`

- एक पैकेज के लिए खोजें:

`pkgin search {{कीवर्ड}}`

- स्थापित पैकेजों की सूची बनाएं:

`pkgin list`

- अनावश्यक निर्भरताएँ हटाएँ:

`pkgin autoremove`
