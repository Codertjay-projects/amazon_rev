# Create your views here.
import json
import os

from rest_framework.generics import ListAPIView

from core.serializers import ProductSerializer, CategorySerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        data = []
        for item in os.listdir("C:\\Users\\Codertjay\\PycharmProjects\\amazon_rev\\json_files"):
            if item.endswith(".json"):
                data.append({"url": item})
        return data


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    lookup_field = "slug"

    def get_queryset(self, *args, **kwargs):
        #  getting the slug and add json to match file path
        slug = f'{self.kwargs.get("slug")}.json'
        PAGE_SIZE = 50
        if self.request.query_params.get("page_count"):
            PAGE_SIZE = int(self.request.query_params.get("page_count"))
        data = []
        for file in os.listdir("C:\\Users\\Codertjay\\PycharmProjects\\amazon_rev\\json_files"):
            # Check whether file is in text format or not
            if file.lower() == slug.lower():
                #  opening the folder in which the json files are
                with open(f'C:\\Users\\Codertjay\\PycharmProjects\\amazon_rev\\json_files\\{file}', 'r') as f:
                    counter = 0
                    try:
                        for l in f:
                            counter += 1
                            #  appending the data to our serializer data
                            json_data = json.loads(l.strip())
                            print(json_data)
                            data.append({
                                "images": json_data.get('image', None),
                                "description": json_data.get('description', None),
                                "name": json_data.get('title', None),
                                "tag": json_data.get('main_cat', None),
                                "rank": json_data.get('rank', None),
                            })
                            if counter == PAGE_SIZE:
                                break
                    except:
                        return []
        return data
