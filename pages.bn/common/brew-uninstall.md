# brew uninstall

> একটি Homebrew ফর্মুলা বা ক্যাস্ক আনইনস্টল করুন।
> অব্যবহৃত ডিপেন্ডেন্সি আনইনস্টল করতে, `brew autoremove` ব্যবহার করুন।
> আরও তথ্য পাবেন: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->।

- একটি ফর্মুলা বা ক্যাস্ক আনইনস্টল করুন:

`brew {{[rm|uninstall]}} {{ফর্মুলা|ক্যাস্ক}}`

- একটি ক্যাস্ক এবং এর সাথে সম্পর্কিত সমস্ত ফাইল আনইনস্টল করুন:

`brew {{[rm|uninstall]}} --zap {{ক্যাস্ক}}`
