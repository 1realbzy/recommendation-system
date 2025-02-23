# Recommendation System Analysis & Modeling

## Project Overview
This project focuses on developing a sophisticated recommendation system using a real-world e-commerce dataset. The system aims to solve two main tasks: predicting item properties from user behavior and detecting abnormal users.

### Dataset Characteristics
- 4.5 months of user interaction data
- 2,756,101 total events
  - 2,664,312 views
  - 69,332 add to carts
  - 22,457 transactions
- 1,407,580 unique visitors
- 417,053 unique items
- 20,275,902 item property records
- 1,669 category relationships

### Key Objectives
1. Task 1: Property Prediction
   - Predict item properties for "addtocart" events
   - Use "view" event patterns
   - Handle implicit user preferences

2. Task 2: Abnormal User Detection
   - Identify abnormal e-shop users
   - Improve recommendation effectiveness
   - Reduce bias in split tests

## Project Timeline (4 Weeks)

### Week 1 (Current)
- [x] Project setup and repository initialization
- [x] Data acquisition and initial understanding
- [ ] Business understanding documentation
- [ ] First Medium article: "Getting Started with Recommendation Systems"

### Week 2
- [ ] Data preprocessing and feature engineering
- [ ] Exploratory Data Analysis (EDA)
- [ ] Initial model prototyping
- [ ] Medium article: "Data Preprocessing and EDA for Recommendation Systems"

### Week 3
- [ ] Model development and optimization
- [ ] Implementation of different recommendation approaches
- [ ] Performance evaluation
- [ ] Medium article: "Building and Optimizing Recommendation Models"

### Week 4
- [ ] Fine-tuning and optimization
- [ ] Documentation and results analysis
- [ ] Final presentation preparation
- [ ] Medium article: "Lessons Learned: Implementing a Production-Ready Recommendation System"

## Daily Progress Tracking

### Week 1
- Day 1: Repository setup, project structure creation ✓
- Day 2: Data acquisition and initial dataset understanding ✓
- Day 3: Business understanding documentation and analysis planning
- Day 4: TBD
- Day 5: TBD

## Project Structure
```
recommendation-system/
├── data/                      # Data files
│   ├── events.csv            # User interaction events (90MB)
│   ├── item_properties_*.csv # Item characteristics (852MB total)
│   └── category_tree.csv     # Category hierarchy (14KB)
├── notebooks/                 # Jupyter notebooks for analysis
├── src/                      # Source code
│   ├── data_preprocessing/   # Data cleaning and preparation
│   ├── feature_engineering/  # Feature creation and transformation
│   ├── models/              # Recommendation system models
│   └── evaluation/          # Model evaluation metrics
├── visualizations/           # Generated plots and visualizations
├── requirements.txt          # Project dependencies
└── README.md                # Project documentation
```

## Data Description

### events.csv
- User interaction events (views, add to cart, transactions)
- Format: timestamp, visitorId, eventType, itemId, [transactionId]

### item_properties.csv
- Time-dependent item characteristics
- Special properties:
  - categoryid: Category identifier
  - available: Item availability (1/0)
- Value formats:
  - Numerical: prefixed with 'n', 3 decimal places
  - Text: stemmed and hashed words

### category_tree.csv
- Category hierarchy relationships
- Format: childCategoryId, parentCategoryId

## Documentation Strategy
1. **Daily GitHub Commits**
   - Code changes and improvements
   - Progress updates in README
   - Documentation updates

2. **Weekly Medium Articles**
   - Technical deep-dives into the week's progress
   - Challenges faced and solutions implemented
   - Insights and learnings

## Tools and Technologies
1. **Python** - Primary programming language
   - pandas: Data manipulation and analysis
   - numpy: Numerical computing
   - scikit-learn: Machine learning algorithms
   - scipy: Scientific computing
   - matplotlib/seaborn: Data visualization
   - surprise: Recommendation system library

2. **Jupyter Notebooks** - Interactive development and documentation

3. **Git/GitHub** - Version control and project management

## CRISP-DM Framework Implementation

### 1. Business Understanding
- Define business objectives and success criteria
- Develop analytical questions
- Identify key stakeholders and requirements

### 2. Data Understanding
- Data collection and exploration
- Quality assessment
- Initial insights discovery

### 3. Data Preparation
- Data cleaning and preprocessing
- Feature engineering
- Dataset splitting

### 4. Modeling
- Implementation of recommendation algorithms:
  - Collaborative Filtering
  - Content-Based Filtering
  - Hybrid Approaches

### 5. Evaluation
- Model performance metrics
- Business success criteria validation
- Model comparison and selection

### 6. Deployment
- Model deployment strategy
- Monitoring and maintenance plan
- Documentation and knowledge transfer

## Getting Started
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Follow the notebooks in the `notebooks/` directory

## License
[MIT License](LICENSE) 
