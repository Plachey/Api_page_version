from django.urls import path
from .views import ArticleView,\
                   SingleConcretArticleView,\
                   ListConcretArticleView,\
                   SingleTrueConcretArticleView,\
                   ArticleUpdate,\
                   ArticleMaineTrue


urlpatterns = [
    path('articles/', ArticleView().as_view()),
    path('articles/<int:article_id>/', ListConcretArticleView.as_view()),
    path('articles/version/<int:version>/', SingleConcretArticleView.as_view()),
    path('articles/current/<int:article_id>/<str:flag>/', SingleTrueConcretArticleView.as_view()),
    path('articles/update/<int:article_id>/', ArticleUpdate.as_view()),
    path('articles/current_set/<int:article_id>/<int:version>/', ArticleMaineTrue.as_view()),
]
