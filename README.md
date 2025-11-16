# السوابق واللواحق / Prefixes and Suffixes Extractor

<div dir="rtl">

## نظرة عامة

أداة متخصصة لاستخراج السوابق (Prefixes) واللواحق (Suffixes) من ملفات الأوزان الصرفية العربية. تساعد الباحثين واللغويين في تحليل البنية الصرفية للكلمات العربية.

## المميزات

- ✅ استخراج السوابق من ملفات الأوزان
- ✅ استخراج اللواحق من ملفات الأوزان
- ✅ معالجة أوزان الأسماء والأفعال
- ✅ مطابقة اللفظ بالشاهد
- ✅ نقل محتويات المنصة إلى نموذج Excel
- ✅ دعم ملفات النصوص و Excel

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث
- مكتبات Python المطلوبة (سيتم تثبيتها تلقائياً)

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/prefixes-suffixes-extractor.git
cd prefixes-suffixes-extractor
```

2. قم بتشغيل البرامج النصية مباشرة:
```bash
python "استخراج السوابق من ملف الأوزان.py"
```

## الاستخدام

### استخراج السوابق

```bash
python "استخراج السوابق من ملف الأوزان.py"
```

### مطابقة اللفظ بالشاهد

```bash
python "مطابقة اللفظ بالشاهد.py"
```

### نقل محتويات المنصة إلى نموذج

```bash
python "نقل محتويات المنصة إلى نموذج.py"
```

## هيكل المشروع

```
السوابق واللواحق/
├── استخراج السوابق من ملف الأوزان.py
├── مطابقة اللفظ بالشاهد.py
├── نقل محتويات المنصة إلى نموذج.py
├── 0.3 أوزان_الأسماء.txt
├── 0.3 أوزان_الأفعال.txt
├── نموذج.xlsx
└── كشكول/
    ├── السوابق.txt
    ├── اللواحق.txt
    ├── prefixes.txt
    ├── suffixes.txt
    └── [ملفات Excel متعددة]
```

## الملفات الرئيسية

- **استخراج السوابق من ملف الأوزان.py**: يستخرج السوابق من ملفات الأوزان
- **مطابقة اللفظ بالشاهد.py**: يطابق الألفاظ بالشواهد
- **نقل محتويات المنصة إلى نموذج.py**: ينقل المحتويات إلى نموذج Excel
- **0.3 أوزان_الأسماء.txt**: ملف أوزان الأسماء
- **0.3 أوزان_الأفعال.txt**: ملف أوزان الأفعال

## ملاحظات مهمة

⚠️ **ملاحظة**: بعض ملفات البيانات الكبيرة (Excel والمدونات) غير مرفوعة في المستودع لتقليل الحجم. يمكنك إضافة ملفاتك الخاصة في مجلد `كشكول/`.

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] دعم المزيد من صيغ الأوزان
- [ ] تحليل إحصائي للسوابق واللواحق
- [ ] تصدير النتائج بصيغ متعددة

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

A specialized tool for extracting prefixes and suffixes from Arabic morphological pattern files. Helps researchers and linguists analyze the morphological structure of Arabic words.

## Features

- ✅ Extract prefixes from pattern files
- ✅ Extract suffixes from pattern files
- ✅ Process noun and verb patterns
- ✅ Match words with examples
- ✅ Transfer platform contents to Excel template
- ✅ Support for text and Excel files

## Installation

### Requirements

- Python 3.7 or later
- Required Python libraries (will be installed automatically)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/prefixes-suffixes-extractor.git
cd prefixes-suffixes-extractor
```

2. Run the scripts directly:
```bash
python "استخراج السوابق من ملف الأوزان.py"
```

## Usage

### Extract Prefixes

```bash
python "استخراج السوابق من ملف الأوزان.py"
```

### Match Words with Examples

```bash
python "مطابقة اللفظ بالشاهد.py"
```

### Transfer Platform Contents to Template

```bash
python "نقل محتويات المنصة إلى نموذج.py"
```

## Project Structure

```
prefixes-suffixes-extractor/
├── استخراج السوابق من ملف الأوزان.py
├── مطابقة اللفظ بالشاهد.py
├── نقل محتويات المنصة إلى نموذج.py
├── 0.3 أوزان_الأسماء.txt
├── 0.3 أوزان_الأفعال.txt
├── نموذج.xlsx
└── كشكول/
    ├── السوابق.txt
    ├── اللواحق.txt
    ├── prefixes.txt
    ├── suffixes.txt
    └── [Multiple Excel files]
```

## Main Files

- **استخراج السوابق من ملف الأوزان.py**: Extracts prefixes from pattern files
- **مطابقة اللفظ بالشاهد.py**: Matches words with examples
- **نقل محتويات المنصة إلى نموذج.py**: Transfers contents to Excel template
- **0.3 أوزان_الأسماء.txt**: Noun patterns file
- **0.3 أوزان_الأفعال.txt**: Verb patterns file

## Important Notes

⚠️ **Note**: Some large data files (Excel files and corpora) are not uploaded to the repository to reduce size. You can add your own files in the `كشكول/` folder.

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Support for more pattern formats
- [ ] Statistical analysis of prefixes and suffixes
- [ ] Export results in multiple formats

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

