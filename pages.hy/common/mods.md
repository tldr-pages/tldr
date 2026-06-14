# ռեժիմ

> AI հրամանի տողի համար, որը կառուցված է խողովակաշարերի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/charmbracelet/mods#usage>:.

- Ընդհանուր հարց տվեք.:

`mods "{{write me a poem about platypuses}}"`

- Բացեք կարգավորումները ձեր `$EDITOR`-ում.:

`mods --settings`

- Խնդրեք մեկնաբանություններ ձեր կոդի վերաբերյալ, նշման ձևաչափով.:

`mods < {{path/to/file}} {{[-f|--format]}} "{{what are your thoughts on improving this code?}}"`

- Խնդրեք օգնություն ձեր փաստաթղթերի հետ կապված՝ նշման ձևաչափով.:

`mods < {{README.md}} {{[-f|--format]}} "{{write a new section to this readme for a feature that sends you a free rabbit if you hit r}}"`

- Կազմակերպեք ձեր տեսանյութերը, նշման ձևաչափով.:

`ls {{path/to/videos}} | mods {{[-f|--format]}} "{{organize these by decade and summarize}}"`

- Կարդացեք չմշակված HTML-ը և ամփոփեք բովանդակությունը՝ նշման ձևաչափով.:

`curl "{{https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m}}" | mods {{[-f|--format]}} "{{summarize this weather data for a human}}"`

- Ցուցադրել օգնությունը.:

`mods --help`
