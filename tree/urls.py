from django.urls import path

from tree.views import (
    AccountTreesView,
    AddTreeView, 
    TreeDetailView, 
    UserTreesView, 
)


urlpatterns = [
    path('user/trees/', UserTreesView.as_view(), name='view_user_trees'),
    path('tree/<int:tree_id>/', TreeDetailView.as_view(), name='planted_tree_detail'),
    path('tree/new/', AddTreeView.as_view(), name='add_planted_tree'),
    path('accounts/trees/', AccountTreesView.as_view(), name='trees_in_accounts'),
]
