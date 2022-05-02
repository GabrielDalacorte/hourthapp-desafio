from django.db import models

# Create your models here.


class HourthApp(models.Model):
    product = models.FileField('products/')
    insertion_date = models.DateField(auto_now_add=True)

    @property
    def generic_function_sum(self):

        dict_sum = {}
        dict_sum.update({self.insertion_date: {'products': []}})

        dict_sum[self.insertion_date]['products'].append(self.product)

        for data, products in dict_sum.items():
            sum_tables = {
                'competence': data,
                'sum': len(products['products'])
            }
            return sum_tables
