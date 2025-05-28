from django.db import models

class reading_level(models.Model):
    level_id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=200, default="MyLevel-default")
    minimum_age = models.IntegerField()
    maximum_age = models.IntegerField()

    def __str__(self):
        #return self.level_id, self.level_name, self.minimum_age, self.maximum_age
        return self.level_name


class reading_prompt(models.Model):
    pid = models.IntegerField()
    prompt_body = models.CharField(max_length=200, default="Not Poulated")
    level_id = models.IntegerField()
    prompt_type = models.CharField(max_length=200, default="Not Poulated")

    def __str__(self):
        #return self.pid, self.prompt_body, self.level_id, self.prompt_type
        return self.prompt_body
