# pkg_delete

> OpenBSD में पैकेज हटाएँ।
> देखें: `pkg_add`, `pkg_info`।
> अधिक जानकारी: <https://man.openbsd.org/pkg_delete>।

- एक पैकेज हटाएँ:

`pkg_delete {{पैकेज}}`

- एक पैकेज हटाएँ, इसके अप्रयुक्त निर्भरताओं सहित:

`pkg_delete -a {{पैकेज}}`

- एक पैकेज का ड्राई-रन हटाना:

`pkg_delete -n {{पैकेज}}`
