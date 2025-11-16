import re
import pandas as pd

class TextProcessor:
    def __init__(self):
        self.arabic_diacritics_pattern = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
        self.shadda_pattern = re.compile(r'\u0651')
        self.arabic_diacritic_pattern = r'[\u064B-\u065F\u0670\u06D6-\u06ED]'
        self.al_sun_letters = set('تثدذرزسشصضطظلن')
        self.root_and_date_pattern = re.compile(
            r'^(?P<pattern1>(?:[\wًٌٍَُِّْ]+(?:\s[\wًٌٍَُِّْ]+)?)\،\ .*\،\ '
            r'(?:(?:لَازِم|مُتَعَدٍّ|مُتَعَدٍّ بِالحَرْف|اسْم|مُلَازِمٌ لِلْبِنَاءِ لِلْمَجْهُول|'
            r'اسْمُ جَمْع|اسْمُ فِعْل|مَصْدَر|اسْمُ مَرَّة|مَصْدَرٌ مِيمِيّ|اسْمُ فَاعِل|'
            r'اسْمٌ مَنْسُوب|صِفَة|اسْمُ جِنْس|مَصْدَرٌ صِنَاعِيّ|اسْمُ مَفْعُول|فِعْلٌ نَاقِص|'
            r'صِيغَةُ مُبَالَغَة|اسْمُ صَوْت|اسْمُ هَيْئَة|ظَرْف|صِفَةٌ مُشَبَّهَة|'
            r'اسْمُ زَمَان|اسْمُ تَفْضِيل|مُثَنًّى عَلَى التَّغْلِيب|اسْمٌ مُصَغَّر|'
            r'اسْمُ آلَة|حَرْف|فِعْل|اسْمُ مَكَان)))$|'
            r'^(?P<pattern2>ن?\d{1,4}هـ/\d{1,4}م.*|ن?\d{1,4}ق\.هـ/\d{1,4}م.*)$',
            re.MULTILINE
        )
        self.arabic_letter_pattern = r'[\u0621-\u064A]'
        self.letter_with_diacritic_pattern = self.arabic_letter_pattern + self.arabic_diacritic_pattern + '*'

    def remove_diacritics(self, text):
        """Removes Arabic diacritics from the text."""
        return self.arabic_diacritics_pattern.sub('', text)

    def split_letters(self, word):
        """Splits a word into its letters, including diacritics."""
        return re.findall(self.letter_with_diacritic_pattern, word)

    def strip_definite_article(self, word):
        """Strips the Arabic definite article 'ال' من الكلمة."""
        match = re.match(r'^(ال)([\u064B-\u065F]*)', word)
        if match:
            return word[match.end():], True
        else:
            return word, False

    def compare_words(self, word1, word2):
        """يقارن كلمتين عربيتين من حيث اختلاف التشكيل على الحروف المتطابقة."""
        word2_stripped, has_definite_article = self.strip_definite_article(word2)
        letters1 = self.split_letters(word1)
        letters2 = self.split_letters(word2_stripped)

        # تجاهل الحرف الأخير من الكلمة الثانية
        if len(letters2) > 1:
            letters2 = letters2[:-1]

        min_length = min(len(letters1), len(letters2))
        diacritics_diff = False

        for i in range(min_length):
            base_letter1 = self.remove_diacritics(letters1[i])
            base_letter2 = self.remove_diacritics(letters2[i])

            # تجاهل الحروف التي تختلف في الأساس
            if base_letter1 != base_letter2:
                continue

            # إذا كانت الكلمة تحتوي على "الـ" الشمسية وتكون الشدة على الحرف الأول
            if has_definite_article and i == 0 and base_letter2 in self.al_sun_letters:
                # تجاهل الشدة على الحرف الأول بعد "الـ"
                letter1_no_shadda = self.shadda_pattern.sub('', letters1[i])
                letter2_no_shadda = self.shadda_pattern.sub('', letters2[i])
                if letter1_no_shadda == letter2_no_shadda:
                    continue

            # تجاهل الاختلاف في التشكيل على الحرف الأخير من الكلمة الأولى إذا كان بدون تشكيل
            if i == len(letters1) - 1:
                if not re.search(self.arabic_diacritic_pattern, letters1[i]):
                    continue

            # إذا كانت التشكيلات مختلفة على نفس الحرف
            if letters1[i] != letters2[i]:
                diacritics_diff = True

        if diacritics_diff:
            return 'اختلاف في التشكيل'
        else:
            return 'تطابق كامل'

    def map_comparison_result(self, comparison_result):
        """يقوم بترجمة نتيجة المقارنة إلى رسالة قابلة للقراءة."""
        mapping = {
            'تطابق كامل': '[متطابق]',
            'اختلاف في التشكيل': '[اختلاف تشكيل]'
        }
        return mapping.get(comparison_result, '')

    def extract_full_word_from_text(self, fr_root, shahed_text):
        """
        يستخرج الكلمة الكاملة من نص 'شاهد' التي تحتوي على الكلمة الأساسية 'فرع',
        بما في ذلك السوابق واللواحق.
        """
        # إزالة التشكيل من الكلمة الأساسية لتسهيل البحث
        fr_root_no_diacritics = self.remove_diacritics(fr_root)

        # إنشاء نمط regex يسمح بوجود تشكيل بين حروف الكلمة الأساسية
        fr_root_pattern = ''
        for char in fr_root_no_diacritics:
            fr_root_pattern += re.escape(char) + self.arabic_diacritic_pattern + '*'

        # نمط regex للبحث عن الكلمات التي تحتوي على الكلمة الأساسية مع السوابق واللواحق
        pattern = rf'(?<!\S)(\S*{fr_root_pattern}\S*)(?!\S)'

        matches = re.findall(pattern, shahed_text)

        if matches:
            # إرجاع أول تطابق موجود
            return matches[0]
        else:
            return ''

    def extract_prefix_suffix(self, full_word, root_word):
        """
        يستخرج السوابق واللواحق من الكلمة الكاملة بناءً على الكلمة الأساسية.
        """
        # إزالة التشكيل
        full_word_no_diacritics = self.remove_diacritics(full_word)
        root_word_no_diacritics = self.remove_diacritics(root_word)

        # إيجاد موضع الكلمة الأساسية في الكلمة الكاملة
        start_index = full_word_no_diacritics.find(root_word_no_diacritics)

        if start_index == -1:
            return '', ''

        # حساب عدد الأحرف الأساسية قبل الكلمة الأساسية
        base_letters_count = 0
        start_pos = 0
        for i, char in enumerate(full_word):
            if not self.arabic_diacritics_pattern.match(char):
                if base_letters_count == start_index:
                    start_pos = i
                    break
                base_letters_count += 1

        # إيجاد نهاية الكلمة الأساسية في الكلمة الكاملة
        end_pos = start_pos
        letters_matched = 0
        for i in range(start_pos, len(full_word)):
            if not self.arabic_diacritics_pattern.match(full_word[i]):
                letters_matched += 1
                if letters_matched == len(root_word_no_diacritics):
                    end_pos = i + 1
                    break

        # تضمين أي تشكيلات بعد نهاية الكلمة الأساسية
        while end_pos < len(full_word) and self.arabic_diacritics_pattern.match(full_word[end_pos]):
            end_pos += 1

        # استخراج السوابق واللواحق
        prefix = full_word[:start_pos]
        suffix = full_word[end_pos:]

        return prefix, suffix

    def process_row(self, فرع, شاهد_text):
        """
        يعمل على مقارنة الكلمتين وإرجاع نتيجة المقارنة والكلمة المقارنة الكاملة مع السوابق واللواحق.
        """
        if not isinstance(فرع, str) or not isinstance(شاهد_text, str):
            return pd.Series({
                'اللفظ الشاهد': 'بيانات غير صالحة',
                'مقارنة': 'بيانات غير صالحة',
                'السوابق': 'بيانات غير صالحة',
                'اللواحق': 'بيانات غير صالحة'
            })

        # استخراج الكلمة الكاملة من نص 'شاهد' التي تحتوي على 'فرع'
        full_word = self.extract_full_word_from_text(فرع, شاهد_text)

        if full_word:
            # مقارنة الكلمة الأساسية مع الكلمة الكاملة المستخرجة
            comparison_result = self.compare_words(فرع, full_word)
            comparison_mapped = self.map_comparison_result(comparison_result)

            # استخراج السوابق واللواحق
            prefix, suffix = self.extract_prefix_suffix(full_word, فرع)

            return pd.Series({
                'اللفظ الشاهد': full_word,
                'مقارنة': comparison_mapped,
                'السوابق': prefix if prefix else '',
                'اللواحق': suffix if suffix else ''
            })
        else:
            return pd.Series({
                'اللفظ الشاهد': 'غير موجود',
                'مقارنة': 'غير موجود',
                'السوابق': '',
                'اللواحق': ''
            })

def main():
    processor = TextProcessor()

    # قراءة ملف الإكسل
    try:
        df = pd.read_excel("المنصة_كامل_3.xlsx", engine='openpyxl')  # تأكد من اسم الملف والمسار
    except FileNotFoundError:
        print("لم يتم العثور على ملف الإكسل المحدد.")
        return
    except Exception as e:
        print(f"حدث خطأ أثناء قراءة ملف الإكسل: {e}")
        return

    # التأكد من وجود الأعمدة المطلوبة
    required_columns = ['فرع', 'شاهد']
    for column in required_columns:
        if column not in df.columns:
            print(f"ملف الإكسل يجب أن يحتوي على عمود: '{column}'.")
            return

    # إضافة الأعمدة الجديدة 'اللفظ الشاهد', 'مقارنة', 'السوابق', 'اللواحق'
    processed_columns = df.apply(lambda row: processor.process_row(row['فرع'], row['شاهد']), axis=1)

    # دمج النتائج مع DataFrame الأصلي
    df = pd.concat([df, processed_columns], axis=1)

    # حفظ النتائج في ملف إكسل جديد
    try:
        df.to_excel("output.xlsx", index=False, engine='openpyxl')  # يمكنك تغيير اسم الملف إذا رغبت
        print("تمت عملية المقارنة بنجاح وحفظ النتائج في 'output.xlsx'.")
    except Exception as e:
        print(f"حدث خطأ أثناء حفظ ملف الإكسل: {e}")

if __name__ == "__main__":
    main()
