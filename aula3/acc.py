"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def extract_pdf_pages(pathname: str) -> list[str]:
  parts = [f"--- START OF PDF ${pathname} ---"]
  # Add logic to read the PDF and return a list of pages here.
  pages = []
  for index, page in enumerate(pages):
    parts.append(f"--- PAGE {index} ---")
    parts.append(page)
  return parts

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document0.pdf")
  },
  {
    "role": "model",
    "parts": ["## Analysis of BSI.CERES - Resolução 01.2024 - Atividades Curriculares Complementares\n\nThis document outlines the guidelines for fulfilling complementary curricular workload requirements for the Information Systems (SI) course at UFRN-CERES, replacing the previous resolution from 2023. \n\nHere's a breakdown of the key points:\n\n**Objectives and Importance:**\n\n* Complementary activities aim to enrich the learning process, connecting students with ethics, social realities, and professional development. \n* They encourage continuous learning, ethical conduct, and social responsibility.\n* Completing these activities is mandatory for graduation.\n\n**Types of Activities:**\n\nThe resolution categorizes activities into seven groups:\n\n* **Teaching Initiation:** Includes activities like participating in mentoring projects, presenting workshops, and involvement in teaching programs.\n* **Research Initiation:** Covers participation in research projects as a scholarship holder, volunteer, or collaborator.\n* **Extension Activities:**  Engaging in extension projects, courses, or events registered with the Pro-Rector of Extension.\n* **Professional Initiation (Non-mandatory):**  This includes non-mandatory internships, participation in junior companies, and working as a professional in the IT field.\n* **Technical/Scientific/Artistic Production:**  Publishing in academic journals, books, conference proceedings, and other publications.\n* **Participation in Events/Seminars:** Attending or participating in technical, scientific, artistic, or sporting events.\n* **Other Activities:** Activities approved by the course board, such as technical-scientific activities within UFRN, volunteering, and participation in sustainability initiatives. \n\n**Workload and Validation:**\n\n* Each activity has a specific workload value, either per activity (CHA) or per semester (CHS).\n* Students must submit documentation as proof of participation to the Complementary Activities Coordinator for validation.\n* The course coordinator maintains records of completed activities.\n\n**Additional Notes:**\n\n* Students must enroll in complementary curricular components during the registration period.\n* Activities not listed in the document can be evaluated and approved by the course board.\n* The document provides detailed instructions on filling out the Activity Completion Request Form (Annex 2). \n\n**Overall, this resolution provides a comprehensive framework for students to engage in diverse learning experiences beyond the traditional curriculum, enhancing their personal and professional development.**"]
  },
  {
    "role": "user",
    "parts": ["Traduza para português"]
  },
  {
    "role": "model",
    "parts": ["## Análise de BSI.CERES - Resolução 01.2024 - Atividades Curriculares Complementares\n\nEste documento descreve as diretrizes para o cumprimento das atividades curriculares complementares do curso de Sistemas de Informação (SI) da UFRN-CERES, substituindo a resolução anterior de 2023.\n\nAqui está um resumo dos pontos principais:\n\n**Objetivos e Importância:**\n\n* As atividades complementares visam enriquecer o processo de aprendizagem, conectando os alunos com a ética, as realidades sociais e o desenvolvimento profissional.\n* Elas incentivam o aprendizado contínuo, a conduta ética e a responsabilidade social.\n* A conclusão dessas atividades é obrigatória para a graduação.\n\n**Tipos de Atividades:**\n\nA resolução categoriza as atividades em sete grupos:\n\n* **Iniciação à Docência:** Inclui atividades como participação em projetos de monitoria, apresentação de workshops e envolvimento em programas de ensino.\n* **Iniciação à Pesquisa:** Abrange a participação em projetos de pesquisa como bolsista, voluntário ou colaborador.\n* **Atividades de Extensão:** Participação em projetos, cursos ou eventos de extensão registrados na Pró-Reitoria de Extensão.\n* **Iniciação Profissional (Não obrigatória):**  Isso inclui estágios não obrigatórios, participação em empresas juniores e trabalho como profissional na área de TI.\n* **Produção Técnica/Científica/Artística:** Publicação em periódicos acadêmicos, livros, anais de conferências e outras publicações.\n* **Participação em Eventos/Seminários:** Assistir ou participar em eventos técnicos, científicos, artísticos ou esportivos.\n* **Outras Atividades:** Atividades aprovadas pelo colegiado do curso, como atividades técnico-científicas na UFRN, voluntariado e participação em iniciativas de sustentabilidade.\n\n**Carga Horária e Validação:**\n\n* Cada atividade possui um valor específico de carga horária, seja por atividade (CHA) ou por semestre (CHS).\n* Os alunos devem enviar a documentação como comprovante de participação ao Coordenador de Atividades Complementares para validação.\n* O coordenador do curso mantém registros das atividades concluídas.\n\n**Observações Adicionais:**\n\n* Os alunos devem se matricular nos componentes curriculares complementares durante o período de matrícula.\n* Atividades não listadas no documento podem ser avaliadas e aprovadas pelo colegiado do curso.\n* O documento fornece instruções detalhadas sobre como preencher o Formulário de Solicitação de Integralização de Atividades (Anexo 2).\n\n**Em geral, esta resolução fornece uma estrutura abrangente para os alunos se envolverem em diversas experiências de aprendizagem além do currículo tradicional, aprimorando seu desenvolvimento pessoal e profissional.**"]
  },
  {
    "role": "user",
    "parts": ["Qual a carga horária de atividades necessária para os alunos do curso de Sistemas de Informação?"]
  },
  {
    "role": "model",
    "parts": ["De acordo com o documento, os alunos do curso de Sistemas de Informação precisam completar um total de **180 horas** em atividades curriculares complementares."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
