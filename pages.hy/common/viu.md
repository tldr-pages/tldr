# viu

> Դիտեք պատկերները տերմինալի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/atanunq/viu#command-line-options>:.

- Ներկայացրեք պատկեր կամ անիմացիոն GIF.:

`viu {{path/to/file}}`

- Ներկայացրեք պատկեր կամ GIF ինտերնետից՝ օգտագործելով `curl`:

`curl {{[-s|--silent]}} {{https://example.com/image.png}} | viu -`

- Ներկայացրեք պատկեր թափանցիկ ֆոնով.:

`viu {{[-t|--transparent]}} {{path/to/file}}`

- Ներկայացրեք պատկերը որոշակի լայնությամբ և բարձրությամբ պիքսելներով.:

`viu {{[-w|--width]}} {{width}} {{[-h|--height]}} {{height}} {{path/to/file}}`

- Ներկայացրեք պատկեր կամ GIF և ցուցադրեք դրա ֆայլի անունը.:

`viu {{[-n|--name]}} {{path/to/file}}`
