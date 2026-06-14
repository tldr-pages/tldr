#bash-it

> Համայնքի կողմից ներկայացված Bash հրամանների և սկրիպտների հավաքածու Bash 3.2+-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://bash-it.readthedocs.io/en/latest/>:.

- Թարմացրեք Bash-it-ը վերջին կայուն/զարգացման տարբերակին.:

`bash-it update {{stable|dev}}`

- Վերբեռնեք Bash պրոֆիլը (ավտոմատ վերաբեռնման համար սահմանեք `$BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE`-ը ոչ դատարկ արժեքի):

`bash-it reload`

- Վերագործարկեք Bash:

`bash-it restart`

- Վերբեռնեք Bash պրոֆիլը միացված սխալով և նախազգուշացման գրանցմամբ.:

`bash-it doctor`

- Վերբեռնեք Bash պրոֆիլը միացված սխալով/նախազգուշացումով/ամբողջ գրանցմամբ.:

`bash-it doctor {{errors|warnings|all}}`

- Փնտրեք Bash-it կեղծանուններ/պլագիններ/լրացումներ.:

`bash-it search {{alias|plugin|completion}}`

- Որոնեք Bash-it կեղծանուններ/պլագիններ/լրացումներ և միացրեք/անջատեք գտնված բոլոր տարրերը.:

`bash-it search --{{enable|disable}} {{alias|plugin|completion}}`
