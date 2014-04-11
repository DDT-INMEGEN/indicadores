import numpy as np
import matplotlib.pyplot as plt
import matplotlib


niveles_sni = [ 'candidato', 'nivel I', 'nivel II', 'nivel III' ]

years = range(2007,2014)

m = [ [5, 7, 7,  8,  3,  3,  6],
      [6, 7, 10, 11, 18, 19, 20],
      [0, 1, 2,  2,  2,  2,  2],
      [0, 0, 0,  2,  2,  3,  4] ]

# fig = plt.figure(figsize=(40,40))
plt.imshow(m, interpolation='none')
plt.xticks(range(len(years)), years)
plt.yticks(range(4),niveles_sni)
plt.colorbar()
plt.set_cmap('jet')
# plt.savefig('niveles_sni.svg')
plt.savefig('niveles_sni.png')



plazas = {'ICM A': [3, 4, 2, 6, 9, 8, 9],
          'ICM B': [10, 12, 8, 10, 7, 9, 8],
          'ICM C': [9, 10, 10, 10, 13, 11, 16,],
          'ICM D': [1, 2, 8, 9, 10, 13, 13],
          'ICM E': [1, 2, 2, 0, 1, 1, 1],
          'ICM F': [0, 0, 0, 0, 3, 0, 2],}

rows = [plazas[p] for p in plazas]

plt.imshow(rows, interpolation='none')
plt.xticks(range(len(years)), years)
plt.yticks(range(6),plazas.keys())
plt.set_cmap('jet')
# plt.savefig('niveles_sni.svg')
plt.savefig('plazas.png')
