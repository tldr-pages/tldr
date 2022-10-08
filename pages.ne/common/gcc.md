# gcc

> C र C++ स्रोत फाइलहरू पूर्वप्रक्रिया र कम्पाइल गर्नुहोस्, त्यसपछि तिनीहरूलाई एकसाथ जोड्नुहोस् र लिङ्क गर्नुहोस्।
> थप जानकारी: <https://gcc.gnu.org>.

- कार्यान्वयनयोग्यमा बहु स्रोत फाइलहरू कम्पाइल गर्नुहोस्:

`gcc {{path/to/source1.c path/to/source2.c ...}} -o {{path/to/output_executable}}`

- आउटपुटमा सामान्य चेतावनीहरू, डिबग प्रतीकहरू देखाउनुहोस्:

`gcc {{path/to/source.c}} -Wall -Og -o {{path/to/output_executable}}`

- फरक मार्गबाट ​​पुस्तकालयहरू समावेश गर्नुहोस्:

`gcc {{path/to/source.c}} -o {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- एसेम्बलर निर्देशनहरूमा स्रोत कोड कम्पाइल गर्नुहोस्:

`gcc -S {{path/to/source.c}}`

- लिङ्क नगरी वस्तु फाइलमा स्रोत कोड कम्पाइल गर्नुहोस्

`gcc -c {{path/to/source.c}}`
