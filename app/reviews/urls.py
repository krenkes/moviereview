from django.urls import path
from reviews import views as reviews_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', reviews_views.index.as_view(), name='home'),
    path('filter/', reviews_views.list_filtered_reviews.as_view(), name='filter'),
    path('api/reviews/', reviews_views.review_list),
    path('api/reviews/<int:pk>/', reviews_views.review_detail),
    path('api/reviews/filter/', reviews_views.review_list_filter)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
