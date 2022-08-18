from celery import shared_task

from .models import Product
import json
import os
import os
import json
import gzip
import pandas as pd
from urllib.request import urlopen

import wget

def run_automation_bot():



@shared_task
def create_amazon_products(json_file):
    with gzip.open(json_file, 'r') as f:
        counter = 0
        for l in f:
            counter += 1
            #  appending the data to our serializer data
            json_data = json.loads(l.strip())
            images = json_data.get('image', None),
            description = json_data.get('description', None),
            name = json_data.get('title', None),
            tag = json_data.get('main_cat', None),
            rank = json_data.get('rank', None),
            try:
                Product.objects.create(images=images, description=description, name=name, tag=tag, rank=rank)
            except Exception as a:
                print(a)
    print("Deleting the json file downloaded")
