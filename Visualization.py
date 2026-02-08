import matplotlib.pyplot as plt
import tkinter as tk
import matplotlib.ticker as mtick

def Graph_Visualizations(data): 
    Pie_Chart_region(data)
    Bar_plot_regions(data)
    Scatter_plot_Year(data)
    Line_plot_Year(data)

def Pie_Chart_region(data):
    continents = sorted(list(set(map(lambda r:r['continent'],data))))
    
    gdp_values = list(map(
                    lambda cont: 
                    sum(map(
                            lambda row:float(row['gdp']),
                            
                            filter(lambda row: row['continent'] == cont and row['gdp'], data)
                            
                        )),
                    continents
    ))
    total = sum(gdp_values)
    percentages = [100 * val / total for val in gdp_values]
    
    fig, ax = plt.subplots(figsize=(10,6))

    ax.pie(
        gdp_values, 
        labels=None,
        startangle=90
    )
    
    # Legend with percentages
    legend_labels = [f"{cont}: {perc:.1f}%" for cont, perc in zip(continents, percentages)]
    ax.legend(legend_labels, title="Continents", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    ax.set_title("GDP Analysis by Continent")
    plt.tight_layout()

    plt.show()

def Bar_plot_regions(data):
    
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    
    fig, ax = plt.subplots(figsize=(screen_width/100, screen_height/100))
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

    continents = sorted(list(set(map(lambda r:r['continent'],data))))
    

    
    gdp_values = list(map(
                    lambda cont: 
                    sum(map(
                            lambda row:float(row['gdp']),
                            
                            filter(lambda row: row['continent'] == cont and row['gdp'], data)
                            
                        )),
                    continents
    ))

    
    

    bar_labels = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'cyan']

    bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown', 'tab:cyan']

    
    ax.bar(continents, gdp_values, label=bar_labels, color=bar_colors)
    
    ax.set_ylabel('GDP values')
    ax.set_title('Region-wise Plot of GDP')
    ax.legend(title='Regions Color')
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    plt.show()

def Scatter_plot_Year(data):

    Years = sorted(list(set(map(lambda r:r['year'],data))))
    
    #print(Years)
    
    gdp_values = list(map(
                    lambda year: 
                    sum(map(
                            lambda row:float(row['gdp']),
                            
                            filter(lambda row: row['year'] == year and row['gdp'], data)
                            
                        )),
                    Years
    ))



    fig, ax = plt.subplots()

    ax.scatter(Years, gdp_values)
    
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP (Trillion)")
    ax.set_title("Year-wise GDP Scatter Plot")
    
    plt.show()
    
def Line_plot_Year(data):

    Years = sorted(list(set(map(lambda r:r['year'],data))))
    
    #print(Years)
    
    gdp_values = list(map(
                    lambda year: 
                    sum(map(
                            lambda row:float(row['gdp']),
                            
                            filter(lambda row: row['year'] == year and row['gdp'], data)
                            
                        )),
                    Years
    ))



    fig, ax = plt.subplots()

    ax.plot(Years, gdp_values)
    
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP (Trillion)")
    ax.set_title("Year-wise GDP Line Plot")
    
    plt.show()
    