import logging,json
from response import buildResponse

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event,context):
    print("event",event)
    return buildResponse(200,{"status":"success","message":"api is working ok!"})