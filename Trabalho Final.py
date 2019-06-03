#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import pandas as pd

#Extraindo as bases necessárias 

data_ies = pd.read_csv("Desktop\Projeto - Pandas\Dados\ies.csv", sep="|", encoding="ANSI")
#data_ies

#Criando Data Frame com as colunas necessárias
data_ies_colunas = pd.DataFrame(data_ies, columns=['CO_IES',  'NO_IES',  'SGL_IES', 'DS_CATEGORIA_ADMINISTRATIVA', 
                                           'DS_ORGANIZACAO_ACADEMICA', 'NO_MUNICIPIO_IES', 'SGL_UF_IES'])

data_ies

# Plotando um gráfico

data_ies_colunas.plot(kind='bar', figsize=(11,5), rot=0, color='green')
plt.show()


# In[11]:


import numpy as np
import pandas as pd

data_docente = pd.read_csv("Desktop\Projeto - Pandas\Dados\docente.csv", sep="|", encoding="ANSI")
data_docente


# In[13]:


import numpy as np
import pandas as pd

data_local_oferta = pd.read_csv("Desktop\Projeto - Pandas\Dados\local_oferta.csv", sep="|", encoding="ANSI")
data_local_oferta


# In[25]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

data_aluno = pd.read_csv('Desktop/Projeto - Pandas/Dados/aluno.csv', sep="|", encoding="ANSI")
data_aluno


# In[ ]:




