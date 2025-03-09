# ani-cli

> A cli to browse and watch anime.
> More information: <https://github.com/pystardust/ani-cli>.

- Search anime by name:

`ani-cli "{{anime_name}}"`

- [d]ownload episode:

`ani-cli -d "{{anime_name}}"`

- [d]ownload a [r]ange of episodes:

`ani-cli -d -r "{{1 6}}" "{{anime_name}}"`

- [d]ownload the entire series (a range of all episodes):

`ani-cli -d -r "1 -1" "{{anime_name}}"`

- Use [v]LC as the media player:

`ani-cli -v "{{anime_name}}"`

- Watch a specific [e]pisode:

`ani-cli -e {{episode_number}} "{{anime_name}}"`

- [c]ontinue watching anime from history:

`ani-cli -c`

- [U]pdate `ani-cli`:

`ani-cli -U`
