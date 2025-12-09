# stdbuf

> एक कमांड को उसके मानक स्ट्रीम के लिए संशोधित बफरिंग ऑपरेशनों के साथ चलाएं।
> अधिक जानकारी: <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>।

- `stdin` बफर का आकार 512 KiB में बदलें:

`stdbuf --input=512K {{आदेश}}`

- `stdout` बफर को लाइन-बफर्ड में बदलें:

`stdbuf --output=L {{आदेश}}`

- `stderr` बफर को अनबफर्ड में बदलें:

`stdbuf --error=0 {{आदेश}}`
