# dockutil

> Manage macOS dock items.
> More information: <https://github.com/kcrawford/dockutil>.

- Add an application to the end of the current user's dock:

`dockutil --add {{/path/to/application}}`

- Replace one application with another in the current user's dock:

`dockutil --add {{/path/to/application}} --replacing '{{dock_item_label_name}}'`

- Add a directory with view options and display it as a folder icon or stack:

`dockutil --add '{{/path/to/directory}}' --view {{grid|fan|list|auto}} --display {{folder|stack}}`

- Add a url dock item after the Downloads dock item:

`dockutil --add {{vnc://example_server.local}} --label '{{Example VNC}}' --after {{Downloads}}`

- Remove an application from the dock given its dock label name:

`dockutil --remove '{{dock_item_label_name}}'`

- Add a spacer tile in the apps section after an Application:

`dockutil --add '' --type {{spacer}} --section {{apps}} --after {{dock_item_label_name}}`

- Remove all spacer tiles:

`dockutil --remove spacer-tiles`
