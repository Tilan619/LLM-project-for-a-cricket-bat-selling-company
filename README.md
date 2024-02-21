# LLM-project-for-a-cricket-bat-selling-store

This is an end to end LLM project based on Google Palm and Langchain. I have build a system that can talk to MySQL database. User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and then executing that query on MySQL database. I made this system for a cricket bat selling store where they maintain their inventory, sales and discounts data in MySQL database. Below is the UI of my system.

![image](https://github.com/Tilan619/LLM-project-for-a-cricket-bat-selling-company/assets/81402719/caf11e2b-9e02-44a1-94ea-247ac6173fc9)


* The cricket bat store sells SS, SG, CA, MRF and Grey Nicolls cricket bats.
* Their inventory, sales and discounts data is stored in a MySQL database.
* I have build an LLM based question and answer system that will use following,
  * Google Palm LLM
  * Hugging face embeddings
  * Streamlit for UI
  * Langchain framework
  * Chromadb as a vector store
  * Few shot learning
* In the UI, store manager/ user can ask questions in a natural language and it will produce the answers.
