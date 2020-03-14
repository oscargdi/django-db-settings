from django.db import models

# Abstract models


class AuditModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Settings models


class Setting(AuditModel, ActiveModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Field(AuditModel, ActiveModel):
    public = models.BooleanField(default=True)
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('setting', 'name',)
        ordering = ('setting__name', 'name',)

    def __str__(self):
        return '{}.{}'.format(self.setting.name, self.name)


class Instance(AuditModel, ActiveModel):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('setting', 'name',)
        ordering = ('setting__name', 'name',)

    def __str__(self):
        return '{} > {}'.format(self.setting.name, self.name)


class Value(AuditModel):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    class Meta:
        unique_together = ('field', 'instance',)

    def __str__(self):
        return self.value
