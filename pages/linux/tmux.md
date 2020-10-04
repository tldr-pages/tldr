# Tmux
> tmux is a terminal multiplexer. 
> It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.
> https://github.com/tmux/tmux/wiki/Getting-Started

The default prefix is Ctrl-b.
When you see {prefix}, press Ctrl-b, release both keys and then hit the next sequence.

- Create a new window:

`{prefix}+c`

- Switch to window *x* (Starts from zero):

`{prefix}+{x}`

- Close a window:

`{prefix}+x`

- Create a pane vertically (|):

`{prefix}+%`

- Create a pane horizontally (-):

`{prefix}-"`

- Move between panes:

`{prefix}-{arrow key}`

- Resize a pane:
`{prefix}+Ctrl-{arrow}
