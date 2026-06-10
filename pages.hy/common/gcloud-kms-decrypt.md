# gcloud kms ապակոդավորումը

> Գաղտնագրված տեքստային ֆայլի վերծանումը՝ օգտագործելով Cloud KMS բանալի:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/kms/decrypt>:.

- գաղտնազերծել ֆայլը` օգտագործելով նշված բանալի, բանալի օղակ և գտնվելու վայրը.:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{global}} --ciphertext-file={{path/to/ciphertext}} --plaintext-file={{path/to/plaintext}}`

- Ապակոդավորեք ֆայլը լրացուցիչ վավերացված տվյալներով (AAD) և գրեք վերծանված պարզ տեքստը `stdout`-ում:

`gcloud kms decrypt --key={{key_name}} --keyring={{keyring_name}} --location={{global}} --additional-authenticated-data-file={{path/to/file.aad}} --ciphertext-file={{path/to/ciphertext}} --plaintext-file=-`
