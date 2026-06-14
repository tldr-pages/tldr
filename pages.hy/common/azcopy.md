# azcopy

> Պատճենել տվյալները Azure Storage-ից և դրանից:.
> Տես նաև՝ `az storage`:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10#list-of-commands>:.

- Մուտք գործեք Azure վարձակալ.:

`azcopy login`

- Վերբեռնեք տեղական ֆայլ.:

`azcopy {{[c|copy]}} '{{path/to/source_file}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}/{{blob_name}}'`

- Վերբեռնեք ֆայլեր `.txt` և `.jpg` ընդլայնումներով.:

`azcopy {{[c|copy]}} '{{path/to/source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --include-pattern '*.txt;*.jpg'`

- Պատճենեք կոնտեյներ անմիջապես երկու Azure պահեստավորման հաշիվների միջև.:

`azcopy {{[c|copy]}} 'https://{{source_storage_account_name}}.blob.core.windows.net/{{container_name}}' 'https://{{destination_storage_account_name}}.blob.core.windows.net/{{container_name}}'`

- Համաժամացրեք տեղական գրացուցակը և ջնջեք ֆայլերը նպատակակետում, եթե դրանք այլևս գոյություն չունեն աղբյուրում.:

`azcopy {{[s|sync]}} '{{path/to/source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --delete-destination true`

- Ցուցադրել օգնությունը.:

`azcopy {{[-h|--help]}}`
