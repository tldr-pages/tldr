# ֆայլ

> Ինտերֆեյս Filen-ի հետ՝ ծայրից ծայր կոդավորված ամպային պահեստավորման ծառայություն:.
> Լրացուցիչ տեղեկություններ. <https://github.com/FilenCloudDienste/filen-cli>:.

- Մուտքագրեք ինտերակտիվ ռեժիմ.:

`filen`

- Վերբեռնեք տեղական ֆայլը որոշակի հեռավոր պանակ.:

`filen upload {{path/to/local_file}} {{remote_folder_id}}`

- Ներբեռնեք ֆայլ կամ թղթապանակ՝ օգտագործելով իր հեռակառավարման նույնացուցիչը.:

`filen download {{remote_id}} {{path/to/local_destination}}`

- Թվարկեք ֆայլերը և թղթապանակները հեռավոր թղթապանակում.:

`filen ls {{remote_folder}}`

- Ջնջել հեռավոր ֆայլ կամ թղթապանակ (տեղափոխել այն աղբարկղ).:

`filen rm {{remote_id}}`

- Վերականգնել աղբարկղը.:

`filen trash restore {{remote_id}}`

- Համաժամացրեք տեղական թղթապանակը հեռավոր թղթապանակի հետ (երկկողմանի համաժամեցում).:

`filen sync {{path/to/local_folder}}:/{{remote_folder}} --continuous`

- Ներբեռնեք փոփոխությունները ամպից տեղական պանակ (միակողմանի համաժամացում).:

`filen sync {{path/to/local_folder}}:ctl:/{{remote_folder}}`
