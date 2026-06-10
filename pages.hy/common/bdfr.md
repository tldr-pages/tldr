# bdfr

> Զանգվածային ներբեռնիչ Reddit-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Serene-Arc/bulk-downloader-for-reddit>:.

- Ներբեռնեք տեսանյութեր/պատկերներ նշված հղումներից դեպի URL կամ հաղորդագրությունների ID-ներ.:

`bdfr download {{path/to/output_directory}} {{[-l|--link]}} {{post_url}}`

- Ներբեռնեք տեսանյութերի/պատկերների առավելագույն հնարավոր քանակը (մոտ 1000) նշված օգտվողից.:

`bdfr download {{path/to/output_directory}} {{[-u|--user]}} {{reddit_user}} --submitted`

- Ներբեռնեք ներկայացման տվյալները (տեքստ, դրական քվեարկություններ, մեկնաբանություններ և այլն) սահմանափակվում է 10 ներկայացումով յուրաքանչյուր ենթագրքի համար (ընդհանուր 30).:

`bdfr archive {{path/to/output_directory}} {{[-s|--subreddit]}} '{{Python, all, mindustry}}' {{[-L|--limit]}} 10`

- Ներբեռնեք տեսանյութեր/պատկերներ subreddit r/Python-ից՝ դասավորված ըստ վերևի (կանխադրվածը թեժ է)՝ օգտագործելով ժամանակի զտիչը՝ սահմանափակված 10 ներկայացումով.:

`bdfr download {{path/to/output_directory}} {{[-s|--subreddit]}} Python {{[-S|--sort]}} top {{[-t|--time]}} all {{[-L|--limit]}} 10`

- Ներբեռնեք ներկայացված տվյալների և տեսանյութերի/պատկերների առավելագույն հնարավոր քանակը subreddit r/Python-ից՝ բաց թողնելով ներկայացումները `.mp4` կամ `.gif` ֆայլերի ընդլայնումներով և ստեղծելով կոշտ հղումներ կրկնօրինակ ֆայլերի համար.:

`bdfr clone {{path/to/output_directory}} {{[-s|--subreddit]}} Python --skip mp4 --skip gif --make-hard-links`

- Ներբեռնեք վավերացված օգտվողի պահպանված գրառումները՝ անվանելով յուրաքանչյուր ֆայլ ըստ սահմանված ձևաչափի: Խուսափեք ելքային գրացուցակում արդեն առկա կրկնօրինակների և գրառումների ներբեռնումից.:

`bdfr download {{path/to/output_directory}} {{[-u|--user]}} me --saved --authenticate --file-scheme '{{ {POSTID}_{TITLE}_{UPVOTES} }}' --no-dupes --search-existing`
