def handler(event, context):
    text = 'Привет! Давай сыграем в "Остров Сокровищ." Рассказать правила?'
    if 'request' in event and 'original_utterance' in event['request'] and len(event['request']['original_utterance']) > 0:
        text = event['request']['original_utterance']
    response = {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': 'false'
        },
    }
    return response

