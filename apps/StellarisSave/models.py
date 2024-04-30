from django.db import models

from apps.user.models import User


# planet
class PlanetType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="description", null=False, blank=False)
    image = models.ImageField(upload_to='static/images/stellaris/planet/')
    type = models.ForeignKey(PlanetType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Background
class Background(models.Model):
    image = models.ImageField(upload_to='static/images/stellaris/background/', null=False, blank=False)


# IconFlag
class FlagType(models.Model):
    name = models.CharField(max_length=100)


class Flag(models.Model):
    image = models.ImageField(upload_to='static/images/stellaris/Flag/', null=False, blank=False)
    type = models.ForeignKey(FlagType, on_delete=models.CASCADE)


# Race
class RaceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/stellaris/race/', null=False, blank=False)
    type = models.ForeignKey(to=RaceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Ship
class ShipType(models.Model):
    image = models.ImageField(upload_to='static/images/stellaris/ship/', null=False, blank=False)


# Origin
class Origin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="description")
    image = models.ImageField(upload_to='static/images/stellaris/origin/', null=False, blank=False)
    effect = models.TextField(default="effect", null=False, blank=False)
    requirement = models.TextField(default="requirement", null=False, blank=False)

    def __str__(self):
        return self.name


# Government
class Government(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="description")
    image = models.ImageField(upload_to='static/images/stellaris/government/', null=False, blank=False)
    effect = models.TextField(default="effect", null=False, blank=False)
    requirement = models.TextField(default="requirement", null=False, blank=False)

    def __str__(self):
        return self.name


# Civic
class Civic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="description")
    image = models.ImageField(upload_to='static/images/stellaris/civic/', null=False, blank=False)
    effect = models.TextField(default="effect", null=False, blank=False)
    requirement = models.TextField(default="requirement", null=False, blank=False)

    def __str__(self):
        return self.name


# Ethics
class Ethic(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/stellaris/ethic/', null=False, blank=False)
    description = models.TextField(default="description", )
    effect = models.TextField(default="effect", )
    cost = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# Gene
class Gene(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="description")
    image = models.ImageField(upload_to='static/images/stellaris/gene/', )
    effect = models.TextField(default="effect", null=False, blank=False)
    requirement = models.TextField(default="requirement", null=False, blank=False)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# color
class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color


# Save

class StellarisSave(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="My Empire", null=False, blank=False)

    backgroundId = models.ForeignKey(Background, on_delete=models.CASCADE)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
    colorPrimaryAndSecondary = models.CharField(max_length=50)  # [1,2,3,4]

    planetName = models.CharField(max_length=100)
    planetId = models.ForeignKey(Planet, on_delete=models.CASCADE)

    raceName = models.CharField(max_length=100)
    raceType = models.ForeignKey(RaceType, on_delete=models.CASCADE)

    shipType = models.ForeignKey(ShipType, on_delete=models.CASCADE)

    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    government = models.ForeignKey(Government, on_delete=models.CASCADE)
    ethic = models.CharField(max_length=100, null=False, blank=False)  # [1,2,3,4]
    civic = models.CharField(max_length=100)  # [1,2,3,4]
    gene = models.CharField(max_length=100)  # [1,2,3,4]

    def __str__(self):
        return f"{self.user_id.username}'s {self.name}"
