from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# TODO: Buscar un nombre más descriptivo
class Profile(models.Model):
    """
    Esta clase permite agregar informacion adicional de los usuarios
    permite extender los perfiles sin modificar User
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


class Group(models.Model):
    """
    grupos a lo que pertenecen los miembros
    """
    name = models.CharField(
        max_length=200
    )

    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_admin'
    )

    class Meta:
        # permite que haya nombre repetidos mientras 
        # el administrador no sea el mismo
        
        unique_together = (
            ('name', 'admin'),
        )

# TODO: Buscar nu mejor nombre para esta clase
class Member(models.Model):
    """
    Relaciona los miembros con los grupos 
    """

    member = models.ForeignKey(
        User,
        related_name='group_member',
        on_delete=models.CASCADE
    )

    group = models.ForeignKey(
        Group,
        related_name='members',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            ('member', 'group'),
        )


class BelbinUserProfile(models.Model):
    """
    formularios realizados
    """

    integrante = models.OneToOneField(
        Member,
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField(
        default=timezone.now
    )

    # perfiles de belbin
    resource_investigator = models.IntegerField(default=0)
    team_worker = models.IntegerField(default=0)
    coordinator = models.IntegerField(default=0)
    plant = models.IntegerField(default=0)
    monitor_evaluator = models.IntegerField(default=0)
    specialist = models.IntegerField(default=0)
    shaper = models.IntegerField(default=0)
    implementer = models.IntegerField(default=0)
    completer_finisher = models.IntegerField(default=0)

    class Meta:
        ordering = ['-timestamp']
