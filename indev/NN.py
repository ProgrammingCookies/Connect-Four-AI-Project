import tensorflow as tf

#git remote test

#Process input data

# Convert the array to one-hot encoding using tf.one_hot()
one_hot_arr = tf.one_hot(arr, depth=3)

# Reshape the one-hot array to match the expected input shape of the model
one_hot_arr = tf.reshape(one_hot_arr, [1, 6, 7, 3])



# Define the input layer with 126 neurons
input_layer = tf.keras.layers.Input(shape=(18,7))

# Reshape the input layer to have a single channel
reshaped_input = tf.reshape(input_layer, [-1, 18, 7, 1])

# Define the convolutional layer with  21 neurons in the second layer. Each neuron being covering one 3x3 patch of the gameboard. 
conv_layer = tf.keras.layers.Conv2D(filters=21, kernel_size=(9, 3), strides=(1, 3), padding="valid", activation="relu")(reshaped_input)

# Flatten the output of the convolutional layer
flattened_layer = tf.keras.layers.Flatten()(conv_layer)

# Define the output layer with 7 neurons
output_layer = tf.keras.layers.Dense(units=7, activation="softmax")(flattened_layer)

# Create the model with the input and output layers
model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.CategoricalCrossentropy(), metrics=["accuracy"])

# Print the model summary
model.summary()

#TODO
#Remaking a square into one hot encoding

