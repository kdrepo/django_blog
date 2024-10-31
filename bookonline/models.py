from django.db import models

# Create your models here.


class B1book(models.Model):
    bookTitle = models.CharField(max_length=200, null=True, blank=True)
    bookAuthor = models.CharField(max_length=200, null=True, blank=True)
    bookprice = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.bookTitle


class B1chapter(models.Model):
    chapTitle = models.CharField(max_length=200, null=True, blank=True)
    chapVolume = models.CharField(max_length=200, null=True, blank=True)
    book = models.ForeignKey(B1book, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapVolume


class B1subhead(models.Model):
    subheads = models.CharField(max_length=500, null=True, blank=True)
    chapvolume = models.ForeignKey(B1chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.subheads


class B1pera(models.Model):
    peratext = models.TextField(max_length=50000, null=True, blank=True)
    subhead = models.ForeignKey(B1subhead, on_delete=models.CASCADE)

    def __str__(self):
        return self.peratext[:150]

# class B1pages(models.Model):
#     pageNO = models.FloatField(null=True, blank=True)
#     peragraphs = models.ForeignKey(B1pera, on_delete=models.CASCADE)


class Books(models.Model):
    bookTitle = models.CharField(max_length=200, null=True, blank=True)
    bookAuthor = models.CharField(max_length=200, null=True, blank=True)
    bookprice = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.bookTitle


class B2chapter(models.Model):
    chapTitle = models.CharField(max_length=200, null=True, blank=True)
    titletext = models.TextField(max_length=100000, null=True, blank=True)
    Books = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapTitle


class B2subhead1(models.Model):
    subhead1titles = models.CharField(max_length=500, null=True, blank=True)
    subhead1text = models.TextField(max_length=100000, null=True, blank=True)
    B2chapter = models.ForeignKey(B2chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.subhead1titles


class B2subhead2(models.Model):
    subhead2titles = models.CharField(max_length=500, null=True, blank=True)
    subhead2text = models.TextField(max_length=100000, null=True, blank=True)
    B2subhead1 = models.ForeignKey(B2subhead1, on_delete=models.CASCADE)

    def __str__(self):
        return self.subhead2titles


class Aindex(models.Model):
    words = models.CharField(max_length=500, null=True, blank=True)
    linklen = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.words


class Bindex(models.Model):
    words = models.CharField(max_length=500, null=True, blank=True)
    linklen = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.words


class Cindex(models.Model):
    words = models.CharField(max_length=500, null=True, blank=True)
    linklen = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.words


class Aurl(models.Model):
    url = models.CharField(max_length=500, null=True, blank=True)
    urltext = models.CharField(max_length=500, null=True, blank=True)
    word = models.ForeignKey(Aindex, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Burl(models.Model):
    url = models.CharField(max_length=500, null=True, blank=True)
    urltext = models.CharField(max_length=500, null=True, blank=True)
    word = models.ForeignKey(Bindex, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Curl(models.Model):
    url = models.CharField(max_length=500, null=True, blank=True)
    urltext = models.CharField(max_length=500, null=True, blank=True)
    word = models.ForeignKey(Cindex, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
