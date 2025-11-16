input_file = r"0.3 أوزان_الأسماء.txt"
output_file_processed = "النص بعد الاقتصاص.txt"
prefix_suffix_file = "السوابق واللواحق.txt"

prefixes = set()
suffixes = set()

with open(input_file, "r", encoding="utf-8") as f, open(output_file_processed, "w", encoding="utf-8") as out_f:
    for line in f:
        original_line = line.rstrip("\n")
        # إذا كان السطر يبدأ بـ "#"، نكتبه كما هو في الملف الناتج، ولا نعالجه.
        if original_line.startswith("#"):
            out_f.write(original_line + "\n")
            continue
        
        # تقسيم السطر إلى كلمات بناءً على الفاصلة العربية "،"
        parts = original_line.split("،")
        # تنظيف الفراغات حول الكلمات
        parts = [p.strip() for p in parts if p.strip()]

        new_parts = []
        for word in parts:
            # نتحقق من وجود 'ف' 
            if 'ف' not in word:
                # لا يوجد 'ف'، نكتب الكلمة كما هي في الناتج
                new_parts.append(word)
                continue
            
            f_index = word.find('ف')
            
            # إيجاد كل مواضع 'ل'
            l_indices = [i for i, ch in enumerate(word) if ch == 'ل']
            if not l_indices:
                # لا توجد 'ل'، لا استخلاص
                new_parts.append(word)
                continue
            
            # إذا كانت أول 'ل' في بداية الكلمة، نتجاهلها
            # نبحث عن لام أخرى
            if l_indices[0] == 0 and len(l_indices) > 1:
                # نتجاهل اللام الأولى ونأخذ الأخيرة
                l_index = l_indices[-1]
            elif l_indices[0] == 0 and len(l_indices) == 1:
                # لا توجد لام أخرى غير الأولى في البداية، لا لاحقة
                l_index = None
            else:
                # لا توجد لام في البداية، نأخذ الأخيرة مباشرة
                l_index = l_indices[-1]

            # إذا لم يتوفر l_index صحيح معتمد
            if l_index is None:
                # لا لاحقة، لا استخراج
                new_parts.append(word)
                continue

            # الآن لدينا f_index و l_index
            # السابقة: قبل الفاء
            prefix = word[:f_index]
            # اللاحقة: بعد اللام المعتمدة
            suffix = word[l_index+1:]

            # نضيف إلى المجموعات
            if prefix:
                prefixes.add(prefix)
            if suffix:
                suffixes.add(suffix)

            # نزيل السابقة واللاحقة من الكلمة، ونبقي الجزء الأوسط
            # الجزء الأوسط = من f_index إلى l_index (يشمل الفاء واللام)
            middle_part = word[f_index:l_index+1]
            
            # الكلمة بعد الاقتصاص
            cropped_word = middle_part
            new_parts.append(cropped_word)

        # إعادة تجميع الكلمات مع الفاصلة العربية "، "
        # ملاحظة: في الأصل كانت ربما هناك فواصل في نهاية السطر، 
        # سنفترض أن التنسيق الجديد هو بنفس أسلوب التقسيم السابق
        out_line = "، ".join(new_parts)
        out_f.write(out_line + "\n")

# بعد الانتهاء من استخراج السوابق واللواحق، نكتبها في الملف الخاص
with open(prefix_suffix_file, "w", encoding="utf-8") as ps_f:
    ps_f.write("السوابق:\n")
    for p in sorted(prefixes):
        ps_f.write(f"\"{p}\", ")
    ps_f.write("\n\nاللواحق:\n")
    for s in sorted(suffixes):
        ps_f.write(f"\"{s}\", ")
