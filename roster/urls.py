from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView


app_name = 'roster'
urlpatterns = [
    # 一覧画面
    path('', ItemFilterView.as_view(), name='index'),
    # 詳細画面
    path('item_detail/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    # 登録画面
    path('item_create/', ItemCreateView.as_view(), name='item_create'),
    # 更新画面
    path('item_update/<int:pk>/', ItemUpdateView.as_view(), name='item_update'),
    # 削除画面
    path('item_delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
]
