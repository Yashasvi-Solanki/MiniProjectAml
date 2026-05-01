import json

notebook_path = "miniproject.ipynb"

# Read notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Define new markdown cell
md_cell = {
   "cell_type": "markdown",
   "id": "roc_curve_md",
   "metadata": {},
   "source": [
    "## Step 2.12: Evaluation - Macro-Average ROC Curves (One-vs-Rest)\n",
    "Plotting the macro-average Receiver Operating Characteristic (ROC) curves for all classification models to evaluate their multi-class discriminatory power."
   ]
}

# Define new code cell
code_source = """from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

# Binarize the test labels for One-vs-Rest ROC evaluation
y_test_bin = label_binarize(y_clf_test, classes=[0, 1, 2])
n_classes = y_test_bin.shape[1]

plt.figure(figsize=(12, 8))

for name, model in clf_models.items():
    if hasattr(model, "predict_proba"):
        # Get probability scores
        y_score = model.predict_proba(X_clf_test_scaled)
        
        fpr = dict()
        tpr = dict()
        
        # Calculate ROC for each class
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_score[:, i])
            
        # Aggregate all false positive rates
        all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
        
        # Interpolate all ROC curves at these points
        mean_tpr = np.zeros_like(all_fpr)
        for i in range(n_classes):
            mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
            
        # Average to get macro-average TPR
        mean_tpr /= n_classes
        
        # Calculate macro AUC
        macro_auc = auc(all_fpr, mean_tpr)
        
        # Plot
        plt.plot(all_fpr, mean_tpr,
                 label=f'{name} (AUC = {macro_auc:.3f})',
                 linewidth=2)

# Plot random guessing baseline
plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Guessing')

plt.xlim([-0.01, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate', fontsize=12)
plt.title('Macro-Average ROC Curves for Water Potability Classification', fontsize=14)
plt.legend(loc="lower right", fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()"""

code_cell = {
   "cell_type": "code",
   "execution_count": None,
   "id": "roc_curve_code",
   "metadata": {},
   "outputs": [],
   "source": [line + "\n" if i < len(code_source.split('\n')) - 1 else line for i, line in enumerate(code_source.split('\n'))]
}

# Append cells
nb['cells'].extend([md_cell, code_cell])

# Write notebook back
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Successfully added ROC curve cells to miniproject.ipynb")
