# import packages
import pandas as pd
import matplotlib.pyplot as plt  
import streamlit as st

# show the title
st.title('Titanic App by Danying Wei')

# read csv and show the dataframe
df = pd.read_csv('train.csv')

st.subheader('The data are as follow:')
st.dataframe(df)

st.subheader('The percentage of the passengers that boarded at different ports:')
port_percentages = df['Embarked'].value_counts(normalize=True) *100
st.dataframe(port_percentages)  

st.subheader('Histogram of the Embarked column:')
fig, ax = plt.subplots()  
plt.style.use("seaborn-v0_8")  
df.Embarked.hist()
st.pyplot(fig)

st.subheader('Survival rates by gender:')
survival_rates_by_gender = df.groupby('Sex')['Survived'].value_counts(normalize =True)
st.dataframe(survival_rates_by_gender)

st.subheader('Ticket price sorted in descending order:')
fig, ax = plt.subplots()
df['Fare'].sort_values(ascending=False).reset_index(drop=True).plot()
plt.ylabel('Ticket Price')
st.pyplot(fig)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

st.subheader('Ticket price with different classes:')
fig, ax = plt.subplots(1,3,figsize=(15, 5))  
plt.style.use("seaborn-v0_8")  

ax[0].boxplot(df[df['Pclass'] == 1]['Fare'])  
ax[0].set_xlabel('PClass = 1')
ax[0].set_ylabel('Fare')
ax[0].set_xticklabels(['Fare'])  

ax[1].boxplot(df[df['Pclass'] == 2]['Fare'])  
ax[1].set_xlabel('PClass = 2')
ax[1].set_xticklabels(['Fare'])  

ax[2].boxplot(df[df['Pclass'] == 3]['Fare'])  
ax[2].set_xlabel('PClass = 3')
ax[2].set_xticklabels(['Fare'])  

st.pyplot(fig)

st.subheader('Different survival rate by different ticket class:')
fig, ax = plt.subplots()
survival_rate_pclass = df.groupby('Pclass')['Survived'].value_counts(normalize=True)
survival_rate_pclass.plot.bar(survival_rate_pclass.index,survival_rate_pclass)
plt.xlabel('Pclass,Survived')  
st.pyplot(fig)

st.text('For people with ticket class 1, the survival rate is the highest, which is 0.63.')