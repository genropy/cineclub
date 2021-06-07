#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch(u"auto")
    auto.thpage(u"!!Proiezione", table="cine.proiezione")
    auto.thpage(u"!!Recensione", table="cine.recensione")
    auto.thpage(u"!!Socio", table="cine.socio")

