
# MLflow Basic Demo: Linear Regression Model Tutorial

This repository contains a step-by-step tutorial for training a linear regression model using MLflow, focusing on the use of ElasticNet from scikit-learn. The tutorial guides you through setting up your environment, training the model with different parameters, and utilizing MLflow's powerful tracking and registry features for managing the machine learning lifecycle.

## Getting Started

### Prerequisites

- Python 3.8
- Conda environment
- Git Bash (for Windows users) or equivalent terminal

### Installation Steps

1. **Environment Setup**: Open VSCode and install necessary packages via `requirements.txt` in the terminal.

   ```bash
   conda create -n mlflow python=3.8 -y
   conda activate mlflow
   pip install mlflow==2.11.0
   pip install -r requirements.txt
   ```

2. **Model Training**: Copy the example code from the [MLflow tutorial](https://mlflow.org/docs/1.24.0/tutorials-and-examples/tutorial.html) and paste it into `example.py`. This example utilizes the ElasticNet model from scikit-learn for linear regression.

   - **Important Notes**: The tutorial employs parameters "alpha" and "l1_ratio" for model training. More details about these parameters are provided within the tutorial documentation.

3. **Data Preparation**: Download the dataset from [UCI Machine Learning Repository](http://archive.ics.uci.edu/dataset/186/wine+quality) and save it to the data folder.

4. **Running the Model**: Execute the model training script by running `python argv_exp.py` in Git Bash or your preferred terminal.

5. **MLflow UI**: To launch the MLflow UI and view your experiments, run `mlflow ui` in the terminal and navigate to `http://localhost:5000`.

## Integrating with DAGsHub

DAGsHub is used for enhancing collaboration among team members by providing a platform for sharing models and experiments. The tutorial includes steps on how to integrate DAGsHub with your MLflow project, facilitating remote tracking and visualization of experiments.

### Running the Model on DAGsHub

1. **Preparation**: Ensure that the `mlruns` folder is deleted to start fresh on the remote server.
2. **Repository Setup**: Create a new repository on DAGsHub and link it with your GitHub project.
3. **Environment Configuration**: Configure your environment to use DAGsHub as the remote server for MLflow tracking.

   ```bash
   export MLFLOW_TRACKING_URI=https://dagshub.com/<YourUsername>/MLflow-Basic-demo.mlflow
   export MLFLOW_TRACKING_USERNAME=<YourUsername>
   export MLFLOW_TRACKING_PASSWORD=<YourDagsHubToken>
   ```

4. **Run and Track**: After setting up the environment variables, run `python example.py` to execute your model training and automatically track the results on DAGsHub.

## Model Version Comparison

Based on the metrics provided for two different model versions, the tutorial guides you through evaluating model performance using common metrics such as MAE, R^2, and RMSE. This comparison highlights the importance of tracking and analyzing model performance over time to select the best version for production.

## Based on the metrics provided for the two model versions from your MLflow experiment:

-  Model Version 1: (Run ID: b6547a41020842e2addf7b005a81b9ff)
  - MAE: 0.627
  - R^2: 0.109
  - RMSE: 0.793

-  Model Version 2:  (Run ID: 33cb7f3eb1ec4c7fa991b21ef3efce0a)
  - MAE: 0.644
  - R^2: 0.071
  - RMSE: 0.81

- The lower: Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE),And the  higher  the R-squared (R^2) value, the better the model performance.

## Comparing the two sets of metrics:

- Model Version 1 has a  " lower MAE "  than Model Version 2 (0.627 compared to 0.644), which means that on average, Model Version 1's predictions are closer to the actual values.
- Model Version 1 also has a " lower RMSE " than Model Version 2 (0.793 compared to 0.81), suggesting that the standard deviation of its prediction errors is smaller.
- Model Version 1 has a " higher R^2 " value than Model Version 2 (0.109 compared to 0.071), indicating that it explains a higher proportion of the variance in the dependent variable.

## Conclusion

This tutorial provides a comprehensive guide to getting started with MLflow for managing the lifecycle of a machine learning project, from setup to integration with collaboration tools like DAGsHub. Follow the steps outlined to train your linear regression model, track experiments, and analyze model performance effectively.

For more detailed instructions and additional resources, refer to the official [MLflow documentation](https://mlflow.org/docs/latest/index.html) and the [DAGsHub documentation](https://dagshub.com/docs/).

## Final Model Address

You can view the final model and its versions directly on DAGsHub at the following address:
[View Models on DAGsHub](https://dagshub.com/farshidhesami/MLflow-Basic-demo.mlflow/#/models)

[View My Page on DAGsHub](https://dagshub.com/farshidhesami/MLflow-Basic-demo)
