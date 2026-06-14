# gpg

> GNU Privacy Guard, OpenPGP գաղտնագրման և ստորագրման գործիք:.
> Տես նաև՝ `sq`:.
> Լրացուցիչ տեղեկություններ. <https://gnupg.org/documentation/manuals/gnupg/Invoking-GPG.html>:.

- Ստեղծեք GPG հանրային և մասնավոր բանալի ինտերակտիվ կերպով.:

`gpg {{[--full-gen-key|--full-generate-key]}}`

- Թվարկեք բոլոր ստեղները հանրային ստեղնաշարից.:

`gpg {{[-k|--list-keys]}}`

- Ստորագրեք `doc.txt` առանց գաղտնագրման (ելքը գրում է `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- Գաղտնագրեք և ստորագրեք `doc.txt` `alice@example.com`-ի և `bob@example.com`-ի համար (ելք՝ `doc.txt.gpg`):

`gpg {{[-es|--encrypt --sign]}} {{[-r|--recipient]}} {{alice@example.com}} {{[-r|--recipient]}} {{bob@example.com}} {{doc.txt}}`

- Գաղտնագրեք `doc.txt`-ը միայն անցաբառով (ելք՝ `doc.txt.gpg`):

`gpg {{[-c|--symmetric]}} {{doc.txt}}`

- Ապակոդավորել `doc.txt.gpg` (ելք՝ `stdout`):

`gpg {{[-d|--decrypt]}} {{doc.txt.gpg}}`

- Ներմուծեք հանրային բանալի WKD-ից (Վեբ բանալիների գրացուցակ), եթե բանալին արդեն չկա ստեղնաշարի մեջ.:

`gpg --locate-keys {{alice@example.com}}`

- Արտահանել հանրային/մասնավոր բանալին `alice@example.com`-ի համար (ելք՝ `stdout`):

`gpg {{--export|--export-secret-keys}} {{[-a|--armor]}} {{alice@example.com}}`
