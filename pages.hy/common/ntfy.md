#ntfy

> Ուղարկեք և ստացեք HTTP POST ծանուցումներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/binwiederhier/ntfy>:.

- Ուղարկեք հաղորդագրություն `security` թեմային.:

`ntfy pub security "{{Front door has been opened.}}"`

- Ուղարկեք վերնագրով, առաջնահերթությամբ և պիտակներով.:

`ntfy publish --title="{{Someone bought your item}}" --priority={{high}} --tags={{duck}} {{ebay}} "{{Someone just bought your item: Platypus Sculpture}}"`

- Ուղարկել ժամը 8:30:

`ntfy pub --at=8:30am {{delayed_topic}} "{{Time for school, sleepyhead...}}"`

- Գործարկել վեբ-կեռիկը.:

`ntfy trigger {{my_webhook}}`

- Բաժանորդագրվեք թեմային (`<Ctrl c>` լսելը դադարեցնելու համար).:

`ntfy sub {{home_automation}}`

- Ցուցադրել օգնությունը.:

`ntfy --help`
