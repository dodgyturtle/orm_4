import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        img_url = pokemon.get_image(request)
        pokemons_on_page.append(
            {
                "pokemon_id": pokemon.id,
                "img_url": img_url,
                "title_ru": pokemon.title_ru,
            }
        )
        pokemonentities = PokemonEntity.objects.filter(pokemon=pokemon)
        for pokemonentity in pokemonentities:
            add_pokemon(
                folium_map,
                pokemonentity.latitude,
                pokemonentity.longitude,
                img_url,
            )

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    pokemon_description = {}
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if not pokemon:
        return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemonentities = PokemonEntity.objects.filter(pokemon=pokemon)
    pokemon_description["img_url"] = pokemon.get_image(request)
    pokemon_description["title_ru"] = pokemon.title_ru
    pokemon_description["title_en"] = pokemon.title_en
    pokemon_description["title_jp"] = pokemon.title_jp
    pokemon_description["description"] = pokemon.description
    for pokemonentity in pokemonentities:
        add_pokemon(
            folium_map,
            pokemonentity.latitude,
            pokemonentity.longitude,
            pokemon_description["img_url"],
        )
    return render(
        request,
        "pokemon.html",
        context={"map": folium_map._repr_html_(), "pokemon": pokemon_description},
    )
