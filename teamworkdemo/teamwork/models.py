from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Member(models.Model):
    """
    personas que pueden crear formularios y resolverlos
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
        related_name='group_admin',
        on_delete=models.CASCADE
    )

    class Meta:
        # un cada miembro puede tener un equipo con el nombre que quiera
        unique_together = (('name', 'admin'),)


class Integrante(models.Model):
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


class BelbinUserProfile(models.Model):
    """
    formularios realizados
    """

    auth_user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    group_id = models.ForeignKey(
        Group,
        related_name='emited_by',
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField(
        default=timezone.now
    )

    # perfiles de belbin
    resource_investigator = models.IntegerField()
    team_worker = models.IntegerField()
    coordinator = models.IntegerField()
    plant = models.IntegerField()
    monitor_evaluator = models.IntegerField()
    specialist = models.IntegerField()
    shaper = models.IntegerField()
    implementer = models.IntegerField()
    completer_finisher = models.IntegerField()

    class Meta:
        ordering = ['-timestamp']
