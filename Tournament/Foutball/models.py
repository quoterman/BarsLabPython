from django.db import models

class Comand(models.Model):
    comand_id = models.AutoField(primary_key=True)
    comand_name = models.CharField(max_length=30)
    comand_kolPlays = models.IntegerField()
    comand_score = models.IntegerField()
    comand_goals = models.IntegerField()
    comand_missed = models.IntegerField()
    comand_wins = models.IntegerField()
    comand_loss = models.IntegerField()
    comand_draw = models.IntegerField()
    def __unicode__(self):
        return self.comand_name

class Match(models.Model):
    match_comand1 = models.ForeignKey(Comand, to_field='comand_id', related_name='foo')
    match_comand2 = models.ForeignKey(Comand, to_field='comand_id', related_name='foo2')
    match_result = models.IntegerField()
    match_date = models.DateField()