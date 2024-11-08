# ML Zoomcamp midterm project - Adult Income Prediction
### Choice of dataset and task description
I was interested in finding some data on correlation between education level and income. So I found this dataset ([link here](https://archive.ics.uci.edu/dataset/2/adult)). This dataset has information about a lot of people from different counties, different age, race and educations level. Also it has information if annual income of a person was more or less then 50k. All data was collected in 1994, so this 50k trashhold shows quet wealthy people. <p>
I was interested in researching this dataset especially to see correlation of factors that influence income. <p>
So the task is to made a model based on current data to be able to predict for any person if they can expect an income over 50k.

### Dataset
Dataset is provided as .csv file, but it is also downloadable through ucimlrepo. In Jupyter and py files I will use .csv version. Code to download dataset also is there, under the comments.

## Model traineng
I have tried different models: regression, design tree, random forest and Gradient Boosting. Tuning parameters for all of those. It was clear that regressing model has the worst results and Gradient Boosting gives much better AUC then all other models. See file `Data_analysys.ipynb` for data analizes and model training. <p>
To re-execute the notebook you copy all the files to your local machine or to other github codespace. Than use pipenv environment from pipfile provided. Running `pipenv install` will automatically create virtual environment and install all necessary modules. Then use `pipenv shell` to enter the environment. Then just go throught `Data_analysys.ipynb`.
As I mention earlier Gradient Boosting looks the best, so I chouse it as my final model. Final model training is prepared in file `train_and_save_model.py`. Running this file will result in training model with tuned parametes and saving it to the `model_gxb.bin` file. This file will be used be prediction function in `Use file`.

## Containerization and Cloud deployment

Provided Dockerfile is made for deployment. Run docker with command `docker build -t income-predict .`. _Be sure you have docker installed and running_. This will take some time and create docker image named  `income-predict`. Now you can try to use model localy. Go to `Use.ipynb` _OR_ `use_model.py` file. <p> **First run it as is**. It will go to my AWS sever where the model is already deployed and shouw you result. <p>
Run docker with command `docker run -it --rm -p 9696:9696 income_predict`. Than change address in url in the `use file` to your localhost and run it again, now you should have response from application running in you local docker.

### Cloud deployment

I have deployed this model to AWS. _That was unexpactedly hard and long_. There where a lot of steps _(coomands proveded here use my AWS account, if you want to re-do it, you should use you account information)_:
* Create an ECR Repository on AWS _(this includes create a account, use, key first)_
* Tag Docker image: `docker tag income_predict 412381739886.dkr.ecr.eu-west-3.amazonaws.com/income_predict:latest`
* Authenticate Docker with ECR: `aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 412381739886.dkr.ecr.eu-west-3.amazonaws.com`
* Push the image: `docker push 412381739886.dkr.ecr.eu-west-3.amazonaws.com/income_predict:latest`
* Set Up an ECS Cluster (Powered by Fargate)
* Create and run a Task to run aplication on that cluster

To check it on AWS go to `Use.ipynb` _OR_ `use_model.py` file. set url to `url= 'http://35.180.97.11:9696/predict'` and run file. You may change data in `adult` dictionary to see other results.


