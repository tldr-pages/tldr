# openssl ts

> comanda OpenSSL pentru a genera și verifica marcajele temporale.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-ts.html>

- Generarea unei solicitări de timestamp SHA-512 a unui anumit fișier și ieșirea către `file.tsq`:

`openssl ts -query -data {{path/to/file}} -sha512 -out {{path/to/file.tsq}}`

- Verificați data și metadatele unui anumit fișier de răspuns al marcajului temporal:

`openssl ts -reply -in {{path/to/file.tsr}} -text`

- Verificați un fișier de solicitare a timestamp și un fișier de răspuns timestamp de pe server cu un fișier certificat SSL:

`openssl ts -verify -in {{path/to/file.tsr}} -queryfile {{path/to/file.tsq}} -partial_chain -CAfile {{path/to/cert.pem}}`

- Creați un răspuns de marcă de timp pentru cerere folosind cheia și certificatul de semnare și de ieșire la `file.tsr`:

`openssl ts -reply -queryfile {{path/to/file.tsq}} -inkey {{path/to/tsakey.pem}} -signer tsacert.pem -out {{path/to/file.tsr}}`
