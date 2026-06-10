# ճոճվել

> Ցուցադրել հաղորդագրություն էկրանի վերևում գտնվող բարում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/swaywm/sway/blob/master/swaynag/swaynag.1.scd>:.

- Ցուցադրել սխալ.:

`swaynag {{[-m|--message]}} "{{error message}}"`

- Ցուցադրել նախազգուշացում.:

`swaynag {{[-t|--type]}} warning {{[-m|--message]}} "{{warning message}}"`

- Ցուցադրել հաղորդագրություն կոնֆիգուրայում սահմանված հատուկ կարգավորումներով.:

`swaynag {{[-t|--type]}} {{custom_type}} {{[-m|--message]}} "{{message}}"`

- Օգտագործեք նշված տառատեսակը.:

`swaynag {{[-f|--font]}} "{{monospace bold 9}}" {{[-m|--message]}} "{{error message}}"`

- Ստեղծեք կոճակ և գործարկեք հրաման նշված տերմինալում՝ սեղմելով.:

`TERMINAL={{terminal_executable}} swaynag {{[-b|--button]}} "{{button text}}" {{command}} {{[-m|--message]}} "{{error message}}"`

- Ստեղծեք կոճակ և գործարկեք հրամանը սեղմելով.:

`swaynag {{[-B|--button-no-terminal]}} "{{button text}}" {{command}} {{[-m|--message]}} "{{error message}}"`

- Ցուցադրել սանդղակը էկրանի ներքևի մասում.:

`swaynag {{[-e|--edge]}} bottom {{[-m|--message]}} "{{error message}}"`

- Բացեք `swaynag` նշված մոնիտորի վրա.:

`swaynag {{[-o|--output]}} {{DP-1}} {{[-m|--message]}} "{{error message}}"`
