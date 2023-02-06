from django.db import models
from django.urls import reverse
from django.db.models import Sum
from netbox.models import NetBoxModel


class StoragePool(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    size = models.PositiveIntegerField()
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT
    )
    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage:storagepool', args=[self.pk])

    def get_utilization(self):
        sum_alloc_size = self.luns.all().aggregate(Sum('size'))['size__sum']
        if sum_alloc_size:
            utilization = float(sum_alloc_size) / self.size * 100
        else:
            utilization = 0

        return min(utilization, 100)


class StorageLUN(NetBoxModel):
    storage_pool = models.ForeignKey(
        to=StoragePool,
        on_delete=models.PROTECT,
        related_name='luns'
    )
    name = models.CharField(
        max_length=100
    )
    size = models.PositiveIntegerField()
    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)
        unique_together = ('storage_pool', 'name')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage:storagelun', args=[self.pk])


class StorageLUNGroup(NetBoxModel):
    storage_lun = models.ManyToManyField(
        to=StorageLUN,
        related_name='lun_groups'
    )
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage:storagelungroup', args=[self.pk])


class StorageSession(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    cluster = models.ForeignKey(
        to='virtualization.cluster',
        on_delete=models.PROTECT,
        related_name='storage_sessions'
    )
    storage_lun_groups = models.ManyToManyField(
        to=StorageLUNGroup,
        related_name='storage_sessions'
    )
    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage:storagesession', args=[self.pk])
