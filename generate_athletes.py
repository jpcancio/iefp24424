import csv
import random
from datetime import datetime, timedelta

# Lists for generating random names
first_names = [
    "João", "Miguel", "António", "Pedro", "Diogo", "Manuel", "Ricardo", "André", "Francisco",
    "Tiago", "Paulo", "Carlos", "José", "Rui", "Fernando", "Jorge", "Daniel", "Hugo", "Bruno",
    "Gonçalo", "David", "Nuno", "Luís", "Marco", "Rafael", "Gabriel", "Guilherme", "Tomás",
    "Vasco", "Eduardo"
]

last_names = [
    "Silva", "Santos", "Ferreira", "Costa", "Oliveira", "Rodrigues", "Martins", "Sousa",
    "Carvalho", "Fernandes", "Pereira", "Almeida", "Ribeiro", "Pinto", "Marques", "Lopes",
    "Monteiro", "Rocha", "Nunes", "Cardoso", "Teixeira", "Correia", "Mendes", "Gomes",
    "Reis", "Guerreiro", "Henriques", "Dias", "Vieira", "Fonseca"
]

positions = [
    "Guarda-Redes", "Ponta Esquerda", "Ponta Direita", "Pivot",
    "Lateral Esquerdo", "Lateral Direito", "Central"
]

# Generate random date between 1990 and 2005
def random_date():
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2005, 12, 31)
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

# Generate 500 athletes
athletes = []
for _ in range(5000):
    athlete = {
        'nome': random.choice(first_names),
        'apelido': random.choice(last_names),
        'data_nascimento': random_date(),
        'posicao': random.choice(positions),
        'mao': random.choice(['Direita', 'Esquerda'])
    }
    athletes.append(athlete)

# Write to CSV file
with open('atletas.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['nome', 'apelido', 'data_nascimento', 'posicao', 'mao']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(athletes)
