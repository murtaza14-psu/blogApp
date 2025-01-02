from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'products/')
    #auto_now_add stores the timestamp when the object is crseated
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now stores the timestamp when the object is saved everytime
    updated_at = models.DateTimeField(auto_now=True)
    
    #if i print a complete object the output will only be the name
    #for this the __str__is used
    def __str__(self):
        return self.name
    
    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()

    def short_description(self):

        words = self.description.split()
        #if the text has more than 30 words, take the first 30 and 
        # add .... in the end
        if len(words)>30:
            return " ". join(words[:30]) + "....."
        else:
            return self.description