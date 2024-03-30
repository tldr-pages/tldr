# dockutil

> Manage macOS dock items.
> More information: <https://github.com/kcrawford/dockutil>.

- Add an application to the end of the current user's dock:

`dockutil --add {{path/to/application}}`

- Replace one application with another in the current user's dock:

`dockutil --add {{/path/to/application}} --replacing '{{dock_item_label}}'`

- Add a directory with view options and display it as a folder icon or stack:

`dockutil --add {{/path/to/directory}} --view {{grid|fan|list|auto}} --display {{folder|stack}}`

- Add a URL dock item after another item:

`dockutil --add {{vnc://example_server.local}} --label '{{Example VNC}}' --after {{dock_item_label}}`

- Remove an application from the dock given its dock label name:

`dockutil --remove '{{dock_item_label}}'`

- Add a spacer in a section after an application:

`dockutil --add '' --type {{spacer|small-spacer|flex-spacer}} --section {{apps}} --after {{dock_item_label}}`

- Remove all spacer tiles:

`dockutil --remove spacer-tiles`
