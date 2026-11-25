# wf-recorder

> ضبط صفحه برای Wayland، به‌صورت اختیاری همراه با صدا.
> به‌طور پیش‌فرض باید فرایند را با `<Ctrl c>` پایان دهید.
> اطلاعات بیشتر: <https://github.com/ammen99/wf-recorder>.

- ضبط و ذخیره در فایل MP4:

`wf-recorder {{[-f|--file]}} {{output.mp4}}`

- ضبط همراه صدا، شامل صدای میکروفون و سیستم:

`wf-recorder {{[-a|--audio]}} {{[-f|--file]}} /{{path/to/file_with_audio.webm}}`

- انتخاب و ضبط بخشی از صفحه با `slurp` و خروجی در فایل پیش‌فرض `recording.mp4`:

`wf-recorder {{[-g|--geometry]}} "$(slurp)"`
