# import csv
# from functools import reduce
# def load_gdp_data(file_path):

#     """
#     Loads a wide-format GDP CSV and converts it into a list of dictionaries:
#     Each dict has: country, continent, year, gdp
#     """

#     try:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             reader = list(csv.DictReader(f))

            
#             # -------- Functional: get year columns --------

#             year_columns = list(filter(lambda col: col.isdigit(), reader[0].keys()))


#         data_1=list(map(
#             lambda year: list(map(
#                 lambda row: {
#                     "country": row["Country Name"].strip(),
#                     "continent": row["Continent"].strip(),
#                     "year": int(year),
#                     "gdp": float(row[year]) if row[year].strip() else None
#                 }, reader
#         )),
#         year_columns
#     ))

#             # data = list(
#             #     map(
#             #         lambda row: list(
#             #             map(
#             #                 lambda year: {
#             #                     "country": row.get("Country Name", "").strip(),
#             #                     "continent": row.get("Continent", "").strip(),
#             #                     "year": int(year),
#             #                     "gdp": float(row[year]) if row[year].strip() else None
#             #                 },
#             #                 year_columns
#             #             )
#             #         ),
#             #         reader
#             #     )
#             # )

#             # Flatten the list of lists
#             #print(data_1)
#         return reduce(lambda a, b: a + b, data_1, [])

#     except FileNotFoundError:
#         raise Exception("CSV file not found. Please check the path.")
