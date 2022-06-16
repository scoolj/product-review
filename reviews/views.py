from .models import Image
from .serializers import ImageSerializer, ProductSerializer
from .models import Product
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny


# Create your views here.




class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class =ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]


class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ProductViewSet(ReadOnlyModelViewSet):

    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
    filterset_fields = ('category',)


    def get_queryset(self):
        queryset = Product.objects.all()


        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        if is_expanded(self.request, 'sites'):
            queryset = queryset.prefetch_related('sites')

        if is_expanded(self.request, 'company'):
            queryset = queryset.prefetch_related('sites__company')

        if is_expanded(self.request, 'productsize'):
            queryset = queryset.prefetch_related('sites__productsize')

        return queryset
