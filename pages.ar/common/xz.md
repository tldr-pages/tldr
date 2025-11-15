# xz

> ضغط أو فك ضغط ملفات XZ و LZMA.
> لمزيد من التفاصيل: <https://manned.org/xz>.

- ضغط ملف باستخدام xz:

`xz {{path/to/file}}`

- فك ضغط ملف XZ:

`xz {{[-d|--decompress]}} {{path/to/file.xz}}`

- ضغط ملف باستخدام خوارزمية lzma:

`xz {{[-F|--format]}} lzma {{path/to/file}}`

- فك ضغط ملف LZMA:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{path/to/file.lzma}}`

- فك ضغط ملف وكتابته إلى المخرجات القياسية (stdout) (يتضمن `--keep`):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{path/to/file.xz}}`

- ضغط ملف بدون حذف النسخة الأصلية:

`xz {{[-k|--keep]}} {{path/to/file}}`

- ضغط ملف باستخدام أسرع ضغط:

`xz -0 {{path/to/file}}`

- ضغط ملف باستخدام أكفأ ضغط:

`xz -9 {{path/to/file}}`
