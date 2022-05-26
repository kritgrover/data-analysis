import matplotlib.pyplot as plt
from pylab import xticks
import numpy as np


# Method to create age histogram
def plot_age_histogram(ages):
    # create the histogram
    plt.hist(ages, bins=[0, 15, 35, 55, 70, 80], color='lightblue', edgecolor='black')

    # set the ticks to the bin values
    xticks([0, 15, 35, 55, 70, 80])

    # set specifics
    plt.title('Ages Histogram')
    plt.ylabel("Number of People")
    plt.xlabel("Age (in cm)")
    plt.show()


# diagnosis is the series extracted from the hospitals dataframe and then converted to a list
def plot_diagnosis_pie_char(diagnosis):
    # the unique names of diagnosis
    labels = np.unique(np.array(diagnosis))

    # sort labels according to their occurrence in the initial list
    sorted(labels, key=lambda x: diagnosis.count(x))

    # stores the occurrences in values
    values = [diagnosis.count(x) for x in labels]

    # explode parameter for the pie chart
    explode = [0.01 for _ in values]

    # generate pie chart
    plt.pie(values, explode, labels=labels, autopct="%.2f%%", shadow=True)
    plt.show()


# heights should be a list of lists: the inner lists should be the of heights of the three hospitals
def plot_height_violin_plot_unified(heights):

    fig, axes = plt.subplots()

    # set the labels on the x-axis
    axes.set_xticks([1])
    axes.set_xticklabels(["Hospitals"])

    # set the labels on the y-axis
    axes.set_ylabel("Heights")
    axes.set_title("Height by hospital")

    # print the plot
    heights = plt.violinplot(heights, showextrema=True, showmeans=True, showmedians=True)
    heights['cmeans'].set_color('r')
    heights['cmedians'].set_color('g')

    plt.show()
