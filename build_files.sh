#!/bin/bash
echo " Building Project... "

# تثبيت الحزم باستخدام أداة uv الذكية المتوافقة مع تحديث Vercel
uv pip install -r requirements.txt --system

# تشغيل أمر تجميع ملفات الستاتيك الخاص بديانغو
python3 manage.py collectstatic --noinput --clear

echo " Build Finished! "