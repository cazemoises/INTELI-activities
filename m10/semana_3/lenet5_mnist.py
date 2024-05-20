"""
Treina uma CNN com o dataset MNIST.
A CNN é inspirada na arquitetura LeNet-5, com algumas
alterações nas funções de ativação, padding e pooling.
"""
# importar pacotes necessários
from keras.utils import to_categorical
from keras.optimizers import SGD
from keras import backend
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from cnn import LeNet5     # ESTA É A CLASSE CRIADA POR NÓS

# importar e normalizar o dataset MNIST
dataset = fetch_mldata("MNIST Original")
labels = dataset.target
data = dataset.data.astype("float32") / 255.0

# dividir o dataset entre train (75%) e test (25%)
(trainX, testX, trainY, testY) = train_test_split(data, labels)
# Transformar labels em vetores binarios
trainY = to_categorical(trainY, 10)
testY = to_categorical(testY, 10)

# inicializar e otimizar modelo
print("[INFO] inicializando e otimizando a CNN...")
model = LeNet5.build(28, 28, 1, 10)
model.compile(optimizer=SGD(0.01), loss="categorical_crossentropy",
              metrics=["accuracy"])

# treinar a CNN
print("[INFO] treinando a CNN...")
H = model.fit(trainX, trainY, batch_size=128, epochs=20, verbose=2,
          validation_data=(testX, testY))

# plotar loss e accuracy para os datasets 'train' e 'test'
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0,20), H.history["loss"], label="train_loss")
plt.plot(np.arange(0,20), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0,20), H.history["acc"], label="train_acc")
plt.plot(np.arange(0,20), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig('cnn.png', bbox_inches='tight')