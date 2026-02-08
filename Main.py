from Loader import load_gdp_data 
from Filter import filter_gdp_data,load_config
from Manipulation import Statistical_Analysis
from Visualization import Graph_Visualizations

def main():
    # Load GDP data

    data = load_gdp_data("gdp.csv")
    print("Total records loaded:", len(data))
    print("Sample record:", data[0])

    # Load config
    config = load_config("config.json")
    print("\nFiltering with config:", config)

    # Filter data
    filtered_data,operation = filter_gdp_data(data, config)
    print("Total records after filter:", len(filtered_data))
    print("Sample filtered record:", filtered_data[0] if filtered_data else "No records match")

    # Calculate Statistical Analysis for given config file
    total = Statistical_Analysis(filtered_data,config,operation)
    print(total)

    # Displaying graphs, Region wise Analysis and Year wise Analysis
    Graph_Visualizations(data)

    # Displaying graphs, Region wise Analysis
    #Bar_plot_regions(data)
    #Pie_Chart_region(data)
    #Scatter_plot_Year(data)
    #Line_plot_Year(data)
   


if __name__ == "__main__":
    main()