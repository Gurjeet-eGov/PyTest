# PyTest

Run test with generate report 
    pytest --alluredir=allure-results
    pytest -s --alluredir=reports/allure-results-$(date +%Y%m%d_%H%M%S)


Generate static html reports 
    allure generate allure-results -o allure-report --clean

View directly on server 
    allure serve allure-results
