import pandas as pd
import streamlit as st
import altair as alt

# Load the data from the CSV file
df = pd.read_csv("nfl_passing_stats.csv")

# Convert numeric columns (YDS, TD, INT) from strings with commas to integers
df['YDS'] = df['YDS'].replace({',': ''}, regex=True).astype(int)
df['AVG'] = df['AVG'].astype(float)
df['YDS/G'] = df['YDS/G'].astype(float)

# Streamlit App
st.title("🏈 NFL Passing Stats Dashboard")
st.write("Analyze and compare NFL quarterback performance with interactive visualizations.")

# Sidebar Filters
st.sidebar.header("Filters")
selected_players = st.sidebar.multiselect("Select Players", options=df['NAME'].unique())
selected_teams = st.sidebar.multiselect("Select Teams", options=df['Team'].unique())

# Filter DataFrame
filtered_df = df.copy()
if selected_players:
    filtered_df = filtered_df[filtered_df['NAME'].isin(selected_players)]
if selected_teams:
    filtered_df = filtered_df[filtered_df['Team'].isin(selected_teams)]

# Show Full Dataset
st.subheader("📊 Full Player Statistics")
st.dataframe(df)

# Add Summary Statistics
st.subheader("📈 Summary Statistics")
if not filtered_df.empty:
    summary_stats = filtered_df[['GP', 'CMP', 'ATT', 'CMP%', 'YDS', 'AVG', 'YDS/G', 'LNG', 'TD', 'INT', 'SACK', 'SYL', 'QBR', 'RTG']].describe().loc[['mean', 'std', 'min', 'max']]
    st.write(summary_stats)
else:
    st.write("No data available for the selected filters.")


# Visualizations
st.subheader("🎨 Visual Insights")

if not filtered_df.empty:
    # Bar chart for Total Yards
    st.write("### Total Passing Yards by Player")
    bar_chart = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X('NAME:N', sort='-y', title="Player"),
        y=alt.Y('YDS:Q', title="Total Yards"),
        color=alt.Color('Team:N', legend=None),
        tooltip=['NAME', 'Team', 'YDS']
    ).properties(width=700, height=400)
    st.altair_chart(bar_chart)
    
    # Scatter Plot for Completion % vs Yards
    st.write("### Completion Percentage vs. Yards")
    scatter_plot = alt.Chart(filtered_df).mark_circle(size=80).encode(
        x=alt.X('CMP%:Q', title="Completion Percentage (%)"),
        y=alt.Y('YDS:Q', title="Total Yards"),
        color=alt.Color('Team:N', legend=None),
        tooltip=['NAME', 'Team', 'CMP%', 'YDS']
    ).properties(width=700, height=400)
    st.altair_chart(scatter_plot)

    # Touchdowns vs Interceptions Ratio
    st.write("### Touchdowns vs Interceptions")
    td_int_chart = alt.Chart(filtered_df).mark_circle(size=100).encode(
        x=alt.X('TD:Q', title="Total Touchdowns"),
        y=alt.Y('INT:Q', title="Total Interceptions"),
        color=alt.Color('Team:N', legend=None),
        tooltip=['NAME', 'Team', 'TD', 'INT']
    ).properties(width=700, height=400)
    st.altair_chart(td_int_chart)

    # Average Yards per Attempt vs. Completion Percentage
    st.write("### Average Yards per Attempt vs. Completion Percentage")
    avg_yds_cmp_chart = alt.Chart(filtered_df).mark_circle(size=80).encode(
        x=alt.X('AVG:Q', title="Average Yards per Attempt"),
        y=alt.Y('CMP%:Q', title="Completion Percentage"),
        color=alt.Color('Team:N', legend=None),
        tooltip=['NAME', 'Team', 'AVG', 'CMP%']
    ).properties(width=700, height=400)
    st.altair_chart(avg_yds_cmp_chart)

    # Pass Attempts vs. Completion Percentage
    st.write("### Pass Attempts vs. Completion Percentage")
    att_cmp_chart = alt.Chart(filtered_df).mark_circle(size=80).encode(
        x=alt.X('ATT:Q', title="Total Pass Attempts"),
        y=alt.Y('CMP%:Q', title="Completion Percentage"),
        color=alt.Color('Team:N', legend=None),
        tooltip=['NAME', 'Team', 'ATT', 'CMP%']
    ).properties(width=700, height=400)
    st.altair_chart(att_cmp_chart)

    # Quarterback Rating vs. Touchdowns
    st.write("### Quarterback Rating vs. Touchdowns")
    qbr_td_chart = alt.Chart(filtered_df).mark_circle(size=80).encode(
        x=alt.X('RTG:Q', title="Quarterback Rating"),
        y=alt.Y('TD:Q', title="Total Touchdowns"),
        color=alt.Color('Team:N', legend=None),
        tooltip=['NAME', 'Team', 'RTG', 'TD']
    ).properties(width=700, height=400)
    st.altair_chart(qbr_td_chart)
else:
    st.write("No data available for the selected filters.")
