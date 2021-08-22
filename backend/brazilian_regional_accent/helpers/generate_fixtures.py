import json
from numpy.lib.ufunclike import fix

import pandas as pd

ESTADOS_CSV_FILENAME = "helpers/estados.csv"
CIDADES_CSV_FILENAME = "helpers/municipios.csv"
SENTENCES_CSV_FILENAME = "helpers/frases.csv"


def parse_estado_to_fixture_json(estado: dict) -> dict:
    """
    Parse estado from json to fixture json
    :param estado: estado from json
    :return: fixture json
    """
    return {
        "model": "accent_collector.state",
        "pk": estado["codigo_uf"],
        "fields": {
            "name": estado["nome"],
            "abbreviation": estado["uf"],
        }
    }


def generate_fixtures_for_estado(fname: str) -> None:
    """
    Generate fixtures for estado
    :param fname: file name
    :return: None
    """
    df = pd.read_csv(ESTADOS_CSV_FILENAME)
    fixture = []
    for _, row in df.iterrows():
        fixture.append(parse_estado_to_fixture_json(row))
    with open(fname, "w") as f:
        json.dump(fixture, f, indent=4)
    print("{} estados foram gerados".format(len(fixture)))


def parse_cidade_to_fixture_json(cidade: dict) -> dict:
    return {
        "model": "accent_collector.city",
        "pk": cidade["codigo_ibge"],
        "fields": {
            "name": cidade["nome"],
            "state": cidade["codigo_uf"],
            "latitude": cidade["latitude"],
            "longitude": cidade["longitude"],
            "is_capital": cidade["capital"],
        }
    }


def generate_fixtures_for_cidade(fname: str) -> None:
    df = pd.read_csv(CIDADES_CSV_FILENAME)
    fixture = []
    for _, row in df.iterrows():
        fixture.append(parse_cidade_to_fixture_json(row))
    with open(fname, "w") as f:
        json.dump(fixture, f, indent=4)
    print("{} cidades foram geradas".format(len(fixture)))


def parse_gender_to_fixture_json(gender: str, text: str, i: int) -> dict:
    return {
        "model": "accent_collector.gender",
        "pk": i,
        "fields": {
            "name": gender,
            "radio_text": text,
        }
    }


def generate_fixtures_for_gender(fname: str) -> None:
    fixture = []
    genders = [
        ("masculino", "Masculino"),
        ("feminino", "Feminino"),
        ("n/a", "Outro / Prefiro não informar"),
    ]
    for i, (gender, text) in enumerate(genders):
        fixture.append(parse_gender_to_fixture_json(gender, text, i))
    with open(fname, "w") as f:
        json.dump(fixture, f, indent=4)
    print("{} gêneros foram gerados".format(len(fixture)))


def parse_sentence_to_fixture_json(frase: dict, i: int) -> dict:
    return {
        "model": "accent_collector.sentence",
        "pk": i,
        "fields": {
            "text": frase["texto"],
        }
    }


def generate_fixtures_for_sentence(fname: str) -> None:
    df = pd.read_csv(SENTENCES_CSV_FILENAME)
    fixture = []
    for i, row in df.iterrows():
        fixture.append(parse_sentence_to_fixture_json(row, i))
    with open(fname, "w") as f:
        json.dump(fixture, f, indent=4)
    print("{} frases foram geradas".format(len(fixture)))


if __name__ == '__main__':

    generate_fixtures_for_estado(
        "fixtures/state.json")
    generate_fixtures_for_cidade(
        "fixtures/city.json")
    generate_fixtures_for_gender(
        "fixtures/gender.json")
    generate_fixtures_for_sentence(
        "fixtures/sentence.json")
