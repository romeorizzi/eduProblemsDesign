## Programmazione Dinamica ##

### Esercizio 2 __\[5 punti\]__ ###

Un robot R, inizialmente situato nella cella A1, deve portarsi nella sua home H situata nella cella G9.

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | R |   |   |   |   |   |   |   | X |
| B |   |   | X |   | X | X |   |   |   |
| C |   | X |   |   |   |   |   |   |   |
| D |   |   | X |   |   | X |   |   |   |
| E |   |   |   | X |   |   |   |   |   |
| F |   |   | X |   | X |   |   |   |   |
| G |   |   |   | X |   |   |   |   | H |

I movimenti base possibili sono il passo verso destra (ad esempio dalla cella A4 alla cella A5) ed il passo verso in basso (ad esempio dalla cella A4 alla cella B4). Tuttavia il robot non può visitare le celle occupate da un Pacman (indicate con la X). Quanti sono i percorsi possibili?

__Richieste__:
1. __\[1 pt\]__ Quanti sono i percorsi possibili se la partenza è in A1?
2. __\[1 pt\]__ E se la partenza è in C3?
3. __\[1 pt\]__ E se con partenza in A1 il robot deve giungere in F6?
4. __\[1 pt\]__ E se con partenza in A1 e arrivo in G9 al robot viene richiesto di passare per la cella D5?
5. __\[1 pt\]__ Ogni cella senza mina contiene un numero di monetine come rappresentato qui sotto. Quante monetine può raccogliere al massimo il robot?

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | R | 2 | 3 | 1 | 1 | 3 | 4 | 7 | X |
| B | 2 | 1 | X | 2 | X | X | 7 | 1 | 2 |
| C | 4 | X | 2 | 3 | 7 | 1 | 1 | 5 | 4 |
| D | 5 | 1 | X | 4 | 5 | X | 9 | 3 | 6 |
| E | 1 | 3 | 3 | X | 3 | 1 | 1 | 10| 8 |
| F | 1 | 4 | X | 5 | X | 3 | 1 | 8 | 9 |
| G | 7 | 5 | 2 | X | 2 | 2 | 3 | 4 | H |
