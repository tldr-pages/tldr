# gpg

> GNU Privacy Guard.
> Mais informações: <https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>.

- Cria uma chave GPG pública e privada interativamente:

`gpg {{[--full-gen-key|--full-generate-key]}}`

- Assina doc.txt sem criptografia (cria um arquivo de saída `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Criptografa e assina `doc.txt` para alice@example.com e bob@example.com (cria um arquivo de saída `doc.txt.gpg`):

`gpg {{[-es|--encrypt --sign]}} {{[-r|--recipient]}} {{alice@example.com}} {{[-r|--recipient]}} {{bob@example.com}} {{doc.txt}}`

- Criptografa `doc.txt` apenas com uma senha simétrica (cria um arquivo de saída `doc.txt.gpg`):

`gpg {{[-c|--symmetric]}} {{doc.txt}}`

- Descriptografa `doc.txt.gpg` (envia saída para `stdout`):

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- Importa uma chave pública:

`gpg --import {{public.gpg}}`

- Exporta a chave pública da alice@example.com (envia saída para `stdout`):

`gpg --export {{[-a|--armor]}} {{alice@example.com}}`

- Exporta chave privada da alice@example.com (envia saída para `stdout`):

`gpg --export-secret-keys {{[-a|--armor]}} {{alice@example.com}}`
