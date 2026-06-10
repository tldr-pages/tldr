#եթե

> Կատարել պայմանական մշակում shell սկրիպտներում:.
> Տես նաև՝ `test`, `[`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>:.

- Կատարեք նշված հրամանները, եթե պայմանի հրամանի ելքի կարգավիճակը զրո է.:

`if {{condition_command}}; then {{echo "Condition is true"}}; fi`

- Կատարեք նշված հրամանները, եթե պայմանի հրամանի ելքի կարգավիճակը զրոյական չէ.:

`if ! {{condition_command}}; then {{echo "Condition is true"}}; fi`

- Կատարեք առաջին նշված հրամանները, եթե պայմանի հրամանի ելքի կարգավիճակը զրոյական է, այլապես կատարեք երկրորդ նշված հրամանները.:

`if {{condition_command}}; then {{echo "Condition is true"}}; else {{echo "Condition is false"}}; fi`

- Ստուգեք, արդյոք [f]ile կա.:

`if [[ -f {{path/to/file}} ]]; then {{echo "Condition is true"}}; fi`

- Ստուգեք, արդյոք կա [d]տեղեկատու.:

`if [[ -d {{path/to/directory}} ]]; then {{echo "Condition is true"}}; fi`

- Ստուգեք, արդյոք ֆայլ կամ գրացուցակ [կա].:

`if [[ -e {{path/to/file_or_directory}} ]]; then {{echo "Condition is true"}}; fi`

- Ստուգեք, թե արդյոք փոփոխականը սահմանված է.:

`if [[ -n "${{variable}}" ]]; then {{echo "Condition is true"}}; fi`

- Թվարկեք բոլոր հնարավոր պայմանները (`test`-ը `[`-ի կեղծանունն է, երկուսն էլ սովորաբար օգտագործվում են `if`-ով):

`man test`
