from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT

def generate_pdf(filename="Project_Explanation_Report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = styles['Title']
    heading1_style = styles['Heading1']
    heading2_style = styles['Heading2']
    heading3_style = styles['Heading3']
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=15,
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )
    
    bullet_style = ParagraphStyle(
        'BulletBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=15,
        alignment=TA_LEFT,
        spaceAfter=6
    )

    story = []

    # Title
    story.append(Paragraph("Machine Learning Project Report", title_style))
    story.append(Paragraph("Dual-Pipeline Analysis: Regression & Classification", heading2_style))
    story.append(Spacer(1, 12))

    # Introduction
    story.append(Paragraph("Introduction", heading1_style))
    intro_text = ("This document outlines the complete machine learning pipeline implemented in "
                  "<b>miniproject.ipynb</b>. The project features a dual-pipeline approach, "
                  "demonstrating continuous regression on the Diamonds dataset and multinomial "
                  "classification on the Water Potability dataset. It explains <b>what</b> was done, "
                  "<b>where</b> it was implemented, and <b>why</b> specific methodologies were chosen.")
    story.append(Paragraph(intro_text, body_style))
    story.append(Spacer(1, 12))

    # Part 1: Regression
    story.append(Paragraph("Part 1: Continuous Regression Pipeline", heading1_style))
    story.append(Paragraph("<b>Dataset:</b> Diamonds", body_style))
    
    story.append(Paragraph("<b>What is done:</b>", heading3_style))
    story.append(Paragraph("Predicting the continuous numerical price of diamonds based on their physical characteristics.", body_style))
    
    story.append(Paragraph("<b>Where is it done:</b>", heading3_style))
    story.append(Paragraph("Steps 1.1 through 1.7 in miniproject.ipynb.", body_style))
    
    story.append(Paragraph("<b>Why is it done:</b>", heading3_style))
    story.append(Paragraph("To demonstrate linear modeling techniques and feature impact analysis on a continuous target variable.", body_style))
    
    story.append(Paragraph("<b>Detailed Pipeline Execution:</b>", heading3_style))
    
    p1_bullets = [
        "<b>1. Data Loading (Step 1.1):</b> Retrieved the dataset via kagglehub.",
        "<b>2. Preprocessing & Data Splitting (Step 1.2):</b> Separated features and target. Used One-Hot Encoding to convert categorical data ('cut', 'color', 'clarity') into numeric forms for model compatibility. Split data into 80% training and 20% testing sets to evaluate unseen performance. Applied StandardScaler to continuous features ensuring uniform gradient descent and preventing features with larger scales from dominating the distance metrics.",
        "<b>3. Model Training (Steps 1.3 - 1.5):</b> Trained three distinct linear models: Standard Linear Regression, Lasso Regression (L1 regularization to force sparsity and perform feature selection), and Ridge Regression (L2 regularization to prevent extreme weights and overfitting).",
        "<b>4. Evaluation & Visualization (Step 1.6):</b> Compared models using R² Score and Mean Squared Error (MSE), plotted with Seaborn to provide visual clarity on model performance.",
        "<b>5. Feature Importance (Step 1.7):</b> Extracted coefficients from the Lasso model to quantitatively demonstrate which physical features of a diamond most heavily dictate its price."
    ]
    
    for bullet in p1_bullets:
        story.append(Paragraph(bullet, bullet_style))
    
    story.append(Spacer(1, 18))

    # Part 2: Classification
    story.append(Paragraph("Part 2: Multinomial Classification Pipeline", heading1_style))
    story.append(Paragraph("<b>Dataset:</b> Water Potability", body_style))
    
    story.append(Paragraph("<b>What is done:</b>", heading3_style))
    story.append(Paragraph("Classifying water samples into three discrete potability categories based on their chemical attributes.", body_style))
    
    story.append(Paragraph("<b>Where is it done:</b>", heading3_style))
    story.append(Paragraph("Steps 2.1 through 2.11 in miniproject.ipynb.", body_style))
    
    story.append(Paragraph("<b>Why is it done:</b>", heading3_style))
    story.append(Paragraph("To implement robust preprocessing that prevents data leakage, resolve class imbalances using synthetic resampling, and evaluate advanced non-linear classification models.", body_style))
    
    story.append(Paragraph("<b>Detailed Pipeline Execution:</b>", heading3_style))
    
    p2_bullets = [
        "<b>1. Data Loading & Target Engineering (Step 2.1):</b> Downloaded data. Since the goal was multinomial classification, a synthetic 3-class target ('Potability_Class') was engineered based on pH quantiles.",
        "<b>2. Preprocessing & Anti-Leakage (Step 2.2):</b> The original 'ph' column was explicitly dropped to prevent severe data leakage. Handled missing data by imputing median values to maintain dataset integrity. Scaled the data with StandardScaler.",
        "<b>3. SMOTE Resampling (Step 2.2):</b> Applied the Synthetic Minority Over-sampling Technique (SMOTE) strictly on the training set. This was crucial to resolve class imbalance and ensure the models wouldn't become biased towards the majority class.",
        "<b>4. Model Initialization & Training (Steps 2.3 - 2.9):</b> Trained an array of algorithms ranging from simple to complex: Logistic Regression (L1 & L2 solvers), Decision Tree, Random Forest, K-Nearest Neighbors, and XGBoost.",
        "<b>5. Evaluation Matrices (Steps 2.4 - 2.9):</b> Calculated Accuracy, Precision, Recall, and Weighted F1-Scores. Visualized detailed performance breakdowns via Confusion Matrices.",
        "<b>6. Final Visual Comparison & Insights (Steps 2.10 - 2.11):</b> Compared all classifiers based on their F1-Scores on a seaborn bar plot. Finally, extracted feature importances via the Random Forest model to identify the most critical chemical components determining water safety."
    ]
    
    for bullet in p2_bullets:
        story.append(Paragraph(bullet, bullet_style))

    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Conclusion:</b>", heading2_style))
    story.append(Paragraph("The pipeline demonstrates an end-to-end best-practice workflow for ML: proper data isolation, anti-leakage principles, rigorous feature scaling, imbalance resolution via SMOTE, and comprehensive metric evaluation across varying model complexities.", body_style))

    # Build PDF
    doc.build(story)
    print(f"Successfully created PDF: {filename}")

if __name__ == "__main__":
    generate_pdf()
