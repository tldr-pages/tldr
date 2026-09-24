# swaynag

> Display a message in a bar on top of a screen.
> More information: <https://github.com/swaywm/sway/blob/master/swaynag/swaynag.1.scd>.

- Display an error:

`swaynag {{[-m|--message]}} "{{error message}}"`

- Display a warning:

`swaynag {{[-t|--type]}} warning {{[-m|--message]}} "{{warning message}}"`

- Display a message with custom settings defined in the config:

`swaynag {{[-t|--type]}} {{custom_type}} {{[-m|--message]}} "{{message}}"`

- Use the specified font:

`swaynag {{[-f|--font]}} "{{monospace bold 9}}" {{[-m|--message]}} "{{error message}}"`

- Create a button and run a command in the specified terminal on click:

`TERMINAL={{terminal_executable}} swaynag {{[-b|--button]}} "{{button text}}" {{command}} {{[-m|--message]}} "{{error message}}"`

- Create a button and run a command on click:

`swaynag {{[-B|--button-no-terminal]}} "{{button text}}" {{command}} {{[-m|--message]}} "{{error message}}"`

- Display the bar on the bottom of the screen:

`swaynag {{[-e|--edge]}} bottom {{[-m|--message]}} "{{error message}}"`

- Open `swaynag` on the specified monitor:

`swaynag {{[-o|--output]}} {{DP-1}} {{[-m|--message]}} "{{error message}}"`
