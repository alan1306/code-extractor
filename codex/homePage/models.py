from django.db import models
import numpy as np 
from PIL import Image
from .utils import getFiltered
class Images(models.Model):
    image=models.ImageField(upload_to='user')
