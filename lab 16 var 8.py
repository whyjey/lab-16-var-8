import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 6, 500)

y = 3 * np.sqrt(x) + x


plt.plot(x, y, linestyle='--', color='green', label=r'$y = 3\sqrt{x} + x$')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y = 3√x + x')
plt.legend()
plt.grid()


plt.savefig('restart.jpg')
plt.show()
from collections import Counter
import matplotlib.pyplot as plt


file_path = 'textlab.txt'  
with open(file_path, 'r') as file:
    
    text = file.read().lower()


words = text.split()


word_count = Counter(words)


words, counts = zip(*word_count.items())


plt.barh(words, counts, color='skyblue')
plt.xlabel('Частота')
plt.ylabel('Слова')
plt.title('Частота появи слів у тексті')
plt.show()
plt.savefig('C:\\Users\\Admin\\Documents\\restart.jpg')
plt.show()
у
plt.savefig('restart.jpg')
plt.show()
import os


if not os.path.exists('images'):
    os.makedirs('images')


plt.savefig('images/restart.jpg')
plt.show()
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 6, 500)

y = 3 * np.sqrt(x) + x


plt.plot(x, y, linestyle='--', color='green', label=r'$y = 3\sqrt{x} + x$')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y = 3√x + x')
plt.legend()
plt.grid()


plt.savefig('restart.jpg')  
plt.show()
from collections import Counter
import matplotlib.pyplot as plt
import os

file_path = 'C:/Users/Admin/Documents/textlab.txt'

