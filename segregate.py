import os
import cv2
import numpy as np
import shutil

import tensorflow as tf

class Docs:

    def __init__(self, labels_pth):
        self.img_size = 500
        with open(labels_pth, "r") as f:
            self.labels = [line.rstrip('\n') for line in f]
        f.close()

    def load_model(self, model_pth):
        print("Loading model")
        self.model = tf.keras.models.load_model(model_pth)
        print("Successfully loaded the model")

    def load_data(self, data_pth) : 
        
        self.data_pth = data_pth
        self.doc_pths = []
        self.docs = []

        print("Loading Data")

        for doc in os.listdir(data_pth):
            if doc.lower().endswith(('.png', '.jpg', '.jpeg')):
                self.doc_pths.append(os.path.join(data_pth, doc))

        for doc_pth in self.doc_pths :
            self.docs.append(cv2.resize(cv2.imread(doc_pth, cv2.IMREAD_COLOR), (self.img_size, self.img_size)))

        print("Successfully Loaded all the data")

    def segregate(self, output_dir):

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        self.preds = self.model.predict(np.array(self.docs))

        for i in range(len(self.doc_pths)):
            index = np.argmax(self.preds[i])
            label = self.labels[index]

            output_label_dir = os.path.join(output_dir, label)

            if not os.path.exists(output_label_dir):
                os.mkdir(output_label_dir)
            
            src_path = self.doc_pths[i]
            dest_path = os.path.join(output_label_dir, os.path.basename(src_path))
            print(dest_path)
            shutil.copy(src_path, dest_path)
            print(f"Successfully Segregated all the documents in {self.data_pth} to {output_dir}")

doc = Docs("classes.txt")
doc.load_data("docs")
doc.load_model("models/model_3_img_500.h5")
doc.segregate("classified_docs")