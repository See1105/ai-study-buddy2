# build_files.sh
pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
python3 manage.py migrate --noinput
