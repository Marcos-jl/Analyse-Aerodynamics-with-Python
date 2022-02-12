# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:53:36 2021

@author: Marcos
"""

#bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import math
import gspread

credentials = {
  "type": "service_account",
  "project_id": "analog-vault-312313",
  "private_key_id": "8c20f0fb97b27817ca9f7b7179ec91a63eba4f26",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1j/wkjo0oICty\n7Rxihboo3e1eY/uNXewOmJzTBMWQ5ezlTC2nY9EEWvVvSPAtEtiAROQJ/FI6lY5R\nt8UhKct3rRD6G57sCHsqK35hByy7FfiLQ7DGmbThVqoN1pisPUjhDE1Y3GUyihHQ\n6YM2VpWgttyAPc/TtqPcU6lJ8guHJnaTQPcecHgiJoExNrjCFDXwUZC400rib1P4\n4JgZTVlfg9ILD45vrgeTYOv8KH/r3aOqxUCrPhLFQLVX6G/oT94Kv3QvOk67gkBO\nE//AzkUK/2ETmL8UoMqVxifjqmbxSaLVXSDIG6oIiUFFdutJ6AfIbFpclXijLN37\nWSD4VS1pAgMBAAECggEAOTbCUhLJ0Jcymei2RSW24CHvJwuCva2XMZJN+QFL8LlD\nyY4T5OfDegffx83IQavqpaEP60Wj8+olCwNKD4VIJNJYwzfpAKA7j7JdBN5p7hqi\nU+Bk2HCfW1MgC3RQcBZv3NsvlIz/Jsnzi03Kl1j5lceJ/K99yk2HnWqPskmf8Fpa\njKgU1pOWkBJ0f69xfqDQSq9+6kTGA14h0i3sVI2LOKAS+oSQbb16ceNdZYdJUjcD\ns2obsy9WfJk/8+aQdq8KzP8+tY19Gvned+0ts+nMPDPN2SAPxBBBUYD/1dyUuxkm\nxSQxm+jdt9PJxF+kyDFmVXVAWLA1fRAH6z3AbCdgsQKBgQDgxNY4PWdjWicrBk5l\nRxBw81SHc8d7Ul676k5qvwU8dIsq2Vrct/PWLvTeaJ0yWX7ZDeQoafTa7abCT35V\ndwQ5ajhAf5oAUTFXhOcGX61Fg3Wv3LFLAZRx6Mmb7O50ANgncmf+MgxT8PJ/9TSy\nOibemW6VE45ogrjE0VbrEeig6wKBgQDOykTYYbMW0YE9DUHcAg1A2q3hiAmTdzi9\n71YmYVlSPi5oF3tWzWvZPZNhtWa5fyCwZw8FJjmtgTrkC1u4M7gDraR1uLKR19vf\nyfkwTfI9L8ZCCVzbNOneYX3YFrXeHjw0wElkoVWTd8/bC54WQYJoBSXchBMiaEgB\nnvSg+hx1+wKBgAT613QviBbfbHa7kQkVZfvaqEjH++dzj73CFzKuQMNyIZM1dZnm\nSXS5XZt/3du7t9+/OwraLh6bnVI4yKfEF0feXpivOw4+vkUeILA3dnNP0k+vKA5t\nXoiXi7/0o+PWEPPuyPcMzNEfSYAkQqKgPzQ3WgfbgxA1tTpHGRHkN685AoGAewD3\n+JoM1CrkrDMhlMOnrIcnXPr1b0FAgEJIRWYsom4YXpRxKk3gtAUbkMg9hWNoR2XW\nGmMFdf5j0FgtQ6GH+LAmHlwx4+y5fiF+10vWJq0vSgKVuFJ+NmhZWdsQbUIg3+Pt\nBC2vYJupCQudCnIHJubBAa2SUColgslRjBuaKFcCgYEAnqjiDbmJsEMcWRPIMt+i\nCyPfsntXFLtqApeKw5hZ9IXOQSNMAE9dgM0sy8C2/F0jH/tj9Rh2If5A9OTwByNC\nUDgRH8EyIupInJrn8vl8LTUrRYcSNLr7y8+j2D7nYowwYeQwf+Z4oZGqoVdUQXaY\nAlE1VDOMIF1TpuTs64rwi5Q=\n-----END PRIVATE KEY-----\n",
  "client_email": "planilhas@analog-vault-312313.iam.gserviceaccount.com",
  "client_id": "113464153978373098448",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/planilhas%40analog-vault-312313.iam.gserviceaccount.com"
}
  

#Asa mista da Aeronave
class wing:
    def __init__(self, cr, ct, af, c, b_ret, b_tra, b, S_ret, S_tra, S, AR, e):
             
        #Parametros do Google SpreadSheet
        self.gc = gspread.service_account_from_dict(credentials)
        self.sh = self.gc.open("Lista de Perfis Asa (Seleção Preliminar)")
        self.worksheet = self.sh.get_worksheet(0)
    
        #Parâmetros Aerodinâmicos
        self.perfil = str(self.worksheet.acell('b2').value) #Perfil de asa
        self.Re = (self.worksheet.acell('b1').value) #Reynolds do perfil
        self.alpha = self.worksheet.get('a4:a24') #Ângulo alpha
        self.CL =  self.worksheet.get('j4:j24')  #Força de sustentação
        self.CD =  self.worksheet.get('c4:c24')  #Força de Arrasto
        self.CM =  self.worksheet.get('d4:d26')  #Coeficiênte de momento

        #Reparando falhas do gspread
        self.CL_array = np.array(self.CL)
        self.CD_array = np.array(self.CD)
        self.CM_array = np.array(self.CM)
        self.alpha_array = np.array(self.alpha)
        self.CL_list = list()
        self.alpha_list = list()
        self.CD_list = list()
        self.CM_list = list()

        #Atribuindo ângulo cl, alpha nas respectivas listas criadas 
        for i in range(0, len(self.alpha)):
            self.CL_list.append(float (self.CL_array[i]))
            self.alpha_list.append(float (self.alpha_array[i]))
            self.CD_list.append(float (self.CD_array[i]))
            self.CM_list.append(float (self.CM_array[i]))

        #Eficiência CL/CD        
        self.efficiency_list = list()
        for i in range(0, len(self.CL_list)):
            self.efficiency_list.append(self.CL_list[i]/self.CD_list[i])

        #Arrasto induzido
        self.CDi = list()    
        for i in range(0, len(self.CL_array)):
            self.CDi.append(math.pow(self.CL_array[i], 2)/(math.pi*e*AR))

    
    #Gráfico do arrasto induzido
    def Drag(self):
        plt.xlabel('Coeficiente de Sustentação (CL)')
        plt.ylabel("Coeficiente de Arrasto Induzido (CDi)")
        plt.title("Análise de Arrasto Induzido\n{} - {} Reynolds".format(self.perfil, self.Re))
        plt.plot(self.CL_list, self.CDi, label='CDi', color='#DC143C')
        plt.scatter(self.CL_list, self.CDi, label='CDi', color='#DC143C')
        plt.savefig('analyse project/drag analyse.png', format='png', dpi=300)
        plt.show()
       
       
    #Gráfico de sustentação
    def Lift(self):
        plt.xlabel('Coeficiente de ângulo de ataque (alpha)')
        plt.ylabel("Coeficiente de Sustenção (CL)")
        plt.title("Análise de Sustentação\n{} - {} Reynolds".format(self.perfil, self.Re))
        plt.plot(self.alpha_list, self.CL_list, label='CL', color='#2E8B57')
        plt.scatter(self.alpha_list, self.CL_list, label='CL', color='#2E8B57')
        plt.savefig('analyse project/lift analyse.png', format='png', dpi=300)
        plt.show()
        
    #Gráfico de Eficiência
    def Efficiency(self):
        plt.xlabel('Coeficiente de Sustentação (CL)')
        plt.ylabel("Coeficiente de Eficiência (CL/CD)")
        plt.title("Análise de Eficiência\n{} - {} Reynolds".format(self.perfil, self.Re))
        plt.plot(self.CL_list, self.efficiency_list, label='CL/CD', color='#4B0082')
        plt.scatter(self.CL_list, self.efficiency_list, label='CL/CD', color='#4B0082')
        plt.savefig('analyse project/Efficiency analyse.png', format='png', dpi=300)
        plt.show()
        
        
    #Gráfico de Momentos
    def Moment(self):
        plt.xlabel('Coeficiente de ângulo de ataque (alpha)')
        plt.ylabel("Coeficiente de Momento (CM)")
        plt.title("Análise de Momentos\n{} - {} Reynolds".format(self.perfil, self.Re))
        plt.plot(self.alpha_list, self.CM_list, label='CL/CD', color='#D2691E')
        plt.scatter(self.alpha_list, self.CM_list, label='CL/CD', color='#D2691E')
        plt.savefig('analyse project/Moment analyse.png', format='png', dpi=300)
        plt.show()
        

