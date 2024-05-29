from django.http import JsonResponse
from celery.result import AsyncResult
from celery_task.task import add

def add_view(request):
    # Trigger the task
    
    # task = add.delay(2, 3)
    task = add.apply_async((62, 55), countdown=60)
    # Get the task ID
    task_id = task.id

    return JsonResponse({'status': 'Task added', 'task_id': task_id})


def check_task_status(request, task_id):
    # Fetch the task result using the task ID
    task_result = AsyncResult(task_id)
    if task_result.state == 'PENDING':
        response = {'status': 'Pending'}
    elif task_result.state == 'SUCCESS':
        response = {
            'status': 'Success',
            'result': task_result.result
        }
    elif task_result.state == 'FAILURE':
        response = {
            'status': 'Failure',
            'result': str(task_result.result)
        }
    else:
        response = {'status': 'Unknown'}

    return JsonResponse(response)
