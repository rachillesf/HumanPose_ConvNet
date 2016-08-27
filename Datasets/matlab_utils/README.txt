Matlab scripts used for extract single person images from LEEDS and FLIC dataset.
The images were croped arround the person based on the largest x and y joint position, then added to a frame in order to make then square shaped, the frame was build using the RGB channels global mean.
Next, the images were resized to 220x220.

All the joints localization were adjusted to those changes.


The provided scripts still lacks generalization due to the fact that they were build on-the-fly and with a bit of hurry, any contribution is welcome!



