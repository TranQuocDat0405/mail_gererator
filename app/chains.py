import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )
    def extract_jobs(self,cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the 
            following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):    
            """
        )

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_email(self,job,links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Trần Quốc Đạt, a student majoring in AI Engineering at VNUHCM - University of Science.
            VNUHCM - University of Science is a scientific institution specializing in teaching information technology
            and automation tools to optimize business processes.
            During my years at the university, I have worked on projects using customized solutions to enable
            scalability, process optimization, cost reduction, and overall efficiency improvement.
            Your task is to write a cold email to a recruiter regarding the mentioned job, describing my ability to meet their needs.
            Additionally, include the most relevant content from the following links to showcase my project portfolio: {link_list}
            Remember, you are Trần Quốc Đạt, a student majoring in AI Engineering at VNUHCM - University of Science.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
