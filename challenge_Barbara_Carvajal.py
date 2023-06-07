import random 
#Se importa el modulo random

def partido(nombreDeJugadorUno, nombreDeJugadorDos):
    # Inicializar variables
    # contadores y listas globales para resultados
    jugadorUnoSets = 0 
    jugadorDosSets = 0 
    jugadorUnoGames = 0  
    jugadorDosGames = 0  
    tantosJugadorUno = []  
    tantosJugadorDos = []  
    setsJugadorUno = [] 
    setsJugadorDos = []  
    contadorGeneral = 1

    listaTantos = ["15", "30", "40", "win"]
    listaJugadores = [nombreDeJugadorUno, nombreDeJugadorDos]
    print(f"\n🏆{nombreDeJugadorUno} VS {nombreDeJugadorDos}🏆")

    while jugadorUnoSets < 2 and jugadorDosSets < 2:
        #contadores y listas por juego
        jugadorUnoTantos = 0
        jugadorDosTantos = 0
        gameTantosJugadorUno = []
        gameTantosJugadorDos = []

        # Mostrar el título del juego actual
        print(f"\n---- Juego {contadorGeneral} 🎾----")

        while jugadorUnoTantos < 4 and jugadorDosTantos < 4:
            # Seleccionar resultado aleatorio para determinar los tantos
            resultado = random.choice(listaJugadores)
            if resultado == nombreDeJugadorUno:
                ganador = nombreDeJugadorUno
                tantosJugador = jugadorUnoTantos
            else:
                ganador = nombreDeJugadorDos
                tantosJugador = jugadorDosTantos

            # Agregar tantos al jugador y mostrar el resultado
            gameTantos = listaTantos[tantosJugador]
            if resultado == nombreDeJugadorUno:
                gameTantosJugadorUno.append(gameTantos)
                jugadorUnoTantos += 1
            else:
                gameTantosJugadorDos.append(gameTantos)
                jugadorDosTantos += 1
            print(f"{ganador}: {gameTantos}")

        if jugadorUnoTantos == 4:
            # El jugador uno gana el set
            jugadorUnoSets += 1
            jugadorUnoGames += 1  # Incrementar el contador de games para el jugador uno
            setsJugadorUno.append(jugadorUnoSets)
            setsJugadorDos.append(jugadorDosSets)
            for tanto in gameTantosJugadorUno:
                tantosJugadorUno.append(tanto)
            for tanto in gameTantosJugadorDos:
                tantosJugadorDos.append(tanto)
            print(f"\n{nombreDeJugadorUno} gana el set.")
        elif jugadorDosTantos == 4:
            # El jugador dos gana el set
            jugadorDosSets += 1
            jugadorDosGames += 1  # Incrementar el contador de games para el jugador dos
            setsJugadorUno.append(jugadorUnoSets)
            setsJugadorDos.append(jugadorDosSets)
            for tanto in gameTantosJugadorUno:
                tantosJugadorUno.append(tanto)
            for tanto in gameTantosJugadorDos:
                tantosJugadorDos.append(tanto)
            print(f"\n{nombreDeJugadorDos} gana el set.")
        
        contadorGeneral +=1

        # Mostrar el número de juegos ganados por cada jugador hasta el momento
        print(f"\nResultados hasta ahora:")
        print(f"{nombreDeJugadorUno}: {jugadorUnoGames} juegos")
        print(f"{nombreDeJugadorDos}: {jugadorDosGames} juegos")

    # Mostrar resultado final
    print("\nResultado final")
    print(f"{nombreDeJugadorUno}: {jugadorUnoSets} sets")
    print(f"{nombreDeJugadorDos}: {jugadorDosSets} sets")

    # Mostrar al jugador ganador
    if jugadorUnoSets == 2:
        jugadorGanador = nombreDeJugadorUno
    else:
        jugadorGanador = nombreDeJugadorDos

    print(f"🎾 Ganador del juego: {jugadorGanador} 🏆")

tenistasChilenos = ["Nicolás Jarry","Christian Garin","Daniela Seguel","Fernanda Brito",
    "Alejandro Tabilo","Alexa Guarachi","Tomás Barrios","Bárbara Gatica","Gonzalo Lama","Cecilia Costa Melgar"]

# Seleccionar dos jugadores aleatorios de la lista
tenistaRandom1, tenistaRandom2 = random.sample(tenistasChilenos, 2)

# Iniciar el partido con los jugadores seleccionados
partido(tenistaRandom1, tenistaRandom2)
