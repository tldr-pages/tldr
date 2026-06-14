# mp4 decrypt

> Վերծանել MP4 ֆայլը:.
> Bento4 գործիքների մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://www.bento4.com/documentation/mp4decrypt/>:.

- Ֆայլի վերծանումը՝ օգտագործելով հատուկ բանալի (բանալու ID-ն վեցանկյունով, բանալին՝ վեցանկյունով).:

`mp4decrypt --key {{key_id_hex}}:{{key_hex}} {{path/to/input_file.mp4}} {{path/to/output_file.mp4}}`

- Ֆայլի գաղտնազերծումը՝ օգտագործելով հատուկ բանալի հետագծի ID-ի համար (ուղու ID-ն տասնորդական, բանալին՝ վեցանկյուն).:

`mp4decrypt --key {{track_id}}:{{key_hex}} {{path/to/input_file.mp4}} {{path/to/output_file.mp4}}`

- գաղտնազերծել ֆայլը մի քանի ստեղների միջոցով՝ ցուցադրելով վերծանման առաջընթացը.:

`mp4decrypt --key {{key_id_1}}:{{key_1}} --key {{key_id_2}}:{{key_2}} --show-progress {{path/to/input_file.mp4}} {{path/to/output_file.mp4}}`
