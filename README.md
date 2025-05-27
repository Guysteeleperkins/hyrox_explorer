# Hyrox Results Explorer

## Planning 

For my capstone project I used my own garmin data, this was a great experience to practice and learn more about the ETL process, however due to time constraints i used downloaded CSV files from my garmin account and therefore the extraction part did not really exist - I wanted to look at data that has come from the fitness industry and I have recently been excited to try out Hyrox. I came across someones post on Kaggle.com on how to scrape the data from the Hyrox website - I will credit this person and code.

I am taking the opportunity to use and tweak existing code to help learn more about webscraping and therefore extraction, whilst also building on my transformation, cleaning and loading skills.

## Project Timeline (I will update this as I go on)

Below you will see how to set up this project, the first time I did this it worked perfectly fine for my capstone project but I came across a problem and needed to delete the virtual environment, this results in breaking everything when I tried again and I had to run PYTHONPATH so the script folder was recognized. I have now fixed this problem, it was due to not modifying the setup.py file for my specific project. If anyone wants to use this or recreate this project, make sure to edit the setup.py file before going to initial project set guide below

I used the initial-project-setup branch to configure and fix this problem and eventually run_etl dev and run_tests all worked and I can now get onto using and tweaking the web-scraping code. I will be using web-scraping branches to complete this step.

Due to my inexperience with certain technologies, after an attempt to scrape through all different events and retrieve the ID, I gave up and went through manually to create a numbers file. I then converted this to a CSV and added it into my data/raw folder.

On the page (https://www.kaggle.com/code/jgug05/hyrox-data-scraping) that I will use the code for web-scraping there is a helper function that has all ID listed but not complete. I will use the CSV file and create a Class Event with all these listed - this will be then used within the web-scraping code to collect all data on these specific events by creating a URL with the correct details for each individual page.


## Initial project setup 


To get the ETL project structure on your machine:

1) Clone a clean copy of `https://github.com/de-2502-a/etl-project-demo.git`
2) Change into the project directory on the terminal and then execute the following commands:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-setup.txt
pip install -e .
```

3) Check the installation has worked by running the command `run_etl dev` - you should see:

```
Setting up environment...
Loading environment variables from: .env.dev
Environment setup complete.
ETL pipeline run successfully in dev environment!
```

4) Check the tests are set up correctly by running the command `run_tests all` - you should see:

```
Loading environment variables from: .env.test
============================================== test session starts ===============================================
platform darwin -- Python 3.12.2, pytest-8.3.5, pluggy-1.5.0 -- "Your path goes here"
cachedir: .pytest_cache
rootdir: "Your path goes here"
plugins: postgresql-7.0.1, mock-3.14.0, cov-6.1.1
collected 5 items                                                                                                

tests/unit_tests/test_db_config.py::test_load_db_config PASSED                                             [ 20%]
tests/unit_tests/test_db_config.py::test_load_db_config_missing_env_var_port_defaults PASSED               [ 40%]
tests/unit_tests/test_db_config.py::test_load_db_config_missing_env_var_errors[SOURCE_DB_NAME] PASSED      [ 60%]
tests/unit_tests/test_db_config.py::test_load_db_config_missing_env_var_errors[SOURCE_DB_USER] PASSED      [ 80%]
tests/unit_tests/test_db_config.py::test_load_db_config_missing_env_var_errors[SOURCE_DB_HOST] PASSED      [100%]

=============================================== 5 passed in 0.15s ================================================
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
config/db_config.py         18      0   100%
utils/logging_utils.py      19      0   100%
------------------------------------------------------
TOTAL                       37      0   100%
Running python linting checks
Running SQL linting checks
Python linting checks passed! 
SQL linting checks passed! All Finished!
```

## Hyrox webscraping

https://www.kaggle.com/code/jgug05/hyrox-data-scraping

The link above walks through how the code works and should be used. It also describes manually inputting each "Event ID" - this is something I want to change and allow the code to iterate through all events to collect all possible data for a larger analysis