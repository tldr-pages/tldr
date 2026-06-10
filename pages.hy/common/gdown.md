#գդուն

> Ներբեռնեք ֆայլեր Google Drive-ից և այլ URL-ներից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wkentaro/gdown#usage>:.

- Ներբեռնեք ֆայլ URL-ից.:

`gdown {{url}}`

- Ներբեռնեք՝ օգտագործելով ֆայլի ID.:

`gdown {{file_id}}`

- Ներբեռնեք անորոշ ֆայլի ID-ի արդյունահանմամբ (աշխատում է նաև <https://docs.google.com> հղումներով).:

`gdown --fuzzy {{url}}`

- Ներբեռնեք թղթապանակ՝ օգտագործելով դրա ID-ն կամ ամբողջական URL-ը.:

`gdown {{folder_id|url}} {{[-O|--output]}} {{path/to/output_directory}} --folder`

- Ներբեռնեք `.tar` արխիվը, գրեք այն `stdout`-ում և հանեք այն՝:

`gdown {{tar_url}} {{[-O|--output]}} - {{[-q|--quiet]}} | tar xvf -`
