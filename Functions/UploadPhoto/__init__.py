import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    body = req.get_body();

    logging.info(f'Received body, length {len(body)}')

    f = open('./photo.jpg', 'wb')
    f.write(body)
    f.close()

    return func.HttpResponse("OK", status_code=200)
