import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from tree.models import PlantedTree, Tree, Account


@method_decorator(login_required, name='dispatch')
class AddTreeView(View):
    """
    Allows adding a new planted tree through a POST request.

    Tree data, including `tree_id`, `location`, `age`, and `account_id`, are provided
    in the request body in JSON format. Returns a success message with the ID of the
    added tree or an error in case of invalid data or failure to add.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
            tree_id = data.get('tree_id')
            location = data.get('location')
            age = data.get('age')
            account_id = data.get('account_id')

            try:
                tree = Tree.objects.get(id=tree_id)
                account = Account.objects.get(id=account_id)

            except (Tree.DoesNotExist, Account.DoesNotExist) as e:
                return JsonResponse({'error': str(e)}, status=400)
            
            planted_tree = PlantedTree.objects.create(
                user=request.user,
                tree=tree,
                location=location,
                age=age,
                account=account
            )

            return JsonResponse({'message': 'Tree added successfully', 'id': planted_tree.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid Input'}, status=400)
