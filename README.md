# Mail Generator
This project retrieves personal information from the database and extracts job requirements from recruitment sites to generate well-suited application emails for the desired positions. This helps save time writing multiple emails while also ensuring diverse and tailored email content for each employer.
## Approaches
![](https://github.com/TranQuocDat0405/mail_gererator/blob/main/app/resource/image.jpg)
## Folder Structure
1. `app/`:
   - Contains the code for load the portfolio
   - Contains the code for clean text from website
   - Contains the code for extract jobs and write the email
2. `resource/`:
   - This folder contains resource files such as test CSV files, output files, images, etc.
3. `vectorstore/`:
   - Stores the data from CSV file to database.
  
## Setup Instructions
1. Install Dependencies: Make sure you have Python installed on your system. Install the required Python libraries by running the following command:
   ```
   pip install -r requirements.txt
   ```
2. Run the FastAPI Server: To start the server, use the following command:
   ```
   streamlit run main.py
   ```
