# dropbearkey

> تولید کلیدهای SSH در قالب Dropbear.
> اطلاعات بیشتر: <https://manned.org/dropbearkey>.

- تولید کلید SSH از نوع ed25519 با `-t` و نوشتن آن در فایل کلید با `-f`:

`dropbearkey -t {{ed25519}} -f {{path/to/key_file}}`

- تولید کلید SSH از نوع ecdsa با `-t` و نوشتن آن در فایل کلید با `-f`:

`dropbearkey -t {{ecdsa}} -f {{path/to/key_file}}`

- تولید کلید SSH از نوع RSA با `-t` و اندازهٔ ۴۰۹۶ بیت با `-s` و نوشتن آن در فایل کلید با `-f`:

`dropbearkey -t {{rsa}} -s {{4096}} -f {{path/to/key_file}}`

- چاپ اثر انگشت کلید خصوصی و کلید عمومی در فایل کلید مشخص‌شده با `-f`:

`dropbearkey -y -f {{path/to/key_file}}`
