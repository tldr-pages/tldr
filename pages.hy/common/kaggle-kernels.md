# kaggle kernels

> Կառավարեք Kaggle միջուկները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#kernels>:.

- Թվարկեք բոլոր միջուկները.:

`kaggle {{[k|kernels]}} list`

- Ցուցակել միջուկի ելքային ֆայլերը.:

`kaggle {{[k|kernels]}} files {{kernel_name}}`

- Նախաձեռնել մետատվյալների ֆայլը միջուկի համար (կանխադրված է ընթացիկ գրացուցակում).:

`kaggle {{[k|kernels]}} init {{[-p|--path]}} {{path/to/directory}}`

- Նոր կոդը մղեք միջուկ և գործարկեք միջուկը.:

`kaggle {{[k|kernels]}} push {{[-p|--path]}} {{path/to/directory}}`

- Քաշեք միջուկը.:

`kaggle {{[k|kernels]}} pull {{kernel_name}} {{[-p|--path]}} {{path/to/directory}}`

- Ստացեք տվյալների ելք միջուկի վերջին գործարկումից.:

`kaggle {{[k|kernels]}} output {{kernel_name}}`

- Ցուցադրել միջուկի վերջին գործարկման կարգավիճակը.:

`kaggle {{[k|kernels]}} status {{kernel_name}}`
