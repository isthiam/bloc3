with open('.env', 'rb') as f:
    content = f.read()
    print(content.decode('utf-8'))  # Cela provoquera une erreur si un caractère est invalide
