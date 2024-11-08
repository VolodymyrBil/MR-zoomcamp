# ML Zoomcamp midterm project - Adult Income Prediction
### Choice of dataset and task description
I was interested in finding some data on correlation between education level and income. So I found this dataset ([link here](https://archive.ics.uci.edu/dataset/2/adult)). This dataset has information about a lot of people from different counties, different age, race and educations level. Also it has information if annual income of a person was more or less then 50k. All data was collected in 1994, so this 50k trashhold shows quet wealthy people. <p>
I was interested in researching this dataset especially to see correlation of factors that influence income. <p>
So the task is to made a model based on current data to be able to predict for any person if they can expect an income over 50k.

### Dataset
Dataset is provided as .csv file, but it is also downloadable through ucimlrepo. In Jupyter and py files I will use .csv version. Code to download dataset also is there, under the comments.

## Model traineng
I have tried different models: regression, design tree, random forest and Gradient Boosting. Tuning parameters for all of those. It was clear that regressing model has the worst results and Gradient Boosting gives much better AUC then all other models. See file `Data_analysys.ipynb` for data analizes and model training. <p>
To re-execute the notebook you copy all the files to your local machine or to other github codespace. Than use pipenv environment from pipfile provided. Running `pipenv install` will automatically create virtual environment and install all necessary modules. Then use `pipenv shell` to enter the environment. Then just go throught `Data_analysys.ipynb`

## Containerization and Cloud deployment
