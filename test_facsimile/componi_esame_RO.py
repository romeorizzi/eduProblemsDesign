#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:44:57 2020

@author: Alice Raffaele
"""

import hashlib
import nbformat
import os
import re
import sys


global percorsi_testi_utili
global count_es
global punti_totali

def inserisci_cella_raw_vuota(note):
    note['cells'] += [nbformat.v4.new_raw_cell()]
    return

def recupera_punti_es(txt):
    return int(re.sub("[^0-9]", "", re.search(r"\\\[\d+ pts\\\]",txt).group()))

def inserisci_pd_stringhe(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_pd_str = os.getcwd() + '/progr_din/stringhe/'
    nb_es = len(os.listdir(percorso_pd_str)) - 1 # indexing file da 0
    scelto = percorso_pd_str + 'stringhe' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw + suggerimento su come ottenere tabelle Markdown
    txt2 = open(percorso_testi_utili + 'nota_markdown_tables.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_pd_robot(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_pd_robot = os.getcwd() + '/progr_din/robot/'
    nb_es = len(os.listdir(percorso_pd_robot)) - 1 # indexing file da 0
    scelto = percorso_pd_robot + 'robot' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw + suggerimento su come ottenere tabelle Markdown
    txt2 = open(percorso_testi_utili + 'nota_markdown_tables.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_grafi_planarita(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_grafi_plan = os.getcwd() + '/grafi/planarita/'
    nb_es = len(os.listdir(percorso_grafi_plan)) - 1 # indexing file da 0
    scelto = percorso_grafi_plan + 'plan' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw + suggerimento su Graph Creator
    txt2 = open(percorso_testi_utili + 'nota_graph_creator.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_grafi_cammini(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_grafi_cam = os.getcwd() + '/grafi/cammini/'
    nb_es = len(os.listdir(percorso_grafi_cam)) - 1 # indexing file da 0
    scelto = percorso_grafi_cam + 'cammini' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw + suggerimento su Markdown e Graph Creator
    txt2 = open(percorso_testi_utili + 'nota_markdown_graph_creator.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_grafi_alberi(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_grafi_alb = os.getcwd() + '/grafi/alberi/'
    nb_es = len(os.listdir(percorso_grafi_alb)) - 1 # indexing file da 0
    scelto = percorso_grafi_alb + 'alberi' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw + suggerimento su Markdown e Graph Creator
    txt2 = open(percorso_testi_utili + 'nota_markdown_graph_creator.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_grafi_flusso(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_grafi_flu = os.getcwd() + '/grafi/flussi/'
    nb_es = len(os.listdir(percorso_grafi_flu)) - 1 # indexing file da 0
    scelto = percorso_grafi_flu + 'flussi' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw + suggerimento su Markdown e Graph Creator
    txt2 = open(percorso_testi_utili + 'nota_markdown_graph_creator.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_pl_due_fasi(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_pl_2f = os.getcwd() + '/progr_lin/due_fasi/'
    nb_es = len(os.listdir(percorso_pl_2f)) - 1 # indexing file da 0
    scelto = percorso_pl_2f+ 'due_fasi' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw + suggerimento su Markdown
    txt2 = open(percorso_testi_utili + 'nota_markdown_tables.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_pl_dualita(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_pl_dual = os.getcwd() + '/progr_lin/dualita/'
    nb_es = len(os.listdir(percorso_pl_dual)) - 1 # indexing file da 0
    scelto = percorso_pl_dual+ 'dualita' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw 
    txt2 = open(percorso_testi_utili + 'nota_raw.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_pl_interattivo(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_pl_inter = os.getcwd() + '/progr_lin/simplesso_interattivo/'
    nb_es = len(os.listdir(percorso_pl_inter)) - 1 # indexing file da 0
    scelto = percorso_pl_inter+ 'simpl_inter' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw 
    txt2 = open(percorso_testi_utili + 'nota_raw.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def inserisci_pl_modello(note, num):
    global count_es
    global punti_totali
    count_es += 1
    # testo esercizio
    percorso_pl_mod = os.getcwd() + '/progr_lin/modelli/'
    nb_es = len(os.listdir(percorso_pl_mod)) - 1 # indexing file da 0
    scelto = percorso_pl_mod+ 'model' + str(nb_es % num) + '.md'
    txt = open(scelto, 'r',encoding='utf-8')
    content = txt.read()
    punti_totali += recupera_punti_es(content)
    content_up = content.replace('NUM?', str(count_es))
    note['cells'] += [nbformat.v4.new_markdown_cell(content_up)]
    
    # nota celle raw 
    txt2 = open(percorso_testi_utili + 'nota_raw.md', 'r', encoding='utf-8')
    content2 = txt2.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content2)]
    
    inserisci_cella_raw_vuota(note)
    return

def sorteggia_esercizi(nome):
    h = hashlib.md5(nome.encode('utf-8')).hexdigest()
    es_scelti = [int(s) for s in h if s.isdigit() and int(s) != 0]
    #print(es_scelti)
    assert len(es_scelti) >= 10
    return es_scelti

def inserisci_intestazione(note, data, matr):
    txt = open(percorso_testi_utili + 'intestazione.md', 'r', encoding='utf-8')
    content = txt.read()
    content_custom = content.replace('DATA?', data[8:10]+'-'+data[5:7]+'-'+data[0:4]).replace('VR?', matr)
    note['cells'] += [nbformat.v4.new_markdown_cell(content_custom)]    
    return

def inserisci_istruzioni(note):
    txt = open(percorso_testi_utili + 'istruzioni.md', 'r', encoding='utf-8')
    content = txt.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content)]    
    return

def inserisci_note_finali(note):
    txt = open(percorso_testi_utili + 'note_finali.md', 'r', encoding='utf-8')
    content = txt.read()
    note['cells'] += [nbformat.v4.new_markdown_cell(content)]    
    return    

def aggiorna_punti_totali(note):
    global punti_totali
    note.cells[0].source = note.cells[0].source.replace('TOT?', str(punti_totali))

def genera_notebook(data_esame, matricola):
    es_scelti = sorteggia_esercizi(data_esame+matricola)
    
    notebook = nbformat.v4.new_notebook()
    inserisci_intestazione(notebook, data_esame, matricola)
    inserisci_istruzioni(notebook)
    
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
    
    inserisci_note_finali(notebook)
    aggiorna_punti_totali(notebook)
    
    nome_foglio = 'esameRO_'+ data_esame + '_' + matricola + '.ipynb'
    nbformat.write(notebook, nome_foglio)
    return


data_esame = '2020-06-30'
matricola = 'VR382079'

if len(sys.argv) > 1:
    data_esame = str(sys.argv[1])
    matricola = str(sys.argv[2])
    
percorso_testi_utili = os.getcwd() + '/testi_utili/'
count_es = 0
punti_totali = 0

genera_notebook(data_esame, matricola)
