import pandas as pd
# === This is for displaying all the columns in the output section ===
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
# ====================================================================

data = [[1, "19 May Street", "Sydney", "NSW", "Australia", "Arijeet Roy"],
        [2, "30 Forest Road", "Sydney", "NSW", "Australia", "Rohan Lala"],
        [3, "12 Carlton", "Sydney", "NSW", "Australia", "Rony Dey"],
        [4, "19 May Street", "Sydney", "NSW", "Australia", "Abhijeet Roy"]]

df = pd.DataFrame(data=data,
                  columns=["ID",
                           "Address",
                           "City",
                           "State",
                           "Country",
                           "Name"])  # Creating the Data frame

# Add another column Continent
df["Continent"] = df["State"] + "," + "Australia"
df["Full Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

print(df)
