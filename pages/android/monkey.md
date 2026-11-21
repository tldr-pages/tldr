# monkey

> Run automated events on an Android.
> More information: <https://developer.android.google.cn/studio/test/other-testing-tools/monkey>.

- Run a set amount of random events against an app:

`monkey -p {{com.example.app}} {{event_count}}`

- Add a 500 millisecond delay between events:

`monkey --throttle 500 -p {{com.example.app}} {{event_count}}`
