from django.http import JsonResponse, Http404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from tree.models import PlantedTree


@method_decorator(login_required, name='dispatch')
class TreeDetailView(View):
    """
    Returns the details of a specific planted tree in JSON format.

    The tree is identified by the `tree_id` provided in the URL. Only the user who planted
    the tree can access its details. Returns a 404 error if the tree is not found,
    or a 403 error if the tree does not belong to the authenticated user.
    """
    def get(self, request, tree_id):
        try:
            tree = PlantedTree.objects.get(id=tree_id)  
            if tree.user != request.user:
                # If the tree does not belong to the user, return a 403 Forbidden error
                return JsonResponse({'error': 'Forbidden: You cannot access details of this tree as it was planted by another user.'}, status=403)
            else:
                # If the tree belongs to the user, return the tree details
                return JsonResponse({'tree': {
                    'id': tree.id,
                    'user': tree.user.username,  
                    'location': tree.location,
                    'age': tree.age,
                    'planted_at': tree.planted_at,
                    'account': tree.account.id  
                }})
        except PlantedTree.DoesNotExist:
            return JsonResponse({'error': 'Tree not found'}, status=404)
