# ntfy

> Send and receive HTTP POST notifications.
> More information: <https://github.com/binwiederhier/ntfy>.

- Send a message to the `security` topic:

`ntfy pub security "{{Front door has been opened.}}"`

- Send with a title, priority and tags:

`ntfy publish --title="{{Someone bought your item}}" --priority={{high}} --tags={{duck}} {{ebay}} "{{Someone just bought your item: Platypus Sculpture}}"`

- Send at 8:30am:

`ntfy pub --at=8:30am {{delayed_topic}} "{{Time for school, sleepyhead...}}"`

- Trigger a webhook:

`ntfy trigger {{my_webhook}}`

- Subscribe to a topic (`<Ctrl c>` to stop listening):

`ntfy sub {{home_automation}}`

- Display help:

`ntfy --help`
