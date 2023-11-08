import numpy as np

quintoP_dnis = np.array([47303601,  # 0 Maxi
                         47797531,  # 1 Vicente
                         47708394,  # 2 Masante
                         47708326,  # 3 Fabri
                         46587536,  # 4 Mati
                         51702027,  # 5 Negro
                         47474935,  # 6 Paris
                         47174994,  # 7 Joaco
                         47351717,  # 8 Gallo
                         47305409,  # 9 Lauti
                         47303819,  # 10 Medrano
                         46586677,  # 11 Oviedo
                         47722877,  # 12 Costi
                         47264202,  # 13 Ariza
                         47173704,  # 14 Cipri
                         47351988,  # 15 Luca
                         47303647   # 16 Paul
                         ])

quintoP_nombres = np.array(["Palavecino", # 0 Maxi
                            "Arhex",      # 1 Vicente
                            "Masante",    # 2 Masante
                            "Silveyra",   # 3 Fabri
                            "Guzman",     # 4 Mati
                            "Coronel",    # 5 Negro
                            "Paris",      # 6 Paris
                            "Arce",       # 7 Joaco
                            "Gallo",      # 8 Gallo
                            "Cuesta",     # 9 Lauti
                            "Medrano",    # 10 Medrano
                            "Oviedo",     # 11 Oviedo
                            "Costilla",   # 12 Costi
                            "Ariza",      # 13 Ariza
                            "Cipriano",   # 14 Cipri
                            "Ramos",      # 15 Luca
                            "Michel"      # 16 Paul
                            ])

aristas_quintoP_I = np.array([(0,4,1), 
                              (1,6,7), 
                              (2,6,3), 
                              (3,2,10), 
                              (4,1,0), 
                              (5,7,6), 
                              (6,14,7), 
                              (7,1,6), 
                              (8,3,2), 
                              (9,6,7), 
                              (10,3,2), 
                              (11,6,16), 
                              (12,3,6), 
                              (13,14,12), 
                              (14,13,6), 
                              (15,7,6), 
                              (16,6,1)])

aristas_quintoP_II = np.array([(0,16,6), 
                               (1,16,6), 
                               (2,16,2), # Votó a uno 
                               (3,3,3), # No votó
                               (4,1,16), 
                               (5,6,16), 
                               (6,15,4), 
                               (7,5,11), 
                               (8,8,8), # No votó
                               (9,6,3), 
                               (10,10,10), # No votó
                               (11,6,15), 
                               (12,3,9), 
                               (13,3,11), 
                               (14,2,14), # Votó a uno 
                               (15,16,6),
                               (16,1,11)])

aristas_quintoP_III = np.array([(0,16,6),
                                (1,10,2), 
                                (2,8,2), 
                                (3,8,3),
                                (4,8,16),
                                (5,3,8), 
                                (6,3,0), 
                                (7,13,6), 
                                (8,4,8), 
                                (9,3,8), 
                                (10,3,2),
                                (11,0,15), 
                                (12,11,7),
                                (13,1,11),
                                (14,3,15), 
                                (15,6,15),
                                (16,3,7)])