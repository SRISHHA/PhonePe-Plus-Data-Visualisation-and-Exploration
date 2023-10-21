import sqlite3
import streamlit as st
import folium
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyo
sqlite_db_file ="youE.db"
sqlite_conn = sqlite3.connect(sqlite_db_file)
sqlite_cursor = sqlite_conn.cursor()



st.write('<h4 style="color: purple;">PHONEPE PLUS DATA VISUALISATION AND EXPLORATION</h4>', unsafe_allow_html=True)
st.write('<h6 style="color: red;">Select the option from the sidebar to view relevant information</h6>', unsafe_allow_html=True)

agg_user = st.sidebar.selectbox("Select Transaction/User", ["Transaction", "User"])
year = st.sidebar.selectbox("Select the year", ["2018", "2019","2020","2021","2022","2023"])
quarters = st.sidebar.selectbox("Select the quarter", ["Q1(Jan-Mar)", "Q2(Apr-Jun)","Q3(Jul-Sept)","Q4(Oct-Dec)"])
def page1():
    if agg_user=="Transaction":
        if quarters=="Q1(Jan-Mar)":
            q=1
        elif quarters=="Q2(Apr-Jun)": 
            q=2
        elif quarters=="Q3(Jul-Sept)":
            q=3
        else:
            q=4
        query='''SELECT State, SUM(sum_column) AS total_transaction_count, 
        SUM(sum1_column) AS total_transaction_amount, 
        AVG(sum2_column) AS avg_transaction_amount
        FROM (
        SELECT State, SUM(Transaction_count) AS sum_column,
	    SUM(Transaction_amount) AS  sum1_column,
	    AVG(Transaction_amount)  AS sum2_column
        FROM agg_tran
        WHERE Quarter = ? AND Year = ?
        GROUP BY State

        UNION ALL

        SELECT State, SUM(Transaction_count),SUM(Transaction_amount) ,AVG(Transaction_amount)  
        FROM top_tran
        WHERE Quarter = ? AND Year = ?
        GROUP BY State

        UNION ALL

        SELECT State, SUM(Transaction_count),SUM(Transaction_amount) ,AVG(Transaction_amount)  
        FROM map_tran
        WHERE Quarter = ? AND Year = ?
        GROUP BY State
        ) AS combined_data 
        GROUP BY State'''
        sqlite_cursor.execute(query, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in sqlite_cursor.description])
        df.drop(columns="State",inplace=True)
        df["State"]=["Andaman & Nicobar","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli and Daman and Diu","Delhi","Goa",
        "Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
        "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan",
        "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
        "Uttarakhand","West Bengal"]
        
        df.to_csv('Agg.csv', index=False)
        df_agg = pd.read_csv('Agg.csv')
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        fig_agg = px.choropleth(df_agg,
        geojson=url,
        featureidkey='properties.ST_NM',locations=df_agg['State'],color=df_agg["total_transaction_amount"],color_continuous_scale='thermal')
        fig_agg.update_geos(fitbounds="locations", visible=False)
        st.write('<h4 style="color: purple;">MAP VISUALISATION FOR TRANSACTION COUNT STATE WISE</h4>', unsafe_allow_html=True)
        st.plotly_chart(fig_agg)
        st.write('<h4 style="color: purple;">TRANSACTION INFORMATION FOR THE SELECTED OPTION</h4>', unsafe_allow_html=True)
        st.write(df)
    if agg_user=="User":
        if quarters=="Q1(Jan-Mar)":
            q=1
        elif quarters=="Q2(Apr-Jun)": 
            q=2
        elif quarters=="Q3(Jul-Sept)":
            q=3
        else:
            q=4
        query2='''SELECT SUM(user)  AS total_count , State
            FROM
           (SELECT SUM(User_Count)  AS user,State  FROM agg_user
            WHERE "Quarter"==? AND "Year"==?
		    GROUP BY State
            UNION ALL
            SELECT SUM(Registered_User),State FROM top_user
            WHERE   "Quarter"==? AND "Year"==?
		    GROUP BY State
            UNION ALL
            SELECT SUM(Registered_User) ,State FROM map_user
             WHERE   "Quarter"==? AND "Year"==?
			  GROUP BY State) AS c
			 GROUP BY State  '''
        sqlite_cursor.execute(query2, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in sqlite_cursor.description])
        
        df.drop(columns="State",inplace=True)
        df["State"]=["Andaman & Nicobar","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli and Daman and Diu","Delhi","Goa",
        "Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep",
        "Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan",
        "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
        "Uttarakhand","West Bengal"]
        df.to_csv('User.csv', index=False)
        df_user = pd.read_csv('User.csv')
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        fig_user = px.choropleth(df_user,
        geojson=url,
        featureidkey='properties.ST_NM',locations=df_user['State'],color=df_user["total_count"],color_continuous_scale='thermal')
        fig_user.update_geos(fitbounds="locations", visible=False)
        st.write('<h4 style="color: purple;">MAP VISUALISATION FOR USER COUNT STATE WISE</h4>', unsafe_allow_html=True)
        st.plotly_chart(fig_user)
        st.write('<h4 style="color: purple;">USER INFORMATION FOR THE SELECTED OPTION</h4>', unsafe_allow_html=True)
        st.write(df)

def page2():
    if agg_user=="Transaction":
        query='''SELECT SUM(sum_column) AS total_amount
        FROM (
        SELECT SUM(Transaction_amount) AS sum_column FROM agg_tran
        WHERE "Quarter"==? AND "Year"==?
        UNION ALL
        SELECT SUM(Transaction_amount) FROM top_tran
        WHERE   "Quarter"==? AND "Year"==?
        UNION ALL
        SELECT SUM(Transaction_amount) FROM map_tran
        WHERE "Quarter"==? AND "Year"==?) AS combined_data;'''
        if quarters=="Q1(Jan-Mar)":
            q=1
        elif quarters=="Q2(Apr-Jun)": 
            q=2
        elif quarters=="Q3(Jul-Sept)":
            q=3
        else:
            q=4
        sqlite_cursor.execute(query, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        my_container = st.container()
        with my_container:
            for row in results:
                val1=row[0]
        query='''SELECT AVG(avg_column) AS total_amount
        FROM (
        SELECT AVG(Transaction_amount) AS avg_column FROM agg_tran
        WHERE "Quarter"==? AND "Year"==?
        UNION ALL
        SELECT AVG(Transaction_amount) FROM top_tran
        WHERE   "Quarter"==? AND "Year"==?
        UNION ALL
        SELECT AVG(Transaction_amount) FROM map_tran
        WHERE "Quarter"==? AND "Year"==?) AS combined_data;'''
        if quarters=="Q1(Jan-Mar)":
            q=1
        elif quarters=="Q2(Apr-Jun)": 
            q=2
        elif quarters=="Q3(Jul-Sept)":
            q=3
        else:
            q=4
        sqlite_cursor.execute(query, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        my_container = st.container()
        with my_container:
            for row in results:
                val2=row[0]
        query='''SELECT SUM(sum_column) AS total_count
        FROM (
        SELECT SUM(Transaction_count) AS sum_column FROM agg_tran
        WHERE "Quarter"==? AND "Year"==?
        UNION ALL
        SELECT SUM(Transaction_count) FROM top_tran
        WHERE   "Quarter"==? AND "Year"==?
        UNION ALL
        SELECT SUM(Transaction_count) FROM map_tran
        WHERE "Quarter"==? AND "Year"==?) AS combined_data;'''
        if quarters=="Q1(Jan-Mar)":
            q=1
        elif quarters=="Q2(Apr-Jun)": 
            q=2
        elif quarters=="Q3(Jul-Sept)":
            q=3
        else:
            q=4
        sqlite_cursor.execute(query, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        my_container = st.container()
        with my_container:
            for row in results:
                val3=row[0]
        
        st.write('<h4 style="color: purple;">TOTAL TRANSACTION INFORMATION </h1>', unsafe_allow_html=True)
        data = {"TOTAL TRANSACTION AMOUNT":[val1],
        "TOTAL AVERAGE TRANSACTION AMOUNT":[val2],
        "TOTAL TRANSACTION COUNT":[val3]}
        df=pd.DataFrame(data)
        st.write("<style>th {font-weight: bold;}</style>", unsafe_allow_html=True)
        st.table(df)
        query='''SELECT State, SUM(sum_column) AS total_transaction_count, 
        SUM(sum1_column) AS total_transaction_amount, 
        AVG(sum2_column) AS avg_transaction_amount
        FROM (
        SELECT State, SUM(Transaction_count) AS sum_column,
	    SUM(Transaction_amount) AS  sum1_column,
	    AVG(Transaction_amount)  AS sum2_column
        FROM agg_tran
        WHERE Quarter = ? AND Year = ?
        GROUP BY State

        UNION ALL

        SELECT State, SUM(Transaction_count),SUM(Transaction_amount) ,AVG(Transaction_amount)  
        FROM top_tran
        WHERE Quarter = ? AND Year = ?
        GROUP BY State

        UNION ALL

        SELECT State, SUM(Transaction_count),SUM(Transaction_amount) ,AVG(Transaction_amount)  
        FROM map_tran
        WHERE Quarter = ? AND Year = ?
        GROUP BY State
        ) AS combined_data 
        GROUP BY State
        ORDER BY total_transaction_count DESC
        LIMIT 10'''
        sqlite_cursor.execute(query, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in sqlite_cursor.description])
        x_values = df["State"]
        y2 = df["total_transaction_amount"]
        y3 = df["avg_transaction_amount"]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x_values, y=y2, name='Transaction_Amount', marker_color='red'))
        fig.add_trace(go.Bar(x=x_values, y=y3, name='Average_Transaction_Amount', marker_color='green'))
        fig.update_layout(width=800, height=400, xaxis_title='Categories', yaxis_title='Values')
        fig.update_layout(barmode='group', xaxis_title='Top 10 Countries', yaxis_title='Values')
        st.write('<h4 style="color: purple;">TOP 10 COUNTRIES ORDERED BY TRANSACTION AMOUNT</h1>', unsafe_allow_html=True)
        st.plotly_chart(fig)
        fig = px.pie(df, names=df["State"], values=df["total_transaction_count"])
        st.write('<h4 style="color: purple;">TOP 10 COUNTRIES ORDERED BY TRANSACTION COUNT</h1>', unsafe_allow_html=True)
        st.plotly_chart(fig)
        query2='''SELECT SUM(Transaction_amount) AS TRANSACTION_AMOUNT ,District 
        FROM map_tran  WHERE Year==? AND Quarter==? GROUP BY District ORDER BY TRANSACTION_AMOUNT DESC LIMIT 10 '''
        sqlite_cursor.execute(query2,(year,q))
        results2 = sqlite_cursor.fetchall()
        df2 = pd.DataFrame(results2, columns=[desc[0] for desc in sqlite_cursor.description])
        fig = px.pie(df2, names=df2["District"], values=df2["TRANSACTION_AMOUNT"])
        st.write('<h4 style="color: purple;">TOP 10 DISTRICTS ORDERED BY TRANSACTION AMOUNT</h1>', unsafe_allow_html=True)
        st.plotly_chart(fig)

        st.write('<h4 style="color: purple;">TRANSACTION AMOUNT ORDERED BY TYPE OF TRANSACTION</h1>', unsafe_allow_html=True)
        query1='''SELECT SUM(Transaction_amount) AS TRANSACTION_AMOUNT ,Transaction_type AS TYPE_OF_TRANSACTION FROM agg_tran WHERE Year==? AND Quarter==?
        GROUP BY Transaction_type
        ORDER BY TRANSACTION_AMOUNT DESC  '''
        sqlite_cursor.execute(query1, (year,q))
        results = sqlite_cursor.fetchall()
        df1 = pd.DataFrame(results, columns=[desc[0] for desc in sqlite_cursor.description])
        st.table(df1)



    if agg_user=="User":
        query='''SELECT SUM(user) AS total_count  
           FROM
           (SELECT SUM(User_Count)  AS user  FROM agg_user
           WHERE "Quarter"==? AND "Year"==?
           UNION ALL
           SELECT SUM(Registered_User) FROM top_user
           WHERE   "Quarter"==? AND "Year"==?
           UNION ALL
           SELECT SUM(Registered_User) FROM map_user
           WHERE "Quarter"==? AND "Year"==?) AS combined_data;'''
        if quarters=="Q1(Jan-Mar)":
            q=1
        elif quarters=="Q2(Apr-Jun)": 
            q=2
        elif quarters=="Q3(Jul-Sept)":
            q=3
        else:
            q=4
        sqlite_cursor.execute(query, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        my_container = st.container()
        with my_container:
            for row in results:
                val1=row[0]
        st.write('<h4 style="color: purple;">USER INFORMATION </h1>', unsafe_allow_html=True)
        data = {"TOTAL USER COUNT":[val1]}
        df=pd.DataFrame(data)
        st.table(df)
        query1='''SELECT SUM(user)  AS total_count , State
           FROM
           (SELECT SUM(User_Count)  AS user,State  FROM agg_user
           WHERE "Quarter"==? AND "Year"==?
		    GROUP BY State
           UNION ALL
           SELECT SUM(Registered_User),State FROM top_user
           WHERE   "Quarter"==? AND "Year"==?
		    GROUP BY State
           UNION ALL
           SELECT SUM(Registered_User) ,State FROM map_user
             WHERE   "Quarter"==? AND "Year"==?
			  GROUP BY State) AS c
			 GROUP BY State
           ORDER BY total_count  DESC LIMIT 10
		    '''
        sqlite_cursor.execute(query1, (q,year,q,year,q,year))
        results = sqlite_cursor.fetchall()
        df1 = pd.DataFrame(results, columns=[desc[0] for desc in sqlite_cursor.description])
        st.write('<h4 style="color: purple;">TOP 10 COUNTRIES ORDERED BY USER COUNT</h1>', unsafe_allow_html=True)
        fig = px.bar(df1, x=df1["State"], y=df1["total_count"])
        st.plotly_chart(fig)
        query2=''' SELECT SUM(Registered_User) AS Count,District,State FROM map_user
                WHERE   "Quarter"==? AND "Year"==?
                GROUP BY District,State 
                ORDER BY  Count  DESC LIMIT 10 '''
        sqlite_cursor.execute(query2, (q,year))
        results = sqlite_cursor.fetchall()
        df2 = pd.DataFrame(results, columns=[desc[0] for desc in sqlite_cursor.description])
        st.write('<h4 style="color: purple;">TOP 10 DISTRICTS ORDERED BY USER COUNT</h1>', unsafe_allow_html=True)
        fig = px.treemap(df2, path=[df2["District"], df2["State"]], values=df2["Count"])
        st.plotly_chart(fig)

        


pages = {
    "Map Visualisation": page1,
    "Analytics": page2,
    
}

# Create a navigation menu to switch between pages
page = st.selectbox("Select a Page you want to view", list(pages.keys()))

# Use the selected page to render content
pages[page]()


    

    
   

    
    


