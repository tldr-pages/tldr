#ֆեհ

> Թեթև պատկերի դիտման ծրագիր:.
> Լրացուցիչ տեղեկություններ. <https://man.finalrewind.org/1/feh/>:.

- Դիտեք պատկերները տեղում կամ օգտագործելով URL.:

`feh {{path/to/images}}`

- Դիտեք պատկերները ռեկուրսիվորեն.:

`feh {{[-r|--recursive]}} {{path/to/images}}`

- Դիտեք պատկերները և ցուցադրեք ֆայլի անունը պատկերների վերևի ձախ մասում.:

`feh {{[-d|--draw-filename]}} {{path/to/images}}`

- Դիտեք պատկերներ առանց պատուհանի եզրագծերի.:

`feh {{[-x|--borderless]}} {{path/to/images}}`

- Սահմանեք վարքագիծը պատկերների ցանկի սկզբին կամ ավարտին հասնելիս.:

`feh --on-last-slide {{hold|quit|resume}} {{path/to/images}}`

- Օգտագործեք հատուկ սլայդերի ցուցադրման ցիկլի ուշացում.:

`feh {{[-D|--slideshow-delay]}} {{seconds}} {{path/to/images}}`

- Օգտագործեք պաստառի հատուկ ռեժիմ (կենտրոնացված, լցված, առավելագույնի հասցված, մասշտաբավորված կամ սալիկապատված).:

`feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}`

- Ստեղծեք բոլոր պատկերների մոնտաժը գրացուցակի մեջ՝ դուրս բերելով որպես նոր պատկեր.:

`feh {{[-m|--montage]}} {{[-E|--thumb-height]}} {{150}} {{[-y|--thumb-width]}} {{150}} --index-info "{{%nn%wx%h}}" {{[-o|--output]}} {{path/to/montage_image.png}}`
