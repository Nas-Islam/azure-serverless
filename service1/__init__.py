import logging
import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    strletters = requests.get('https://nasservices.azurewebsites.net/api/service2?code=Zx0L/ycKO7OYPYR0l6g2ax3qbAk2k8hZg9fafqv0wW4mtuHqaE3yAw==')
    numbers = requests.get('https://nasservices.azurewebsites.net/api/service3?code=yLMcCWqiuTiSCZV128M1izMaRo9V3jXmFHJvUnxtxdzMQSLsq7XLvw==')
    infoletters = strletters.text
    infonumbers = numbers.text
    combined = ''
    for i in range(5):
        combined+=infoletters[i]+infonumbers[i]
    return func.HttpResponse(str(combined),status_code=200)
