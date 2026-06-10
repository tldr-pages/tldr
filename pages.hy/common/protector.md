#պաշտպան

> Պաշտպանեք կամ չպաշտպանեք մասնաճյուղերը GitHub պահեստներում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/jcgay/protector#usage>:.

- Պաշտպանեք GitHub պահեստի մասնաճյուղերը (ստեղծեք ճյուղերի պաշտպանության կանոններ).:

`protector {{branches_regex}} -repos {{organization/repository}}`

- Օգտագործեք չոր վազքը՝ տեսնելու, թե ինչն է պաշտպանված (կարող է օգտագործվել նաև ազատման համար).:

`protector -dry-run {{branches_regex}} -repos {{organization/repository}}`

- GitHub պահեստի անվճար մասնաճյուղեր (ջնջել ճյուղերի պաշտպանության կանոնները).:

`protector -free {{branches_regex}} -repos {{organization/repository}}`
