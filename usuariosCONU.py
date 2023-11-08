import numpy as np

usuarios = np.array(["Tomás\nSantillán",     #0
                     "Sofía\nMarshall",      #1
                     "Consuelo\nQuevedo",    #2
                     "Giuliana\nDe Luca",    #3
                     "Lucía\nQuiroga",       #4
                     "Emilia\nHerrera",      #5
                     "Valentina\nLobo",      #6
                     "Luciano\nCortesini",   #7
                     "Lucía\nAbiega",        #8
                     "Rebecca\nMartinez",    #9
                     "Virginia\nBonsignori", #10
                     "Micaela\nCapdevila",   #11
                     "Azul\nVittar",         #12
                     "Tomás\nDíaz",          #13
                     "Rocío\nChiggio",       #14
                     "Nicolás\nWilkys",      #15
                     "Ezequiel\nReyes"       #16
                     ])

aristas_usuarios_I = np.array([(0, 5, 8), (12, 7, 5), (14, 9, 4), (8, 5, 9),
                               (16, 6, 0), (1, 12, 8), (4, 1, 10), (2, 1, 5),
                               (5, 0, 4), (13, 0, 8), (10, 7, 14), (11, 7, 0),
                               (6, 7, 12), (9, 5, 8), (15, 14, 12), (7, 0, 4),
                               (3, 5, 12)])

aristas_usuarios_II = np.array([(2, 3, 7), (11, 9, 14), (14, 8, 9), (12, 7, 0), 
                                (4, 7, 3), (10, 3, 15), (5, 16, 12), (13, 4, 1), 
                                (7, 5, 12), (16, 3, 1), (6, 1, 4), (3, 0, 2), 
                                (15, 1, 10), (1, 4, 11), (0, 12, 7), (8, 9, 3)])

aristas_usuarios_III = np.array([(5, 16, 3), (6, 16, 3), (7, 16, 3), (16, 15, 2),
                                 (2, 11, 3), (15, 2, 12), (12, 7, 13), (13, 7, 5),
                                 (3, 13, 2), (0, 3, 13), (8, 3, 14), (1, 2, 13), (10, 14, 13),
                                 (14, 3, 13), (4, 14, 16), (11, 3, 13), (9, 2, 13)])