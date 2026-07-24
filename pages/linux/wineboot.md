# wineboot

> Simulate a Windows reboot, or initialize, update, or shut down a Wine prefix.
> More information: <https://manned.org/wineboot>.

- Perform a simulated reboot of the Wine prefix:

`wineboot`

- Initialize or update the prefix (e.g. after upgrading Wine):

`wineboot {{[-u|--update]}}`

- Restart Wine without performing a full boot:

`wineboot {{[-r|--restart]}}`

- Shut down the Wine session without rebooting:

`wineboot {{[-s|--shutdown]}}`

- End the current session, [f]orcing unresponsive processes to close:

`wineboot {{[-ef|--end-session --force]}}`

- Kill all processes in the prefix without any cleanup:

`wineboot {{[-k|--kill]}}`

- Display help:

`wineboot {{[-h|--help]}}`
