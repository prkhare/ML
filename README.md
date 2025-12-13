# ML

- mkdir -p data/raw data/processed src models metrics

- git init (ignore in codepsace)
- create .gitignore
    - __pycache__
    - .venv
    - *.pkl
    - *.log
    - .env

- virtualenv venv OR python -m venv .venv
- source venv/bin/activate OR source .venv/bin/activate
- pip install pandas scikit-learn dvc
- pip freeze > requirements.txt OR pip install -r requirements.txt
- dvc init
