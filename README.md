# Django IPL project

## Setting up the environment
If you want to run this in a virtual environment check this [link to set a venv](https://docs.python.org/3/library/venv.html)

- To run this project first we have to install the django and import the dataset from  the terminal 
```bash
# installing the django frameworlk
pip install django


# migrate the databse file
python3 manage.py makemigrations

python3 manage.py migrate


# import the datasets
python3 manage.py import_csv path/to/your/matches.csv

python3 manage.py import_csv path/to/your/deliveries.csv
```
- **NOTE** *You can download the dataset from the link given below*

    [IPL Dataset](https://www.kaggle.com/manasgarg/ipl/version/5)

- Next start the django server by 
```bash
# strating the development server
python3 manage.py runserver
```

### First page of this project is the list of questions through wich you can navigate to a particular question

Further to view the charts you have to add /chart at the end of the URL 

EXAMPLE
```bash
http://localhost:8000/ques-1/chart
```