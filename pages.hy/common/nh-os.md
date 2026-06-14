# nh os

> Վերակազմավորեք կամ կարգաբերեք NixOS սարքը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/nix-community/nh#usage>:.

- Կառուցեք և անցեք նշված NixOS փաթիլային կազմաձևին.:

`nh os switch {{path/to/flake}}`

- Թարմացրեք նշված NixOS փաթիլային կոնֆիգուրացիայի բոլոր փաթիլային մուտքերը, կառուցեք այն և դարձրեք այն բեռնման լռելյայն:

`nh os boot {{path/to/flake}} {{[-u|--update]}}`

- Կառուցեք և ակտիվացրեք NixOS փաթիլների կազմաձևման հատուկ մասնագիտացում.:

`nh os test {{path/to/flake}} {{[-s|--specialisation]}} {{specialisation}}`

- Կառուցեք նշված NixOS փաթիլների կազմաձևման հոսթ և ստեղծեք արդյունքի սիմվոլիկ Nix խանութից ընթացիկ գրացուցակում.:

`nh os build-vm {{path/to/flake}} {{[-H|--hostname]}} {{host}}`

- Բեռնել նշված NixOS փաթիլային կոնֆիգուրացիան Nix REPL-ում (Nix գնահատման միջավայր).:

`nh os repl {{path/to/flake}}`

- Թվարկեք բոլոր հասանելի սերունդները պրոֆիլի ուղուց.:

`nh os info`

- Հետադարձ դեպի նշված սերունդ.:

`nh os rollback {{[-t|-to]}} {{generation}}`
