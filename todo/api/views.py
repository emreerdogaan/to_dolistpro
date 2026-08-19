import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from todo.models import Todo

def serialize_todo(todo):
    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description or '',
        'completed': todo.completed,
        'priority': todo.priority,
        'category': todo.category,
        'due_date': todo.due_date.strftime('%Y-%m-%d') if todo.due_date else None,
        'created_at': todo.created_at.isoformat(),
        'updated_at': todo.updated_at.isoformat(),
    }

@csrf_exempt
def todo_list_create_api(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        category = request.GET.get('category')
        priority = request.GET.get('priority')
        completed = request.GET.get('completed')
        
        if category and category != 'all':
            todos = todos.filter(category=category)
        if priority and priority != 'all':
            todos = todos.filter(priority=priority)
        if completed is not None and completed != 'all':
            completed_bool = completed.lower() == 'true'
            todos = todos.filter(completed=completed_bool)
            
        data = [serialize_todo(t) for t in todos]
        return JsonResponse(data, safe=False)
        
    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            title = body.get('title')
            if not title:
                return JsonResponse({'error': 'Title is required'}, status=400)
                
            due_date = body.get('due_date')
            if due_date == '':
                due_date = None
                
            todo = Todo.objects.create(
                title=title,
                description=body.get('description', ''),
                completed=body.get('completed', False),
                priority=body.get('priority', 'medium'),
                category=body.get('category', 'personal'),
                due_date=due_date
            )
            return JsonResponse(serialize_todo(todo), status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def todo_detail_update_delete_api(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'GET':
        return JsonResponse(serialize_todo(todo))
        
    elif request.method in ('PUT', 'PATCH'):
        try:
            body = json.loads(request.body)
            if 'title' in body:
                todo.title = body['title']
            if 'description' in body:
                todo.description = body['description']
            if 'completed' in body:
                todo.completed = body['completed']
            if 'priority' in body:
                todo.priority = body['priority']
            if 'category' in body:
                todo.category = body['category']
            if 'due_date' in body:
                due_date = body['due_date']
                todo.due_date = None if due_date == '' or due_date is None else due_date
                
            todo.save()
            return JsonResponse(serialize_todo(todo))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'message': 'Todo deleted successfully'}, status=200)
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)
