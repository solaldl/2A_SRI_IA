"""
module principal pour l'etape 4
"""

from projet.outils.GrapheDeLieux import GrapheDeLieux

# rajouter ensuite le import permettant d'utiliser le solver (l'algo) choisi
from projet.solvers.SolverCSP import SolverCSP

class Etape4 :
    """
    classe de test pour l'etape 4
    """

    if __name__ == '__main__':

        print("\n========== TEST  ==========")
        print("=============================")

        #    TEST 1 : town10.txt avec 3 couleurs
        tg : GrapheDeLieux = GrapheDeLieux.loadGraph("Data/town10.txt",True)
        print("\nTest sur town10 avec 3 couleurs (on attend OK) :")
        solver = SolverCSP(tg,3)
        solver.solve(False)

        #    TEST 2 : town10.txt avec 2 couleurs
        print("\nTest sur town10 avec 2 couleurs (on attend NOK) :")
        solver = SolverCSP(tg,2)
        solver.solve(False)

        #    TEST 3 : town10.txt avec 4 couleurs
        print("\nTest sur town10 avec 4 couleurs (on attend OK) :")
        solver = SolverCSP(tg, 4)
        solver.solve(False)



        #    TEST 4 : flat20_3_0.col avec 4 couleurs
        tg = GrapheDeLieux.loadGraph("Data/pb-etape1/flat20_3_0.col",False)
        print("Test sur flat20_3_0.col avec 4 couleurs (on attend OK) :")
        solver = SolverCSP(tg, 4)
        solver.solve(False)

        #    TEST 5 : flat20_3_0.col avec 3 couleurs
        print("Test sur flat20_3_0.col avec 3 couleurs (on attend OK) :")
        solver = SolverCSP(tg, 3)
        solver.solve(False)

        #    TEST 6 : flat20_3_0.col avec 2 couleurs
        print("Test sur flat20_3_0.col avec 2 couleurs (on attend NOK) :")
        solver = SolverCSP(tg, 2)
        solver.solve(False)



        #    TEST 7 : jean.col avec 10 couleurs
        tg = GrapheDeLieux.loadGraph("Data/pb-etape1/jean.col",False)
        print("Test sur jean.col avec 10 couleurs (on attend OK) :")
        solver = SolverCSP(tg, 10)
        solver.solve(False)

        #    TEST 9 : jean.col avec 3 couleurs
        print("Test sur jean.col avec 3 couleurs (on attend NOK) :")
        solver = SolverCSP(tg, 3)
        solver.solve(False)

#long
        #    TEST 8 : jean.col avec 9 couleurs
        #print("Test sur jean.col avec 9 couleurs (on attend NOK) :")
        # solver = SolverCSP(tg, 9)
        #solver.solve(False)

