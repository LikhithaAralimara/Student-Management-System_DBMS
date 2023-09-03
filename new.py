import pandas as pd
import streamlit as st
import mysql.connector

c = mysql.connector.connect(user='root', host='127.0.0.1' , database='studentmanagement')
cursor = c.cursor()

def main():
    st.subheader("query section")
    querry=st.text_input("type your query")


    if(st.button("execute")):

        try:
            cursor.execute(querry)
            data=cursor.fetchall()
            df=pd.DataFrame(data)

            st.success("query successful")
            with st.expander("query results"):
                st.dataframe(df)
        except mysql.connector.Error as err:
            st.error(err)
if __name__=='__main__':
    main()
