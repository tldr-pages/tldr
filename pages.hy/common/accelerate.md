#արագացնել

> Գրադարան, որը հնարավորություն է տալիս նույն PyTorch կոդը գործարկել ցանկացած բաշխված կազմաձևում:.
> Լրացուցիչ տեղեկություններ. <https://huggingface.co/docs/accelerate/index>:.

- Տպել շրջակա միջավայրի տեղեկատվություն.:

`accelerate env`

- Ինտերակտիվ կերպով ստեղծեք կազմաձևման ֆայլ.:

`accelerate config`

- Տպեք GPU-ի հիշողության գնահատված արժեքը Hugging Face մոդելի գործարկման համար՝ տվյալների տարբեր տեսակներով.:

`accelerate estimate-memory {{name/model}}`

- Փորձարկել Accelerate կազմաձևման ֆայլը.:

`accelerate test --config_file {{path/to/config.yaml}}`

- Գործարկել մոդելը պրոցեսորի վրա Accelerate-ով.:

`accelerate launch {{path/to/script.py}} {{--cpu}}`

- Գործարկեք մոդելը բազմա-GPU-ով Accelerate-ով, 2 մեքենայով.:

`accelerate launch {{path/to/script.py}} --multi_gpu --num_machines 2`
