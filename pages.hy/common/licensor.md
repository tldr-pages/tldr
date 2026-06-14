# արտոնագրող

> Գրեք լիցենզիաներ `stdout`-ում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/raftario/licensor>:.

- Գրեք MIT լիցենզիան `LICENSE` անունով ֆայլում՝:

`licensor {{MIT}} > {{LICENSE}}`

- Գրեք MIT լիցենզիան `LICENSE` անունով ֆայլի վրա տեղապահի հեղինակային իրավունքի մասին ծանուցմամբ:

`licensor {{[-p|--keep-placeholder]}} {{MIT}} > {{LICENSE}}`

- Նշեք հեղինակային իրավունքի սեփականատիրոջ անունը Bobby Tables:

`licensor {{MIT}} "{{Bobby Tables}}" > {{LICENSE}}`

- Նշեք լիցենզիայի բացառությունները WITH արտահայտությամբ.:

`licensor "{{Apache-2.0 WITH LLVM-exception}}" > {{LICENSE}}`

- Թվարկեք բոլոր առկա լիցենզիաները.:

`licensor {{[-l|--licenses]}}`

- Թվարկեք բոլոր առկա բացառությունները.:

`licensor {{[-e|--exceptions]}}`
