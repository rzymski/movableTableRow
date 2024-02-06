from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    position = models.IntegerField()

    class Meta:
        required_db_features = {
            'supports_deferrable_unique_constraints',
        }
        constraints = [
            models.UniqueConstraint(
                fields=['position'],
                name='position_init_deferred_uniq',
                deferrable=models.Deferrable.DEFERRED,
            )]
