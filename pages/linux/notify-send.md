# notify-send

> Uses the current desktop environment's notification system to create a notification.
> More information: <https://manned.org/notify-send>.

- Show a notification with the title "Test" and the content "This is a test":

`notify-send "{{Test}}" "{{This is a test}}"`

- Show a notification with a custom icon:

`notify-send -i {{icon.png}} "{{Test}}" "{{This is a test}}"`

- Show a notification for 5 seconds:

`notify-send -t 5000 "{{Test}}" "{{This is a test}}"`

- Show a notification with an app's icon and name:

`notify-send "{{Test}}" --icon={{google-chrome}} --app-name="{{Google Chrome}}"`
