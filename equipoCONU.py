import numpy as np

equipo = np.array(["Fede",  #0
                   "Nachi", #1
                   "Clari", #2
                   "Geni",  #3
                   "Ivan",  #4
                   "Juli",  #5
                   "Lupa",  #6
                   "May",   #7
                   "Nico",  #8
                   "Octi",  #9
                   "Zeta",  #10
                   "Toti",  #11
                   "Trini"  #12
                   ])

aristas_equipo_I = np.array([(7, 12, 1), (11, 0, 1), (12, 7, 8), (4, 8, 6),
                             (2, 12, 10), (3, 10, 6), (1, 4, 12), (8, 12, 9),
                             (9, 2, 8), (0, 1, 8), (10, 4, 11), (5, 1, 12),
                             (6, 10, 7)])

aristas_equipo_II = np.array([(3, 5, 12), (7, 8, 10), (1, 10, 12), (9, 10, 7), (2, 5, 4),
                              (8, 7, 4), (5, 3, 2), (0, 10, 11), (4, 7, 10), (12, 1, 11),
                              (11, 10, 5), (10, 8, 2), (6, 0, 2)])

aristas_equipo_III = np.array([(6, 3, 11), (11, 4, 7), (7, 1, 2), (8, 4, 11), (3, 7, 12), 
                               (10, 7, 8), (9, 3, 6), (1, 6, 11), (0, 4, 2), (12, 3, 4),
                               (5, 0, 11), (4, 0, 3), (2, 0, 11)])