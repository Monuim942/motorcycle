#!/bin/bash
echo " Building Project... "

# تثبيت الحزم بأمان وتحديث الـ pip
python3 -m pip install --upgrade pip
uv pip install -r requirements.txt --system --break-system-packages

# تجميع الملفات الثابتة
python3 manage.py collectstatic --noinput --clear

echo " Build Finished! "