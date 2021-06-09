#!/usr/bin/python3
# -*- coding: utf-8 -*-


class AppPref(object):

    def prefpane_cine(self,parent,**kwargs): 
       
        pane = parent.contentPane(**kwargs)
        fb = pane.formbuilder(cols=1,border_spacing='3px')
        fb.numberTextBox(value='^.cast_max', lbl='Dimensione massima cast', width='4em')
