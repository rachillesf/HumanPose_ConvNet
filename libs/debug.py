from input_data import *
from GLOBAL import *

d = Dataset()

batch = d.next_batch("Train",10)
print np.shape(batch)
io.imshow(batch[0])
io.show()
