from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from tree.models import PlantedTree


@method_decorator(login_required, name='dispatch')
class AccountTreesView(View):
    """
    Lists all trees planted in accounts associated with the authenticated user.

    Trees are filtered through accounts related to the user via planted trees.
    Returns the trees in JSON format, including trees from all associated accounts.
    """
    def get(self, request):
        user_trees = PlantedTree.objects.filter(user=request.user)
        
        accounts_ids = user_trees.values_list('account', flat=True).distinct()
        
        trees_in_user_accounts = PlantedTree.objects.filter(account__id__in=accounts_ids).values()
        
        return JsonResponse(list(trees_in_user_accounts), safe=False)

