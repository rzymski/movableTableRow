from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    position = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.position:
            max_position = Product.objects.aggregate(models.Max('position'))['position__max']
            self.position = max_position + 1 if max_position is not None else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} {self.name} p={self.price} q={self.quantity} position={self.position}"

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
