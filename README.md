## MLflow  tuturial  for linear regression model :

Create a project folder  ( mlflow  project) and navigate to it : 
```

0-  Open a VScode and install a package (requirements.txt) in the terminal 
1-  Install a virtual environment (conda create -n mlflow python=3.8 -y)
2-  Activate a conda environment (conda activate mlflow) 
3-  Install mlflow ( pip install mlflow==2.11.0 )
4-  pip install -r requirements.txt 
5-  Copy example code from "https://mlflow.org/docs/1.24.0/tutorials-and-examples/tutorial.html" Training the Model and paste to example.py 
6-  Go to python interpreter and select a conda environment (mlflow)
7-  download a data from "http://archive.ics.uci.edu/dataset/186/wine+quality" and save it to data folder.
8-  Go to "https://mlflow.org/docs/2.11.0/python_api/index.html" and choose a "mlflow.sklearn"
9-  Create  a "argv_exp.py" .
10- we use a "argv_exp.py" to pass a parameter to the model for "alpha" and "l1_ratio"
11- Run the "python argv_exp.py" in Git bash terminal.
12- Run a code "python example.py and see a result.

    - Elasticnet model (alpha=0.500000, l1_ratio=0.500000):
    - RMSE: 0.7931640229276851
    - MAE: 0.6271946374319586
    - R2: 0.10862644997792614

13- for lunch a mlflow UI write in Git bash terminal "mlflow ui" and go to "http://
