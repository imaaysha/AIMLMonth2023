# -*- coding: utf-8 -*-
"""Copy of <23019.>_<AAYSHA NIGAR>_EMAIL SPAM CLASSIFICATION DATASET

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aPrz5-AO8Grmh8V3KezZZjvqbDuSKzVi

# **MINOR PROJECT**

---

# **TASK 1** - Exploratory Data Analysis

<-----------------------Question 1----------------------------->
"""

import pandas as pd

# Read the dataset into a DataFrame
df = pd.read_csv('dataset.csv')

# Generate the summary report
summary_report = df.describe()

# Print the summary report
print(summary_report)

""" variable will contain statistical information such as count, mean, standard deviation, minimum value, 25th percentile, median (50th percentile), 75th percentile, and maximum value for each numerical column in the dataset. By analyzing these statistics, you can gain insights into the dataset's overall structure, the range and distribution of values in each column, as well as any missing data. These insights are crucial for understanding the dataset's characteristics and can guide further analysis or preprocessing steps."""

structure_info = df.info()

summary_stats = df.describe()

"""<-----------------------Question 2----------------------------->"""

import matplotlib.pyplot as plt

# Assuming you have a list or array of labels indicating spam or not-spam
labels = ['spam', 'spam', 'not-spam', 'spam', 'not-spam', 'not-spam', 'not-spam', 'spam']

# Count the occurrences of each label
spam_count = labels.count('spam')
not_spam_count = labels.count('not-spam')

# Create the bar chart
plt.bar(['Spam', 'Not Spam'], [spam_count, not_spam_count])
plt.xlabel('Email Type')
plt.ylabel('Count')
plt.title('Distribution of Spam and Not-Spam Emails')

# Show the bar chart
plt.show()

# Create the pie chart
plt.pie([spam_count, not_spam_count], labels=['Spam', 'Not Spam'], autopct='%1.1f%%')
plt.title('Proportion of Spam and Not-Spam Emails')

# Show the pie chart
plt.show()



"""Bar Chart:

Count the number of spam and not-spam emails in your dataset.
Create a bar chart with two bars, one representing the count of spam emails and the other representing the count of not-spam emails.
Label the x-axis as "Spam" and "Not-Spam" and the y-axis as "Count" or "Frequency."
Adjust the scale of the y-axis to fit the count of emails appropriately.
Optionally, you can add titles, axis labels, and a legend to enhance the clarity of the chart.
Pie Chart:

Count the number of spam and not-spam emails in your dataset.
Calculate the proportions of spam and not-spam emails by dividing their counts by the total count.
Create a pie chart with two sectors, one representing the proportion of spam emails and the other representing the proportion of not-spam emails.
Optionally, you can add labels to the sectors indicating the proportions or percentages.
Additionally, you can emphasize the spam sector by exploding it slightly from the chart to highlight its significance.
You may also add a legend to clarify the colors or labels used in the chart.
Both the bar chart and pie chart will provide a visual summary of the distribution of spam and not-spam labels in your dataset, allowing you to quickly understand the proportion of each category. Choose the visualization that best suits your data and context.Summarizing your analysis and observations
"""





"""<-----------------------Question 3----------------------------->"""

import matplotlib.pyplot as plt
from collections import Counter

# Sample email subjects
email_subjects = [
    "Important information regarding your account",
    "Reminder: Upcoming meeting on Friday",
    "Action required: Update your password",
    "Invitation to the company's annual party",
    "Urgent: Payment overdue for invoice #12345",
    "Re: Your inquiry about product support",
    "Congratulations! You've won a prize",
    "Notification: Package delivery delayed",
    "Meeting minutes for last week's discussion",
    "Reminder: Submit your monthly report"
]

# Combine all email subjects into a single string
all_subjects = ' '.join(email_subjects)

# Split the string into individual words
words = all_subjects.split()

# Count the frequency of each word
word_counts = Counter(words)

# Get the top 5 most frequent words
top_words = word_counts.most_common(5)

# Extract the words and frequencies
word_labels = [word[0] for word in top_words]
word_frequencies = [word[1] for word in top_words]

# Plot the bar chart
plt.bar(word_labels, word_frequencies)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 5 Most Frequent Words in Email Subjects')
plt.show()

"""Using the Counter class from the collections module, the code counts the frequency of each word in the email subjects. It then identifies the top 5 most frequent words using the most_common() method of the Counter object.

To visualize the results, the code creates a bar chart using matplotlib. The x-axis of the chart represents the words, and the y-axis represents the frequency of each word. The labels and title are added to provide context for the chart. Running the code will display the bar chart with the frequencies of the top 5 most common words in the email subjects.

You can modify the email_subjects list with your own data to analyze a different dataset and gain insights into the relative importance of the most frequent words in that dataset.Summarizing your analysis and observation
"""





"""<-----------------------Question 4----------------------------->"""

def calculate_the_frequency(emails):
    total_emails = len(emails)
    the_counts = 0

    for email in emails:
        # Assuming emails are stored as strings
        words = email.split()
        the_counts += words.count("the")

    the_frequency = the_counts / total_emails
    return the_frequency


def is_spam(emails, threshold=0.05):
    the_frequency = calculate_the_frequency(emails)

    if the_frequency > threshold:
        return True
    else:
        return False

email_corpus = [
    "Hello, how are you?",
    "The quick brown fox jumps over the lazy dog.",
    "Get rich quick!",
    "The best deals are here.",
    "Click here for a special offer!"
]

spam_result = is_spam(email_corpus)

print("The frequency of the word 'the' in emails is:", calculate_the_frequency(email_corpus))
print("Is it likely spam?", spam_result)

""" the function calculate_the_frequency takes a list of emails and counts the occurrences of the word "the" in each email. It then calculates the frequency by dividing the total count by the number of emails.

The function is_spam takes the list of emails and an optional threshold parameter. It uses the calculate_the_frequency function to determine the frequency of "the" in the emails and compares it with the threshold. If the frequency is greater than the threshold, it returns True, indicating that the emails are likely spam. Otherwise, it returns False.

The code provided includes an example usage with a sample email_corpus list. You can modify the list with your own email data or use a larger dataset to analyze the frequency and likelihood of spam.Summarizing your analysis and observations
"""



"""<-----------------------Question 5----------------------------->"""

import matplotlib.pyplot as plt

# Sample data (replace with your actual frequency data)
email_numbers = [1, 2, 3, ..., 100]  # Replace with actual email numbers
the_frequencies = [10, 15, 8, ..., 12]  # Replace with actual "the" frequencies
and_frequencies = [8, 12, 6, ..., 10]  # Replace with actual "and" frequencies

# Plotting the data
plt.plot(email_numbers, the_frequencies, label='the')
plt.plot(email_numbers, and_frequencies, label='and')

# Customize the chart
plt.title('Frequency Comparison of "the" and "and" in First 100 Emails')
plt.xlabel('Email Number')
plt.ylabel('Frequency')
plt.legend()

# Display the chart
plt.show()
In this code template, you would replace the email_numbers, the_frequencies, and and_frequencies lists with your actual data. These lists should contain the corresponding email numbers and frequencies for the words "the" and "and" in each email.

Make sure you have the matplotlib library installed (pip install matplotlib) before running this code. It will generate a line graph displaying the frequency comparison of the words "the" and "and" in the first 100 emails.

Remember to adapt this code to your specific data source and extraction method in order to obtain accurate frequency data for the words "the" and "and" in the emails you are analyzing.

"""To plot a comparison chart (line graph) showing the difference in frequency of the words "the" and "and" in the first 100 emails, we would need the actual frequency data for each word in each email. Since I don't have access to your email data or the ability to retrieve specific emails, I can't provide you with an accurate line graph. However, I can still explain how you can create the graph using your own data.

Here are the general steps to create a comparison chart:

Collect the frequency data: Count the occurrences of the words "the" and "and" in each of the first 100 emails. Make sure to record the count for each email separately.

Organize the data: Create a table or a spreadsheet where you can enter the email number (1 to 100) and the corresponding frequencies of "the" and "and" in separate columns.

Prepare the chart: Open a data visualization tool like Microsoft Excel, Google Sheets, or any other graphing software. Select the columns with the email numbers and the frequencies for "the" and "and."

Create a line graph: Once the data is selected, choose the appropriate chart type (line graph) in your graphing software. The email numbers should be on the x-axis, and the word frequencies should be on the y-axis.

Format the chart: Customize the chart as desired, such as adding titles, axis labels, and gridlines. You can also change the line colors, add legends, or adjust the scale of the axes to enhance readability.

Interpret the chart: Analyze the resulting line graph to compare the frequencies of "the" and "and" across the first 100 emails. The line for each word will show the trend in its frequency, allowing you to observe any differences or patterns.

Remember, without the actual frequency data, I can't provide you with a specific line graph, but by following these steps, you should be able to create one using your own data.Summarizing your analysis and observation
"""





"""# **TASK 2** - Classification/Regression

Perform following steps on the same dataset which you used for EDA.
> - Data Preprocessing (as per requirement)
> - Feature Engineering
> - Split dataset in train-test (80:20 ratio)
> - Model selection
> - Model training
> - Model evaluation
> - Fine-tune the Model
> - Make predictions

Summarize your model's performance by evaluation metrices
Simple Linear Regression: This model assumes a linear relationship between a single independent variable and the dependent variable. It uses a straight line to represent the relationship and estimates the slope and intercept of the line.

Multiple Linear Regression: Similar to simple linear regression, but it involves multiple independent variables to predict the dependent variable. It assumes a linear relationship between the predictors and the target variable.

Polynomial Regression: This model extends linear regression by including higher-order polynomial terms of the independent variables. It can capture more complex relationships between variables by introducing curves in the prediction line.

Logistic Regression: Despite its name, logistic regression is used for binary classification problems. It models the relationship between the independent variables and the probability of an event occurring.

Ridge Regression: A regularization technique that helps prevent overfitting in linear regression models by adding a penalty term to the cost function. It reduces the magnitudes of the regression coefficients.

Lasso Regression: Another regularization technique similar to ridge regression but with a different penalty term. Lasso regression performs variable selection by forcing some regression coefficients to become exactly zero, effectively eliminating them from the model.

Elastic Net Regression: Combines the penalties of ridge and lasso regression, providing a balance between both regularization techniques.
"""