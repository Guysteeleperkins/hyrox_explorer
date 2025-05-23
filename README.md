# Hyrox Results Explorer

# Initial project setup 



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