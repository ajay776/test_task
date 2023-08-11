from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255, null=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name +  ' - ' + self.worker.name


class Visit(models.Model):
    visit_date = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.unit.name +  ' - ' + self.unit.worker.name + ' - ' + str(self.visit_date)


