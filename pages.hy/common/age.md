#տարիք

> Պարզ, ժամանակակից և անվտանգ ֆայլերի կոդավորման գործիք:.
> Տես նաև՝ `age-keygen`, `age-inspect`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/FiloSottile/age#usage>:.

- Ստեղծեք կոդավորված ֆայլ, որը կարող է վերծանվել անցաբառով.:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{path/to/encrypted_file.age}} {{path/to/unencrypted_file}}`

- Գաղտնագրեք ֆայլը մեկ կամ մի քանի հանրային բանալիներով, որոնք մուտքագրված են որպես բառացի (կրկնեք `--recipient` դրոշը՝ մի քանի հանրային բանալիներ նշելու համար):

`age {{[-r|--recipient]}} {{public_key}} {{[-o|--output]}} {{path/to/encrypted_file.age}} {{path/to/unencrypted_file}}`

- Գաղտնագրեք ֆայլը մեկ կամ մի քանի հասցեատերերի համար, որոնց հանրային բանալիները նշված են ֆայլում (մեկ տողում).:

`age {{[-R|--recipients-file]}} {{path/to/recipients_file.txt}} {{[-o|--output]}} {{path/to/encrypted_file.age}} {{path/to/unencrypted_file}}`

- գաղտնազերծել ֆայլը անցաբառով.:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{path/to/decrypted_file}} {{path/to/encrypted_file.age}}`

- գաղտնազերծել ֆայլը մասնավոր բանալի ֆայլով.:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{path/to/private_key_file}} {{[-o|--output]}} {{path/to/decrypted_file}} {{path/to/encrypted_file.age}}`
