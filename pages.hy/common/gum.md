# մաստակ

> Կազմեք հմայիչ կճեպի սցենարներ:.
> Տես նաև՝ `whiptail`, `dialog`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/charmbracelet/gum#tutorial>:.

- Ինտերակտիվ կերպով ընտրեք որոշակի տարբերակ `stdout`-ով տպելու համար:

`gum choose {{"option1" "option2" "..."}}`

- Բացեք ինտերակտիվ հուշում, որպեսզի օգտագործողը մուտքագրի տող հատուկ տեղապահով.:

`gum input --placeholder "{{value}}"`

- Բացեք հաստատման ինտերակտիվ հուշումը և դուրս եկեք `<0>` կամ `<1>`-ով:

`gum confirm "{{Continue?}}" --default=false --affirmative "{{Yes}}" --negative "{{No}}" {{&& echo "Yes selected" || echo "No selected"}}`

- Ցույց տվեք մանող, մինչ հրաման է կատարվում տեքստի կողքին՝:

`gum spin {{[-s|--spinner]}} {{dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger}} --title "{{loading...}}" {{command}}`

- Ձևաչափեք տեքստը՝ էմոջիներ ներառելու համար.:

`gum format {{[-t|--type]}} {{emoji}} "{{:smile: :heart: hello}}"`

- Ինտերակտիվ կերպով հուշում է բազմաշերտ տեքստ և մուտքագրում ֆայլի մեջ.:

`gum write > {{path/to/file}}`
