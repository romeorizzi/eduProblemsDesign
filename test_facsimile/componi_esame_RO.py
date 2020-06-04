#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:44:57 2020

@author: alice
"""

import hashlib
import nbformat
import os
import sys


def inserisci_pd_stringhe(note, num):
    percorso_pd_str = os.getcwd() + '/progr_din/stringhe/'
    nb_es = len(os.listdir(percorso_pd_str))
    scelto = percorso_pd_str + 'stringhe' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    note['cells'] = [nbformat.v4.new_markdown_cell(content)]
    return

def inserisci_pd_robot(note, num):
    return

def inserisci_grafi_planarita(note, num):
    return

def inserisci_grafi_cammini(note, num):
    return

def inserisci_grafi_alberi(note, num):
    return

def inserisci_grafi_flusso(note, num):
    return

def inserisci_pl_due_fasi(note, num):
    return

def inserisci_pl_dualita(note, num):
    return

def inserisci_pl_interattivo(note, num):
    return

def inserisci_pl_modello(note, num):
    return

def genera_notebook(nome_foglio, es_scelti):
    notebook = nbformat.v4.new_notebook()
    
    inserisci_pd_stringhe(notebook, es_scelti[0])
    inserisci_pd_robot(notebook, es_scelti[1])
    inserisci_grafi_planarita(notebook, es_scelti[2])
    inserisci_grafi_cammini(notebook, es_scelti[3])
    inserisci_grafi_alberi(notebook, es_scelti[4])
    inserisci_grafi_flusso(notebook, es_scelti[5])
    inserisci_pl_due_fasi(notebook, es_scelti[6])
    inserisci_pl_dualita(notebook, es_scelti[7])
    inserisci_pl_interattivo(notebook, es_scelti[8])
    inserisci_pl_modello(notebook, es_scelti[9])
    
    nbformat.write(notebook, nome_foglio)
    return


data_esame = '2020-06-30'
matricola = "VR382079"
nome_foglio = 'esameRO_'+ data_esame + '_' + matricola + '.ipynb'

h = hashlib.md5((data_esame+matricola).encode('utf-8')).hexdigest()
es_scelti = [int(s) for s in h if s.isdigit()]
assert len(es_scelti) >= 10
genera_notebook(nome_foglio, es_scelti)
