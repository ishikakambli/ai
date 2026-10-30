# =====================================================================
#combined
# =====================================================================
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.upper()
# 1. Dates & Text Cleaning
if "DOB" in df.columns:
    df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce").fillna("1900-01-01")
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].ffill().bfill().fillna("Unknown")
# 2. Numeric: Coerce strings to NaN, remove negatives, cap outliers (IQR)
num_cols = ["AGE", "MARKS", "PRICE", "QUANTITY", "DISCOUNT"]
for col in num_cols:
    s = pd.to_numeric(df[col], errors="coerce").mask(lambda x: x < 0)
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    df[col] = s.clip(q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)).fillna(s.median())
# 3. Scaling
for col in ["MARKS", "AGE", "PRICE"]:
    df[f"{col}_MINMAX"] = MinMaxScaler().fit_transform(df[[col]]) 
    df[f"{col}_ZSCORE"] = StandardScaler().fit_transform(df[[col]])
# 4. Save
df.dropna(how="all").to_csv("cleaned_data.csv", index=False)
print(df.head())

# =====================================================================
#Data Cleaning-Missing Values
# =====================================================================
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.upper()
print("missing values :\n", df.isna().sum())
print("rows with any missing value:\n", df[df.isna().any(axis=1)])
# Impute values
df["NAME"] = df["NAME"].fillna("unknown")
df["CITY"] = df["CITY"].ffill().bfill()
df["DOB"] = df["DOB"].fillna("1900-01-01")
df["MARKS"] = pd.to_numeric(df["MARKS"], errors="coerce")
df[“MARKS”] = df[“MARKS”]fillna(df["MARKS"].mean())
# Scaling
df["MARKSMINMAX"] = MinMaxScaler().fit_transform(df[["MARKS"]])
df["MARKSZSCORE"] = StandardScaler().fit_transform(df[["MARKS"]])
print(df["MARKS"].describe())
df_any, df_all = df.dropna(how="any"), df.dropna(how="all")
df.to_csv("cleaned.csv", index=False)
# =====================================================================
#Data Cleaning-Handling Noisy data
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt
try:
    df = pd.read_csv('noisy_data.csv')
except Exception:
    df = pd.DataFrame({
        'Date': ['01-01-2023', '02-01-2023', '03-01-2023', '04-01-2023', '05-01-2023'],
        'Product_ID': ['P1001', 'P1002', 'P1003', 'P1004', 'P1005'],
        'Price': [25.99, 19.95, 12.49, 9.99, 150.0],
        'Quantity': [5, 3, 8, 12, 1],
        'Sales_Region': ['North', 'South', 'East', 'West', 'North'],
        'Discount': ['0.1', '0.05', '0.15', '0.2', '0']
    })
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
# Boxplot BEFORE
df['Price'].plot.box(title="Price Before Cleaning")
plt.show()
# IQR Outlier Removal
def remove_outliers(col):
    q1, q3 = col.quantile(0.25), col.quantile(0.75)
    return col.where(col.between(q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)))
df['Price'] = remove_outliers(df['Price'])
df['Quantity'] = remove_outliers(df['Quantity'])
# Handle Categorical Data & Fill Missing Values
df = df[df['Sales_Region'].isin(['North', 'South', 'East', 'West'])]
cols = ['Price', 'Quantity', 'Discount']
df[cols] = df[cols].fillna(df[cols].median())
# Export & Boxplot AFTER
df.to_csv("cleaned_sales_data.csv", index=False)
df['Price'].plot.box(title="Price After Cleaning")
plt.show()
print("Cleaned Data:\n", df)
# =====================================================================
#Data Cleaning-Handling Noisy data
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
df = pd.read_csv("student-data.csv")
print("Missing before:\n", df.isna().sum())
# Dynamic Fill by column type
cat_cols = df.select_dtypes(include=['object', 'string']).columns
num_cols = df.select_dtypes(include='number').columns
df[cat_cols] = df[cat_cols].ffill().bfill()
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
# Scaling
df["age_minmax"] = MinMaxScaler().fit_transform(df[["age"]])
df["age_zscore"] = StandardScaler().fit_transform(df[["age"]])
# Outlier handling with IQR
df["age"].plot.box(title="Age Before Outlier Removal")
plt.show()
q1, q3 = df["age"].quantile(0.25), df["age"].quantile(0.75)
df["age"] = df["age"].where(df["age"].between(q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1))).fillna(df["age"].median())

df["age"].plot.box(title="Age After Outlier Removal")
plt.show()
df_any, df_all = df.dropna(how='any'), df.dropna(how='all')
df.to_csv("student-data-cleaned.csv", index=False)
# =====================================================================
#Data Preprocessing correlation ,heatmap ,chi-square
# =====================================================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
df = pd.read_csv("Suicide-rates-master.csv")
# 1. Heatmap
corr = df.select_dtypes(include='number').corr()
print("Correlation Matrix:\n", corr)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
# 2. Chi-Square Test
def run_chi2(data, col1, col2):
    chi2, p, dof, _ = chi2_contingency(pd.crosstab(data[col1], data[col2]))
    print(f"--- Chi-Square: {col1} vs {col2} ---")
    print(f"Chi2: {chi2:.4f} | p-value: {p:.4f} | DoF: {dof}")
    print("Conclusion:", "REJECT H0 (Dependent)" if p < 0.05 else "FAIL TO REJECT H0 (Independent)")
run_chi2(df, "sex", "generation")
# =====================================================================
#EDA
# =====================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Suicide-rates-master.csv")
# 1. Statistics & Skewness
for col in df.select_dtypes(include=np.number).columns:
    mean, med, mode, skew = df[col].mean(), df[col].median(), df[col].mode()[0], df[col].skew()
    interp = "Symmetric" if np.isclose(mean, med, atol=0.1) else ("Right-skewed" if skew > 0 else "Left-skewed")	
    print(f"{col} | Mean: {mean} | Med: {med} | Mode: {mode} | Skew: {skew} -> {interp}")
# 2. Basic Plots
df['sex'].value_counts().plot.bar(title='Bar - Gender'); 
plt.show()
df['suicides_no'].plot.hist(bins=20, title="Histogram"); 
plt.show()
df['suicides_no'].plot.box(title="Box Plot"); 
plt.show()
# Violin & Scatter
plt.violinplot(df['suicides_no'].dropna());
plt.title("Violin Plot"); 
plt.show()
df.plot.scatter(x='year', y='suicides_no', title="Scatter Plot"); 
plt.show()
# 3. Advanced Plots
df.pivot_table(values='suicides_no', index='year', columns='sex', aggfunc='sum').plot.bar(stacked=True, title="Stacked Bar")
plt.show()
df.groupby('sex')['suicides_no'].sum().plot.pie(labels=['Female', 'Male'], autopct='%1.1f%%', title="Donut Chart")
plt.gca().add_artist(plt.Circle((0, 0), 0.70, fc='white'))
plt.show()
# =====================================================================
#Classification-Decision Tree
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import *
# 1. Load Data (Outcome is already 0 and 1 in diabetes.csv!)
df = pd.read_csv("diabetes.csv")
X = df.drop(columns=['Outcome'])
y = df['Outcome']
# 2. Split, Fit & Predict
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 3. Print All Metrics Directly
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
print("Std Error:", ((acc * (1 - acc)) / len(y_test)) ** 0.5)
print("Precision:", precision_score(y_test, y_pred))
print("Sensitivity:", recall_score(y_test, y_pred))
print("Specificity:", recall_score(y_test, y_pred, pos_label=0))
print("AUC:", roc_auc_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# 4. Plot ROC Curve (1-Line Built-in Shortcut!)
RocCurveDisplay.from_estimator(clf, X_test, y_test, plot_chance_level=True)
plt.show()
# 5. Plot Decision Tree
plot_tree(clf, feature_names=X.columns, class_names=['0', '1'], filled=True, max_depth=3)
plt.show()
# =====================================================================
#Comparing Classification Algorithms
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, roc_curve, auc
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC		
# 1. Load Data & Split
df = pd.read_csv("diabetes.csv")
X = df.drop(columns=['Outcome'])
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 2. Models
models = {
    "DT": DecisionTreeClassifier(max_depth=3, random_state=42),
    "RF": RandomForestClassifier(n_estimators=100, random_state=42),
    "NB": GaussianNB(),
    "LR": LogisticRegression(max_iter=1000),
    "SVM": SVC(probability=True)
}
# 3. Loop
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]   
    # Calculate All Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    spec = cm[0, 0] / (cm[0, 0] + cm[0, 1])   
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    # Unformatted Prints
    print(name)
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("Specificity:", spec)
    print("AUC:", roc_auc)
    print("Confusion Matrix:")
    print(cm)
    plt.plot(fpr, tpr, label=name)
# 4. Plot
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Comparison')
plt.legend()
plt.show()
# =====================================================================
#Classification-Improving Accuracy
# =====================================================================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, roc_curve, auc
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.utils import resample
from scipy.stats import chi2_contingency
# Load data
df = pd.read_csv('dataDecision.csv')
# Data Cleaning
df = df.dropna()  # Drop missing values
df = pd.get_dummies(df, columns=['GENDER', 'AGE'], drop_first=True)
df['LUNG_CANCER'] = df['LUNG_CANCER'].map({'YES': 1, 'NO': 0})
# Exploratory Data Analysis
print("Data Head:")
print(df.head())
# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
# # Chi-Square Test for Categorical Features
# cat_cols = ['GENDER', 'AGE',]  # Replace with actual column names
# for col in cat_cols:
#     contingency_table = pd.crosstab(df[col], df['LUNG_CANCER'])
#     chi2, p, dof, expected = chi2_contingency(contingency_table)
#     print(f"Chi-Square Test for {col}:")
#     print(f"  Chi2: {chi2:.3f}, p-value: {p:.3f}")
# Feature Selection and Target Variable
X = df.drop(columns=['LUNG_CANCER'])
y = df['LUNG_CANCER']
# Scaling
standard_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()
X_std = standard_scaler.fit_transform(X)
X_mm = minmax_scaler.fit_transform(X)
# Train/test split
X_train_std, X_test_std, y_train, y_test = train_test_split(X_std, y, test_size=0.2, random_state=69)
X_train_mm, X_test_mm, _, _ = train_test_split(X_mm, y, test_size=0.2, random_state=69)
# Simple PCA
pca = PCA(n_components=5)
X_train_std_pca = pca.fit_transform(X_train_std)
X_test_std_pca = pca.transform(X_test_std)
X_train_mm_pca = pca.fit_transform(X_train_mm)
X_test_mm_pca = pca.transform(X_test_mm)
# Evaluation function
def evaluate_model(y_true, y_pred, y_prob):
    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=1)
    sens = recall_score(y_true, y_pred)
    spec = cm[0, 0] / (cm[0, 0] + cm[0, 1]) if (cm[0, 0] + cm[0, 1]) else 0
    se = (acc * (1 - acc)) / len(y_true)
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    model_auc = auc(fpr, tpr)
    return acc, cm, prec, sens, spec, se, model_auc
# Models
dt_bag = BaggingClassifier(DecisionTreeClassifier(random_state=69), n_estimators=50, random_state=69)
nb_bag = BaggingClassifier(GaussianNB(), n_estimators=50, random_state=69)
lr = LinearRegression()
# Boosting model
dt_ada = AdaBoostClassifier(DecisionTreeClassifier(random_state=69), n_estimators=50, random_state=69)
# Bootstrap Sampling
X_bootstrap, y_bootstrap = resample(X, y, replace=True, random_state=69)
# Cross-validation setup
cv = KFold(n_splits=5, shuffle=True, random_state=69)
def cross_val_accuracy(model, X_data, y_data):
    scores = cross_val_score(model, X_data, y_data, cv=cv, scoring='accuracy')
    return np.mean(scores)
# Train and evaluate (Standardized)
dt_bag.fit(X_train_std, y_train)
nb_bag.fit(X_train_std, y_train)
lr.fit(X_train_std, y_train)
dt_ada.fit(X_train_std, y_train)
pred_dt_bag = dt_bag.predict(X_test_std)
pred_nb_bag = nb_bag.predict(X_test_std)
pred_lr = lr.predict(X_test_std)
pred_lr_bin = (pred_lr > 0.5).astype(int)
pred_dt_ada = dt_ada.predict(X_test_std)
res_std = {
    'Bagging DT': evaluate_model(y_test, pred_dt_bag, dt_bag.predict_proba(X_test_std)[:, 1]),
    'Bagging NB': evaluate_model(y_test, pred_nb_bag, nb_bag.predict_proba(X_test_std)[:, 1]),
    'Linear Regression': evaluate_model(y_test, pred_lr_bin, pred_lr),
    'AdaBoost DT': evaluate_model(y_test, pred_dt_ada, dt_ada.predict_proba(X_test_std)[:, 1])
}
# Cross-validation accuracy comparison (Bagging DT example)
dt_cv_std = cross_val_accuracy(dt_bag, X_std, y)
# Print results
print("Model Evaluation Results (Standardized)\n")
for model_name in res_std:
    acc_std, cm_std, prec_std, sens_std, spec_std, se_std, auc_std = res_std[model_name]
    print(f"{model_name}:")
    print(f"  Accuracy: {acc_std:.3f}")
    print(f"  Confusion Matrix:\n{cm_std}")
    print(f"  Precision: {prec_std:.3f}")
    print(f"  Sensitivity: {sens_std:.3f}")
    print(f"  Specificity: {spec_std:.3f}")
    print(f"  Standard Error: {se_std:.4f}")
    print(f"  AUC: {auc_std:.3f}\n")
print("Cross-Validation Accuracy (Bagging DT example):")
print(f"  Standard Scaler: {dt_cv_std:.3f}")
# =====================================================================
#Clustering
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
# 1. Load & Scale Data
df = pd.read_csv("C:/Users/Admin/Downloads/Mall_Customers.csv")
print(df.describe())
X = df.drop(columns=['CustomerID', 'Gender'])
X_scaled = StandardScaler().fit_transform(X)
# 2. Elbow Method
wss = [KMeans(k, n_init=10, random_state=42).fit(X_scaled).inertia_ for k in range(1, 16)]
plt.plot(range(1, 16), wss, marker='o')
plt.title("Elbow Method")
plt.show()
# 3. K-Means & PCA Plot
km = KMeans(3, n_init=10, random_state=42).fit_predict(X_scaled)
X_pca = PCA(2).fit_transform(X_scaled)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=km)
plt.title("K-Means (PCA)")
plt.show()
# 4. Dendrogram & Hierarchical Clustering
dendrogram(linkage(X_scaled, method='ward'))
plt.title("Dendrogram")
plt.show()
hc = AgglomerativeClustering(3).fit_predict(X_scaled)
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=hc)
plt.title("Hierarchical Clustering")
plt.show()
# 5. Scores & Cluster Counts
print("K-Means Silhouette:", silhouette_score(X_scaled, km))
print("Hierarchical Silhouette:", silhouette_score(X_scaled, hc))
print("\nK-Means Counts:\n", pd.Series(km).value_counts())
print("\nHierarchical Counts:\n", pd.Series(hc).value_counts())
# =====================================================================
#Association-Apriori
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules
data = pd.read_csv("groceries.csv")
basket = data["Items"].str.get_dummies(sep=", ").astype(bool)
freq = apriori(basket, min_support=0.05, use_colnames=True)
freq.nlargest(15, 'support').plot.bar()
plt.show()
r = association_rules(freq, metric="lift", min_threshold=1.0)
print(r[["antecedents", "consequents", "support", "confidence", "lift"]].head())
# =====================================================================
#Association II-FP Tree
# =====================================================================
import pyfpgrowth, csv
data = [r.split(", ") for r in pd.read_csv("groceries.csv")["Items"]] 
print("Some records:", data[:10])
patterns = pyfpgrowth.find_frequent_patterns(data, 2)
print("Patterns:", patterns)
rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
print("rules output",rules)
# =====================================================================
#Association -III
# =====================================================================
import numpy as np
import pandas as pd
import pyfpgrowth
df = pd.read_csv("diabetes.csv")
baskets = pd.DataFrame({
    "Glucose":  np.where(df["Glucose"] >= 126, "High_Glucose", "Normal_Glucose"),
    "BMI":      np.where(df["BMI"] >= 25, "High_BMI", "Normal_BMI"),
    "Age":      np.where(df["Age"] >= 40, "Age_40_plus", "Age_below_40"),
    "Outcome":  np.where(df["Outcome"] == 1, "Diabetes", "No_Diabetes"),
})
trans = baskets.values.tolist()
print("Some Records:\n", *trans[:10], sep="\n")
patterns = pyfpgrowth.find_frequent_patterns(trans, 200)
for itemset, count in patterns.items():
    print(f"{', '.join(itemset)}: {count}")


