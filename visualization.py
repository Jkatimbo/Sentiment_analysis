import matplotlib.pyplot as plt

def plot_sentiments(sentiments):
    """
    Plot a histogram of sentiment distribution.

    Parameters:
    sentiments (list): A list of sentiments to plot.

    """
    plt.hist(sentiments, bins=3, edgecolor='black')  # Plot histogram with 3 bins
    plt.title('Sentiment Analysis')  # Set the title of the plot
    plt.xlabel('Sentiment')  # Set the x-axis label
    plt.ylabel('Frequency')  # Set the y-axis label
    plt.show()  # Display the plot
