nome = input(("qual é o seu nome: "))

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = ((nota1 + nota2 + nota3) / 3)

if media >= 7: 
    print("Parabens voce passou")
else: 
    print("REPROVADO :(")

print(f"A media do aluno {nome} é: {media: .1f}")

