from django.urls import path
from.import views

urlpatterns = [
    path('', views.PostList.as_view(), name='list' ),
    path('create/', views.CreatePost.as_view(), name='create' ),
    path('<pk>', views.Retrieve.as_view(), name='read' ),
    path('<pk>/update/', views.Update.as_view(), name='update' ),
    path('<pk>/delete/', views.Delete.as_view(), name='delete' ),
    
    
    
    
]
