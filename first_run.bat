cd /home/yelemama/cours_python_web/
python3 -m venv venv
. venv/bin/activate
pip install Flask
export FLASK_APP=application.py
export FLASK_ENV=development
flask run
