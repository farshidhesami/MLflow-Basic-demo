## MLflow  tuturial  for linear regression model :

Create a project folder  ( MLflow-Basic-demo ) and navigate to it : 
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
    - image\Mlflow-01.png
    

## What is "dagshub" ?

- when we work with a team and we want to share a model with a team member, we can use a remote server or repository ,All the logs remote server or repository are
  stored in the mlruns directory.

### Introduction to DAGsHub : 

- Integrating DAGsHub with MLflow in machine learning projects leverages the strengths of both platforms, offering a comprehensive solution for managing the lifecycle of machine learning projects with enhanced collaboration features. Here's why combining DAGsHub with MLflow can be particularly beneficial:

### Enhanced Collaboration and Version Control :

- DAGsHub  focuses on facilitating collaboration in data science and machine learning projects. It provides a GitHub-like interface for data science, allowing users to manage projects, track issues, and collaborate on notebooks, datasets, and models.

- MLflow , on the other hand, is designed for managing the machine learning lifecycle, including experimentation, model versioning, and deployment.

- By using DAGsHub with MLflow, teams can effectively version control not only their code but also their data and models, making collaborative work more seamless and organized. DAGsHub enhances the collaboration aspect by providing a platform for sharing and discussing the work, while MLflow focuses on tracking the experiments, managing models, and streamlining the workflow.

### Experiment Tracking and Visualization :

- MLflow allows for detailed experiment tracking, including parameters, metrics, and artifacts. This helps in comparing experiments to find the most effective models.

- DAGsHub integrates with MLflow to provide a visual interface for these experiments. 

- This combination means you can easily track your experiments' progress and outcomes within a collaborative environment, enhancing both transparency and reproducibility.

### Streamlined Project Management : 

- DAGsHub provides a central hub for project management, including issue tracking and documentation, tailored to data science workflows.
- Integrating MLflow into this environment means that you can manage the entire lifecycle of a machine learning project in one place, from initial data analysis to deployment, with tools specifically designed for each stage of the process.


## Run a model in "dagshub" :

- Note : before "dagshub" we need to commit a " example.py " code to the "github" and then we can run a model in "dagshub" we should go to :

    - Note  : Go to "MLflow-Basic-demo" folder and delete a "mlruns" because we want to run in remote server.

    - Go to Github website and create a new repository " https://dagshub.com/repo/create " .
    - Connect a new repository to the "dagshub" and "github" .
    - Go to remote and inside it click in "Experiments" and copy "Using Mlflow tracking" code below : 
      MLFLOW_TRACKING_URI=https://dagshub.com/farshidhesami/MLflow-Basic-demo.mlflow \
      MLFLOW_TRACKING_USERNAME=farshidhesami \
      MLFLOW_TRACKING_PASSWORD=650aa1c0a81ee25d18a1e3cead472320dc4e6d71 \
      python script.py
    
    - Go to "example.py" and change the code : 

      - Delete a "tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme" 
      - Add insted of add a code : remote_server_uri = "https://dagshub.com/farshidhesami/MLflow-Basic-demo.mlflow" for remote server.
      - Add a code : "tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme " for remote server. 

    - Export all credential into the Environment variable in **Git bash** terminal :

      - export MLFLOW_TRACKING_URI=https://dagshub.com/farshidhesami/MLflow-Basic-demo.mlflow
      - export MLFLOW_TRACKING_USERNAME=farshidhesami 
      - export MLFLOW_TRACKING_PASSWORD=650aa1c0a81ee25d18a1e3cead472320dc4e6d71 

    - Open a Terminal "GitBash" and paste all "export MLFLOW" into the terminal and go to " https://dagshub.com/farshidhesami/MLflow-Basic-demo" and click in "Experiments" and then click a "Go to mlflow UI" and see "No Experiments Exist" in page .
    
    - Go to terminal and type "python example.py" and see a result in "dagshub" remote server.
    - Then "Successfully registered model 'ElasticnetWineModel'" appear in terminal .
    - Go to "https://dagshub.com/farshidhesami/MLflow-Basic-demo" again and see a result in "Experiments" page.

    - Note : This is a link address that you share to anyone to see a result in server :
       - "https://dagshub.com/farshidhesami/MLflow-Basic-demo.mlflow/#/experiments/0?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&datasetsFilter=W10%3D&modelVersionFilter=All%20Runs&selectedColumns=attributes.%60Source%60,attributes.%60Models%60,attributes.%60Dataset%60&compareRunCharts=W3sidXVpZCI6IjE3MTAwNzg4MzUyNTYxNDNucTBmOSIsInR5cGUiOiJCQVIiLCJydW5zQ291bnRUb0NvbXBhcmUiOjEwLCJtZXRyaWNLZXkiOiJtYWUifSx7InV1aWQiOiIxNzEwMDc4ODM1MjU2aDA0a3VlYXAiLCJ0eXBlIjoiQkFSIiwicnVuc0NvdW50VG9Db21wYXJlIjoxMCwibWV0cmljS2V5Ijoicm1zZSJ9LHsidXVpZCI6IjE3MTAwNzg4MzUyNTY1ZWM4NTNncSIsInR5cGUiOiJCQVIiLCJydW5zQ291bnRUb0NvbXBhcmUiOjEwLCJtZXRyaWNLZXkiOiJyMiJ9LHsidXVpZCI6IjE3MTAwNzg4MzUyNTZxbXQxdzV6cSIsInR5cGUiOiJQQVJBTExFTCIsInJ1bnNDb3VudFRvQ29tcGFyZSI6MTAsInNlbGVjdGVkUGFyYW1zIjpbXSwic2VsZWN0ZWRNZXRyaWNzIjpbXX1d"

       - We can see a registered Model in web page : "https://dagshub.com/farshidhesami/MLflow-Basic-demo.mlflow/#/models" 
       - Three steps within MLflow's Model Registry:
         - 1.  Transition to Staging    : Models are tested and validated in a pre-production environment to ensure they meet necessary performance and business criteria.
         - 2.  Transition to Production : Approved models are moved to production for real-world use, where they are continuously monitored for performance.
         - 3. Transition to Archived    : Outdated or superseded models are moved to an archived state for historical reference, removing them from active deployment
              considerations. 

- Go to the terminal GitBash and write a " python example.py 0.5 0.6 " and see a version 02 of model in "dagshub" remote server.
- Compare Version 01 and Version 02 in "dagshub" remote server.

## Based on the metrics provided for the two model versions from your MLflow experiment:

-  Model Version 1: (Run ID: b6547a41020842e2addf7b005a81b9ff)
  - MAE: 0.627
  - R^2: 0.109
  - RMSE: 0.793

-  Model Version 2:  (Run ID: 33cb7f3eb1ec4c7fa991b21ef3efce0a)
  - MAE: 0.644
  - R^2: 0.071
  - RMSE: 0.81

- Note : " The lower " Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE),And the  higher  the R-squared (R^2) value, the better the model performance.

## Comparing the two sets of metrics:

- Model Version 1 has a  " lower MAE "  than Model Version 2 (0.627 compared to 0.644), which means that on average, Model Version 1's predictions are closer to the actual values.
- Model Version 1 also has a " lower RMSE " than Model Version 2 (0.793 compared to 0.81), suggesting that the standard deviation of its prediction errors is smaller.
- Model Version 1 has a " higher R^2 " value than Model Version 2 (0.109 compared to 0.071), indicating that it explains a higher proportion of the variance in the dependent variable.

- Given these metrics, " Model Version 1 " is performing better than Model Version 2 according to these three common measures of fit for regression models. 

- It's important to note that both models have very low R^2 values, suggesting that neither model explains much of the variance in the dependent variable, and there might be room for improvement in the modeling process.