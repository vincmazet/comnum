"""
COMNUM - Module Python pour les communications numériques à Télécom Physique Strasbourg.

Ce programme est distribué sous licence CeCILL-B (www.cecill.info).
Copyright Université de Strasbourg 2013-2021 (2021-03-23)
Contributeur : vincent.mazet@unistra.fr
"""


import numpy as np
import matplotlib.pyplot as plt


def eyediag(t, x, T, alpha=.5):
    
    """
    Diagramme de l'oeil.
    
    Entrées :
    t (array)      : temps
    x (array)      : signal
    T (scalar)     : durée d'un symbole
    alpha (scalar) : transparence (0,5 par défaut)
    
    Sortie :
    aucune
    """
    
    # % Détecte les instants auxquels le temps revient à -T/2
    t = t%T - T/2
    idx = np.flatnonzero(t[1:] < t[:-1])

    # Affichage des traces, séparément
    j = 0
    for i in idx:
        plt.plot(t[j:i+1], x[j:i+1], alpha=alpha, color='tab:blue')
        j = i+1
        

def randmary(N,p):
    
    """
    Génération d'une séquence M-aire.
    
    Entrées :
    N (scalar) : taille de la séquence (nombre de symboles)
    P (aray)   : probabilité des symboles (sa taille correspond à la taille de l'alphabet)
    
    Sortie :
    c (array) : séquence aléatoire M-aire où M = len(P).
    
    Exemples :
    
    # séquence binaire de taille 1000, symboles équiprobables :
    c1 = randmary(1000,[0.5, 0.5])
    
    # séquence binaire de taille 100, p("0") = 0.3, p("1") = 0.7 :
    c2 = randmary(100,[0.3, 0.7])    
    
    # # séquence 4-aire de taille 10, symboles équiprobables :
    c3 = randmary(10,np.ones(4)/4)
    """

    # Base
    M = len(p)
    
    # Normalisation des probabilités
    p = p / np.sum(p)
    
    # Fonction de répartition
    q = np.cumsum(p)
    
    # Vecteur aléatoire uniforme
    u = np.random.rand(N)
    
    # Matrice NxM des u et q
    U = np.tile(u,(M,1)).T
    Q = np.tile(q,(N,1))
    
    # Séquence de symboles
    c = np.sum(U>Q, axis=1)
    
    return c


def bin2mary(x,M):
    
    """
    Convertit une séquence binaire en séquence M-aire.
    Si la taille de x n'est pas multiple de log2(M), des "0" sont rajoutés à la fin de x.
    
    Entrées :
    x (array)  : séquence binaire
    M (scalar) : taille de l'alphabet de la séquence traduite (M est une puissance de 2)
    
    Sortie :
    y (array) : séquence M-aire
    """
    
    # Nombre de bits par symboles
    N = np.log2(M).astype("int")
    
    # Nombre de bits dans la séquence binaire x
    K = len(x)
    
    # Nombre de symboles dans la séquence M-aire y
    L = np.ceil(K/N).astype("int")
    
    # Rajoute des zéros en fin de z pour avoir un nombre de bits en puissance de N
    z = np.concatenate((x, np.zeros(N*L-K, dtype="int")))
    
    # Initialisation de la séquence de sortie
    y = np.array([], dtype="int")
    
    # Array des puissances
    powers = np.power(2,range(N))
    
    for i in range(0, K, N):
        m = z[i:i+N]
        c = np.sum(m*powers)
        y = np.append(y, c)
    
    return y


def mod_a(x, v, d):
    
    """
    Modulation mystère A.
    
    Entrées :
    x (array)    : séquence binaire
    v (scalaire) : amplitude de la forme d'onde
    d (scalaire) : durée de la forme d'onde
    
    Sorties :
    t (array) : vecteur temps
    y (array) : signal modulé
    """

    N = len(x)
    y = np.zeros(100*N)
    sgn = -1

    for n in range(N):
        i = 100*n + np.arange(100)
        if x[n] == 0:
            y[i] = 0
        elif x[n] == 1:
            sgn = -sgn
            y[i] = sgn*v * np.ones(100)

    t = np.arange(100*N)/100*d
    
    return t, y


def mod_b(x, v, d):
    
    """
    Modulation mystère B.
    
    Entrées :
    x (array)    : séquence binaire
    v (scalaire) : amplitude de la forme d'onde
    d (scalaire) : durée de la forme d'onde
    
    Sorties :
    t (array) : vecteur temps
    y (array) : signal modulé
    """

    N = len(x)
    y = np.zeros(100*N)
    t = np.arange(100)*d/100
    z = v * np.cos(2*np.pi*4*t)

    for n in range(N):
        i = 100*n + np.arange(100)
        if x[n] == 0:
            y[i] = -z
        elif x[n] == 1:
            y[i] = +z

    t = np.arange(100*N)/100*d
    
    return t, y


def mod_c(x, v, d):
    
    """
    Modulation mystère C.
    
    Entrées :
    x (array)    : séquence binaire
    v (scalaire) : amplitude de la forme d'onde
    d (scalaire) : durée de la forme d'onde
    
    Sorties :
    t (array) : vecteur temps
    y (array) : signal modulé
    """

    N = len(x)
    y = np.zeros(100*N)

    for n in range(N):
        i = 100*n + np.arange(100)
        if x[n] == 0:
            y[i] = v * np.concatenate((-np.ones(50), np.ones(50)))
        elif x[n] == 1:
            y[i] = v * np.concatenate((np.ones(50), -np.ones(50)))

    t = np.arange(100*N)/100*d
    
    return t, y


def mod_d(x, v, d):
    
    """
    Modulation mystère D.
    
    Entrées :
    x (array)    : séquence binaire
    v (scalaire) : amplitude de la forme d'onde
    d (scalaire) : durée de la forme d'onde
    
    Sorties :
    t (array) : vecteur temps
    y (array) : signal modulé
    """

    N = len(x)
    y = np.zeros(100*N)

    for n in range(N):
        i = 100*n + np.arange(100)
        if x[n] == 0:
            y[i] = -v * np.ones(100)
        elif x[n] == 1:
            y[i] = v * np.ones(100)

    t = np.arange(100*N)/100*d
    
    return t, y


def mod_e(x, v, d):
    
    """
    Modulation mystère E.
    
    Entrées :
    x (array)    : séquence binaire
    v (scalaire) : amplitude de la forme d'onde
    d (scalaire) : durée de la forme d'onde
    
    Sorties :
    t (array) : vecteur temps
    y (array) : signal modulé
    """
    f = 4
    N = len(x)
    y = np.zeros(100*N)
    t = np.arange(100)*d/100
    
    constellation = [
        {'a': -3, 'b': +3},
        {'a': -1, 'b': +3},
        {'a': -3, 'b': +1},
        {'a': -1, 'b': +1},
        {'a': +3, 'b': +3},
        {'a': +1, 'b': +3},
        {'a': +3, 'b': +1},
        {'a': +1, 'b': +1},
        {'a': -3, 'b': -3},
        {'a': -1, 'b': -3},
        {'a': -3, 'b': -1},
        {'a': -1, 'b': -1},
        {'a': +3, 'b': -3},
        {'a': +1, 'b': -3},
        {'a': +3, 'b': -1},
        {'a': +1, 'b': -1}
    ]
    
    for n in range(N):
        i = 100*n + np.arange(100)
        y[i] = constellation[x[n]]['a']*v*np.cos(2*np.pi*f*t) + constellation[x[n]]['b']*v*np.sin(2*np.pi*f*t)
    
    t = np.arange(100*N)/100*d
    
    return t, y