from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Review.objects.all()
    return render(request, "reviews/index.html", {'reviews': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'reviews/index.html'

    def get(self, request):
        queryset = Review.objects.all()
        return Response({'reviews': queryset})

    def post(self, request):
        queryset = Review.objects.all()
        return Response({'reviews': queryset})


class list_all_reviews(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'reviews/review_list.html'

    def get(self, request):
        queryset = Review.objects.all()
        return Response({'reviews': queryset})

# class list_filtered_reviews(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'reviews/review_list.html'

#     def get(self, request):
#         queryset = Review.objects.filter(industry_rating= "PG")
#         return Response({'reviews': queryset})

@api_view(['GET', 'POST', 'DELETE'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            reviews= reviews.filter(title__icontains=title)

        reviews_serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(reviews_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        review_data = JSONParser().parse(request)
        review_serializer = ReviewSerializer(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse(review_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(review_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Review.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Reviews were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        review_serializer = ReviewSerializer(review)
        return JsonResponse(review_serializer.data)

    elif request.method == 'PUT':
        review_data = JSONParser().parse(request)
        review_serializer = ReviewSerializer(review, data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse(review_serializer.data)
        return JsonResponse(review_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return JsonResponse({'message': 'Review was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_list_filter(request):
    review_data = JSONParser().parse(request)
    return JsonResponse(review_data, safe=False)
    # print(review_data)
    # reviews = Review.objects.all()
    # reviews = reviews.filter(industry_rating = review_data[reviewsindustry_rating])

    # if request.method == 'GET':
    #     review_serializer = ReviewSerializer(reviews, many=True)
    #     return JsonResponse(review_serializer.data, safe=False)