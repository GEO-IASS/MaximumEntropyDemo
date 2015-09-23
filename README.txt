# MaximumEntropyDemo
MaximumEntropyDemo use the Stanford Classifier

Example
java -jar stanford-classifier-3.5.2.jar  -prop ./test.prop

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
