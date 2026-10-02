# PRD.md --- Spam Email Detection System

## 1. Document Information

  Field                    Details
  ------------------------ -----------------------------------------------
  Product Name             Spam Email Detection System
  Document Type            Product Requirements Document (PRD)
  Version                  1.0
  Status                   Final
  Primary Interface        REST API
  API Testing Tool         Postman
  Backend                  Python + Flask
  ML/NLP Stack             Pandas, NumPy, Scikit-learn, TensorFlow/Keras
  Initial Dataset          UCI SMS Spam Collection
  Primary Classification   Spam / Ham
  Project Type             NLP + Machine Learning + Flask API

------------------------------------------------------------------------

# 2. Product Overview

The **Spam Email Detection System** is an NLP and Machine Learning based
application that analyzes the text of a message and predicts whether it
is **Spam** or **Not Spam (Ham)**.

The system will accept text through a REST API and return a
machine-learning prediction. The first implementation will use the **UCI
SMS Spam Collection** dataset, which contains labeled spam and
legitimate messages. Although the initial dataset contains SMS messages,
the same text-classification architecture can be extended to email
content.

The project is designed as an end-to-end machine learning application:

``` text
Raw Dataset
    ↓
Data Loading
    ↓
Data Validation
    ↓
Data Cleaning
    ↓
NLP Preprocessing
    ↓
Feature Extraction
    ↓
Train/Test Split
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Model Serialization
    ↓
Flask REST API
    ↓
Postman Request
    ↓
Spam / Ham Prediction
```

------------------------------------------------------------------------

# 3. Problem Statement

Unwanted messages such as advertisements, fraudulent offers, fake
rewards, phishing-style messages, and unsolicited promotional content
are common in digital communication.

Manually identifying every unwanted message is inefficient. A
machine-learning based text classifier can learn patterns from
previously labeled messages and automatically classify new messages.

The product should therefore provide a simple API where a user or
another application can submit message text and receive a
classification.

### Example

Input:

``` text
Congratulations! You have won a free cash prize. Click now to claim.
```

Expected classification:

``` text
SPAM
```

Input:

``` text
Hi, please send me the project report before 5 PM.
```

Expected classification:

``` text
HAM
```

------------------------------------------------------------------------

# 4. Product Goals

## 4.1 Primary Goals

1.  Build a complete text classification pipeline.
2.  Load and validate the spam/ham dataset using Pandas.
3.  Perform appropriate NLP preprocessing.
4.  Convert text into numerical features using TF-IDF.
5.  Train and evaluate a classification model.
6.  Save the trained model and vectorizer.
7.  Expose the model through a Flask REST API.
8.  Test the API using Postman.
9.  Return a clear and consistent prediction response.
10. Maintain a clean project structure suitable for GitHub and portfolio
    use.

## 4.2 Secondary Goals

1.  Experiment with more than one classification approach.
2.  Include a neural-network based model as an advanced experiment.
3.  Compare model metrics such as accuracy, precision, recall, F1-score
    and ROC-AUC where applicable.
4.  Handle invalid API requests safely.
5.  Document the complete development and deployment flow.

------------------------------------------------------------------------

# 5. Non-Goals

The following are outside the scope of the initial version:

-   Real-time integration with Gmail, Outlook, or another mailbox.
-   Automatically deleting user emails.
-   Automatically moving messages to a spam folder.
-   Sending emails.
-   Building a browser extension.
-   Building a mobile application.
-   Training a large language model from scratch.
-   Guaranteeing 100% spam detection accuracy.
-   Storing users' private email content permanently.
-   Database integration in Version 1.

The initial version is intentionally focused on **NLP classification +
ML + REST API**.

------------------------------------------------------------------------

# 6. Target Users

## 6.1 Primary Users

### ML/NLP Learner

A student or beginner who wants to understand an end-to-end NLP project.

### Developer

A developer who wants a reusable spam-classification API.

### Recruiter/Reviewer

A reviewer who wants to inspect a practical project demonstrating
Python, NLP, machine learning and Flask skills.

## 6.2 Future Users

-   Email clients
-   Customer-support systems
-   Messaging platforms
-   Enterprise communication systems
-   Security or fraud-detection applications

------------------------------------------------------------------------

# 7. User Stories

## US-01 --- Submit a message

**As a user**, I want to submit message text to the API so that the
system can classify it.

### Acceptance Criteria

-   API accepts a text input.
-   Empty text is rejected.
-   Valid text is processed.
-   A prediction is returned.

------------------------------------------------------------------------

## US-02 --- Receive classification

**As a user**, I want to receive a clear classification so that I know
whether the message is spam.

### Acceptance Criteria

Response contains:

-   input status
-   prediction
-   confidence/probability when available

Example:

``` json
{
  "prediction": "spam",
  "confidence": 0.94
}
```

------------------------------------------------------------------------

## US-03 --- Handle invalid requests

**As a user**, I want a meaningful error message when I submit invalid
input.

Example:

``` json
{
  "error": "Message text is required."
}
```

------------------------------------------------------------------------

## US-04 --- Reuse the trained model

**As a developer**, I want the API to load a previously trained model so
that the model does not need to be retrained for every request.

------------------------------------------------------------------------

# 8. Functional Requirements

## FR-01 --- Dataset Loading

The system must load the raw dataset using Pandas.

Initial dataset structure:

``` text
label<TAB>message
```

The dataset loader should convert it into:

``` text
label | text
```

Example:

``` text
ham  | Please call me when you reach home.
spam | Congratulations! You have won a prize.
```

------------------------------------------------------------------------

## FR-02 --- Dataset Validation

The system must inspect:

-   Number of rows
-   Number of columns
-   Column names
-   Data types
-   Missing values
-   Duplicate records
-   Class distribution

Expected initial dataset size is approximately:

``` text
5574 rows × 2 columns
```

The exact values should always be verified from the local dataset rather
than hard-coded into the application.

------------------------------------------------------------------------

## FR-03 --- Data Cleaning

The preprocessing pipeline may include:

1.  Convert text to lowercase.
2.  Remove unnecessary whitespace.
3.  Handle missing text values.
4.  Remove duplicate records where appropriate.
5.  Normalize text consistently between training and inference.

Example:

``` text
"WIN A FREE PRIZE!!!"
```

may become:

``` text
"win a free prize"
```

The exact preprocessing strategy should be kept consistent between
training and prediction.

------------------------------------------------------------------------

## FR-04 --- Punctuation Handling

Punctuation removal is optional and must be evaluated rather than
blindly applied.

For example:

``` text
"Free!!!"
```

may become:

``` text
"free"
```

However, punctuation can sometimes contain useful signals in spam
messages. Therefore, the project should compare preprocessing choices
where practical.

------------------------------------------------------------------------

## FR-05 --- NLP Feature Extraction

The initial feature extraction method will be **TF-IDF (Term
Frequency-Inverse Document Frequency)**.

Example:

``` text
Raw Text
   ↓
Cleaned Text
   ↓
TF-IDF Vectorizer
   ↓
Numerical Feature Vector
```

The vectorizer used during training must be saved and reused during
prediction.

------------------------------------------------------------------------

## FR-06 --- Train/Test Split

The dataset must be divided into training and testing subsets.

Recommended initial configuration:

``` text
Training: 80%
Testing: 20%
```

A fixed `random_state` should be used for reproducibility.

Because spam datasets can be imbalanced, stratified splitting should be
considered so that both classes are represented appropriately in
training and testing data.

------------------------------------------------------------------------

## FR-07 --- Model Training

The project should support a baseline classification model.

Suitable initial models include:

-   Logistic Regression
-   Naive Bayes
-   Linear Support Vector Machine

The initial implementation may use **Logistic Regression** as a simple,
interpretable baseline.

A neural-network experiment can be added separately using
TensorFlow/Keras.

------------------------------------------------------------------------

## FR-08 --- Model Evaluation

The model must be evaluated on unseen test data.

Required metrics:

-   Accuracy
-   Precision
-   Recall
-   F1-score
-   Confusion Matrix

Where the model exposes appropriate probability scores, ROC-AUC may also
be reported.

### Why these metrics matter

Accuracy alone can be misleading when classes are imbalanced.

For spam detection:

-   **Precision** helps measure how many predicted spam messages are
    actually spam.
-   **Recall** helps measure how many actual spam messages are detected.
-   **F1-score** balances precision and recall.

------------------------------------------------------------------------

## FR-09 --- Model Serialization

After training, the final model must be saved to disk.

Example:

``` text
models/
├── spam_model.pkl
└── tfidf_vectorizer.pkl
```

The API should load these files during application startup.

------------------------------------------------------------------------

## FR-10 --- Flask REST API

The system must expose a REST endpoint for prediction.

### Health Endpoint

``` http
GET /
```

Expected response:

``` json
{
  "message": "Spam Detection API is running"
}
```

### Prediction Endpoint

``` http
POST /predict
```

Request:

``` json
{
  "text": "Congratulations! You won a free prize!"
}
```

Response:

``` json
{
  "prediction": "spam",
  "confidence": 0.95
}
```

------------------------------------------------------------------------

# 9. API Requirements

## 9.1 POST /predict

### Request Content-Type

``` text
application/json
```

### Request Body

``` json
{
  "text": "Your message here"
}
```

### Successful Response

HTTP Status:

``` text
200 OK
```

Example:

``` json
{
  "prediction": "ham",
  "confidence": 0.91
}
```

------------------------------------------------------------------------

## 9.2 Invalid Request

If `text` is missing:

HTTP Status:

``` text
400 Bad Request
```

Response:

``` json
{
  "error": "Message text is required."
}
```

------------------------------------------------------------------------

## 9.3 Empty Text

Input:

``` json
{
  "text": ""
}
```

Expected:

``` json
{
  "error": "Message text cannot be empty."
}
```

HTTP Status:

``` text
400
```

------------------------------------------------------------------------

## 9.4 Unsupported HTTP Method

Requests to unsupported methods should return an appropriate HTTP error
response.

------------------------------------------------------------------------

# 10. API Flow

``` text
Client / Postman
       ↓
POST /predict
       ↓
Validate JSON
       ↓
Extract "text"
       ↓
Preprocess text
       ↓
Load/use TF-IDF vectorizer
       ↓
Transform text into features
       ↓
Load/use trained model
       ↓
Predict class
       ↓
Calculate confidence if supported
       ↓
Return JSON response
```

------------------------------------------------------------------------

# 11. Machine Learning Architecture

## 11.1 Training Architecture

``` text
Dataset
   ↓
Pandas DataFrame
   ↓
Validation
   ↓
Cleaning
   ↓
Label Encoding
   ↓
Train/Test Split
   ↓
TF-IDF
   ↓
Classifier
   ↓
Evaluation
   ↓
Model + Vectorizer
```

## 11.2 Prediction Architecture

``` text
API Request
   ↓
Input Validation
   ↓
Text Preprocessing
   ↓
Saved TF-IDF Vectorizer
   ↓
Saved Classifier
   ↓
Prediction
   ↓
JSON Response
```

------------------------------------------------------------------------

# 12. Label Definition

The initial dataset contains two labels:

``` text
ham
spam
```

The application should expose user-friendly output:

``` text
ham  → Not Spam
spam → Spam
```

Internally, the model may represent labels numerically, for example:

``` text
ham  → 0
spam → 1
```

The exact encoding must remain consistent between training and
inference.

------------------------------------------------------------------------

# 13. Neural Network Extension

A TensorFlow/Keras neural-network experiment may be implemented after
the baseline model.

Possible architecture:

``` text
Input
  ↓
TF-IDF / numerical representation
  ↓
Dense Layer
  ↓
ReLU
  ↓
Dropout (optional)
  ↓
Dense Layer
  ↓
Sigmoid
  ↓
Spam Probability
```

Example conceptual architecture:

``` text
Input Features
     ↓
Dense(64, ReLU)
     ↓
Dense(32, ReLU)
     ↓
Dense(1, Sigmoid)
```

The neural network should be evaluated using the same test set
methodology where appropriate.

The neural-network model should not automatically replace the baseline
model unless evaluation demonstrates that the replacement is justified.

------------------------------------------------------------------------

# 14. Data Requirements

## Dataset

Initial dataset:

**UCI SMS Spam Collection**

The dataset contains labeled SMS messages and is used as the initial
text-classification dataset.

### Expected raw format

``` text
ham<TAB>message
spam<TAB>message
```

### Converted DataFrame

``` text
label | text
```

------------------------------------------------------------------------

# 15. Data Quality Requirements

Before training, the pipeline should check:

### Missing Values

``` python
df.isnull().sum()
```

### Duplicates

``` python
df.duplicated().sum()
```

### Class Distribution

``` python
df["label"].value_counts()
```

### Data Types

``` python
df.info()
```

### Sample Records

``` python
df.head()
```

Data quality issues must be handled before model training.

------------------------------------------------------------------------

# 16. Project Directory Structure

Final recommended structure:

``` text
Spam-Email-Detection/
│
├── data/
│   └── SMSSpamCollection
│
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── PRD.md
```

If an advanced neural-network implementation is added:

``` text
models/
└── spam_model.keras
```

may also be included.

------------------------------------------------------------------------

# 17. Module Responsibilities

## `load_data.py`

Responsible for:

-   Loading the raw dataset.
-   Assigning column names.
-   Displaying basic dataset information.
-   Checking missing values.
-   Checking duplicates.
-   Checking label distribution.

## `preprocessing.py`

Responsible for:

-   Text normalization.
-   Cleaning.
-   NLP preprocessing.
-   Reusable preprocessing functions.

## `train.py`

Responsible for:

-   Loading processed data.
-   Splitting the dataset.
-   Creating TF-IDF features.
-   Training the classifier.
-   Evaluating the classifier.
-   Saving the model.
-   Saving the vectorizer.

## `predict.py`

Responsible for:

-   Loading saved artifacts.
-   Transforming new text.
-   Generating predictions.

## `app.py`

Responsible for:

-   Starting Flask.
-   Defining API routes.
-   Validating requests.
-   Calling prediction logic.
-   Returning JSON responses.

------------------------------------------------------------------------

# 18. Dependencies

Initial Python dependencies:

``` text
pandas
numpy
scikit-learn
flask
tensorflow
```

Optional development/testing dependencies may be added later.

A `requirements.txt` file must be generated from the final working
environment.

------------------------------------------------------------------------

# 19. Environment Requirements

Recommended environment:

``` text
Python 3.12
VS Code
Windows
Virtual Environment (.venv)
```

The project should be executed inside a virtual environment.

Example:

``` powershell
python -m venv .venv
```

Activate:

``` powershell
.venv\Scripts\Activate.ps1
```

------------------------------------------------------------------------

# 20. Security and Privacy Requirements

The initial API must not permanently store submitted message text.

Requirements:

1.  Do not log complete message content by default.
2.  Do not save user messages to a database in Version 1.
3.  Do not expose model files through an API route.
4.  Validate request payloads.
5.  Limit unreasonable request sizes.
6.  Do not include sensitive user information in application logs.
7.  Keep secrets and credentials outside source code if future
    integrations require them.

------------------------------------------------------------------------

# 21. Performance Requirements

For the initial local application:

-   API should return predictions quickly for normal-sized messages.
-   Model should be loaded once during application startup rather than
    retrained per request.
-   TF-IDF transformation should be performed only for the incoming
    text.
-   Training is an offline operation.
-   Prediction is an online operation.

### Important distinction

``` text
Training:
Dataset → Model
```

is performed before serving predictions.

``` text
Prediction:
New message → Saved Model → Result
```

is performed for each API request.

------------------------------------------------------------------------

# 22. Error Handling

The application must handle:

### Missing JSON body

``` text
400 Bad Request
```

### Missing `text`

``` text
400 Bad Request
```

### Empty `text`

``` text
400 Bad Request
```

### Invalid JSON

``` text
400 Bad Request
```

### Model file missing

The application should return a clear server-side error and log the
configuration problem.

### Unexpected prediction error

Return a controlled server response rather than exposing Python stack
traces to API clients in production.

------------------------------------------------------------------------

# 23. Testing Requirements

## Dataset Tests

Verify:

-   Dataset loads successfully.
-   Expected columns exist.
-   Text column is usable.
-   Labels contain valid classes.
-   Missing values are handled.
-   Duplicates are identified.

## Model Tests

Verify:

-   Training completes.
-   Model produces predictions.
-   Test metrics are generated.
-   Saved model can be loaded again.
-   Saved vectorizer can transform new text.

## API Tests

Test using Postman.

### Test Case 1 --- Normal Message

``` json
{
  "text": "Please send me the project report."
}
```

Expected:

``` text
ham / Not Spam
```

### Test Case 2 --- Promotional/Prize Message

``` json
{
  "text": "Congratulations! You have won a free prize. Claim now!"
}
```

Expected:

``` text
spam
```

### Test Case 3 --- Empty Message

``` json
{
  "text": ""
}
```

Expected:

``` text
400 Bad Request
```

### Test Case 4 --- Missing Field

``` json
{}
```

Expected:

``` text
400 Bad Request
```

### Test Case 5 --- Health Check

``` http
GET /
```

Expected:

``` text
200 OK
```

------------------------------------------------------------------------

# 24. Model Evaluation Requirements

The project report must include:

``` text
Accuracy
Precision
Recall
F1-score
Confusion Matrix
```

Example reporting format:

``` text
Accuracy : XX.XX%
Precision: XX.XX%
Recall   : XX.XX%
F1 Score : XX.XX%
```

Actual values must be generated from the trained model and must not be
hard-coded into the documentation.

------------------------------------------------------------------------

# 25. Confusion Matrix Interpretation

The confusion matrix should identify:

``` text
                 Predicted
               Ham     Spam

Actual Ham      TN       FP
Actual Spam     FN       TP
```

Where:

-   **TP** = Spam correctly identified as spam.
-   **TN** = Ham correctly identified as ham.
-   **FP** = Ham incorrectly classified as spam.
-   **FN** = Spam incorrectly classified as ham.

For spam detection, both false positives and false negatives are
important and should be discussed.

------------------------------------------------------------------------

# 26. Model Selection Criteria

The project should not select a model based only on accuracy.

Model comparison should consider:

1.  Precision
2.  Recall
3.  F1-score
4.  Confusion matrix
5.  Inference simplicity
6.  Model size
7.  Training time
8.  Interpretability
9.  Suitability for API deployment

The final model should be selected based on measured results and project
requirements.

------------------------------------------------------------------------

# 27. Logging Requirements

Application logs may include:

``` text
Server started
Request received
Prediction completed
Model loaded
Error occurred
```

Logs should avoid storing complete user message content unless
explicitly required for development and handled safely.

------------------------------------------------------------------------

# 28. Deployment Considerations

The first version is intended for local development and Postman testing.

Local server example:

``` text
http://127.0.0.1:5000
```

Future deployment can use a production WSGI server and a cloud platform.

Potential future deployment architecture:

``` text
Client
  ↓
Cloud API
  ↓
Flask Application
  ↓
Saved ML Model
  ↓
Prediction
```

------------------------------------------------------------------------

# 29. Development Phases

## Phase 1 --- Project Setup

-   Create project folder.
-   Create virtual environment.
-   Install dependencies.
-   Create project structure.

## Phase 2 --- Dataset

-   Download dataset.
-   Place dataset under `data/`.
-   Load using Pandas.
-   Inspect structure.

## Phase 3 --- Data Cleaning

-   Handle missing values.
-   Identify duplicates.
-   Normalize labels.
-   Clean text.

## Phase 4 --- NLP

-   Lowercase text.
-   Evaluate punctuation handling.
-   Apply required preprocessing.
-   Generate TF-IDF features.

## Phase 5 --- Model Training

-   Train baseline classifier.
-   Evaluate model.
-   Generate confusion matrix.
-   Compare metrics.

## Phase 6 --- Model Saving

-   Save classifier.
-   Save TF-IDF vectorizer.

## Phase 7 --- Flask API

-   Build health endpoint.
-   Build prediction endpoint.
-   Add validation.
-   Add error handling.

## Phase 8 --- Postman Testing

-   Test normal messages.
-   Test spam messages.
-   Test invalid requests.
-   Test empty requests.

## Phase 9 --- Documentation

-   Create README.
-   Document architecture.
-   Document API.
-   Document model metrics.
-   Document setup instructions.

------------------------------------------------------------------------

# 30. Definition of Done

The project is considered complete when all of the following are true:

-   [ ] Dataset is stored correctly.
-   [ ] Dataset loads successfully using Pandas.
-   [ ] Dataset quality checks are implemented.
-   [ ] Text preprocessing is implemented.
-   [ ] TF-IDF feature extraction works.
-   [ ] Train/test split is implemented.
-   [ ] ML classifier is trained.
-   [ ] Model is evaluated.
-   [ ] Model artifacts are saved.
-   [ ] Flask API starts successfully.
-   [ ] `GET /` health endpoint works.
-   [ ] `POST /predict` works.
-   [ ] Invalid requests are handled.
-   [ ] Postman testing is successful.
-   [ ] README is complete.
-   [ ] PRD is complete.
-   [ ] Project can be reproduced using documented setup instructions.

------------------------------------------------------------------------

# 31. Future Enhancements

Possible future versions may include:

### Version 2

-   Email-specific datasets.
-   Larger and more diverse datasets.
-   Better class balancing.
-   Hyperparameter tuning.
-   Model comparison dashboard.

### Version 3

-   Gmail/Outlook integration.
-   User authentication.
-   Database storage with explicit privacy controls.
-   Admin dashboard.
-   Feedback-based model improvement.

### Advanced NLP

-   Word embeddings.
-   Word2Vec.
-   FastText.
-   Transformer-based models.
-   BERT-style classifiers.

### Production Features

-   Docker.
-   CI/CD.
-   Cloud deployment.
-   API authentication.
-   Rate limiting.
-   Monitoring.
-   Model versioning.

------------------------------------------------------------------------

# 32. Risks and Mitigations

## Risk 1 --- Class Imbalance

Spam and ham counts are not equal.

**Mitigation:**

Use stratified splitting and evaluate precision, recall and F1-score
instead of relying only on accuracy.

## Risk 2 --- Overfitting

The model may perform well on training data but poorly on unseen
messages.

**Mitigation:**

Use a held-out test set and appropriate validation procedures.

## Risk 3 --- Data Leakage

Text vectorization performed before splitting can leak information from
the test set into training.

**Mitigation:**

Fit the TF-IDF vectorizer on training data only and transform the test
data using the fitted vectorizer.

## Risk 4 --- Preprocessing Mismatch

Training and API prediction may use different preprocessing.

**Mitigation:**

Keep preprocessing reusable and consistent.

## Risk 5 --- False Positives

A legitimate message may be classified as spam.

**Mitigation:**

Monitor precision and false-positive behavior.

## Risk 6 --- False Negatives

Spam may be classified as legitimate.

**Mitigation:**

Monitor recall and inspect misclassified examples.

------------------------------------------------------------------------

# 33. Acceptance Criteria

The product will meet the initial requirements when:

1.  A valid message can be submitted using Postman.
2.  The Flask API returns a spam/ham classification.
3.  The model is trained using the project dataset.
4.  The TF-IDF vectorizer used during training is reused during
    inference.
5.  Invalid requests return meaningful HTTP errors.
6.  Dataset validation is performed before model training.
7.  Model evaluation metrics are produced from unseen test data.
8.  Model and vectorizer can be saved and loaded successfully.
9.  The application can be started using documented commands.
10. The project structure is understandable and maintainable.

------------------------------------------------------------------------

# 34. Example End-to-End Usage

Start the application:

``` powershell
python app.py
```

Server:

``` text
http://127.0.0.1:5000
```

Postman:

``` http
POST http://127.0.0.1:5000/predict
```

Body → raw → JSON:

``` json
{
  "text": "Congratulations! You have won a free cash prize. Claim now!"
}
```

Example response:

``` json
{
  "prediction": "spam",
  "confidence": 0.96
}
```

For a legitimate message:

``` json
{
  "text": "Hi, can you send me the assignment before tomorrow?"
}
```

Example response:

``` json
{
  "prediction": "ham",
  "confidence": 0.93
}
```

The numerical confidence shown above is illustrative only. The actual
value must come from the trained model.

------------------------------------------------------------------------

# 35. Success Metrics

The project should be evaluated using measurable technical outcomes
rather than a predefined accuracy target.

Required measurements:

-   Test-set accuracy
-   Precision
-   Recall
-   F1-score
-   Confusion matrix
-   Prediction latency for normal requests
-   Successful API request rate during testing

Actual results must be recorded after training.

------------------------------------------------------------------------

# 36. Documentation Requirements

The final repository should contain:

``` text
README.md
PRD.md
requirements.txt
```

README should explain:

1.  Project overview
2.  Features
3.  Technology stack
4.  Installation
5.  Dataset
6.  Training
7.  Running Flask
8.  Postman API usage
9.  Model evaluation
10. Project structure

PRD should remain the authoritative product requirement document.

------------------------------------------------------------------------

# 37. Final Product Vision

The final system should demonstrate a complete and understandable
machine-learning product lifecycle:

``` text
              DATA
                │
                ▼
        Data Validation
                │
                ▼
       NLP Preprocessing
                │
                ▼
             TF-IDF
                │
                ▼
        Machine Learning
                │
                ▼
          Evaluation
                │
                ▼
         Saved Artifacts
                │
                ▼
          Flask REST API
                │
                ▼
             Postman
                │
                ▼
       Spam / Not Spam
```

The project should prioritize **reproducibility, clean architecture,
correct evaluation, consistent preprocessing, API usability, and clear
documentation**.

------------------------------------------------------------------------

# 38. Final Scope Summary

### In Scope

-   Spam/ham text classification
-   UCI SMS Spam Collection as initial dataset
-   Pandas data analysis
-   NLP preprocessing
-   TF-IDF
-   Machine learning classification
-   Model evaluation
-   Optional TensorFlow/Keras neural-network experiment
-   Model serialization
-   Flask REST API
-   Postman testing
-   Error handling
-   Documentation

### Out of Scope for Version 1

-   Gmail/Outlook integration
-   Database
-   User authentication
-   Automatic email deletion
-   Automatic mailbox filtering
-   Mobile application
-   Browser extension
-   Production-scale monitoring

------------------------------------------------------------------------

**End of PRD**
