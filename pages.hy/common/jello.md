#ժելո

> JSON պրոցեսոր՝ օգտագործելով Python շարահյուսությունը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kellyjonbrazil/jello#usage>:.

- Գեղեցիկ տպագիր JSON կամ JSON-Lines տվյալներ `stdin`-ից մինչև `stdout`:

`cat {{file.json}} | jello`

- Արտադրեք JSON կամ JSON Lines տվյալների սխեման `stdin`-ից մինչև `stdout` (օգտակար grep-ի համար).:

`cat {{file.json}} | jello -s`

- Արտադրեք բոլոր տարրերը զանգվածներից (կամ բոլոր արժեքները օբյեկտներից) JSON կամ JSON-Lines տվյալների `stdin`-ից մինչև `stdout`:

`cat {{file.json}} | jello -l`

- Արտադրեք JSON կամ JSON-Lines տվյալների առաջին տարրը `stdin`-ից մինչև `stdout`:

`cat {{file.json}} | jello _[0]`

- Ելք բերեք JSON կամ JSON-Lines տվյալների յուրաքանչյուր տարրի տվյալ բանալու արժեքը `stdin`-ից մինչև `stdout`:

`cat {{file.json}} | jello '[i.{{key_name}} for i in _]'`

- Արտադրեք մի քանի ստեղների արժեքը որպես նոր JSON օբյեկտ (ենթադրելով, որ JSON մուտքագրվածն ունի `key_name1` և `key_name2` ստեղները):

`cat {{file.json}} | jello '{{{"key1": _.key_name1, "key2": _.key_name2, ...}}}'`

- Տրված բանալիի արժեքը լարեք (և անջատեք JSON ելքը).:

`cat {{file.json}} | jello -r '"{{some text}}: " + _.{{key_name}}'`
