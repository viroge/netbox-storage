from django.db import models
from django.urls import reverse
from django.db.models import Sum
from netbox.models import NetBoxModel


class StoragePool(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    size = models.PositiveBigIntegerField(
        help_text='Size in bytes'
    )
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


class LUN(NetBoxModel):
    storage_pool = models.ForeignKey(
        to=StoragePool,
        on_delete=models.PROTECT,
        related_name='luns'
    )
    name = models.CharField(
        max_length=100
    )
    size = models.PositiveBigIntegerField(
        help_text='Size in bytes'
    )
    description = models.TextField(
        blank=True
    )
    wwn = models.CharField(
        max_length=64,
        blank=True,
        verbose_name='WWN'
    )

    class Meta:
        ordering = ('name',)
        unique_together = ('storage_pool', 'name')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage:lun', args=[self.pk])


class Datastore(NetBoxModel):
    lun = models.ManyToManyField(
        to=LUN,
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
        return reverse('plugins:netbox_storage:datastore', args=[self.pk])

    def get_utilization(self):
        sum_lun_size = self.lun.all().aggregate(Sum('size'))['size__sum']
        sum_vmdk_size = self.vmdks.all().aggregate(Sum('size'))['size__sum']
        if sum_lun_size and sum_vmdk_size:
            utilization = float(sum_vmdk_size) / float(sum_lun_size) * 100
        else:
            utilization = 0

        return min(utilization, 100)


class StorageSession(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    cluster = models.ForeignKey(
        to='virtualization.cluster',
        on_delete=models.PROTECT,
        related_name='storage_sessions'
    )
    datastores = models.ManyToManyField(
        to=Datastore,
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


class VMDK(NetBoxModel):
    vm = models.ForeignKey(
        to='virtualization.virtualmachine',
        on_delete=models.PROTECT,
        related_name='vmdks'
    )
    name = models.CharField(
        max_length=100
    )
    datastore = models.ForeignKey(
        to=Datastore,
        related_name='vmdks',
        on_delete=models.PROTECT
    )
    size = models.PositiveBigIntegerField(
        help_text='Size in bytes'
    )

    class Meta:
        ordering = ('datastore', 'name',)

    def __str__(self):
        return f'{self.vm}-{self.datastore}-{self.name}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage:vmdk', args=[self.pk])
