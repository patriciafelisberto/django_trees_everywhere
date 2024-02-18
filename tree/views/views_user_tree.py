from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from tree.models import PlantedTree


@method_decorator(login_required, name='dispatch')
class UserTreesView(View):
    """
    Lists all trees planted by the authenticated user in JSON format.

    Returns an empty list if the user has not planted any trees.
    """
    def get(self, request):
        user_trees = PlantedTree.objects.filter(user=request.user).values()
        return JsonResponse(list(user_trees), safe=False)


