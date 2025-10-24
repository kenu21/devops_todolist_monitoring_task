from django.http import HttpResponse
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST


GET_COUNTER = Counter('todo_get_requests_total', 'Total GET requests')
POST_COUNTER = Counter('todo_post_requests_total', 'Total POST requests')

def metrics(request):
    if request.method == 'GET':
        GET_COUNTER.inc()
    elif request.method == 'POST':
        POST_COUNTER.inc()

    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)
