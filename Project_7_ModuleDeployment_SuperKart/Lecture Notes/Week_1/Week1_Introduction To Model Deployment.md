# 1.2 The Need of Model Deployment


Common Problems in Machine Learning:
```mermaid
graph TD
    A[Customer Churn]
    B[Predictive Maintenance]
    C[Fraud Detection]
    D[Personalised Recommendation]
    D --> E[Spotify]
    D --> F[Amazon]
    D --> G[Netflix]
  
```


**Process for ML Process**

- Gather Data
- Data Exploration -> Corelation (Univariate/ Bivariate Analysis)
- Preprocessing Data 
- Train Model -> Evaluate -> Hyperparameter Tuning (Decision Trees/Neural Networks/ XG Boost etc.)
- Tuning (Gennie)
- Best Model -> Deployment

Best model -> | How to expose the best model | --> customer


**Challenges with Python Nb:**
-  Accessability (Lot of Py code + company secrets)
-  need a simple way w/o exposing company's secrets
-  ensure dependencies are taken care of at customer's end (Platform Agnostic)
-  make sure ML model is generatinf recommendations that is fast enough (Latency/ Lag is min)
-  Approch is scalable (Horizontal scaling)

=================================================

# 1.3  Introduction to Model Deployment    

1. How can we share the model?
   - the model should also be re-trainable
2. Platform Agnostic



```mermaid
flowchart LR
    A1["A way to share<br>the model"]
    A2["A way to ensure<br><b>consistent<br>configurations</b>"]
    A3["<b>Interface for<br>communication</b><br>to get <i>fast</i><br>predictions"]
    A4["<b>Concurrent<br>access</b> for<br>multiple users"]

    B1["Sharing and Consistency<br><br><b>'Package'</b> the model and dependencies"]
    B2["Speed and Scalability<br><br><b>'Set'</b> it up for fast and concurrent <b>'usage'</b>"]

    A1 --> B1
    A2 --> B1
    A3 --> B2
    A4 --> B2
```

**Model Deployment**
- taking a trained ML model, package it and set it up for inference
- - we dont train it during deployment

**How do we package it?**

=================================================

# 1.4  Need for Model Serialization

**Environment**
- set of specific cond. and config under which software and systems operate

1. Development Environment
   - used for training ML models by `hyperparameter tuning`
2. Production Environment
   - used to deploy final ML model to serve end users


=================================================

# 1.5 Introduction to Model Serialization

![](..\Diagrams\modelSerialization.png)


```mermaid
graph LR
   A[Model Serialization] --> a((format that can be stored / transmitted and transmitted later))


   B(Data Exploration and Preprocessing) --> b[Training] --> b1[Best Model] --> b2[Serialization]

   b2 --> b3(can load it in any environment)
   b2 --> b4(No Need to execute the code again)
   b2 --> b5(can make faster predictions)


```

**Model Serilization Formats**

- Pickle : save/ load in pyhon for quick and loaal use
- Joblib : large NumPy models
- ONNX : Deploying across diff frameworks / running them on edge devices
- TensorFLowModel: deploy deep learning model in production with TF 


![](..\Diagrams\serialization.png)


**The main idea:**

- We need to serialize the best model along witht he data preprocessing steps that were used to preprocess the data used to train the model


```mermaid
graph TD
    A[Data Preprocessing Steps] --> B[Trained Model]
    B --> C[Best Model]
    A --> D[Serialization]
    C --> D
    D --> E[Reusable in Production]
```

=================================================

# 1.6 Introduction to API's


### Need for a Communication interface

![alt text](image.png)


```mermaid
graph LR

   A[API] --> a1[Interface that allows seamless communication between the model and users]

   a1 --> a2[Accept input data]
   a1 --> a3[Process Request]
   a1 --> a4[Return Prediction]

```


### Application Programming Interface API

API :- Mechanism that enables two software components to `communicate` with each other `using a set of definations/ protocols`


![alt text](image-1.png)



### HTTP Methods

- when a user wants to get predictions from a model , they need to send a request


**API request:**
- is a message sent to a server asking an API to provide a service / information


```mermaid
graph LR

   A[send Data ] ---a[Profle info from new users]
   B[Update data ] ---b[Modifications to user intrest/ preferences]

   C[Delete Data] ---c[clean watch history]


```


![alt text](image-2.png)


#### HTTP status codes


| Status Code | Status Message        | Description                       |
| ----------- | --------------------- | --------------------------------- |
| 200         | OK                    | Request was successful            |
| 400         | Bad Request           | request Invalid                   |
| 401         | Unauthorized          | Authentication reqd               |
| 403         | Forbidden             | access not allowed                |
| 404         | Not Found             | Requested resource does not exist |
| 500         | Internal Server Error | The server encountered an error   |




# 1.7 Introduction to Endpoints

```mermaid
graph RL
   A[Serialized Model] --> a[API]
   C[END User] --> B[API request] -->a

```


-API endpoints make it easy for the end user

- an API endpoint is a digital location where API recieves API requests, for resources on its server


# 1.8 Handling Dependencies

- Diffrent users/machines can have different envirionments
  - for example Numpy verion might be different acrosss different machines and this can affect the experience of two different users
  


  - In Python we can create a  `Dependencies` file  that act as a blueprint for recreating the exact environment where the model was trained and tested
    - such a file is usually a `requirements.txt` file  which creates a reproducible environment
  


 # 1.9 Securely Hosting a Deployed Model

  ![alt text](image-3.png)



**Security**

- `Access Keys` : Its a unique identifier to authenticate and authorise a user/application to access a secure resource

![alt text](image-4.png)



# 1.10 Architecture of Model Deployment

 ![alt text](image-6.png)

 # 1.11 Model Deploymenr - Learning Outcomes and Summary

 - You cannot share jupyter nb as an ML solution with end users as this is enfficient
   - dependency issue
   - Not Fast
   - Not consistent
   - scalability

- Deployment should be done by serialization 
  - make it as a binary
    - different format
      - ONYX
      - PICKLE
      - Tensor flow
  - API
    - HTTP methods
      - status codes
  
    - Idea of Endpoints
      - Hosting
        - cloud solutions
    - Dependency Handling
      - we have requirements.txt to replicate what we have in the production env
    - Security
      - Access keys
    - Architecture:
      - Backend: Server
      - Frontend : End user will only communicate on frontend


# 1.12 - 1.16 Case Study







