'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificios indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
import time
for cont in range (10, -1, -1):
  time.sleep(1) #´Para puxar a função SLEEP da biblioteca TIME, basta inserir um PONTO (.) E refrenciar a biblioteca. Outra opção seria inserir no lugar do import = from time import sleep e nesta linha usar apenas sleep()
  print(cont)
print ('BOOOOM BOOMMM BUMMMM!!!')