# yarac

> Կազմեք YARA կանոնների աղբյուրի ֆայլերը երկուական ձևաչափով՝ ավելի արագ բեռնելու համար:.
> Տես նաև՝ `yara`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/yarac>:.

- Կազմեք հատուկ կանոնների ֆայլ.:

`yarac {{path/to/rule.yar}} {{path/to/rule.bin}}`

- Կազմեք կանոնների բազմաթիվ ֆայլեր մեկ երկուականի մեջ.:

`yarac {{path/to/rule1.yar path/to/rule2.yar ...}} {{path/to/rules.bin}}`

- Կազմման ընթացքում սահմանեք արտաքին փոփոխական.:

`yarac -d {{identifier}}={{value}} {{path/to/rule.yar}} {{path/to/rule.bin}}`

- Անջատել նախազգուշացումները կազմման ժամանակ.:

`yarac {{[-w|--no-warnings]}} {{path/to/rule.yar}} {{path/to/rule.bin}}`

- Չհաջողվեց հավաքել որևէ նախազգուշացում (մի օգտագործեք `--no-warnings`-ի հետ միասին).:

`yarac --fail-on-warnings {{path/to/rule.yar}} {{path/to/rule.bin}}`
