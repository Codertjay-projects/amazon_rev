import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amazon_rev.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

import gzip
import json

import wget
from celery import shared_task

from core.bot import AmazonBotAutomation
from core.models import Product, Category

file_download_path = "./downloads"


@shared_task
def run_automation_bot():
    bot = AmazonBotAutomation(teardown=True)
    bot.land_page()
    urls = bot.download_all_reviews()
    # deleting all products to prevent us from creating it again
    Product.objects.all().delete()
    for item in urls:
        filename = wget.download(item,
                                 out=file_download_path)

        create_amazon_products.delay(filename)


@shared_task
def create_amazon_products(filename):
    try:
        #  creating a name which could be used for the product Example meta_Computers
        name = filename.split("/")[2].split(".")[0]
    except:
        #  if there is an error we use this to create the name  Example: meta_Computersjsongz
        name = filename.split("/")[:-1].replace(".", "")
    #  i literally could use get_or_create, but sometimes it returns an error
    category = Category.objects.filter(name=name).first()
    if not category:
        category = Category.objects.create(name=name)

    #  create the product
    #  unzipping the file and also opening it at once
    with gzip.open(filename, 'r') as f:
        counter = 0
        #  looping though the file to create a product
        for l in f:
            counter += 1
            # creating a variable to be used to create products
            json_data = json.loads(l.strip())
            images = json_data.get('image', None),
            description = json_data.get('description', None),
            name = json_data.get('title', None),
            tag = json_data.get('main_cat', None),
            rank = json_data.get('rank', None),
            date = json_data.get('date', None),
            brand = json_data.get('brand', None),
            try:
                #  creating the product
                Product.objects.create(
                    images=images,
                    description=description,
                    name=name,
                    tag=tag,
                    rank=rank,
                    date=date,
                    brand=brand,
                    category=category)
            except Exception as a:
                #  an error occurred
                print(a)
    # deleting the downloaded file
    os.remove(filename)
    print("Deleted the gzip.json file downloaded")


"""
"""
run_automation_bot()
