# Notify-send

Uses the current desktop environment's notification system to create a notification. This should work on many modern desktop environments such as XFCE, GNOME, and Cinnamon.

- Sends out a notification with the title "Test" and the content "This is a test"

`notify-send {{"Test"}} {{"This is a test"}}`

- Sends out a notification with the title "Test", the content "This is a test", and the icon icon.png

`notify-send -i ./icon.png {{"Test"}} {{"This is a test"}}`

- Sends out a notification with the title "Test", the content "This is a test", and the notification shows up for 5 seconds

`notify-send -t 5000 {{"Test"}} {{"This is a test"}}`
