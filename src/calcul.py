"""Petites fonctions de calcul pour les recettes."""


def doubler(quantite):
    return quantite * 2


def adapter(quantite, personnes_origine, personnes_voulues):
    return quantite * personnes_origine / personnes_voulues


def total(quantites):
    return sum(quantites)


def tripler(quantite):
    return quantite * 3


def moitie(quantite):
    return quantite / 2


def en_kilos(grammes):
    return grammes / 1000


def en_grammes(kilos):
    return kilos * 1000
