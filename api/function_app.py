import azure.functions as func
import logging
import json
from datetime import datetime

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="message")
def message(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            json.dumps({ 
                "message": f"Hello, {name}. This HTTP triggered function executed successfully." 
            })
        )
    else:
        return func.HttpResponse(
             json.dumps({ "message": f"{datetime.now()} => This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response." }),
             status_code=200
        )

@app.route(route="htptriger", auth_level=func.AuthLevel.ANONYMOUS)
def htptriger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"{datetime.now()} => This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )