# g++

> C++ स्रोत फाइलहरू कम्पाइल गर्छ।
> GCC को भाग (GNU कम्पाइलर संग्रह).
> थप जानकारी: <https://gcc.gnu.org>.

- स्रोत कोड फाइललाई कार्यान्वयनयोग्य बाइनरीमा कम्पाइल गर्नुहोस्:

`g++ {{path/to/source.cpp}} -o {{path/to/output_executable}}`

- सामान्य चेतावनीहरू प्रदर्शन गर्नुहोस्:

`g++ {{path/to/source.cpp}} -Wall -o {{path/to/output_executable}}`

- (C++98/C++11/C++14/C++17) को लागि कम्पाइल गर्न भाषा मानक छान्नुहोस्:

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} -o {{path/to/output_executable}}`

- स्रोत फाइल भन्दा फरक मार्गमा अवस्थित पुस्तकालयहरू समावेश गर्नुहोस्:

`g++ {{path/to/source.cpp}} -o {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- एक्जिक्युटेबल बाइनरीमा बहु स्रोत कोड फाइलहरू कम्पाइल र लिङ्क गर्नुहोस्:

`g++ -c {{path/to/source_1.cpp path/to/source_2.cpp ...}} && g++ -o {{path/to/output_executable}} {{path/to/source_1.o path/to/source_2.o ...}}`

- प्रदर्शन संस्करण:

`g++ --version`
