#!/bin/bash
echo " 🚀 Building Project... "
python3 -m pip install pip-run --break-system-packages
python3 -m pip_run -r requirements.txt -- -m pip install -r requirements.txt --break-system-packages
python3 manage.py collectstatic --noinput --clear
echo " 🎉 Build Finished Successfully! "