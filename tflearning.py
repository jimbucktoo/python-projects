import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

learn = tf.contrib.learn
tf.logging.set_verbosity(tf.logging.ERROR)

mnist = learn.datasets.load_dataset('mnist')
data = mnist.train.images
labels = np.asarray(mnist.train.labels, dtype=np.int32)
test_data = mnist.test.images
test_labels = np.asarray(mnist.test.labels, dtype=np.int32)

max_examples = 10000
data = data[:max_examples]
labels = labels[:max_examples]


def display(i):
    img = test_data[i]
    plt.title('Example %d. Label: %d' % (i, test_labels[i]))
    plt.imshow(img.reshape((28,28)), cmap=plt.cm.gray_r)

plt.show(display(8))

print(len(data[0]))

feature_columns = learn.infer_real_valued_columns_from_input(data)
classifier = learn.LinearClassifier(feature_columns=feature_columns, n_classes=10)
classifier.fit(data, labels, batch_size=100, steps=1000)
classifier.evaluate(test_data, test_labels)
print(classifier.evaluate(test_data, test_labels)["accuracy"])

new_samples = np.array([test_data[8]], dtype=float)
y = list(classifier.predict(new_samples, as_iterable=True))
print("Predicted %s, Label: %d" % (str(y), test_labels[8]))

weights = classifier.weights_
f, axes = plt.subplots(2, 5, figsize=(10,4))
axes = axes.reshape(-1)
for i in range(len(axes)):
    a = axes[i]
    a.imshow(weights.T[i].reshape(28, 28), cmap=plt.cm.seismic)
    a.set_title(i)
    a.set_xticks(())
    a.set_yticks(())

plt.show()