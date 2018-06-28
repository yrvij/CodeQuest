import time

def transcription():
    mRNA = []
    for i in range(0,len(code)):
        if code[i] == 'A':
            mRNA.append('U')
        elif code[i] == 'T':
            mRNA.append('A')
        elif code[i] == 'C':
            mRNA.append('G')
        elif code[i] == 'G':
            mRNA.append('C')
    global mRNA_code
    mRNA_code = ''.join(mRNA)

def translation():   
    global anti_codons 
    anti_codons = []
    for i in range(0,len(mRNA_code)):
        if mRNA_code[i] == 'A':
            anti_codons.append('U')
        elif mRNA_code[i] == 'U':
            anti_codons.append('A')
        elif mRNA_code[i] == 'C':
            anti_codons.append('G')
        elif mRNA_code[i] == 'G':
            anti_codons.append('C')
    global anti_codons_code
    anti_codons_code = ''.join(anti_codons)

def polypeptide_chain():
    codon_dict = {
        'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
        'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser',
        'UAU':'Tyr','UAC':'Tyr','UAA':'STOP','UAG':'STOP',
        'UGU':'Cyr','UGC':'Cyr','UGA':'STOP','UGG':'Trp',
        'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
        'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
        'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln',
        'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
        'AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met',
        'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
        'AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lyr',
        'AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
        'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',
        'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
        'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
        'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}
    
    
    anti_codon_triplets = [anti_codons_code[i:i+3] for i in range(0, len(anti_codons_code), 3)]
    if (anti_codon_triplets[0] == 'UGA') or (anti_codon_triplets[0] == 'UAG') or (anti_codon_triplets[0] == 'UAA'):
        print('This is an empty polypeptide chain.')
        
    if len(anti_codon_triplets[len(anti_codon_triplets)-1]) < 3:
        anti_codon_triplets.remove(anti_codon_triplets[len(anti_codon_triplets)-1])
       
    if len(anti_codon_triplets[len(anti_codon_triplets)-1]) == 1:
        add_info = '*There was an extra nitrogen base in your DNA strand, so we removed it from the DNA transcript during transcription.'
    else:
        add_info = '*There were extra nitrogen bases in your DNA strand, so we removed them from the DNA transcript during transcription.'
   
    polypeptide_chain = []
    for codon in anti_codon_triplets:
        if (codon_dict[codon] == 'STOP'):
            break
        polypeptide_chain.append(codon_dict[codon])
    print('> '+'-'.join(polypeptide_chain))
    if len(code) % 3 != 0:
        print(add_info)

def protein_synthesis():
    global code 
    code = input('Please enter a valid strand of DNA: (containing A,T,G,or C only)').upper()
    code = code.replace(' ','').replace('-','')
    DNA_nucleotides = {'A','C','G','T'}
    
    if (set(sorted(set(code))).issubset(DNA_nucleotides)):
        print()
        print('Commencing Protein Synthesis...')
        time.sleep(3)
        print()
        print('- Transcription ✓')
        time.sleep(3)
        print()
        print('- Translation ✓')
        time.sleep(3)
        print()
        print('- Protein Synthesis ✓')
        time.sleep(3)
        print()
        print('Here is the resulting protein: ')
        time.sleep(5)
        print()
        print()
        transcription()
        translation()
        polypeptide_chain()
    
    elif 'U' in code:
        print('Loading...')
        time.sleep(3)
        print()
        print('Uracil found: Please enter a DNA strand not an RNA strand.')
        protein_synthesis()
    
    else:
        print('Loading...')
        time.sleep(3)
        print()
        print('This is an invalid DNA sequence. Please enter a correct sequence: ')
        protein_synthesis()
        
protein_synthesis()
