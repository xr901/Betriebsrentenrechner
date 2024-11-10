#!/usr/bin/env python
# -*- coding: utf-8  -*-
#
# Rechner für betriebliche Altersversorgung

import locale

alter = 25
gehalt = 40000			# steuerpflichtiges Arbeitsentgelt pro Jahr
zugeh = 5			# Zugehörigkeit im Unternehmen in Jahren
erh = 2000			# jährliche Gehaltserhöhung (ca.)
eigenbeitrag = 0		# je Monat
refentgelt = 1000		# Referenzentgelt, fixer Faktor
multiplikator = 4		# in Euro
punktesum = 0			# summierte Versorgungspunkte
punkte = 0			# Versorgungspunkte je Jahr
jahr = 1			# Start im Jahr 1 der Zugehörigkeit
betriebsrente = 0		# monatliche Betriebsrente

locale.setlocale(locale.LC_ALL, '')
def euro(value):
	return locale.currency(value, grouping=True)
alterstabelle = {
	25: 2.4,
	26: 2.3,
	27: 2.2, 28: 2.2,
	29: 2.1,
	30: 2.0, 31: 2.0,
	32: 1.9, 33: 1.9,
	34: 1.8,
	35: 1.7, 36: 1.7,
	37: 1.6, 38: 1.6, 39: 1.6,
	40: 1.5, 41: 1.5,
	42: 1.4, 43: 1.4,
	44: 1.3, 45: 1.3, 46: 1.3,
	47: 1.2, 48: 1.2, 49: 1.2,
	50: 1.1, 51: 1.1, 52: 1.1,
	53: 1.0, 54: 1.0, 55: 1.0, 56: 1.0,
	57: 0.9, 58: 0.9, 59: 0.9, 60: 0.9, 61: 0.9,
	62: 0.8, 63: 0.8, 64: 0.8, 65: 0.8, 66: 0.8, 67: 0.8
}

print("┌─────────────── Betriebsrentenrechner ────────────────┐")
print("\tAlter:\t\t\t" + str(alter) + " Jahre")
print("\tGehalt:\t\t\t" + euro(gehalt) + "/a")
print("\tZugehörigkeit:\t\t" + str(zugeh) + " Jahre")
print("\tGehaltserhöhung:\t" + euro(erh) + "/a")
print("├──────────────────────────────────────────────────────┤\n")

while jahr <= zugeh:
	punkte = gehalt/12/refentgelt*alterstabelle[alter]
	punktesum += punkte
	betriebsrente = punktesum * multiplikator
	print("Jahr der Zugehörigkeit:\t\t\t" + str(jahr))
	print("\tBruttojahresgehalt:\t\t" + euro(gehalt))
	print("\tVersorgungspunkte dieses Jahr:\t" + str(round(punkte, 2)))
	print("\tVersorgungspunkte summiert:\t" + str(round(punktesum, 2)))
	print("\tMonatliche Betriebsrente:\t" + euro(betriebsrente) + "\n")
	gehalt += erh
	jahr += 1

print("├──────────────────────────────────────────────────────┤")
print("\tMonatliche Betriebsrente:\t" + euro(betriebsrente))

if zugeh >= 3:
	abschlag = 36 * 0.3 / 100	# in Prozent
	print("\tRentenabschlag durch vorzeitige\n\tInanspruchnahme mit 64 Jahren:\t" 
		+ euro(betriebsrente * abschlag) + ", " + str(round(abschlag*100,1)) + " %")
	print("\tBetriebsrente nach Abschlag:\t" + euro(betriebsrente - (betriebsrente * abschlag)))
print("└──────────────────────────────────────────────────────┘")
