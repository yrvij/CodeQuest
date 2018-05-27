def futuro(verbo):
    futuro_irregulares = {
        'decir':'dir','hacer':'har','haber':'habr','poner':'pondr','poder':'podr','querer':'querr',
        'saber':'sabr','salir':'saldr','tener':'tendr','venir':'vendr'
    }
    
    endings = ['é','ás','á','emos','án']
    print()
    if not verbo in futuro_irregulares.keys():
        for i in range(0,5):
            print(verbo+endings[i])
    else:
        for i in range(0,5):
            print(futuro_irregulares[verbo]+endings[i])
            

def conditional(verbo):
    condicional_irregulares = {
        'decir':'dir','hacer':'har','haber':'habr','poner':'pondr','poder':'podr','querer':'querr',
        'saber':'sabr','salir':'saldr','tener':'tendr','venir':'vendr'
    }

    endings = ['ía','ías','ía','íamos','ían']
    print()
    if not verbo in condicional_irregulares.keys():
        for i in range(0,5):
            print(verbo+endings[i])
    else:
        for i in range(0,5):
            print(condicional_irregulares[verbo]+endings[i])
 
perfecto_irregulares = {
    'abrir':'abierto','decir':'dicho','romper':'roto','poner':'puesto','morir':'muerto',
    'resolver':'resuelto','ver':'visto','volver':'vuelto','devolver':'devuelto','hacer':'hecho'
}

progressivo_irregulares = {
    'decir':'dici','dormir':'durmi','creer':'crey','ir':'y','traer':'tray','destruir':'destruy'
}

def presente_progressivo(verbo):
    auxillary = ['estoy','estás','está','estámos','están']
    extract = verbo[:len(verbo)-2]
    print()
    if not verbo in progressivo_irregulares.keys():
        if verbo[len(verbo)-2:] == 'ar':
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ando')
        else:
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'iendo')
    else:
        for i in range(0,5):
            print(auxillary[i]+ ' '+progressivo_irregulares[verbo]+'endo')
            
            

def imperfecto_progressivo(verbo):
    auxillary = ['estaba','estabas','estaba','estábamos','estaban']
    extract = verbo[:len(verbo)-2]
    print()
    if not verbo in progressivo_irregulares.keys():
        if verbo[len(verbo)-2:] == 'ar':
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ando')
        else:
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'iendo')
    else:
        for i in range(0,5):
            print(auxillary[i]+ ' '+progressivo_irregulares[verbo]+'endo')
            
            

def presente_perfecto(verbo):
    auxillary = ['he','has','ha','hemos','han']
    extract = verbo[:len(verbo)-2]
    print()
    if not verbo in perfecto_irregulares.keys():
        if verbo[len(verbo)-2:] == 'ar':
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ado')
        else:
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ido')
    else:
        for i in range(0,5):
            print(auxillary[i]+ ' '+perfecto_irregulares[verbo])
            
            

def pluscuamperfecto(verbo):
    auxillary = ['había','habías','había','habíamos','habían']
    extract = verbo[:len(verbo)-2]
    print()
    if not verbo in perfecto_irregulares.keys():
        if verbo[len(verbo)-2:] == 'ar':
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ado')
        else:
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ido')
    else:
        for i in range(0,5):
            print(auxillary[i]+ ' '+perfecto_irregulares[verbo])
            

def presente_perfecto_subjuntivo(verbo):
    auxillary = ['haya','hayas','haya','hayamos','hayan']
    extract = verbo[:len(verbo)-2]
    print()
    if not verbo in perfecto_irregulares.keys():
        if verbo[len(verbo)-2:] == 'ar':
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ado')
        else:
            for i in range(0,5):
                print(auxillary[i]+' '+extract+'ido')
    else:
        for i in range(0,5):
            print(auxillary[i]+ ' '+perfecto_irregulares[verbo])
            

def futuro_perfecto(verbo):
    auxillary = ['habré','habrás','habrá','habremos','habrán']
    extract = verbo[:len(verbo)-2]
    print()
    if not verbo in perfecto_irregulares.keys():
        if verbo[len(verbo)-2:] == 'ar':
            for i in range(5):
                print(auxillary[i]+' '+extract+'ado')
        else:
            for i in range(5):
                print(auxillary[i]+' '+extract+'ido')
    else:
        for i in range(5):
            print(auxillary[i]+ ' '+perfecto_irregulares[verbo])
            

def imperfecto_subjuntivo(verbo):
    imperfecto_subjuntivo_irregulares = {
        'ir':'fu','haber':'hubi','pedir':'pidi','construir':'construy','poner':'pusi',
        'tener':'tuvi','poder':'pudi','saber':'supi','decir':'dij','estar':'estuvi',
        'dormir':'durmi','servir':'sirvi','leer':'ley','creer':'creey','destruir':'destruy','hacer':'hici'
        
    }
    print()
    ar_endings = ['ara','aras','ara','áramos','aran']
    er_ir_endings = ['iera','ieras','iera','iéramos','ieran']
    irregular_endings = ['era','eras','era','éramos','eran']
    extract = verbo[:len(verbo)-2]
    if not verbo in imperfecto_subjuntivo_irregulares.keys():
        if verbo[len(verbo)-2:] == 'ar':
            for i in range(5):
                print(extract+ar_endings[i])
        else:
            for i in range(5):
                print(extract+er_ir_endings[i])
    else:
        for i in range(5):
            print(imperfecto_subjuntivo_irregulares[verbo]+irregular_endings[i])
            

def main():
    verbo = input()
 
    presente_progressivo(verbo)
    imperfecto_progressivo(verbo)
    presente_perfecto(verbo)
    pluscuamperfecto(verbo)
    presente_perfecto_subjuntivo(verbo)
    futuro(verbo)
    conditional(verbo)
    futuro_perfecto(verbo)
    imperfecto_subjuntivo(verbo)
