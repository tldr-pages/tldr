#միսս

> Կառավարեք լեզուների գործարկման ժամանակները, ինչպիսիք են Node.js-ը, Python-ը, Ruby-ը, Go-ն, Java-ն և այլն, և տարբեր գործիքներ:.
> Լրացուցիչ տեղեկություններ. <https://mise.jdx.dev/cli/>:.

- Թվարկեք բոլոր հասանելի հավելվածները.:

`mise plugins list-all`

- Տեղադրեք plugin.:

`mise plugins add {{name}}`

- Տեղադրեք գործարկման ժամանակի տարբերակները, որոնք հասանելի են տեղադրման համար.:

`mise ls-remote {{name}}`

- Տեղադրեք փաթեթի որոշակի տարբերակ.:

`mise install {{name}}@{{version}}`

- Սահմանեք գլոբալ տարբերակը փաթեթի համար.:

`mise use {{[-g|--global]}} {{name}}@{{version}}`

- Սահմանեք տեղական տարբերակը փաթեթի համար.:

`mise use {{name}}@{{version}}`

- Սահմանել շրջակա միջավայրի փոփոխականը կազմաձևման մեջ.:

`mise set {{variable}}={{value}}`

- Pass plugin ընտրանքներ.:

`mise use {{name}}\[{{option1}}={{option1_value}},{{option2}}={{option2_value}}\]@{{version}}`
