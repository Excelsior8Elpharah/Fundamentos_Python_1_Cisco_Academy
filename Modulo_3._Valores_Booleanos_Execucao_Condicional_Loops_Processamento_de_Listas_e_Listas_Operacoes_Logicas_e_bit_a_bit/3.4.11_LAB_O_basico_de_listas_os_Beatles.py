# Cenário
# Os Beatles foram um dos grupos de música mais populares dos anos 60, e a banda mais vendida na história. 
# Algumas pessoas consideram que eles são o ato mais influente da era do rock. 
# Na verdade, eles foram incluídos na compilação da revista Time das 100 pessoas mais influentes do século XX.
# A banda passou por muitas mudanças na formação, culminando em 1962 com a formação de John Lennon, Paul McCartney, 
# George Harrison e Richard Starkey (mais conhecido como Ringo Starr).

# Etapa 1: Criar uma lista vazia chamada beatles
beatles = []
print("Etapa 1:", beatles)

# Etapa 2: Adicionar John Lennon, Paul McCartney e George Harrison à lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

# Etapa 3: Solicitar ao usuário para adicionar Stu Sutcliffe e Pete Best à lista
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(input(f"Adicione um membro da banda: {member}: "))
print("Etapa 3:", beatles)

# Etapa 4: Remover Stu Sutcliffe e Pete Best da lista
del beatles[4]  # Remove Stu Sutcliffe
del beatles[3]  # Remove Pete Best
print("Etapa 4:", beatles)

# Etapa 5: Adicionar Ringo Starr ao início da lista
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)