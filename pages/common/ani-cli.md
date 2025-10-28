# ani-cli

> A cli to browse and watch anime.
> See also: `animdl`.
> More information: <https://manned.org/ani-cli>.

- Search anime by name:

`ani-cli "{{anime_title}}"`

- Download an episode:

`ani-cli {{[-d|--download]}} "{{anime_title}}"`

- Download a range of episodes:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{anime_title}}"`

- Download the entire series (a range of all episodes):

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{anime_title}}"`

- Use VLC as the media player:

`ani-cli {{[-v|-vlc]}} "{{anime_title}}"`

- Watch a specific episode:

`ani-cli {{[-e|--episode]}} {{episode_number}} "{{anime_title}}"`

- Continue watching anime from history:

`ani-cli {{[-c|--continue]}}`

- Update `ani-cli`:

`ani-cli {{[-U|--update]}}`
