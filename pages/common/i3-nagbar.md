# i3-nagbar

> Display an error/warning in a bar on top of a screen.
> More information: <https://manned.org/i3-nagbar>.

- Display an error:

`i3-nagbar {{[-m|--message]}} "{{error_message}}"`

- Display a warning:

`i3-nagbar {{[-t|--type]}} warning {{[-m|--message]}} "{{warning_message}}"`

- Use the specified font:

`i3-nagbar {{[-f|--font]}} "{{pango:monospace bold 9}}" {{[-m|--message]}} "{{error_message}}"`

- Create a button and run a command in a terminal on click:

`i3-nagbar {{[-b|--button]}} "{{button_text}}" {{command}} {{[-m|--message]}} "{{error_message}}"`

- Create a button and run a command on click:

`i3-nagbar {{[-B|--button-no-terminal]}} "{{button_text}}" {{command}} {{[-m|--message]}} "{{error_message}}"`

- Always open `i3-nagbar` on the primary monitor (default: focused monitor):

`i3-nagbar {{[-pm|--primary --message]}} "{{error_message}}"`
