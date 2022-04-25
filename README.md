# Cloud Continuous Delivery of Garbage Classification Microservice<img width=90 align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Duke_University_logo.svg/1024px-Duke_University_logo.svg.png">
## Final Project for IDS 721: Data Analysis at Scale in Cloud

*Contributors: Ying Feng, Ruoxuan Wang, Jiankai Xu, Zheng Zhang*

### Abstract
Garbage classification is an emerging issue in recent years. As garbage classification during disporsal has been adopted by countries all over the world as a environemntal protection policy, letting the robort to automatically perform garbage classification can has significant social and environment effect, which also leverage manual effort. Through this project, we built a complete pipeline to perform the garbage classification pipline with machine learning model, feature engineering, model training, and model deployment from a simple garbage image. A ResNet50 ML prediction model performes the best in our hold-out dataset in classifying the type of a garbage, Google Kubernets Engine is used as our model deployment platform. We also built a frontend app service as an interactive platform. 

A demo video can be found [here](https://www.youtube.com/watch?v=V8Ux7_8jzjU), which mainly involves the following three steps:
* Open homepage:

  <img width="900" alt="WechatIMG269" src="https://user-images.githubusercontent.com/90076441/164934582-0b907733-cbab-4ef8-9ac3-759e03af60fe.png">

* Select a picture: 
 
  <img width="400" alt="WechatIMG270" src="https://user-images.githubusercontent.com/90076441/164934578-6302870d-10a6-4652-8289-0f27b92756b5.png">

* Result: 
 
  <img width="900" alt="WechatIMG268" src="https://user-images.githubusercontent.com/90076441/164934583-d7918b30-911f-4638-801f-57bf125812fa.png">


### Data & Model
The dataset used in this project was collected from [Kaggle](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification). The goal for this project is to identify the type of the garbage when providing an image. The original dataset has 2,467 observations which contains 6 classifications: `cardboard (393)`, `glass (491)`, `metal (400)`, `paper(584)`, `plastic (472)` and `trash(127)`. Example pictures for each category can be found [here](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification).

The garbage classification model we used in this model was also from [Kaggle](https://www.kaggle.com/code/sudarshansrinivasan/garbage-classify-95-accuracy-scr-p-2), which uses PyTorch, TensorFlow and ResNet50.

### Deployment
* Structure:  

  <img width="700" alt="image" src="https://user-images.githubusercontent.com/88390268/164998016-9c018b60-a41d-44c3-b91b-369620e20fab.png">

* We used Docker to continerize the service, and the docker image was pushed to Google Artifact Registry:  
  
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/88390268/164997694-7d666a7c-f485-49aa-be87-dddf3519e153.png">

* The cluster was deployed on Google Kubernetes Engine: 

  <img width="900" alt="image1" src="https://user-images.githubusercontent.com/88390268/164997015-6b567e99-697e-4e2c-a795-4373899518d0.png">. 
  
  <img width="900" alt="image" src="https://user-images.githubusercontent.com/88390268/164997354-07528487-19fc-4423-a6bb-339f9c596d5d.png">
  
* To enable external access, we also deployed the service on Google Cloud Run:  
  
  <img width="900" alt="image" src="https://user-images.githubusercontent.com/88390268/164996943-4aff226a-6f26-4e32-bacc-1b4e7b83cfd7.png">

### Requirements

This project is built with Python 3. The following steps can be followed to replicate the analysis:

* Clone repo with SSH key
  ```
  git@github.com:miley-wangrx/Garbage-Classification.git
  ```
* Install all packages for analysis. 
  First, cd into the repo
  ```
  cd Garbage-Classification/
  ```
* Then run the following command
  ```
  make install
  ```
  ```
  python main.py
  ```
* The following steps are needed if changes are made:  

  - Build and tag the Docker image:
    ```
    docker build -t us-west1-docker.pkg.dev/garbage-classfication/garbage-classify-repo/hello-app:latest .
    ```
  - Run Locally:  
    ```
    docker run --rm -p 8080:8080 us-west1-docker.pkg.dev/garbage-classfication/garbage-classify-repo/hello-app:latest
    ```
  - Pushing the Docker image to Artifact Registry:  
    First, configure the Docker command-line tool to authenticate to Artifact Registry
    ```
    gcloud auth configure-docker us-west1-docker.pkg.dev
    ```
    Then, push
    ```
    docker push us-west1-docker.pkg.dev/garbage-classfication/garbage-classify-repo/hello-app:latest
    ```

### Reference
1. Garbage Classification Dataset on Kaggle:     
https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification 
2. Deployment of Machine Learning Application on GKE:  
https://cloud.google.com/community/tutorials/kubernetes-ml-ops?hl=en
3. Store Docker container images in Artifact Registry:  
https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images?_ga=2.250712257.677951756.1650740441-47603023.1648964420
4. How to create Artifact Registry repositories:  
https://cloud.google.com/artifact-registry/docs/repositories/create-repos#overview
5. Using Container Registry with Google Cloud:  
https://cloud.google.com/container-registry/docs/using-with-google-cloud-platform?authuser=1
6. Deploying a containerized web application:  
https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app#building_the_container_image 
