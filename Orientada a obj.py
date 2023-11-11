#CLASSES E OBJETOS
#CLASSE PODE SER UMA RECEITA QUE DEFINE A ESTRUTURA E O COMPORTAMENTO DOS OBJETOS
#ATRIBUTOS  SAO VARIAIVES QUE PERTENCEM A UM OBJETOS> EX> CARRO, COR, QUANTIDADE DE PORTAS..
#MÉTODOS REALIZAM OPERAÇÕES RELACIONADAS A OBJETOS EX: O QUE FAZER COM O CARRO: (LIGAR, ACELERAR...)
#HERANÇA - PODE HERDAR OU NÃO A CLASSE
#ENCAPSULAMENTO AGRUPAMENTO DE ATRIBUTOS E METODOS
#POLIFORMISMO CAPACIDADE DE OBJETOS DIFERENTES DE RESPONDER A MENSAGENS...

# A classe pode ser exemplificada como a planta de uma casa. Ou seja, é a partir da classe que nasce o objeto(casa)
#__init__ é o construtor (Quarda os parametros)
#ex:class planta:
    # def __init__(self, comprimento, cor):
    #     self.comprimento = comprimento
    #     self.cor = cor

#INSTANCIANDO
# class house:
#     pass
# house = House()
# print (house)

class user:
    def __init__(self,nome, idade ):
      self.nome = nome
      self.idade = idade

    def display(self):
     print(self.nome, self.idade)
#instanciado
nome= input( "Digite o nome: ")
idade= input( "Digite a idade: ")
user = user(nome, idade)
user.display()
# nome2= input( "Digite o nome: ")
# idade2= input( "Digite a idade: ")
# user2 = user(nome, idade)
# user2.display()


#----------------------------------------------------------------------------
class House:
   def __init__(self, length):
      self.length = length
      self.color = 'color'

def display(self):
    print(self.length, self.color)

house = house(100, 'green')
print (house.comprimento, house.color )

house2 =  house(200, 'red')
house2.display()

#exercicios

class user:
    def __init__(self,nome, idade ):
      self.nome = nome
      self.idade = idade

    def display(self):
     print(self.nome, self.idade)
#instanciado
nome= input( "Digite o nome: ")
idade= input( "Digite a idade: ")
user = user(nome, idade)
user.display()
nome2= input( "Digite o nome: ")
idade2= input( "Digite a idade: ")
user2 = user(nome, idade)
user2.display()


#----------------------------------------------------------------------------
class House:
   def __init__(self, length):
      self.length = length
      self.color = 'color'

def display(self):
    print(self.length, self.color)

house = house(100, 'green')
print (house.comprimento, house.color )

house2 =  house(200, 'red')
house2.display()

# 1 - Crie uma classe chamada Cachorro com um atributo nome e um método 
# latir que imprima "Woof!" quando chamado. 
# Em seguida, crie um objeto da 
# classe Cachorro e chame o método latir.
class Dog:
  def __init__(self, nome, raca):
    self.nome = nome
    self.raca = raca

  def latir(self):
    print('Wooolf')
#instanciado
nome = input('Nome do cachorro:')
raca = input('Qual a raça: ')
latir = ('Agora de um latido')
dog = Dog(nome, raca)
dog.latir()

# 2Crie uma classe chamada Retangulo com atributos largura e 
# altura. Adicione um método chamado calcular_area que retorna a área do retângulo.

class Retangulo: 
  def __init__(self, largura, altura):
    self.largura = largura
    self. altura = altura

  def calcular_area(self):
    print(self.largura * self.altura)
    
  #instanciado
largura = 5
altura = 4
retangulo = Retangulo(largura, altura)
retangulo.calcular_area()
  
# 3: Crie uma classe chamada Carro com um atributo chamado velocidade 
# (inicialmente 0). Em seguida, adicione um método chamado acelerar que aumenta a
# velocidade em 5 unidades.

class Carro:
 def __init__ (self, velocidade):
   self.velocidade = velocidade  
      
 def acelerar(self):
   self.velocidade +=5
   print(self.velocidade)
#instanciado
velocidade = float(input('Digite a velocidade: '))
carro = Carro(velocidade)
carro.acelerar()

##desafio da aula:
