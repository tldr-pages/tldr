# բեռնախցիկ

> Լինտերի հավաքածու՝ սովորական սխալները բացահայտելու և ձեր Rust կոդը բարելավելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/rust-lang/rust-clippy>:.

- Ստուգեք ընթացիկ գրացուցակի կոդը.:

`cargo clippy`

- Պահանջեք, որ `Cargo.lock`-ը արդիական լինի՝:

`cargo clippy --locked`

- Գործարկեք ստուգումներ աշխատանքային տարածքում գտնվող բոլոր փաթեթների վրա.:

`cargo clippy --workspace`

- Փաթեթի համար ստուգումներ կատարեք.:

`cargo clippy --package {{package}}`

- Կազմեք ստուգումներ մի խմբի համար (տե՛ս <https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness, հնացած, մանկապարտեզ, մանկական, կատարյալ, սահմանափակում, ոճ, կասկածելի>):

`cargo clippy -- {{[-W|--warn]}} clippy::{{lint_group}}`

- Զգուշացումները վերաբերվեք որպես սխալներ.:

`cargo clippy -- {{[-D|--deny]}} warnings`

- Գործարկեք ստուգումներ և անտեսեք նախազգուշացումները.:

`cargo clippy -- {{[-A|--allow]}} warnings`

- Կիրառել Clippy առաջարկները ինքնաբերաբար.:

`cargo clippy --fix`
