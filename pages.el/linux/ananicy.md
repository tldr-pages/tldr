# ananicy

> Auto-nice daemon for Linux to manage process priorities automatically.
> More information: <https://github.com/NGRhitchhiker/Ananicy>.

- Start the Ananicy service:

`sudo systemctl start ananicy`

- Enable Ananicy to auto-start on boot:

`sudo systemctl enable --now ananicy`

- Check the status of the Ananicy daemon and active rules:

`sudo systemctl status ananicy`

- View live logging:

`journalctl -fu ananicy`

- Dump active rules and configured process types:

`ananicy dump rules`

- Check if a specific process name matches any active rule:

`ananicy check {{process_name}}`
