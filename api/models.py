from django.db import models

class UrineStripImage(models.Model):
    image = models.ImageField(upload_to='urine_strips/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
