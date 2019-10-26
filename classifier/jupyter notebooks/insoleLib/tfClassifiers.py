import os
import pandas as pd
import numpy as np
from columns import DataColumns
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import keras

#sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
#print("Session: ", sess)
#keras.backend.set_session(sess)

#gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.3)
#sess = tf.Session(config=tf.ConfigProto(
#allow_soft_placement = True, log_device_placement=True))


import matplotlib.pyplot as plt
import seaborn as sn

# https://www.tensorflow.org/tutorials/keras/basic_classification

# https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/

class TfClassifiers:
    """
    Neaural network classifiers that are implemented with tensorflow/keras.
    """

    @staticmethod
    def testNn(data, x_cols, y_cols, plots=False, orig_acc=0, orig_auc=0):
        """
        Testing basic neural network classifier with two hidden layers
        
        Arguments:
            data {[type]} -- [description]
            x_cols {[type]} -- [description]
            y_cols {[type]} -- [description]
        
        Keyword Arguments:
            plots {bool} -- [description] (default: {False})
            orig_acc {double} -- [description] (default: {0})
            orig_auc {double} -- [description] (default: {0})
        """
        
        
        data = shuffle(data)
        x = data.loc[:, x_cols]
        y = data.loc[:, y_cols]
        
        y_dummies = pd.get_dummies(y) #to binary labels
        bin_cols = ["label_Normal","label_Fall"]
        
        dimensions = x.shape[1]
        print("dimensions ", dimensions)
        
        ##encode class values as integers
        #encoder = LabelEncoder()
        #encoder.fit(y)
        #y = encoder.transform(Y)
        #dummy_y = np_utils.to_categorical(y) # convert to dummy one hot encoding
        
        y = y_dummies
        
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0, shuffle=True) #used for suffling for now
        
        #Defining model
        model = Sequential()
        model.add(Dense(dimensions, input_dim=dimensions, activation='relu'))
        model.add(Dense(dimensions, activation='relu'))
        model.add(Dense(2, activation='softmax'))
        
        #Compiling the model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        
        #early stop
        early_stop = EarlyStopping(monitor='val_loss', patience=80, verbose=1, mode="auto")
        
        accuracy_a = []
        real_label = []
        pred_label = []
        
        #Fitting model
        model.fit(xtrain, ytrain, epochs=200, batch_size=10, callbacks=[early_stop], validation_split = 0.3, verbose=1)
        
        np_xtest = np.array(xtest) #converting to numpy array
        ypred = model.predict(xtest, verbose=1)
        
        pred_label.append(ypred)
        real_label.append(ytest.values)
        
        ytest_nondum = ytest.idxmax(axis=1)
        print("ytest", ytest)
        print("ypred", ypred)
        
        acc = accuracy_score(ytest_nondum, ypred)
        accuracy_a.append(acc)
        
        avg_acc = np.mean(accuracy_a)
        print("NN Average accuracy ", avg_acc)
        
        pred_label_df = pd.DataFrame(columns=["label"])
        real_label_df = pd.DataFrame(columns=["label"])
        
        #Forming the dataframes
        #for row in range(0,len(pred_label)):
        #    label_str = pred_label[row][0]
        #    pred_label_df.loc[row] = label_str
        #
        #for row in range(0,len(real_label)):
        #    label_str = real_label[row][0][0]
        #    real_label_df.loc[row] = label_str
        
        #if(plots):
        #    #accuracy
        #    plt.plot(model.history['acc'])
        #    plt.plot(model.history['val_acc'])
        #    plt.title('Model accuracy')
        #    plt.ylabel('accuracy')
        #    plt.xlabel('epoch')
        #    plt.legend(['train', 'test'], loc='best')
        #    plt.show()
        #
        #    #loss
        #    plt.plot(model.history['loss'])
        #    plt.plot(model.history['val_loss'])
        #    plt.title('Model loss')
        #    plt.ylabel('loss')
        #    plt.xlabel('epoch')
        #    plt.legend(['train', 'test'], loc='best')
        #    plt.show()
        #    
        #    cm = confusion_matrix(real_label_df, pred_label_df)
        #    cm_df = pd.DataFrame(cm, ["Fall", "Normal"], ["Fall", "Normal"])
        #    
        #    sn.set(font_scale=1.5)
        #    sn.heatmap(cm_df, annot=True, annot_kws={"size": 32}, fmt='d')
        #    plt.savefig("../figs/tf_heatmap.png", facecolor="w", bbox_inches="tight")
        #    plt.show()

        #avg_acc = np.mean(accuracy_a)
        #
        ##Checking accuracy
        #print("Tree average accuracy: ", round(avg_acc, 2)) #2 decimals
        #
        ##More detailed report
        #print(classification_report(real_label_df, pred_label_df))

        return(avg_acc, real_label, pred_label)
        
        
    
#pred_df = pd.DataFrame(pred)
#real_df = pd.DataFrame(real)
#
##fixing labels
#pred_df = pred_df.replace(0, "Normal")
#pred_df = pred_df.replace(1, "Fall")
        
    @staticmethod
    def generateNnModel(data, x_cols, y_cols, plots=False):
        
        return(data)
    
    #using pretrained model
    @staticmethod
    def nnClassify(train, test):
        
        return(test)
    
    
    
    
#    # TF SNIPPETS FROM VSCODE EXTENSION BELOW:
#    
#    #Name: TensorFlow Snippets
#    #Id: vahidk.tensorflow-snippets
#    #Description: TensorFlow Snippets for VS Code
#    #Version: 0.3.3
#    #Publisher: Vahid Kazemi
#    #VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=vahidk.tensorflow-snippets
#    
#    """This module handles training and evaluation of a neural network model.
#    
#    Invoke the following command to train the model:
#    python -m trainer --model=cnn --dataset=mnist
#    
#    You can then monitor the logs on Tensorboard:
#    tensorboard --logdir=output"""
#    
#    from __future__ import absolute_import
#    from __future__ import division
#    from __future__ import print_function
#    
#    
#    
#    tf.logging.set_verbosity(tf.logging.INFO)
#    
#    tf.flags.DEFINE_string("model", "", "Model name.")
#    tf.flags.DEFINE_string("dataset", "", "Dataset name.")
#    tf.flags.DEFINE_string("output_dir", "", "Optional output dir.")
#    tf.flags.DEFINE_string("schedule", "train_and_evaluate", "Schedule.")
#    tf.flags.DEFINE_string("hparams", "", "Hyper parameters.")
#    tf.flags.DEFINE_integer("num_epochs", 100000, "Number of training epochs.")
#    tf.flags.DEFINE_integer("save_summary_steps", 10, "Summary steps.")
#    tf.flags.DEFINE_integer("save_checkpoints_steps", 10, "Checkpoint steps.")
#    tf.flags.DEFINE_integer("eval_steps", None, "Number of eval steps.")
#    tf.flags.DEFINE_integer("eval_frequency", 10, "Eval frequency.")
#    
#    FLAGS = tf.flags.FLAGS
#    
#    MODELS = {
#        # This is a dictionary of models, the keys are model names, and the values
#        # are the module containing get_params, model, and eval_metrics.
#        # Example: "cnn": cnn
#    }
#    
#    DATASETS = {
#        # This is a dictionary of datasets, the keys are dataset names, and the
#        # values are the module containing get_params, prepare, read, and parse.
#        # Example: "mnist": mnist
#    }
#    
#    HPARAMS = {
#        "optimizer": "Adam",
#        "learning_rate": 0.001,
#        "decay_steps": 10000,
#        "batch_size": 128
#    }
#    
#    def get_params():
#        """Aggregates and returns hyper parameters."""
#        hparams = HPARAMS
#        hparams.update(DATASETS[FLAGS.dataset].get_params())
#        hparams.update(MODELS[FLAGS.model].get_params())
#    
#        hparams = tf.contrib.training.HParams(**hparams)
#        hparams.parse(FLAGS.hparams)
#    
#        return hparams
#    
#    def make_input_fn(mode, params):
#        """Returns an input function to read the dataset."""
#        def _input_fn():
#            dataset = DATASETS[FLAGS.dataset].read(mode)
#            if mode == tf.estimator.ModeKeys.TRAIN:
#                dataset = dataset.repeat(FLAGS.num_epochs)
#                dataset = dataset.shuffle(params.batch_size * 5)
#            dataset = dataset.map(
#                DATASETS[FLAGS.dataset].parse, num_threads=8)
#            dataset = dataset.batch(params.batch_size)
#            iterator = dataset.make_one_shot_iterator()
#            features, labels = iterator.get_next()
#            return features, labels
#        return _input_fn
#    
#    def make_model_fn():
#        """Returns a model function."""
#        def _model_fn(features, labels, mode, params):
#            model_fn = MODELS[FLAGS.model].model
#            global_step = tf.train.get_or_create_global_step()
#            predictions, loss = model_fn(features, labels, mode, params)
#    
#            train_op = None
#            if mode == tf.estimator.ModeKeys.TRAIN:
#                def _decay(learning_rate, global_step):
#                    learning_rate = tf.train.exponential_decay(
#                        learning_rate, global_step, params.decay_steps, 0.5,
#                        staircase=True)
#                    return learning_rate
#    
#                train_op = tf.contrib.layers.optimize_loss(
#                    loss=loss,
#                    global_step=global_step,
#                    learning_rate=params.learning_rate,
#                    optimizer=params.optimizer,
#                    learning_rate_decay_fn=_decay)
#    
#            return tf.contrib.learn.ModelFnOps(
#                mode=mode,
#                predictions=predictions,
#                loss=loss,
#                train_op=train_op)
#    
#        return _model_fn
#    
#    def experiment_fn(run_config, hparams):
#        """Constructs an experiment object."""
#        estimator = tf.contrib.learn.Estimator(
#            model_fn=make_model_fn(), config=run_config, params=hparams)
#        return tf.contrib.learn.Experiment(
#            estimator=estimator,
#            train_input_fn=make_input_fn(tf.estimator.ModeKeys.TRAIN, hparams),
#            eval_input_fn=make_input_fn(tf.estimator.ModeKeys.EVAL, hparams),
#            eval_metrics=MODELS[FLAGS.model].eval_metrics(hparams),
#            eval_steps=FLAGS.eval_steps,
#            min_eval_frequency=FLAGS.eval_frequency)
#    
#    def main(unused_argv):
#        """Main entry point."""
#        if FLAGS.output_dir:
#            model_dir = FLAGS.output_dir
#        else:
#            model_dir = "output/%s_%s" % (FLAGS.model, FLAGS.dataset)
#    
#        DATASETS[FLAGS.dataset].prepare()
#    
#        session_config = tf.ConfigProto()
#        session_config.allow_soft_placement = True
#        session_config.gpu_options.allow_growth = True
#        run_config = tf.contrib.learn.RunConfig(
#            model_dir=model_dir,
#            save_summary_steps=FLAGS.save_summary_steps,
#            save_checkpoints_steps=FLAGS.save_checkpoints_steps,
#            save_checkpoints_secs=None,
#            session_config=session_config)
#    
#        tf.contrib.learn.learn_runner.run(
#            experiment_fn=experiment_fn,
#            run_config=run_config,
#            schedule=FLAGS.schedule,
#            hparams=get_params())
#    
#    if __name__ == "__main__":
#        tf.app.run()
#    