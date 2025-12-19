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
- create dummy data
- dvc add data/raw/iris.csv
- git add .
- git commit
- prepare data - 80% for training 20% for testing
- 2 files will be generated
- validation script
- git add,commit
- now add these files to dvc and create yaml file:

dvc stage add \
> -n prepare \ 
> -d src/prepare_data.py -d data/raw/iris.csv \
> -o data/processed/train.csv -o data/processed/test.csv \
> python src/prepare_data.py

-"prepare" is the name of the stage

now, we will create "validate" stage

- dvc stage add -n validate -d src/validate_data.py -d data/processed/train.csv python src/validate_data.py


-To check the flow: run
- dvc repro validate  -> it will automaticaly run prepare_data first.then after its success will run validate
- dvc.lock will be created