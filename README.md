## MLflow  tuturial  for linear regression model :

Create a project folder  ( mlflow  project) and navigate to it : 
```

0-  Open a VScode and install a package (requirements.txt) in the terminal 
1-  Install a virtual environment (conda create -n mlflow python=3.8 -y)
2-  Activate a conda environment (conda activate mlflow) 
3-  Install mlflow ( pip install mlflow==2.11.0 )
4-  pip install -r requirements.txt 
5-  Copy example code from "https://mlflow.org/docs/1.24.0/tutorials-and-examples/tutorial.html" Training the Model and paste to example.py 

    - Note :
      - we use a "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html" for linear regression model.
      - Parameters "alpha" and "l1_ratio" are used to train the model.
      - use a ElasticNet model to train the model.
      - This is "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression" for linear regression
        model.
        
      - The alpha parameter in ElasticNet regression represents the constant that scales the penalty terms, with a default value of 1.0. If alpha is set to 0, ElasticNet behaves like ordinary least squares regression, which can be solved using the LinearRegression object. However, it's not recommended to use alpha = 0 with the Lasso object due to numerical issues. Instead, in such cases, the LinearRegression object should be used.

      - The l1_ratio parameter in ElasticNet regression controls the mixing between L1 and L2 penalties and should be within the range of 0 to 1. A l1_ratio of 0 corresponds to an L2 penalty (Ridge regression), while a l1_ratio of 1 corresponds to an L1 penalty (Lasso regression). For values between 0 and 1, ElasticNet applies a combination of L1 and L2 penalties, resulting in ElasticNet regression. 

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
    - https://github.com/farshidhesami/MLflow-Basic-demo/blob/7586ae3622b27dcc86d73d87117b01032c5724ad/image/Mlflow.jpg
    
