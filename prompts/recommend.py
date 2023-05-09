import logging

from rich.console import Console
from rich.traceback import install

from lib.json_tools import parse_json
from lib.openai_wrapper import get_response
from lib.prompt_builder import PromptBuilder
from lib.timer import timer

install()
console = Console()


products = [
    "Łaciate Mleko UHT bez laktozy,",
    "Kupiec Płatki owsiane błyskawiczne,",
    "Passata spar,",
    "Jabłka mix,",
    "Banan kg,",
    "Arbuz czerwony,",
    "Muszynianka Naturalna woda mineralna wysokozmineralizowana,",
    "Olej z pestek winogron,",
    "Dawtona Koncentrat pomidorowy 80 g,",
    "Ser Gouda Holenderska,",
    "Ziemniaki,",
    "Boczek bell wędzony,",
    "Knoppers Baton orzechowy Dark.",
    "Seler naciowy - Hiszpania",
    "Por",
    "Pomidor malinowy",
    "Schär Wafel bezglutenowy z orzechami",
    "Szynka Góralska",
    "Bułka sznytka - Cymes",
]


@timer
def recommend_prompt_1(**kwargs):  # pylint: disable=missing-function-docstring
    logging.info(
        "Rekomenduje przepis na obiad na podstawie listy produktów które mam w koszyku"
    )
    prompt = PromptBuilder(temperature=0.9, max_tokens=2000, **kwargs)

    how_many_products = 5
    prompt.text("Produkty: " + "\n- ".join(products) + ". ")
    prompt.text(
        f"Na podstawie listy produktów zarekomenduj inne {how_many_products} produktów które mogą mi się przydać."
    )  # pylint: disable=line-too-long
    prompt.text(
        "Podziel je na kategorie: jedzenie(c_id=1), chemia gospodarcza(c_id=2), kosmetyki(c_id=3)"
    )  # pylint: disable=line-too-long
    prompt.json({"data": [{"c_id": "integer", "name": "string"}]})

    res = get_response(prompt)

    return parse_json(res["choices"][0]["message"]["content"].strip())


@timer
def recommend_prompt_2(**kwargs):  # pylint: disable=missing-function-docstring
    logging.info(
        "Rekomenduje przepis na obioad, podstawie listy produktów które mam w koszyku"
    )
    prompt = PromptBuilder(temperature=0.8, max_tokens=500, **kwargs)

    prompt.text("Produkty: " + "\n- ".join(products) + ". ")
    prompt.text(
        "Na podstawie listy produktów zarekomenduj przepis na obiad. W kluczu `ingredients` podaj listę składników w formacie Markdown, w kluczu `receipe` podaj przepis w formacie Markdown, a w kluczu `name` nazwę potrawy."
    )  # pylint: disable=line-too-long
    prompt.json({"name": "string", "receipe": "string", "ingredients": "string"})

    res = get_response(prompt)
    return parse_json(res.choices[0].message.content.strip())
