from django.urls import path, include
from photographyapp import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('shop/<int:book_id>', views.detail, name='detail'),

    path('', views.item1, name='item1'),
    path('item/<int:shop_id>', views.item2, name='item2'),

# ADD product

    path('add/',views.add_product,name='add_product'),

    # update

    path('update/<int:id>',views.update,name='update'),

# delete

    path('delete/<int:id>', views.delete, name='delete')

]


