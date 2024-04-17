import random

guests = [
    ('Diogo','Male','A'),
    ('Amanda','Female','B'),
    ('Pedro','Male','B'),
    ('Bia','Female', 'A'),
    ('Flavia','Female','B'),
    ('Peres','Male','A'),
]

# Definição dos quartos e suas capacidades
rooms = { 
   0: [(0, 120), (1, 120), (2, 120)], 
   1: [(0, 60), (1, 60), (2, 60)], 
   2: [(0, 200), (1, 200), (2, 200)],
   3: [(0, 120), (1, 120), (2, 120)], 
   4: [(0, 60), (1, 60), (2, 60)], 
   5: [(0, 200), (1, 200), (2, 200)],
   6: [(0, 120), (1, 120), (2, 120)], 
   7: [(0, 60), (1, 60), (2, 60)], 
   8: [(0, 200), (1, 200), (2, 200)],
   9: [(0, 120), (1, 120), (2, 120)], 
   10: [(0, 60), (1, 60), (2, 60)]}

solucao = [
  1,0,
  2,0,
  1,1,
  2,1,
  2,2,
  1,2]

def imprimir_quartos(solucao):

  id_quarto = 0
  for i in range( len(solucao) // 2 ):
    name = guests[i][0]
    gender = guests[i][1]
    school = guests[i][2]
    room = rooms[solucao[id_quarto]]
    print(f'{name} {gender} {school} esta no quarto {solucao[id_quarto]} e ele eh o hospede {room[solucao[id_quarto+1]][0]} e o valor da hospedagem eh de {room[0][1]}')
    id_quarto += 2

def funcao_custo(solucao):
  preco_total = 0
  id_quarto = 0
  arrayDidSeen = []

  for i in range( len(solucao) // 2 ):
    if solucao[id_quarto] not in arrayDidSeen:
     arrayDidSeen.append(solucao[id_quarto])
     id_quarto_in_for = 0
     arrayGuests = []
     index = 0
    
     for j in range( len(solucao) // 2 ):
        if solucao[id_quarto_in_for] == solucao[id_quarto]:
          arrayGuests.append(guests[id_quarto_in_for//2])
          if solucao[id_quarto_in_for+1] == 0:
            index = id_quarto_in_for//2
        id_quarto_in_for += 2
     firstSchool = guests[index][2]
     firstGender = guests[index][1]
     #penalidades
     for guest in arrayGuests:
        if guest[2] != firstSchool:
          preco_total += 500
        if guest[1] != firstGender:
          preco_total += 500
          
     room = rooms[solucao[id_quarto]]
     preco_total += room[0][1] * len(arrayGuests)
    id_quarto += 2

  return preco_total

def funcao_custo_p(solucao):
  print(solucao)
  preco_total = 0
  id_quarto = 0
  arrayDidSeen = []

  for i in range( len(solucao) // 2 ):
    if solucao[id_quarto] not in arrayDidSeen:
     arrayDidSeen.append(solucao[id_quarto])
     id_quarto_in_for = 0
     arrayGuests = []
     index = 0
    
     for j in range( len(solucao) // 2 ):
        if solucao[id_quarto_in_for] == solucao[id_quarto]:
          arrayGuests.append(guests[id_quarto_in_for//2])
          if solucao[id_quarto_in_for+1] == 0:
            index = id_quarto_in_for//2
        id_quarto_in_for += 2
     firstSchool = guests[index][2]
     firstGender = guests[index][1]
     #penalidades
     print(arrayGuests)
     for guest in arrayGuests:
        if guest[2] != firstSchool:
          preco_total += 500
        if guest[1] != firstGender:
          preco_total += 500
          
     room = rooms[solucao[id_quarto]]
     preco_total += room[0][1] * len(arrayGuests)
    id_quarto += 2
  return preco_total

def allocate_guests(rooms, guests):
    allocation = []  # Lista para armazenar a alocação de convidados
    room_count = {room: 0 for room in rooms}  # Dicionário para acompanhar quantos convidados foram alocados em cada quarto

    for guest_index, (_, _, _) in enumerate(guests):
        room = random.choice(list(rooms.keys()))  # Escolhe um quarto aleatório

        if room_count[room] < len(rooms[room]):  # Verifica se o quarto não excedeu sua capacidade
            allocation.extend([room, room_count[room]])  # Adiciona o quarto e a posição do convidado à alocação
            room_count[room] += 1  # Atualiza o contador de convidados no quarto
        else:
            for alt_room in rooms.keys():  # Se o quarto estiver cheio, tenta novamente em outro quarto
                if room_count[alt_room] < len(rooms[alt_room]):
                    allocation.extend([alt_room, room_count[alt_room]])  # Adiciona o quarto e a posição do convidado à alocação
                    room_count[alt_room] += 1  # Atualiza o contador de convidados no quarto
                    break

    return allocation

def pesquisa_randomica(funcao_custo):
  melhor_custo = 9999999
  melhor_soluc = []
  for i in range(0, 1000):
    solucao_random = allocate_guests(rooms, guests)
    custo = funcao_custo(solucao_random)
    if custo < melhor_custo:
      melhor_custo = custo
      melhor_soluc = solucao_random
  return melhor_soluc

pr = pesquisa_randomica(funcao_custo)
fc = funcao_custo(pr)
print(fc)
