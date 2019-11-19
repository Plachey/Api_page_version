from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView

from .models import Article
from .serializers import ArticleSerializer, ArticleUpdateSerializer, ArticleCurrentSerializer


# 1) getting list pages
class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        return serializer.save()


# 2) getting list pages version
class ListConcretArticleView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        identifier = self.kwargs['article_id']
        return Article.objects.filter(article_id=identifier)


# 3) getting a single page version
class SingleConcretArticleView(RetrieveAPIView):
    serializer_class = ArticleSerializer

    def get_object(self):
        obj = Article.objects.get(version=self.kwargs['version'])
        return obj


# 4) getting a current single page version
class SingleTrueConcretArticleView(RetrieveAPIView):
    serializer_class = ArticleSerializer

    def get_object(self):
        obj = Article.objects.get(article_id=self.kwargs['article_id'], flag_default=self.kwargs['flag'])
        return obj


# 5) editing page
class ArticleUpdate(CreateAPIView):
    serializer_class = ArticleUpdateSerializer

    def perform_create(self, serializer):
        identifier = self.kwargs['article_id']
        Article.objects.filter(article_id=identifier).update(flag_default=False)
        return serializer.save()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "article_id": self.kwargs['article_id']
        })
        return context


# 6) to do any version pages current
class ArticleMaineTrue(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCurrentSerializer
    lookup_field = 'version'

    def put(self, request, *args, **kwargs):
        identifier = self.kwargs['article_id']
        Article.objects.filter(article_id=identifier).update(flag_default=False)
        return self.update(request, *args, **kwargs)
