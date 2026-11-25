# certtool

> تولید و مدیریت گواهی‌ها و کلیدهای X.509 و ساختارهای PKI با استفاده از GnuTLS.
> اطلاعات بیشتر: <https://gnutls.org/manual/gnutls.html#certtool-Invocation>.

- تولید یک کلید خصوصی و ذخیرهٔ آن در فایل:

`certtool {{[-p|--generate-privkey]}} --outfile {{path/to/private.key}}`

- تولید یک گواهی خودامضاشده با استفاده از کلید خصوصی و فایل قالب:

`certtool {{[-s|--generate-self-signed]}} --load-privkey {{path/to/private.key}} --template {{path/to/info.template}} --outfile {{path/to/certificate.crt}}`

- تولید درخواست امضای گواهی (CSR):

`certtool {{[-q|--generate-request]}} --load-privkey {{path/to/private.key}} --template {{path/to/info.template}} --outfile {{path/to/request.csr}}`

- تولید گواهی مرجع صدور گواهی (CA):

`certtool {{[-s|--generate-self-signed]}} --load-privkey {{path/to/ca.key}} --template {{path/to/ca.template}} --outfile {{path/to/ca.crt}}`

- اعتبارسنجی یک گواهی در برابر گواهی CA:

`certtool --verify --infile {{path/to/certificate.crt}} --load-ca-certificate {{path/to/ca.crt}}`
