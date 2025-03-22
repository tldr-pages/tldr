# openai

> أداة سطر الأوامر للوصول إلى واجهة برمجة تطبيقات OpenAI.
> مزيد من المعلومات: <https://github.com/openai/openai-python>.

- عرض قائمة النماذج المتاحة:

`openai api models.list`

- إنشاء إكمال نصي:

`openai api completions.create --model {{ada}} --prompt "{{مرحبا بالعالم}}"`

- إنشاء إكمال محادثة:

`openai api chat_completions.create --model {{gpt-3.5-turbo}} --message {{user "مرحبا بالعالم"}}`

- إنشاء صور باستخدام API الخاصة بـ DALL·E:

`openai api image.create --prompt "{{كلبان يلعبان الشطرنج، كرتوني}}" --num-images {{1}}`
