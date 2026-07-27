## 1. Variance and bias: 
what is bias and variance in machine learning
- used for understand data distributions 

**Bias** is the error caused by overly simplistic assumptions in the learning algorithm, leading to **underfitting** where the model fails to capture underlying patterns. It represents the difference between the average prediction and the actual value, resulting in high errors on both training and test datasets.

**Variance** is the error from a model being too sensitive to small fluctuations in the training data, leading to **overfitting** where the model captures noise as if it were signal. It measures how much model predictions vary when trained on different datasets, resulting in low training error but high test error.

The **bias-variance tradeoff** dictates that decreasing bias typically increases variance, and vice versa. Effective machine learning requires balancing these two sources of error to minimize total prediction error and ensure the model generalizes well to unseen data.


## 2. Transfer learning:   
- it is the practice of applying knowledge gained from one task to different but related task, often used for improve model performance. 

**Transfer learning** in the context of Large Language Models (LLMs) is a technique where a model pre-trained on a vast, general corpus of text is reused as a starting point for a specific, related task. This approach leverages the model's learned linguistic structures, grammar, and factual knowledge to improve performance on new tasks like sentiment analysis, summarization, or translation, significantly reducing the need for extensive training from scratch.

Implementation typically follows a structured process:
1.  **Model Selection**: Choose a pre-trained foundation model (e.g., GPT, BERT, Llama) aligned with the target domain.
2.  **Data Preprocessing**: Prepare domain-specific data through tokenization and cleaning to match the model’s input requirements.
3.  **Adaptation Techniques**:
    *   **Fine-tuning**: Adjust the model’s weights using a smaller, task-specific dataset. This is the most common method for specialized domains.
    *   **Feature Extraction**: Use the pre-trained model’s layers to generate features for a separate, simpler model.
    *   **Domain Adaptation**: Further train the model on data from a different but related domain to align with specific terminology or workflows.
4.  **Evaluation and Iteration**: Assess performance using metrics like accuracy or F1 score and iteratively adjust hyperparameters or data to prevent overfitting.

Despite its efficiency, transfer learning faces several limitations:
*   **Domain Mismatch**: Models may struggle if the pre-training data differs significantly from the target domain, leading to poor generalization.
*   **Overfitting**: Fine-tuning on small datasets can cause the model to memorize specific examples rather than learning generalizable patterns.
*   **Bias Propagation**: Any biases present in the original pre-training data are transferred to the new model, potentially causing unfair or inaccurate outputs.
*   **Computational Cost**: While cheaper than training from scratch, fine-tuning large models still requires significant computational resources and expertise.
*   **Rigidity**: Some approaches, like freezing layers, may limit the model's flexibility to adapt to highly nuanced or rapidly changing domain requirements.

## Gradient descent: 
> it is a optimisation algorithm used to find local minimum of a funciton by iteratively adjusting its parameter in the opposite directions of the gradient. 
## Stocastic gradient descent: 
> it is a varient of gradient descent that updates the models parameter using only a sigle data point at each intgration 

## vanishing gradient : 
>it is a problem in training neural networks where gradients becomes too small for effective weight updates 
## sentiment analysis: 
> it is the use of NLP tp identifying and categorizing opinions expresed in the Text or processed text . 

## Regularisation : 
it is technique used to prevent overfitting by adding a panelaty term to loss funciton

## oversampling: 
it is a technique used to balsance calss distribution by randomly duplication minority class, it helps in reduce underfitting 

## overfitting : 
> it is a modelling error that occures when an ML algo captures noise in the training data 
## overfitting prevention methods : 


**Data-centric methods** involve increasing dataset size, applying **data augmentation** (e.g., rotation, flipping) to improve diversity, and performing **feature selection** to remove irrelevant or redundant inputs that increase model variance.

**Model complexity reduction** strategies include choosing simpler architectures, **reducing layers or neurons**, and using **ensemble methods** like Random Forests or Gradient Boosting to combine multiple models and reduce variance.

**Regularization and training constraints** add penalties to the loss function, such as **L1 (Lasso)** which sparsifies coefficients, and **L2 (Ridge)** which shrinks them. Additional techniques include **dropout** (randomly ignoring neurons in neural networks), **cross-validation** for robust evaluation, and **early stopping** to halt training when validation performance degrades.

## underfitting prevention methods 
what are the different types of underfitting prevention methods in ml

To prevent underfitting, which occurs when a model is too simple to capture underlying data patterns, you must **increase model complexity** and **improve data representation**.

*   **Increase Model Complexity**: Switch to more sophisticated algorithms (e.g., polynomial regression instead of linear) or add more layers and parameters in neural networks to better capture non-linear relationships.
*   **Add Relevant Features**: Perform **feature engineering** and selection to include meaningful variables that help the model learn the target relationship; removing important features can cause underfitting.
*   **Reduce Regularization**: Lower the strength of regularization penalties (L1/L2) or dropouts, as excessive constraints can oversimplify the model and prevent it from learning necessary patterns.
*   **Train Longer**: Increase the number of training epochs or iterations to ensure the model has sufficient time to converge and learn from the data.
*   **Use Ensemble Methods**: Techniques like **Boosting** (e.g., AdaBoost, Gradient Boosting) specifically reduce bias by combining multiple weak learners to create a stronger, more complex model.
## Regression : 
> it is a statistical method used to model the relationship between the a dependent variable and one or more independent variables 
## Logistic Regression : 
>it is a statistical method used for bianry classification problems modeling the probability of a particular class 


**Logistic regression** is a supervised machine learning algorithm primarily used for **classification problems**, specifically predicting categorical outcomes such as binary yes/no decisions. 
logistic regression estimates the **probability** that an input belongs to a specific class by applying a **sigmoid function** to a linear combination of input features, outputting values strictly between **0 and 1**.

The algorithm is most effective for the following problem types:
*   **Binary Classification**: Predicting outcomes with two possible classes, such as spam detection (spam vs. not spam), medical diagnosis (disease presence vs. absence), or customer churn (leave vs. stay).
*   **Multiclass Classification**: Handling problems with more than two categories, often by breaking the problem into multiple binary classification tasks or using multinomial logistic regression.
*   **Ordinal Classification**: Predicting outcomes with a natural order, such as survey ratings (poor, average, good).


## linear Regression: 
> it is also a statistical method used for modelling and analysing linear relationships between dependent varaible and one or more indepedent variables 
- which predicts continuous numerical values, 

In contrast, **regression problems** in machine learning involve predicting **continuous numerical values** rather than discrete classes. These problems include:
*   **Linear Regression**: Modeling linear relationships to predict quantities like house prices, stock prices, or temperature.
*   **Objective**: The goal is to minimize error (e.g., Mean Squared Error) between predicted continuous values and actual values, fitting a best-fit line or curve through the data points.

## Reinforcement Learning: 
> it is type of machine learning where an agent learns to make decisioins by interacting with an environment to achieve a goal 



**Reinforcement Learning (RL)** is a branch of machine learning where an autonomous agent learns to make decisions by interacting with a dynamic environment to maximize cumulative rewards. Unlike supervised learning, which relies on labeled datasets, RL agents learn through trial-and-error, balancing the exploration of new actions with the exploitation of known rewarding behaviors. The agent observes the current **state**, selects an **action** based on a **policy**, and receives a numerical **reward** that guides the optimization of long-term outcomes.

Key terminology in RL includes:
*   **Agent**: The learner or decision-maker that interacts with the environment.
*   **Environment**: The external system or scenario with which the agent interacts.
*   **State (S)**: A representation of the current situation or configuration of the environment.
*   **Action (A)**: The set of possible moves the agent can make in a given state.
*   **Reward (R)**: Immediate feedback (positive or negative) received after an action, indicating its desirability.
*   **Policy ($\pi$)**: The strategy the agent employs to determine the next action based on the current state.
*   **Value Function**: An estimate of the expected cumulative reward from a given state or state-action pair.

Popular RL algorithms are generally categorized into value-based, policy-based, and actor-critic methods:
*   **Q-Learning**: A model-free, off-policy algorithm that uses a Q-table to estimate the value of state-action pairs, updating them via the Bellman equation.
*   **SARSA**: Similar to Q-learning but is an on-policy algorithm that updates values based on the action actually taken.
*   **REINFORCE**: A policy gradient method that directly optimizes the policy to maximize expected returns without estimating value functions.
*   **Proximal Policy Optimization (PPO)**: A popular policy-based algorithm that ensures stable updates by limiting how much the policy can change in each step.
*   **Deep Q-Networks (DQN)**: Combines Q-learning with deep neural networks to handle high-dimensional sensory inputs, such as video game pixels.
*   **Actor-Critic**: A hybrid approach that combines value-based and policy-based methods, using an "actor" to determine actions and a "critic" to evaluate them.
## Decision Trees : 
these are type of  supervised machine learning algo, used for both classification and regression task; that make decisions based on splitting data along feature values 

## Random  Forest : 
it is an ensember learning method that consists of multiple decision trees and output the average predicitions od the individual trees for regression task or the class that receive the most votes for the classification task .
## Truncation: 
it is method of limiting the number of elements in a data set or the numbers of nodes in a neural network. sometime related with deletion 
## Principal Compoent analysis (PCA)
>it is  a Dimensionality reduciton technique that transforms the original variable into a new set of uncorrelated variables 

**Principal Component Analysis (PCA)** is a statistical technique used for **dimensionality reduction** that transforms correlated variables into a smaller set of **uncorrelated variables** called principal components, which retain the most significant variance in the dataset.

### Related Algorithms
*   **Kernel PCA (KPCA):** A variant that uses kernel functions to find **nonlinear** principal components, extending PCA to handle complex data structures.
*   **Sparse PCA (SPCA):** An algorithm that applies Lasso regularization to produce principal components with **sparse loadings**, improving interpretability by eliminating less important variables.
*   **Robust PCA (RPCA):** An adaptation designed to handle **outliers** and noise in large datasets, often used in image analysis and web data processing.
*   **Linear Discriminant Analysis (LDA):** A supervised learning counterpart to PCA that reduces dimensions while maximizing separation between **class labels**.
*   **Independent Component Analysis (ICA):** A technique that seeks **statistically independent** components rather than just uncorrelated ones, useful for separating mixed signals.

### Popular Terms
*   **Principal Components (PCs):** New variables that are linear combinations of original features, ordered by the amount of variance they explain.
*   **Eigenvalues:** Coefficients that denote the **importance** of an eigenvector; higher eigenvalues indicate directions of greater variance.
*   **Eigenvectors:** Directions in space along which the data points have the highest variance, forming the axes of the new coordinate system.
*   **Covariance Matrix:** A symmetric matrix that summarizes how variables vary from the mean with respect to each other, used to identify correlations.
*   **Orthogonal:** A property where principal components are **uncorrelated** (perpendicular), meaning the correlation between any pair is zero.
*   **Biplot:** A graphical representation that maps cases and original variables together to support the interpretation of distances and relationships in the reduced space.

## Pretraining: 
it is a practive of training a machine learning model  on a large dataset before finetuning it on a specific task 
## object detection: 
it is a computer vision task that identifies and locates the objects within images or videos. 

## outlier :  out lier: outside of the data 
it is a data point that deviates significantly from the rest of the data set often considered as noise or anomaliy 

## one hot encoding: 
it is a representation of categorical variables as binary vectors commonly used in machine learning algos 
## KNN:  
it is an alog used to find the data points in a dataset that are closest to a given point .
## Normal distribution: 
it is a probability distribution characterised by bell shaped curve commonly used in representing data in ML 
## Normalization: 
it is a process of scalling the features to a standard ranfge commonly used in ML to improve algo performance 


## NLP: 
it is a field of AI that focus on the interaction between computer and human language
## matrix factorisation : 
it is used to decompose a matrix into muiltiple matrics commonly used in recommendation system
## Markov chains : 
it is a stochastic model representing a sequence of possible events where the probabiliy of each event depeneds solely on the state attained in the previous event 
- often used in the ML and DS for simulationg sampling from complex probability  distributions and studing systems over overtime. 

## Knoledge transfer : 
it is the process of applying knoledge gained from one domain to another domain but similar type.
- used for impove model performamce

## knowledge graphs : 
 it is representations of the fact and relationships. 
 - used in semantic search and recommmendation systems 

 ## joint probability : 
 multiple events occuring together
 - used in probabilistic models
 ## indcutive bias : 
  it is a set of assumptions, a ML algo makes togeneralize from training data to unseen data 
  ## information extraction: 
  it is a process of automatically extracting useful informatioin from unstructured data sources: 
## inference : 
it is the process of making predictioins using a trained ML model 

## Generalization: 
it is an ability of ML perform well on unseen data 
## GAN:: 
it is a class of ML frameworks where two neural Nets : the generator and the discriminator are trained together commonly used for image gernerations tasks: 

## Ensemble methods :
these are the techniques that combine multiple machinelearning models to overall performance 

## Data preprocessing : 
Raw data  --> Cleaning --> Normalisation --> Feature Extractions 

## Different type of ML tasks: 


## Loss Funcitions: 
it is a type of mathematical fucntin that quantifies the difference between the predictied and the actual ourcomes ML algos. 
## sigmoid Function : 
it is an activation function in neural network
- it gives output betweeen zero and one Commonly used in logistic regression and neural networks 

## Evolutionary Algos: 
these are optimisation algos inspired buy the process of natural selection used in ML for parameter tuning 

## Language model : 
these are type o ML models that predicts the liklehood of words commonly used in   natural language processing such as chatgpt

## numerical models: 


## backpropagation: 
it is an optimisation algo used to minimize the loss funciton by adjusting the model weights. 
- it is fundamental to training of ANN 

## bagging: 
it is an ensemble learning technique that improves stability and accuracy by training multiple instances of same model on different subset of training  data 

## Dense vector:
 it is a type of vector in which most of the vectors are non zero , used for feature representation and various computations. 

 ## feature engineering:
  it is  process of transforming data into a format that makes it easier for machine learning algorithms to interpret 

  ## SVMs: 
  supervised learning algos 
  - used for classification and regerssion tasks: 
  - it finds the hyperplane that best separates the different classes in the feature space 

## cross validation : 
it is technique for assessing the performance of ML model by dividing the data set into multiple subsets and evaluating the model on different combinations of these subsets

## P values: 
it a measure used  in hypothesis testing to indicate the probability of observing a test statistic as extrem as  one computes, given that the null hypothes is true 

## T test : 
it is a statistical test used ot compare the means of two groups and determine if they are significantly different from each other 

## Cosine similarity :
it is a a metric used to measure the cosine of the angle between non zero vectors in and inner product space : 
     - used to measure document similarity 


## droupout: 
it is a regularisation technique used in a neural networks where randomly selected neurons  are ignored during training helping to prevents overfitting 

## Softmax function : 
it turns a vector of raw scores into probability 
- used in output layer of classification neural netork 

## tan h function: 
it gives the output between [-1,1]
- zero centereed and smooth funcitons 
## Relu funciton: 
it zero  all the negative values and keep the positives as it is 
- non linear
- Computationally efficient  and Zero centered
- can cause dying Relu problem , means lossing neagative data 
## MSE : Mean square Error
 
 it is used in regression problems that measures the average of the squares of the errors netween  pridicted and actual values 

## RMSE :
it is a square  root of the mean squared error providing 
a measure of the average magnitude of the errors between pridicted and the actual observations. 



## Bayes theorem : 
it is a principle in probability theory  and statistics that describes the probability of an event based on prior knowledge of related conditions

## L1 and L2 regularisation: 
     - these are regularisation techniques that add penalty terms to the loss functions to prevent overfitting with L1 leading to sparse solutions
     and l2 simply shringking the weights 

## learning rate : 
it is a tuniunng parameter in an optimisation algorithms  used when we train the model 
- it determine the step size at  each iteration while moving towards a minimum of a loss funcitons 
- it metaphorically represents the speed at which a machine learining  learns influencing the extent to which newly acquired information overrides old information 

## Naive bayes: 
it is   a probabilistic classifier based on appling baye theorem. Assuming that all features are independents of each other given the category of the object 

##  Confusion matrix
it is also know as  error matrix, a specific type of table layout of TRue positive an false negative values
- it allows the visualisation of the performance of an algorithm, typically a supervised learning algos. 
- Each row of matrix represents the instance in an actual class while each column represents the instance in predicted class 

## AUC ROc : area under curve 

## Grid search:
 used to systematically work through multiple combinaions of pararmetes tunes, cross validating as it goes to determines which tunes gives the best performance. 
 - used for hyperparamter tunnig 

## Manhatten distance : 
sum of the horizontal and vertical distance between points in a grid based path  

## jacard similarity :
- it quantifies the similarity between two sets as the size of the intersection divided by the size of the union 

## K means Clustering : 
Partitions data into k cluseters whre each data point 
belongs to cluster with the nearest mean 


## ANN: 
## perceptron 
## CNN
## RNN
## LSTM 
## transfer model 
## padding
## pooling
## Variational autoencoder 
## Quantum machine learning 



## Bias-variance tradeoff, regularization, gradient descent, and evaluation metrics (precision, recall, AUC-ROC). 
## Deep Learning & GenAI: Transformer architectures, attention mechanisms, RAG (Retrieval-Augmented Generation),
there are 3 main retreivel strategies for RAG:
- 1. Sparse retrieveal : old technique
     - relieing on keyword search 
     - it use methods like TF IDF, BM25 
     - it counts how often query terms appears in documents  and then scores the document accordingly 
- pros: 
     - it simple fast and scalable 
     - in some case BM 25 outperform more domain specific models 

- cons: it doesnt handle synonyms very good way 
     - When should we use it ? 
     - any situation where exact word match matters, like in short well definedd queries code search logs or leagal caluses. 
     - it doesn;t require embeddings => so its a cost effective method

- examples: Apache Luchene built on BM25 , milvus also supports bm25 
- 2. Dense retrieal / semantic work horse: 
     - it is recent technology
     - both queres and document are mapped into high diemensional vector spaces . 
     - results are found based on semantic semialrity, meannings of the word is found near, 
     - this totally depends on embedding models. 
     - similarities can be calculated using algorithms like  ANN(approx near neighbors), knn, 
     - eg: jvector opensource high performance java lib that speed up the dense retireveal 
     - used for natural language application 
     - best for chatbots,  cusotmer serives, knowledge base , where the things are phrase in many different ways like sarcasam, fun, astonsishing etc. 
     - its powerful , context aware 
     - it can miss rare and jargon heavyterms 
     - not good with short few word queries . 

3. hybrid retireval: current state of Rt;
     - latest tech in practical 
     - combined the both vector and semantic 
     - semantic handles the synonyms and concepts while the keyword matching ensures that rare but critical terms dont get lost 
     - benchs show hybrid retireval is best , and outperform orthodox methods. 

     - boosts both percision and recal meticx of the comparisions 
- how does it works : 
     - the query  runs both ways in parallel : ones as a vector embeddings against our embedded knowlege set and again as a keyword search .
     - it then use a fusion algo to merge based on scores from both 
     - 1.  most common fusion algo is wieghted sum : it picks the balance between both : 70% dense +30 % sparse: 
     - 2.  resiprocal ranked fusion  (RRF): it doesnt use raw scores, but instead merge based on the ranked positions from each retirever. 
     - works best in domains where specialise jargons  used 
     - legal , technical , mediacal field . 
     - it balance the speed, precison and recall. 
- example : elastic search, weaviate, datastax,astra db 


## fine-tuning (LoRA, RLHF), and prompt engineering. 
## MLOps & Deployment: CI/CD pipelines, model monitoring, drift detection, containerization (Docker/Kubernetes), and cloud platforms (AWS SageMaker, GCP Vertex AI). 
## Coding: Proficiency in Python, SQL, and frameworks like PyTorch or TensorFlow is essential, alongside standard data structure and algorithm skills
 
 ## How CHATGPT works technically :
 - it use a LLM model to generate the response. 
 - [what is LLM refer it to the above.] trained on massive amount of text data and it understand and generate the human language. 
- it use that data to learn and then predict on the basis of that , what come next in the sentense. 
- standard chatgpt use GPT3.5 model, and it has 175 billion parameters, withing 96 layers in neural network 

- then it goes to the tokens 
- numerical repesentation of the words , or parts of the word. 
- numerbs can process effeciently by the computer so words converted to the numbers. 

- source data contians more than 500 B tokens . 