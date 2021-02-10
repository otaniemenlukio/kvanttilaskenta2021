#!/usr/bin/env python
# coding: utf-8

# # Tervetuloa kvanttilaskennan lukiokurssille 2021 4.jakso
# 
# Etäluennot MA klo 15.00 - 16.15 ja etäharjoitukset 8-palkissa KE klo 15.00 - 16.15.  Kurssi alkaa 8.2.2021. 
# 
# Luennot ja harjoitukset Streamataan verkkoon osallistua voi myös etänä. Viikottaisia kokoontumisia on yleensä 2 oppituntia. MA Luento ja KE opastettu laskuharjoitus, tehtävät voi palauttaa viikottain perjantaina klo 16.15 mennessä. Voit siis osallistua kurssille myös siten, että seuraat luentojen harjoitusten tallenteita omalla ajalla.
# 
# ## Luentojen ja laskuharjoitusten Meet-linkki ja tiedottaminen
# 
# Olet saanut pysyvän Meet-linkin sähköpostiisi. Luennoilla ja harjoituksissa käytetään __aina samaa linkkiä__.
# 
# 
# Seuraa kurssin tiedottamista sähköpostissasi ja GitHubissa.
# 
# ## Ohjelmointiympäristöt
# 
# Voit valita seuraavista:
# 
# 1 Omalle koneelle asennettu paikallinen Jupyter-ympäristö, asennusohjeet (advanced users):
#   * <a href="https://qiskit.org/documentation/install.html" target ="_blank">IBM QISKIT Installation</a>
#     
#   * <a href="https://drive.google.com/file/d/1wkgPYrJ15oS_SI0BuTMr02ASOzoA-vty/view?usp=sharing" target ="_blank">Lisäohjeita Linux-käyttäjille</a>
# 
#   * Jos käytät Omalla tietokoneella toimivaa Jupyter-ympäristöä, niin sinun on osattava kloonata kurssin GitHub-repositorio tehtävien lataamista varten. Pikaohje, macissa ja linuxissa komentoriviltä eli terminaalista:
# 
#   * repositorion lataus komennolla: `git clone https://github.com/otaniemenlukio/kvanttilaskenta2021`
# 
#   * repositorion päivitys (reposition kansiossa annettava komento): `git pull`
# 
#   * Tehtävät voi myös ladatajaetusta Google-kansiosta, jonka osoitteen olet saanut sähköpostiisi.  
# 
#   * Tehtävien palautus tehdään tällöin __aina samalla Google Form-lomakkeella__, jonka linkin olet saanut sähköpostiisi.
# 
# 2 Verkkoselaimessa toimiva ohjelmointiympäristö (suositellaan, helppokäyttöinen)
#     <a href="https://koodikoulu.net" target ="_blank">koodikoulu.net</a>
# 
#   * Tehtävätiedostot ladataan (fetch) ja palautetaan verkkoympäristön sisällä. Ei edellytä asennuksia omalle koneelle. Suositellaan verkkopalvelun käyttöä, jos asennukset ei onistu tai GitHubin käyttö on sinulle vierasta. Koodikoulu.net-palvelun käyttöä harjoitellaan ensimmäisellä laskuharjoituskerralla.
# 
#   * Kirjautuminen tehdään koodikoulu.net -palveluun gmail-tilillä tai eduespoo.fi-tilillä. Käyttöoikeudet saa Matti Heikkiseltä.
# 
# ## Laskuharjoitustehtävien lataaminen ja palautus
# 
# Tehtävät voi ladata ja palauttaa kahdella eri tavalla.
# 
# 1) Jos käytät omassa tietokoneessa olevaa paikallista Jupyteria
#   * <a href="https://forms.gle/prDEWkMYrXiH5Cne6" target ="_blank"></a>
# 
# 2) Jos käytät koodikoulu.net -verkkopalvelua, niin tehtävät ladataan ja palautetaan palvelun sisällä.
# 
# 
# 

# ### Johdantoesimerkki 1 Jupyter-notebookin suorittaminen
# Kerrataan pythonin perusteet
# int muuttujat  luku1 ja luku2 saavat alkuarvot
# Komennolla print tulostetaan näytölle
# suorita ohjelma yläpaneelista painamalla "run"
# 
# ![run](run.png)
# 
# Testaa myös mitä muista yläpaneelin pikanäppäimistä tapahtuu. Muista talentaa tiedostosi. Klikkaa lopuksi auki tämä solu, jossa on kuva yläpaneelista. Tämä solu ei ole koodiblokki, vaan markdown-kenttä. Huomaa ero.

# In[1]:


luku1 = 4
luku2 = 6
print("Valitut luvut ovat", luku1, "ja", luku2)


# ### Johdantosimerkki 2
# 
# Testaa koodia vaihtamalla muuttujien luku1 ja luku2 arvoja. Tavoite on vain harjoitella Jupyter-notebookin käyttöä. 
# 
# Jos tarvitset lisäharjoitusta python-perusteista, niin lyhyt pikaohje on erillisessä tiedostossa python-perusteet.ipynb. Voita ladata (fetch)-tidoston tai ladata sen kursssin jaetusta google-drivesta.

# In[3]:



luku1 = -2
luku2 = 10
print("Lukujen summa on", luku1 + luku2)


# ## Tehtävä 1: Rekisteröityminen IBM:n palveluun
# 
# Tehtävän 1 tavoiteena on varmistaa että jokainen on saanut oman avaimen eli tokenin aktivoitua qiskit-palvelussa.
# 
# Tehtävä on nopea tehdä: suorita alla olevat koodilohkot järjestyksessä läpi.
# 
# Jos et ole vielä ottanut tokenia käyttöön, tee näin:
# 
# Rekisteröitymisen jälkeen liitä tokenisi [IBM Quantum Experiencen käyttäjäsivulta](https://quantum-computing.ibm.com/account) heittomerkkien sisään, ja aja koodi:

# In[ ]:


from qiskit import IBMQ
IBMQ.save_account("LIITÄ OMA TOKEN")


# Token täytyy syöttää vain kerran, koska se tallennetaan kvanttilaskenta.net-käyttäjäsi tai oman tietokoneen käyttäjäsi yhteyteen.
# 
# **HUOM:** Ennen kuin palautat notebookin, ota tokenisi pois kentästä. Meidän ei tarvitse tietää sitä!
# 
# Alla on yksinkertaisen kvanttipiirin koodi, jotka käsittelimme jo kierroksen 2 laskuharjoituksissa. Rakenna, simuloi ja lähetä piiri lopuksi oikealle kvanttitietokoneelle laskettavaksi.
# 

# $$\newcommand{\ket}[1]{\left|{#1}\right\rangle}$$
# $$\newcommand{\bra}[1]{\left\langle{#1}\right|}$$
# 
# ## Tehtävä 2 Harjoitellaan kvanttipiirin määrittelyä ja ohjelmointia pythonilla.
# 
# Seuraavassa esimerkissä kvanttipiiriä täydennetään kahdella kvanttirekisterillä ja kahdella klassisella rekisterillä. Kvanttipiiri luodaan syöttämällä rekisterit parametrina komennolle QuantumCircuit(). Kun H-portti operoi systeemiin, niin systeemin, niin kubitin 0 tila on määritetty tilojen $\ket 0$ ja $\ket 1$ superpositiona. Kun piirin tila mitataan, niin silloin systeemi siirtyy tiettyyn hyvin määritettyyn tilaan, jonka arvo tallenetaan klassiseen rekisteriin. Tämän jälkeen piirin toiminta simuloidaan, mutta piiriä ei vielä suoriteta oikealla kvanttitietokoneella.
# 
# Tehtävän tavoite on harjoitella kvanttipiirin määrittelyä pythonin avulla. Piirin toiminta selitetään myöhemmin. 
# 
# 
# Kvanttimekaanisella systeemillä jokaisella mahdollisella mitatulla tilalla on tietty todennäköisyys, ja kaikkien eri tilavaihtoehtojen todennäköisyyksien summa on 1.
# 
# Voit halutessasi ohjelmoida piirin toteutuksen ja ajamisvaiheet itse seuraavan tutoriaalin avulla:
# 
# <a href="https://youtu.be/RrUTwq5jKM4" target="_blank">IBM:n "Hello World"-piirin tutoriaali</a>

# In[4]:


# Jos kirjoitat koodin itse, niin aloita tästä.
from qiskit import *


# In[ ]:


# vaihtoehto 1: tyhjä koodiblokki josta voit jatkaa videon ohjeiden mukaisesti


# In[26]:


# Vaihtoehto 2: valmis esimerkkikoodi tehtävään 2 suoritettavaksi.
# Etene vaiheittain, suorita koodilohkot painamalla Run-nappia ylhäältä.

from qiskit import *
# Luodaan kvanttipiiriin 2 kvanttirekisteriä ja 2 klassista rekisteriä
quantum_register = QuantumRegister(2)
classical_register = ClassicalRegister(2)
circuit = QuantumCircuit(quantum_register, classical_register)

get_ipython().run_line_magic('matplotlib', 'inline')
circuit.draw(output='mpl')


# In[27]:


# Lisätään Hadamard-portti H 
circuit.h(quantum_register[0])
circuit.draw(output='mpl')


# In[28]:


# Lisätään kvanttipiiriin CNOT-portti cx()-komennolla
circuit.cx(quantum_register[0], quantum_register[1])
circuit.draw(output='mpl')


# In[29]:


# Mitataan molemmat kubitit, ja tallennetaan tulokset klassiseen rekisteriin
circuit.measure(quantum_register, classical_register)
circuit.draw(output='mpl')


# In[30]:


# Simuloidaan piirin toiminta.
simulator = Aer.get_backend('qasm_simulator')
execute(circuit, backend=simulator)
result = execute(circuit, backend=simulator).result()
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))


# In[35]:


from qiskit import IBMQ
#IBMQ.load_account()
provider=IBMQ.get_provider('ibm-q')
qcomp=provider.get_backend('ibmq_16_melbourne')
job=execute(circuit, backend=qcomp)


# In[36]:


from qiskit.tools.monitor import job_monitor
job_monitor(job)
result=job.result()


# In[37]:



plot_histogram(result.get_counts(circuit))


# ## Johdantoesimerkki 3
# 
# Tutustu esimerkiksi seuraavan esimerkin avulla miten matriisien avulla voidaan esittää xy-tason lineaarisia kuvauksia matematiikassa:
# <a href ="https://www.lukemaverkosto.fi/materiaali/valokuvien-matematiikkaa-geogebralla-ja-ohjelmoimalla-osa-1-2/" target="_blank">xy-tason lineaarikuvaukset</a>
# 
# Lasketaan esimerkkinä seuraava $2x2$ matriisin $A$ ja pystyvektorin $v$ tulo:
# ![tulo1](tulo1.png)
# 
# Aukikirjoitetutta algebra etenee seuraavasti:
# ![tulo2](tulo2.png)
# 
# Pythonissa matriisin $A$ ja pystyvektorin $v$ tulo voidaan esitettää seuraavasti:
# 

# In[12]:


import numpy as np

#lineaarinen kuvaus a
A = np.array([[3, 2],[-2, 1]])
print("tulostetaan matriisi A")
print(A)

# pystyvektori v
v = np.array([[-1],[1]])
print("tulostetaan pystyvektori v")
print(v)

# lasketaan tulo
u = A@v
print("tulostetaan pystyvektori u")
print(u)


# $$\newcommand{\ket}[1]{\left|{#1}\right\rangle}$$
# $$\newcommand{\bra}[1]{\left\langle{#1}\right|}$$
# 
# ## Tehtävä 3
# 
# Kvanttitietokoneen muistissa tieto esitetään kubittien avulla. Kubitin perustilat ovat $\ket 0$ ja $\ket{1}$, ja ne esitetään pystyvektoreina
# 
# $$
# \begin{align}
# \ket 0 &= \pmatrix {1 \\ 0}, \\
# \ket 1 &= \pmatrix {0 \\ 1}.
# \end{align}
# $$
# 
# NOT-portin matriisiesitys on seuraava:
# 
# $$
# X=\pmatrix {0 & 1 \\ 1 & 0}
# $$
# 
# Osoita laskemalla matriisin $X$ ja pystyvektorien tulot, että kun $X$-portti operoi kubittiin, niin kubitin tila muuttuu käänteiseksi (bit-flip gate), eli
# 
# $$
# X\ket 0 = \ket 1 \\
# X\ket 1 = \ket 0
# $$

# In[18]:


# Laske tehtävä tähän pythonilla:
# määritellään pystyvektorina kubitin tila 0:
q0 = np.array([[1],[0]])
print("tulostetaan kubitin tila 0: ")
print(q0)

q1 = np.array([[0],[1]])
print("tulostetaan kubitin tila 1: ")
print(q1)

X =  np.array([[0, 1],[1, 0]])
print("NOT portin matriisiesitys")
print(X)

print("Xq0 = q1")
print(X@q0)

print("Xq1 = q0")
print(X@q1)


# In[19]:


# sama määrittely qiskitin työkaluilla:
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram#, plot_bloch_vector
from math import sqrt, pi


# In[23]:


# luodaan kvanttippiri yhdelle kubitille
qc = QuantumCircuit(1) # oletus kubitti 0 tilassa
initial_state = [0,1]  # state |1>
qc.initialize(initial_state,0)
qc.draw()


# In[ ]:





# In[21]:


backend = Aer.get_backend('statevector_simulator')
result = execute(qc,backend).result()
out_state = result.get_statevector()
print(out_state)


# In[22]:


from qiskit.visualization import plot_bloch_multivector
plot_bloch_multivector(out_state)


# ## Tehtävä 4
# Lue johdantoartikkeli <a href="https://www.lukemaverkosto.fi/materiaali/johdanto-kvanttilaskentaan/" target ="_blank">Kvanttitietokoneet ja kvanttilaskennan perusteet</a>
# 
# a) Artikkelin esimerkin avulla muunna binääriluvuksi 10-järjestelmän luku $123_{10}$ 
# 
# b) Kokeile kuvata seuraava klassisen tietokoneen loogisen portin toiminta totuustaulukon avulla.
# ![gate](gate.png)
# Käyttämällä apuna seuraavaa liitettä
# 
# <a href ="https://drive.google.com/file/d/1QiqiPUY9S8bUTxdQkYb5NK-fqpYoyE-E/view?usp=sharing" target="_blank">Loogiset peruspiirit</a>

# Esitetään luku 123 binäärijärjestelmässä
# Kakosen potensseja:
# $2^0=1$ ja $2^4=16$  ja $2^5=32$ ja $2^6=64$
# 
# $123_{10} = 64 + 32 +16 +8 +2+1 = 1*2^4 +1*2^5 +1*2^4+1*2^3+0*2^2+1*2^1+1*2^0 =1111011_{2} $  

# 

# In[25]:


print("10-järjestelmän luku 123 binäärilukuna")
print(bin(123))


# ![table](table.png)

# In[ ]:




