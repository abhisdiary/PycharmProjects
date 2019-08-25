import convert_images_to_numpy_arrays

image_grey = convert_images_to_numpy_arrays.image_grey
print(image_grey[0:2])
print(image_grey[0:2, 2:4])
print(image_grey.shape)  # array size

# iterating over numpy array
for i in image_grey:
    print(i)
# Iterating over every single values
for i in image_grey.flat:
    print(i)
