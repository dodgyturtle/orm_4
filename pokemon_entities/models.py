from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField("Русское название покемона", max_length=200)
    title_en = models.CharField("Английское название покемона", max_length=200)
    title_jp = models.CharField("Японское название покемона", max_length=200)
    image = models.ImageField(
        "Изображение покемона", upload_to="pokemon_images", null=True, blank=True
    )
    description = models.TextField("Описание покемона")
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="next_evolutions",
        verbose_name="Из кого эволюционирует",
    )

    def __str__(self):
        return f"{self.title_ru}"

    def get_image(self, request, default_image_utl):
        return (
            request.build_absolute_uri(self.image.url)
            if self.image
            else default_image_utl
        )


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name="Покемон"
    )
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    appeared_at = models.DateTimeField("Время и дата появления", null=True, blank=True)
    disappeared_at = models.DateTimeField(
        "Время и дата исчезновения", null=True, blank=True
    )
    level = models.IntegerField("Уровень", default=0, )
    health = models.IntegerField("Здоровье", default=0)
    strength = models.IntegerField("Сила", default=0)
    defence = models.IntegerField("Защита", default=0)
    stamina = models.IntegerField("Выносливость", default=0)

    def __str__(self):
        return f"{self.pokemon.title_ru}_{self.level}"
