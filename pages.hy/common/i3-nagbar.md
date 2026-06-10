# i3-nagbar

> Ցուցադրել սխալ/նախազգուշացում էկրանի վերևի տողում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/i3-nagbar>:.

- Ցուցադրել սխալ.:

`i3-nagbar {{[-m|--message]}} "{{error message}}"`

- Ցուցադրել նախազգուշացում.:

`i3-nagbar {{[-t|--type]}} warning {{[-m|--message]}} "{{warning message}}"`

- Օգտագործեք նշված տառատեսակը.:

`i3-nagbar {{[-f|--font]}} "{{pango:monospace bold 9}}" {{[-m|--message]}} "{{error message}}"`

- Ստեղծեք կոճակ և գործարկեք հրաման տերմինալում՝ սեղմելով.:

`i3-nagbar {{[-b|--button]}} "{{button text}}" {{command}} {{[-m|--message]}} "{{error message}}"`

- Ստեղծեք կոճակ և գործարկեք հրամանը սեղմելով.:

`i3-nagbar {{[-B|--button-no-terminal]}} "{{button text}}" {{command}} {{[-m|--message]}} "{{error message}}"`

- Միշտ բացեք `i3-nagbar`-ը հիմնական մոնիտորի վրա (կանխադրված՝ կենտրոնացված մոնիտոր).:

`i3-nagbar {{[-pm|--primary --message]}} "{{error message}}"`
