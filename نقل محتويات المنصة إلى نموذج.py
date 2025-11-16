import pandas as pd

# تحديد مسار ملف Excel
file_path = r"12345.xlsx"

# قراءة ملف Excel
data = pd.read_excel(file_path)

# تجميع القيم الفريدة للفرع لكل جذر
result = data.groupby('الجذر')['الفرع'].apply(lambda x: list(dict.fromkeys(x))).reset_index()

# إنشاء DataFrame جديد بحيث يتم وضع كل كلمة في عمود منفصل
final_result = pd.DataFrame(result['الفرع'].to_list(), index=result['الجذر']).reset_index()
final_result.columns = ['الجذر'] + [f"فرع {i+1}" for i in range(final_result.shape[1] - 1)]

# حفظ النتائج في ملف Excel جديد
output_path = r"123456789.xlsx"
final_result.to_excel(output_path, index=False)

print(f"تم حفظ الملف الناتج في: {output_path}")
