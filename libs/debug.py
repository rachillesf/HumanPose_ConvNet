from input_data import *
from GLOBAL import *

d = Dataset()

[x_batch,y_batch] = d.next_batch("Train",10)

print y_batch
io.imshow(x_batch[0])
io.show()
