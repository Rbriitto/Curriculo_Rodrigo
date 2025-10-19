from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit_scrollable_textbox as stx


#Configurações estruturais 
diretorio  = Path(__file__).parent if "__file__" in locals() else Path.cwd()
placeholder = st.empty()
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "curriculo.pdf"
#arquivo_img = diretorio / "assets" / "foto.png"

# Configurações Geral das Informações

TITULO = "Curriculum | Rodrigo de Britto Aquino"
NOME = "Rodrigo de Britto Aquino"
RESUMO_PROFISSIONAL = """

"""
EMAIL = "rodrigobritto.web@gmail.com"
MIDIA_SOCIAL = {
    "LinkedIn":"https://www.linkedin.com/in/rodrigo-britto-506a00b9/",
    "GitHub":"github.com/Rbriitto",
    "Instagram":"https://www.instagram.com/rodrigobriitto"
}

CURSOS_COMPLEMENTARES= {
    "🎯 BootCamp Claro - Java com Spring Boot ":"https://www.dio.me/certificate/RPB9UDGB/share",
    "🎯 Excel do Básico ao Avançado – Formação Especialista  ":"https://www.udemy.com/course/curso-de-excel-avancado-2016-para-se-tornar-especialista/",
    "🎯 Power BI Completo - Do Básico ao Avançado ":"https://www.udemy.com/course/power-bi-completo-do-basico-ao-avancado/",
    "🎯 Formação Python Fundamentals":"https://web.dio.me/track/a5a120c9-12f7-41bf-a767-94e2febb0b7e",
    "🎯 Dashboards com Python - Streamlit e Dash":"https://www.udemy.com/course/desenvolvendo-dashboards-em-python/"
    
    
}

st.set_page_config(
    page_title=TITULO
)

#Carregando Assets

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html = True)

with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
    
#image = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap = "small")

st.markdown(
    """
    <div style='display: flex; align-items: center; gap: 20px;'>
       <h1 style='margin:0; white-space: nowrap;'>Rodrigo de Britto Aquino</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.write(RESUMO_PROFISSIONAL)
st.markdown(
       """
    <div color: white; font-size:16px; font-weight: 500;">
        <a href="mailto:rodrigobritto.web@gmail.com" style="color: #9ad0ec; text-decoration: none;">
            rodrigobritto.web@gmail.com
        </a> 
        | (21) 97638-5715 | 30 Anos | Casado
    </div>
    """,
    unsafe_allow_html=True
)
st.write("---")
#Midias Sociais:
colunas = st.columns(len(MIDIA_SOCIAL))
for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[indice].write(f"[{plataforma}]({link})")
    
#Experiencias 

st.write("---")
st.subheader("🔎 Resumo Profissional")
st.write(
    """
         - 💹 Profissional com trajetória sólida em telecomunicações, com atuação consistente em faturamento, 
                contas a receber e gestão de contratos. Experiência em qualidade, monitoramento de redes e suporte técnico, 
                aliada ao desenvolvimento de dashboards e análise de indicadores.
                Apoio estratégico à diretoria, transformando dados em informações relevantes para decisões de negócio.

    """
)
st.write("---")
st.subheader("📚 Formação Acadêmica")
st.markdown("""
**🎓 Bacharel em Sistemas de Informação**  
Universidade Estácio de Sá - Conclusão: 12/2019


**👷🏻‍♂️ Técnico em Informática para Internet**  
Universidade Estácio de Sá - Conclusão: 12/2015

""")
st.write("---")
#Skills 
st.subheader("🕵🏻 Skills")
st.write("""🏆 - Ferramentas de Dados: """)
st.code("Power Bi, SQL, Python, Streamlit, Dash, Google Analitycs, Tableu")

st.write("""🏅 Gestão e Projetos: """)
st.code("Scrum, MS Project, Kanban")

st.write("""🥈 Versionamento e Dev: """)
st.code("Git, GitHub, Java")

st.write("""🥉 Outros: """)
st.code("Excel, IA, Html, Css, Firebase, AutoCad, Netcool IBM, Sydle, Smart Service.")
st.write("---")
    
#      - Gestão e Projetos: .
    
#      - Versionamento e Dev: Git, GitHub, Java
    
#      - Outros: Excel, IA, Html, AutoCad, Visual Basic, Firebase, Netcool IBM, Sydle, Smart Service.
    
#     ⭐ - + 
      
#     """
# )
#Historico Profissional
st.write("#")
st.subheader("👨‍🦳 Experiência Profissional")

  
with st.container():    
   st.markdown("""
<style>
.scroll-container {
    height: 600px; /* altura visível */
    overflow-y: auto; /* adiciona rolagem vertical */
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 10px;
    background-color: #003644;
    color: white;
}
.scroll-container::-webkit-scrollbar {
    width: 8px;
}
.scroll-container::-webkit-scrollbar-thumb {
    background-color: #aaa;
    border-radius: 4px;
}
</style>
""", unsafe_allow_html=True)

# --- Conteúdo completo dentro da mesma div ---
st.markdown("""
<div class="scroll-container">

**👩🏻‍💻 Analista de Redes | Hypermatrix do Brasil**  
02/2025 - 07/2025 
 
• Monitoramento e gestão de eventos na infraestrutura de rede utilizando HyperManage, assegurando alta disponibilidade e desempenho contínuo.  
    
• Realização de análises preditivas para antecipar falhas e degradações antes de impactarem a operação.  

• Emissão de notificações técnicas e acompanhamento completo do ciclo de vida dos eventos, garantindo ações corretivas eficazes.

• Registro padronizado e detalhado de eventos para histórico, rastreabilidade e auditoria.

• Suporte direto às equipes de campo e consolidação de dados operacionais para tomada de decisã
    
• Elaboração de dashboards em BI e acompanhamento de métricas de desempenho para direcionar melhorias.  

• Apoio na execução de cronogramas de projetos, alinhando operação e estratégia.  

---

**Martinstec Manutenção e Reparos - 09/2017 - 01/2025**

**💼 Supervisor |**
    Período na Função: 07/2021 - 01/2025  
• Apoio direto à coordenação e gerência no gerenciamento de contratos de obras no setor de telecomunicações.

• Responsável pela análise e aprovação de faturamento de pedidos, garantindo conformidade com orçamentos e critérios técnicos.

• Gestão e controle de POs (Purchase Orders), assegurando alinhamento com contratos e entregas previstas. Controle de orçamentos enviados e faturamento emitido para diferentes clientes, com atuação em diversos Estados do Brasil.

• Gestão de contratos de obras em andamento, finalizadas e em negociação, assegurando visibilidade e organização dos processos.

• Desenvolvimento de painel em Business Intelligence (BI) para consolidação de dados operacionais e financeiros.

• Apresentação periódica do BI à diretoria e gerência, contribuindo para decisões estratégicas e otimização de resultados.

• Suporte à coordenação no Projeto de Aquisição (IHS), elaborando documentação, realizando levantamento de candidatos e solicitando faturamento.
  

---

**💼 Supervisor de Qualidade | Martinstec Manutenção e Reparos**  
    Período na Função: 06/2020 - 07/2021  

• Atuação como ponto focal de qualidade em projeto terceirizado da Ericsson, assegurando conformidade das obras com os padrões exigidos pelo cliente.

• Prestação de suporte técnico às equipes de campo em temas relacionados à qualidade e execução dos serviços.

• Condução de treinamentos técnicos para equipes operacionais e líderes de campo. Realização de auditorias presenciais e remotas com foco em instalações elétricas e sistemas de rádio.

• Revisão e auditoria interna de relatórios de finalização das obras antes do envio ao cliente.

• Gestão da documentação técnica para faturamento, controlando materiais aptos para cobrança.  

---

**💼 Auxiliar Técnico | Martinstec Manutenção e Reparos**  
    Período na Função:07/2017 - 06/2020  
    
• Atuação na finalização de documentações técnicas e relatórios para encerramento de obras terceirizadas.

• Utilização de AutoCAD, Excel e editores de PDF para elaboração, revisão e padronização de documentos.

• Apoio à coordenação e supervisão na gestão operacional, fortalecendo o alinhamento entre campo e escritório.

• Acompanhamento do progresso das obras em campo, assegurando execução conforme cronograma e padrões de qualidade.

• Verificação do cumprimento de metas e prazos, contribuindo para entregas eficientes e dentro dos parâmetros contratados.

</div>
""", unsafe_allow_html=True)
    


#Cursos 
st.write("---")
st.subheader("💻 Cursos Complementares")
for curso, link in CURSOS_COMPLEMENTARES.items():
    st.write(f"[{curso}]({link})")
st.write("---")
    

    
st.download_button(
    label = "Download Curriculo",
    data = pdfLeitura,
    file_name=arquivo_pdf.name,
    mime = "application/octet-stream"
   )


remove_st_estilo = """
    <style>
        #MainMenu {visibility:hidden;}
        #footer {visibility:hidden;}
        #header {visibility:hidden;}        
    </style>

"""
st.markdown(remove_st_estilo, unsafe_allow_html=True)