from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)      

    def __str__(self):
        return self.name

class Publication(models.Model):
    name = models.CharField(max_length=100)
    date_of_establishment = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ISBN = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField()
    publisher = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='covers/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    @property
    def is_in_stock(self):
        return self.stock > 0

    def decrease_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Insufficient stock")
        
    def __str__(self):
        return self.title
