# PyTest

Run test with generate report 
pytest --alluredir=allure-results


Generate static html reports 
allure generate allure-results -o allure-report --clean

View directly on server 
allure serve allure-results
