#5) Exploratory Data Analysis (EDA) - exploring and analyzing data

#importing packages directly on top of the program
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import pearsonr

def EDA(data):

    #5.1) ata exploration - exploring (or) understanding (or) visualizing data (data patterns (or) relationship)
    #data relationship - finding relationship between salary and job experience of the people 
    def data_exploration(data):
        
        #i) identifying nature of variables salary and job experience of the people
        def identify_variable_nature(data):
            #a) checking data types
            print(f"Data Types Of Variables:\n{data.dtypes}")
            #b) checking unique values
            print(f"Unique Values Of Variables:\n{data.nunique()}")
            var_len = len(data.columns)
            for v in range(var_len):
                print(f"Variable {v+1}: {data.columns[v]}:\n{data[data.columns[v]].value_counts()}\n")
        
        #i) exploring histogram for variables salary and job experience of the people to visualize their nature
        def explore_histogram(data):
            
            #a) creating histogram
            def create_histogram(data):
                
                #analyzing distribution
                data.hist()
                plt.xlabel(f"{data.columns[0]} (years)")
                plt.ylabel(f"{data.columns[1]} (₹)")
                plt.title(f"Nature of {data.columns[0]} and {data.columns[1]}")
                return plt
            
            #b) saving histogram
            def save_histogram(plt):
                
                #saving matplotlib plot
                plt.savefig('salary_prediction_histogram.png', format = 'png', dpi = 500, transparent = False)
            
            #c) displaying histogram
            def show_histogram(plt):
                plt.gcf().canvas.manager.set_window_title("Histogram")
                plt.show()
            
            #executing sub-steps of scatter plot exploration
            def execute_all_histogram_explore(data):
                plt = create_histogram(data)
                save_histogram(plt)
                show_histogram(plt)
            
            execute_all_histogram_explore(data)
        
        #ii) exploring box plot to detect outliers in the data
        def explore_box_plot(data):
            
            #a) creating box plot
            def create_box_plot(data):
                #a) using seaborn
                
                #creating sub-plots for variables x and y
                fig, axes = plt.subplots(1, 2, figsize = (12, 5))
                
                #analyzing outliers (continuous data distribution - y-axis; categorical data distribution - x-axis)
                sns.boxplot(y = data[data.columns[0]], ax = axes[0])
                axes[0].set_title(f"Box plot of {data.columns[0]}")
                sns.boxplot(y = data[data.columns[1]], ax = axes[1])
                axes[1].set_title(f"Box plot of {data.columns[1]}")
                
                return plt
            
            #b) saving box plot
            def save_box_plot(plt):
                
                #saving matplotlib plot
                plt.savefig('salary_prediction_boxplot.png', format = 'png', dpi = 500, transparent = False)
            
            #c) displaying box plot
            def show_box_plot(plt):
                plt.gcf().canvas.manager.set_window_title("Box Plot")
                plt.show()
            
            #executing sub-steps of box plot exploration
            def execute_all_box_plot_explore(data):
                plt = create_box_plot(data)
                save_box_plot(plt)
                show_box_plot(plt)
            
            execute_all_box_plot_explore(data)
        
        #iii) exploring scatter plot for salary and job experience of the people with regression line
        def explore_scatter_plot(data):
            
            #a) creating scatter plot
            def create_scatter_plot(data):
                #a) using plotly
                plotly_figure = px.scatter(data_frame = data, x = data.columns[0], y = data.columns[1], size = data.columns[1], trendline = 'ols')
                
                #b) using seaborn and matplotlib
                plt.figure(figsize = (7,5))
                sns.regplot(data = data, x = data.columns[0], y = data.columns[1], order = 1, scatter = True,
                            scatter_kws = {'color': 'blue', 's': 100, 'alpha': 0.7}, line_kws = {'color': 'red', 'linewidth': 2, 'linestyle': 'solid'})
                plt.xlabel(f"{data.columns[0]} (years)")
                plt.ylabel(f"{data.columns[1]} (₹)")
                plt.title(f"Relationship between {data.columns[0]} and {data.columns[1]}")
                plt.legend(labels = [f"{data.columns[0]} (years)",f"{data.columns[1]} (₹)"], fontsize = 12,
                           title = 'Legend', loc = 'upper left', frameon = True, shadow = True)
                
                return plotly_figure, plt
            
            #b) saving scatter plot
            def save_scatter_plot(plotly_figure, plt):
                
                #saving plotly figure
                if plotly_figure is not None:
                    plotly_figure.write_html("salary_prediction_scatterplot.html")
                
                #saving matplotlib plot
                plt.savefig('salary_prediction_scatterplot.png', format = 'png', dpi = 500, transparent = False)
            
            #c) displaying scatter plot
            def show_scatter_plot(plotly_figure, plt):
                plotly_figure.show()
                plt.gcf().canvas.manager.set_window_title("Scatter Plot")
                plt.show()
            
            #executing sub-steps of scatter plot exploration
            def execute_all_scatter_explore(data):
                plotly_figure, plt = create_scatter_plot(data)
                save_scatter_plot(plotly_figure, plt)
                show_scatter_plot(plotly_figure, plt)
            
            execute_all_scatter_explore(data)
        
        #iv) exploring correlation matrix for salary and job experience of the people
        def explore_correlation_matrix(data):
            
            #q) creating correlation matrix
            def create_correlation_matrix(data):
                correlation_matrix = data.corr()
                plt.figure(figsize = (5,4))
                sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm', fmt = '.2f', linewidths = 1, linecolor = 'black', vmin = 0, vmax = 1)
                plt.title(f"Correlation heatmap for {data.columns[0]} and {data.columns[1]}")
                return plt
            
            #b) saving correlation matrix
            def save_correlation_matrix(plt):
                
                #saving matplotlib plot
                plt.savefig('salary_prediction_correlation_matrix.png', format = 'png', dpi = 500, transparent = False)
            
            #c) displaying correlation matrix
            def show_correlation_matrix(plt):
                plt.gcf().canvas.manager.set_window_title("Correlation Matrix")
                plt.show()
            
            #executing sub-steps of scatter plot exploration
            def execute_all_corr_mat_explore(data):
                plt = create_correlation_matrix(data)
                save_correlation_matrix(plt)
                show_correlation_matrix(plt)
            
            execute_all_corr_mat_explore(data)
        
        #executing all sub-steps of data exploration
        def execute_all_explore(data):
            print("Identifying Variable Nature")
            identify_variable_nature(data)
            print("Using Histogram...")
            explore_histogram(data)
            print("Using Box Plot...")
            explore_box_plot(data)
            print("Using Scatter Plot...")
            explore_scatter_plot(data)
            print("Using Correlation Matrix...")
            explore_correlation_matrix(data)
            print("Data is explored successfully\n")
        
        execute_all_explore(data)
    
    #5.2) data analysis - analysing data - drawing insights and conclusions from data
    def data_analysis(data):
        
        #i) displaying correlation coefficient
        def show_correlation_coefficient(data):
            #a) scipy
            correlation, p_value = pearsonr(data[data.columns[0]], data[data.columns[1]])
            print(f"Correlation = {correlation:.2f}, p_value = {p_value:.5f}")
        
        #ii) executing all sub-steps of data analysis
        def execute_all_analyse(data):
            show_correlation_coefficient(data)
            print("Data is analysed successfully\n")
        
        execute_all_analyse(data)
    
    def execute_all_EDA(data):
        data_exploration(data)
        data_analysis(data)
        print("Data is explored and analysed successfully\n")

    execute_all_EDA(data)
