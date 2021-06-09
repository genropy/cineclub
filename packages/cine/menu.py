#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch(u"Cineclub")
    auto.thpage(u"Soci", table="cine.socio")
    auto.thpage(u"Proiezioni", table="cine.proiezione")
    #auto.thpage(u"Recensioni", table="cine.recensione")
    #auto.thpage(u"Iscrizioni", table="cine.iscrizione_proiezione")
    auto.thpage(u"Film", table="cine.film")
    auto.lookups('Tabelle lookup', lookup_manager='cine')

