# am

> Android faoliyat boshqaruvi.
> Ko'proq malumot: <https://developer.android.com/tools/adb#am>.

- Anniq bir faoliyatni boshlash:

`am start -n {{com.android.settings/.Settings}}`

- Faoliyatni boshlash va unga malumot o'tkazish:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Biron harakat va kategoriyaga mos keluvchi faoliyatni boshlash:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Intentni URI ga o'zgartirish:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
