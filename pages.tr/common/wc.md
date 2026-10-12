# wc

> Satırları, kelimeleri ve baytları say.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Bir dosyadaki tüm satırları say:

`wc {{[-l|--lines]}} {{dosya/yolu}}`

- Bir dosyadaki tüm kelimeleri say:

`wc {{[-w|--words]}} {{dosya/yolu}}`

- Bir dosyadaki tüm baytları say:

`wc {{[-c|--bytes]}} {{dosya/yolu}}`

- Bir dosyadaki tüm karakterleri say (çok baytlı karakterleri dikkate alarak):

`wc {{[-m|--chars]}} {{dosya/yolu}}`

- Standart girdiden (`stdin`) gelen tüm satırları, kelimeleri ve baytları say:

`{{find .}} | wc`

- En uzun satırın uzunluğunu karakter sayısı olarak say:

`wc {{[-L|--max-line-length]}} {{dosya/yolu}}`
