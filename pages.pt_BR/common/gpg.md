# gpg

> GNU Privacy Guard.
> Veja `gpg2` para o GNU Privacy Guard 2. A maioria dos sistemas operacionais criam link simbólico entre `gpg` e `gpg2`.
> Mais informações: <https://gnupg.org>.

- Cria uma chave GPG pública e privada interativamente:

`gpg --full-generate-key`

- Assina doc.txt sem criptografia (cria um arquivo de saída `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Criptografa e assina `doc.txt` para alice@example.com e bob@example.com (cria um arquivo de saída `doc.txt.gpg`):

`gpg --encrypt --sign --recipient {{alice@example.com}} --recipient {{bob@example.com}} {{doc.txt}}`

- Criptografa `doc.txt` apenas com uma senha simétrica (cria um arquivo de saída `doc.txt.gpg`):

`gpg --symmetric {{doc.txt}}`

- Descriptografa `doc.txt.gpg` (envia saída para `stdout`):

`gpg --decrypt {{doc.txt.gpg}}`

- Importa uma chave pública:

`gpg --import {{public.gpg}}`

- Exporta a chave pública da alice@example.com (envia saída para `stdout`):

`gpg --export --armor {{alice@example.com}}`

- Exporta chave privada da alice@example.com (envia saída para `stdout`):

`gpg --export-secret-keys --armor {{alice@example.com}}`
