# gpg

> GNU Privacy Guard.
> Mais informações: <https://gnupg.org>.

- Assina doc.txt, sem criptografá-lo (cria um arquivo de saída doc.txt.asc):

`gpg --clearsign {{doc.txt}}`

- Criptografa doc.txt para alice@example.com (cria um arquivo de saída `doc.txt.gpg`):

`gpg --encrypt --recipient {{alice@example.com}} {{doc.txt}}`

- Criptografa doc.txt apenas com uma senha simétrica (cria um arquivo de sadída `doc.txt.gpg`):

`gpg --symmetric {{doc.txt}}`

- Descriptografa doc.txt.gpg (envia saída para `stdout`):

`gpg --decrypt {{doc.txt.gpg}}`

- Importa uma chave pública:

`gpg --import {{public.gpg}}`

- Exporta a chave pública da alice@example.com (envia saída para `stdout`):

`gpg --export --armor {{alice@example.com}}`

- Exporta chave privada da alice@example.com (envia saída para `stdout`):

`gpg --export-secret-keys --armor {{alice@example.com}}`
