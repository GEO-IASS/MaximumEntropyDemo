# MaximumEntropyDemo
MaximumEntropyDemo use the Stanford Classifier

Example:
java -jar ./tools/maxent/stanford-classifier-3.5.2.jar  -prop ./tools/maxent/basic.prop

Result:
female	male	0.839	0.161
male	male	0.839	0.839
male	male	0.839	0.839
male	male	0.839	0.839
male	male	0.839	0.839
......

199 examples in test set
Cls male: TP=156 FN=0 FP=43 TN=0; Acc 0.784 P 0.784 R 1.000 F1 0.879
Cls female: TP=0 FN=43 FP=0 TN=156; Acc 0.784 P 1.000 R 0.000 F1 0.000
Accuracy/micro-averaged F1: 0.78392
Macro-averaged F1: 0.43944

# SVM
SVMDemo use the libSVM

Example:
python3 ./tools/svm/easy.py ./data/svm/svm_train ./data/svm/svm_test

Result:
Scaling training data...
Cross validation...
Best c=32.0, g=0.001953125 CV rate=84.0141
Training...
Output model: svm_train.model
Scaling testing data...
Testing...
Accuracy = 89% (178/200)
TP = 164
FN = 3
FP = 19
TN = 14
Positive (+1) class:
  precision = 0.896175
     recall = 0.982036
   F1 value = 0.937143

Negative (-1) class:
  precision = 0.823529
     recall = 0.424242
   F1 value = 0.56
