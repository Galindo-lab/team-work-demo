from django.db import models

# Create your models here.


class BelbinQuestionary(models.Model):
    """
    Esta clase contiene los resultados de las secciones del 
    cuestionario completo y su tiempo de captura 
    """

    creation_datetime = models.DateTimeField(auto_now_add=True)
    
    

class BelbinSection(models.Model):
    """
    Modelo para representar los resultados de una seccion del 
    formulario Belbin

    Attributes
    ----------
    sh : models.IntegerField 
        Shaper - Impulsor

    imp : models.IntegerField  
        Implementer - Implementador

    cf : models.IntegerField  
        Completer-Finisher - Finalizador

    co : models.IntegerField  
        Coordinator - Coordinador

    tw : models.IntegerField  
        Team Worker - Cohesionador

    ri : models.IntegerField  
        Resource Inv. - Investigador

    pl : models.IntegerField  
        Plant - Cerebro

    me : models.IntegerField  
        Monitor-Evaluator - Monitor-eva

    sp : models.IntegerField  
        Specialist - Especialista
    """

    questionary = models.ForeignKey(
        BelbinQuestionary,
        on_delete=models.CASCADE,
        related_name="questionary",
        null=True,
        blank=True,
    )

    sh = models.IntegerField(default=0)
    imp = models.IntegerField(default=0)
    cf = models.IntegerField(default=0)
    co = models.IntegerField(default=0)
    tw = models.IntegerField(default=0)
    ri = models.IntegerField(default=0)
    pl = models.IntegerField(default=0)
    me = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
