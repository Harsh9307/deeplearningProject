# ❓**PROBLEM DEFINITION**
<div style="background-color:#f2f2f2; padding: 20px;">
  <p style="font-size:20px; font-family:verdana; line-height: 1.7em">
Lung cancer remains a significant global health challenge, with its early detection and type classification being crucial for effective treatment. One detection method involves analyzing CT scan images. These images can then be interpreted by doctors to determine the presence and type of lung cancer. However, this method has limitations; human interpretation may miss subtle patterns indicative of early-stage lung cancer. In contrast, deep learning models offer a promising avenue on this matter. They excel in recognizing intricate patterns, identifying subtle abnormalities not easily observable through other methods. Another advantage is they automatically learn relevant features from data, eliminating the need for manual feature engineeing, which is particulary usefull in medical imaging where definining explicit features can be complex.
      <p style="font-size:20px; font-family:verdana; line-height: 1.7em">
      In this study, we use a dataset containing CT scan images of lungs categorized as normal, squamous cell carcinoma, adenocarcinoma and large cell carcinoma. Our objective is to train three different models (VGG16, Inceptionv3 and EfficientNetB0), compare their accuracy and make predictions with the one with hightest accuracy.

<h3>About Dataset:</h3>
<p>Dataset Link : https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images</p>

<h3>Model 1:VGG 16</h3>
<p style="font-size:20px">
    <strong>Batch size</strong>: 32<br>
    <strong>Epochs</strong>: 32<br>
    <strong>Input Shape</strong>: (350, 350, 3)<br>
    <strong>Output layer</strong>: 16
  </p>
</div>

<h3>Inception V3</h3>
 <p style="font-size:20px">
    <strong>Batch size</strong>: 32<br>
    <strong>Epochs</strong>: 32<br>
    <strong>Input Shape</strong>: (350, 350, 3)<br>
    <strong>Output layer</strong>: 1024
  </p>
</div>

<h3>EfficientNetB0</h3>h3>
 <div>
    <p style="font-size:20px">
    <strong>Batch size</strong>: 32<br>
    <strong>Epochs</strong>: 32<br>
    <strong>Input Shape</strong>: (350, 350, 3)<br>
    <strong>Output layer</strong>: 4
  </p>
</div>
