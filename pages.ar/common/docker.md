# docker

> إدارة حاويات وصور Docker.
> بعض الأوامر الفرعية مثل `run` لها توثيق استخدام خاص بها.
> لمزيد من التفاصيل: <https://docs.docker.com/reference/cli/docker/>.

- عرض جميع حاويات Docker (التشغيلية والمتوقفة):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- تشغيل حاوية من صورة مع اسم مخصص:

`docker {{[run|container run]}} --name {{container_name}} {{image}}`

- تشغيل أو إيقاف حاوية موجودة:

`docker container {{start|stop}} {{container_name}}`

- سحب صورة من سجل Docker:

`docker {{[pull|image pull]}} {{image}}`

- عرض قائمة الصور المحملة مسبقًا:

`docker {{[images|image ls]}}`

- فتح وحدة تحكم تفاعلية داخل حاوية تعمل مع شيل Bourne (`sh`):

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- إزالة الحاويات المتوقفة:

`docker {{[rm|container rm]}} {{container1 container2 ...}}`

- متابعة وعرض سجلات الحاوية:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{container_name}}`
