from django.db import models


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    trik = models.BooleanField(default=True)
    yosh = models.PositiveSmallIntegerField()
    Kitoblar_soni = models.PositiveSmallIntegerField(blank=True)
    def __str__ (self):
        return self.ism

class Kitob(models.Model):
    J = (
        ('1',"Fantastik"),
        ('2',"Detiktiv"),
        ('3',"Badiiy"),
        ('4',"Ilmiy")
        )
    nom = models.CharField(max_length=50)
    sana = models.DateField(blank=True)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30, choices=J)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE, related_name="m_kitoblari")
    def __str__(self):
        return self.nom
    class Meta:
        ordering = ("ism",)

class Student(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=30,blank=True)
    k_soni = models.PositiveSmallIntegerField(default=0)
    bitiruvchi = models.BooleanField(default=False)
    def __str__(self):
        return self.ism
    class Meta:
        ordering = ("nom",)


class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    qaytardi = models.CharField(max_length=5, blank=True, default="Yo'q")
    qaytarish_sans = models.DateField(blank=True, null=True)
    def __str__(self):
        return f"{self.kitob} ({self.student})"


class Printer(models.Model):
    turi = models.CharField(max_length=30)
    narxi = models.PositiveSmallIntegerField()
    rangli = models.BooleanField()
    yangi = models.BooleanField()
    def __str__(self):
        return self.turi



class Pc(models.Model):
    turi = models.CharField(max_length=30)
    narxi = models.PositiveSmallIntegerField()
    tezkor_xotirasi = models.BooleanField()
    chiqrilgan_sanasi = models.DateField()
    def __str__(self):
        return self.turi


class Telefon(models.Model):
    nomi = models.CharField(max_length=30)
    modeli = models.CharField(max_length=30)
    narxi = models.PositiveSmallIntegerField
    sanasi = models.DateField()
    def __str__(self):
        return self.nomi



