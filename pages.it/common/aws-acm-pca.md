# aws acm-pca

> Autorità di certificazione privata AWS Certificate Manager.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/acm-pca/>.

- Crea un'autorità di certificazione privata:

`aws acm-pca create-certificate-authority --certificate-authority-configuration {{ca_config}} --idempotency-token {{token}} --permanent-deletion-time-in-days {{number}}`

- Descrivi un'autorità di certificazione privata:

`aws acm-pca describe-certificate-authority --certificate-authority-arn {{ca_arn}}`

- Elenca le autorità di certificazione private:

`aws acm-pca list-certificate-authorities`

- Aggiorna un'autorità di certificazione:

`aws acm-pca update-certificate-authority --certificate-authority-arn {{ca_arn}} --certificate-authority-configuration {{ca_config}} --status {{status}}`

- Elimina un'autorità di certificazione privata:

`aws acm-pca delete-certificate-authority --certificate-authority-arn {{ca_arn}}`

- Emetti un certificato:

`aws acm-pca issue-certificate --certificate-authority-arn {{ca_arn}} --certificate-signing-request {{cert_signing_request}} --signing-algorithm {{algorithm}} --validity {{validity}}`

- Revoca un certificato:

`aws acm-pca revoke-certificate --certificate-authority-arn {{ca_arn}} --certificate-serial {{serial}} --reason {{reason}}`

- Ottieni dettagli del certificato:

`aws acm-pca get-certificate --certificate-authority-arn {{ca_arn}} --certificate-arn {{cert_arn}}`
