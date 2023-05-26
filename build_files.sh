# build_files.sh
pip install -r requirements.txt
python3.9 manage.py collectstatic
python manage.py createsuperuser --username=admin --email=admin@gmail.com