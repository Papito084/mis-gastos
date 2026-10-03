import sys, os

# Read the original file  
src = open('gastos-mensuales.html', 'r', encoding='utf-8').read()

# Build the new HTML
# Categories definition
cats = [
    ('alimentacion',  'Alimentacion',      '\U0001f6d2', '#34d399'),
    ('transporte',    'Transporte',         '\U0001f697', '#60a5fa'),
    ('ocio',          'Ocio',               '\U0001f389', '#f472b6'),
    ('restaurantes',  'Restaurantes',       '\U0001f37d\ufe0f', '#fb923c'),
    ('salud',         'Salud y Farmacia',   '\U0001f48a', '#f87171'),
    ('hogar',         'Hogar y Servicios',  '\U0001f3e0', '#fbbf24'),
    ('ropa',          'Ropa y Moda',        '\U0001f457', '#c084fc'),
    ('tecnologia',    'Tecnologia',         '\U0001f4bb', '#38bdf8'),
    ('educacion',     'Educacion',          '\U0001f4da', '#4ade80'),
    ('viajes',        'Viajes',             '\u2708\ufe0f', '#a78bfa'),
    ('suscripciones', 'Suscripciones',      '\U0001f4cb', '#94a3b8'),
    ('otros',         'Otros',              '\U0001f4e6', '#fb923c'),
]

print('OK - script ran, categories:', len(cats))
