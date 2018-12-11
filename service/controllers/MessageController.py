from service.schemas import EmailSchema, MessageSchema

def saveMessage(request):
    json_data = request.get_json()
    if not json_data:
        return 'No input data provided')

