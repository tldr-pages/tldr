# csslint

> Lint CSS կոդը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/CSSLint/csslint/wiki/Command-line-interface>:.

- Տեղադրեք մեկ CSS ֆայլ.:

`csslint {{file.css}}`

- Lint բազմաթիվ CSS ֆայլեր.:

`csslint {{file1.css file2.css ...}}`

- Թվարկեք ոճի բոլոր հնարավոր կանոնները.:

`csslint --list-rules`

- Որոշ կանոններ դիտարկեք որպես սխալներ (որը հանգեցնում է ոչ զրոյական ելքի կոդը).:

`csslint --errors={{errors,universal-selector,imports}} {{file.css}}`

- Որոշ կանոններին վերաբերվեք որպես նախազգուշացումների.:

`csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}`

- Անտեսեք հատուկ կանոնները.:

`csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}`
