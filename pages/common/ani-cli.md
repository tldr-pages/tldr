# ani-cli

> A cli to browse and watch anime.
> More information: <https://manned.org/ani-cli>.

- Search anime by name:

`ani-cli "{{anime_name}}"`

- Download an episode:

`ani-cli {{[-d|--download]}} "{{anime_name}}"`

- Download a range of episodes:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{anime_name}}"`

- Download the entire series (a range of all episodes):

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{anime_name}}"`

- Use VLC as the media player:

`ani-cli {{[-v|-vlc]}} "{{anime_name}}"`

- Watch a specific episode:

`ani-cli {{[-e|--episode]}} {{episode_number}} "{{anime_name}}"`

- Continue watching anime from history:

`ani-cli {{[-c|--continue]}}`

- Update `ani-cli`:

`ani-cli {{[-U|--update]}}`
