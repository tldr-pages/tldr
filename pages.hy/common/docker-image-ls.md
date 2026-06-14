# docker պատկեր ls

> Ցուցակեք Docker պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/image/ls/>:.

- Թվարկեք բոլոր Docker պատկերները.:

`docker {{[images|image ls]}}`

- Թվարկեք բոլոր Docker պատկերները, ներառյալ միջանկյալները.:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Թվարկեք ելքը հանգիստ ռեժիմում (միայն թվային ID-ներ).:

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Թվարկեք բոլոր Docker պատկերները, որոնք չեն օգտագործվում որևէ կոնտեյների կողմից.:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- Թվարկեք պատկերները, որոնք իրենց անունով ենթատող են պարունակում.:

`docker {{[images|image ls]}} "{{*name*}}"`

- Տեսակավորել պատկերները ըստ չափի.:

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
