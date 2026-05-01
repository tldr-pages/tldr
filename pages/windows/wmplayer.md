# wmplayer

> Play and manage media files using Windows Media Player.
> Note: This command only applies to Windows Media Player versions released prior to Windows 10.
> More information: <https://learn.microsoft.com/previous-versions/windows/desktop/wmp/command-line-parameters>.

- Launch Windows Media Player:

`wmplayer`

- Play an audio, video, or playlist file:

`wmplayer {{path\to\file}}`

- Play a DVD or Audio CD:

`wmplayer /device:{{dvd|audiocd}}`

- Play a file in fullscreen mode:

`wmplayer {{path\to\file}} /fullscreen`

- Specify an user interface skin when playing file:

`wmplayer "{{path\to\file}}?wmpskin={{skin_name}}"`

- Show the Media Library page:

`wmplayer /Task MediaLibrary`

- Show the Now Playing page:

`wmplayer /Task NowPlaying`
