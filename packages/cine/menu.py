#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    cine = root.branch('Cineclub')
    cine.thpage('Proiezioni',table='cine.proiezione')
