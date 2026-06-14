#հարգելի

> Պաշտոնական Oh Dear CLI:.
> Լրացուցիչ տեղեկություններ. <https://ohdear.app/docs/tools-and-sdks/our-cli-tool#available-commands>:.

- Ցուցադրել տվյալ պահին վավերացված օգտվողի մասին մանրամասներ.:

`ohdear get-me`

- Ավելացնել նոր մոնիտոր Oh Dear:

`ohdear create-monitor --field "team_id={{team_id}}" --field "type={{http|ping|tcp}}" --field "url={{url}}"`

- Ցուցադրել մոնիտորների ցանկը և դրանց ընթացիկ կարգավիճակը.:

`ohdear list-monitors`

- Ցուցադրել մանրամասներ կոնկրետ մոնիտորի մասին.:

`ohdear get-monitor --monitor-id {{monitor_id}}`
