#!/usr/bin/env python 
# Created by: Lee Bergstrand
# Descript: A Bio-Python program that takes a list of query proteins and uses local BLASTp to search
#           for highly similer proteins within a local blast database (usally a local db of a target 
#           proteome). The program then BLASTps backward from the found subject protein to the proteome 
#           for which the original query protein is in to confirm orthology. 
#             
# Requirements: - This program requires the Biopython module: http://biopython.org/wiki/Download
#               - All operations are done with protien sequences.
#               - All query proteins should be from sequenced genomes in order to facilitate backwards BLAST. 
#               - MakeBlastDB must be used to create BLASTp databases for both query and subject proteomes.
#               - BLAST databases require the FASTA file they were made from to be in the same directory.
#  
# Usage: BackBLAST.py <queryGeneList.faa> <subject1.faa> ... <subjectN.faa> 
# Example: BackBLAST.py queryGeneList.faa ./*.faa
#----------------------------------------------------------------------------------------
#===========================================================================================================
#Imports:
	
#===========================================================================================================
# Functions:

# 1: Checks if in proper number of arguments are passed gives instructions on proper use.
def argsCheck():
	if len(sys.argv) < 3:
		print "Orthologous Gene Finder"
		print "By Lee Bergstrand\n"
		print "Please refer to source code for documentation\n"
		print "Usage: " + sys.argv[0] + " <queryGeneList.faa> <subject1.faa> ... <subjectN.faa>\n"
		print "Examples:" + sys.argv[0] + " queryGeneList.faa ./*.faa"
		exit(1) # Aborts program. (exit(1) indicates that an error occured)
#===========================================================================================================
# Main program code:

# House keeping...
argsCheck() # Checks if the number of arguments are correct.

queryFile = sys.argv[1]

# File extension check
if not inFile.endswith(".faa"):
	print "[Warning] " + inFile + " may not be a amino acid fasta file!"
	
