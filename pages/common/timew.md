# timew

> A time tracking tool used to measure the duration of activities.
> More information: <https://timewarrior.net/docs>.

- Start tracking an activity:

`timew start`

- Tag the current activity:

`timew tag {{activity_tag}}`

- Start tracking and tag a new activity:

`timew start {{activity_tag}}`

- Stop the current activity:

`timew stop`

- Track an activity in the past:

`timew track {{start_time}} - {{end_time}} {{activity_tag}}`

- View tracked items of the day:

`timew summary`

- View report for the last day, week, current month, etc.:

`timew summary :{{today|yesterday|week|lastweek|month|lastmonth|year|lastyear}}`
