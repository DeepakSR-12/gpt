import json
import time
import random
import string

from rest_framework import response, status
from rest_framework.decorators import api_view
from g4f import ChatCompletion

@api_view(["POST"])
def chat(request):
    request_data = json.loads(request.body.decode('utf-8'))
    model    = request_data.get('model', 'gpt-3.5-turbo')
    stream   = request_data.get('stream', False)
    messages = request_data.get('messages')

    # Trigger a chat completion
    completion_data = ChatCompletion.create(model = model, stream = stream, messages = messages)

    completion_id = ''.join(random.choices(string.ascii_letters + string.digits, k=28))
    completion_timestamp = int(time.time())

    response_data = {
        'id': f'chatcmpl-{completion_id}',
        'object': 'chat.completion',
        'created': completion_timestamp,
        'model': model,
        'content': completion_data,
    }
     
    return response.Response(status=status.HTTP_200_OK, data=response_data)
