from django.db import models

# Create your models here.
class Prediccion(models.Model):
    home_team = models.CharField(max_length=50, blank=False)
    home_team_score = models.IntegerField()
    away_team = models.CharField(max_length=50, blank=False)
    away_team_score = models.IntegerField()


    class Meta:
        verbose_name = ('Prediccion')
        verbose_name_plural = ('Predicciones')

    def __unicode__(self):
        return "%s(%d) - %s(%d)" % (self.home_team, self.home_team_score,
                                    self.away_team, self.away_team_score)

    