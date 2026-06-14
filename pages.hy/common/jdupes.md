# jdupes

> Կրկնօրինակ ֆայլերի հզոր որոնիչ և `fdupes`-ի ընդլայնված պատառաքաղ:.
> Լրացուցիչ տեղեկություններ. <https://codeberg.org/jbruchon/jdupes#usage>:.

- Որոնեք մեկ գրացուցակ.:

`jdupes {{path/to/directory}}`

- Որոնեք բազմաթիվ դիրեկտորիաներ.:

`jdupes {{directory1 directory2 ...}}`

- Որոնել բոլոր դիրեկտորիաները ռեկուրսիվ կերպով.:

`jdupes {{[-r|--recurse]}} {{path/to/directory}}`

- Փնտրեք գրացուցակը ռեկուրսիվորեն և թույլ տվեք օգտվողին ընտրել ֆայլեր՝ պահպանելու համար.:

`jdupes {{[-d|--delete]}} {{[-r|--recurse]}} {{path/to/directory}}`

- Փնտրեք բազմաթիվ դիրեկտորիաներ և հետևեք ենթադիրեկտորներին դիրեկտորիայի2, այլ ոչ թե տեղեկատու 1-ի տակ:

`jdupes {{directory1}} {{[-R|--recurse:]}} {{directory2}}`

- Որոնեք բազմաթիվ դիրեկտորիաներ և պահեք գրացուցակի կարգը արդյունքում.:

`jdupes {{[-O|--param-order]}} {{directory1 directory2 directory3 ...}}`
