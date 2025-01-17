#primeira letra maiuscula e estilo camelcase


#class NomeDela:
    #conteudo dela

# class Animal:
#     pass

# leao = Animal()
# macaco = Animal()
# print(type(leao))
# print(type(macaco))

# class Carro:

#     def __init__(self, portas, cor):
#         self.portas = portas #publico
#         self.__arcondicionado = True #privado

# carroPai = Carro(4, 'prata')
# print(carroPai.portas)


# class Sapato:
#     qtdd = 7

#     def __init__(self, cor, tamanho, preco, qtddComprada):
#         self.preco = preco
#         self.qtddComprada = qtddComprada
#         self.cor = cor
#         self.tamanho = tamanho

# tamanco = Sapato(cor='azul', tamanho=42, preco=1200, qtddComprada=10)
# print(tamanco.preco)







#@classmethodé pra categorizar o metodo de classe


class Myclass:
    @classmethod
    def class_method(cls, x, y):
        return
    
result = Myclass.class_method(x=3, y=5)
print(result)


# @staticmethod é pra nao precisar modificar as instancias da classe

