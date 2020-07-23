conecta(inicio,0).
conecta(1,7).
conecta(2,3).
conecta(2,8).
conecta(3,4).
conecta(3,9).
conecta(4,10).
conecta(5,6).
conecta(5,11).
conecta(7,13).
conecta(8,9).
conecta(10,16).
conecta(11,17).
conecta(12,18).
conecta(13,14).
conecta(14,15).
conecta(14,20).
conecta(15,21).
conecta(16,22).
conecta(17,23).
conecta(18,24).
conecta(19,25).
conecta(20,26).
conecta(21,22).
conecta(23,29).
conecta(24,30).
conecta(25,31).
conecta(26,27).
conecta(27,28).
conecta(28,29).
conecta(28,34).
conecta(30,36).
conecta(31,32).
conecta(32,33).
conecta(32,fin).
conecta(33,34).
conecta(34,35).
conecta(35,36).
conectado(Pos1,Pos2) :- conecta(Pos1,Pos2).
conectado(Pos1,Pos2) :- conecta(Pos2,Pos1).
miembro(X,[X|_]).
miembro(X,[_|Y]) :- miembro(X,Y) .
sol :- camino([inicio],Sol),write(Sol) .
camino([fin|RestoDelCamino],[fin|RestoDelCamino]).
camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+ miembro(PosSiguiente,RestoDelCamino),camino([PosSiguiente,PosActual|RestoDelCamino],Sol).