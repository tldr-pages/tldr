# kubectl certificate

> Управлять запросами на подпись сертификатов.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/>.

- Одобрить запрос на подпись сертификата по имени:

`kubectl certificate approve {{имя_csr}}`

- Отклонить запрос на подпись сертификата по имени:

`kubectl certificate deny {{имя_csr}}`

- Одобрить запрос на подпись сертификата, определённый в файле манифеста:

`kubectl certificate approve --filename {{путь/к/csr.yaml}}`

- Отклонить запрос на подпись сертификата, определённый в файле манифеста:

`kubectl certificate deny --filename {{путь/к/csr.yaml}}`

- Принудительно переодобрить запрос на подпись сертификата, который был ранее отклонён:

`kubectl certificate approve --force {{имя_csr}}`
