from django.db import models

class reading_level(models.Model):
    level_id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=20000, default="")
    age_min = models.IntegerField(db_column='age_min', default=0)
    age_max = models.IntegerField(db_column='age_max', default=100)

    def __str__(self):
        return self.text


class reading_prompt(models.Model):
    prompt_id = models.IntegerField(db_column='prompt_id', default=10)
    prompt_body = models.CharField(max_length=20000, default="Not Poulated")
    level_id = models.ForeignKey(reading_level, on_delete=models.CASCADE)
    prompt_type = models.CharField(max_length=20000, default="Not Poulated")

    def __str__(self):
        return self.text

