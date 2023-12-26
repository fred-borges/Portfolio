import streamlit as st

# Title
st.title("Meu Portfólio")

# Sidebar
st.sidebar.title('Menu')
menu_options = ['Sobre Mim', 'Projetos', 'Habilidades', 'Contato']
choice = st.sidebar.selectbox('Navegar', menu_options)

if choice == 'Sobre Mim':
    st.header('Sobre Mim')
    st.write("Meu nome é Ulisses, uma pessoa dedicada e apaixonada por aprendizado. Estou imerso no mundo da programação, especialmente focado no Python. Além disso, tenho experiência em criar interfaces gráficas envolventes e estou constantemente aprimorando minhas habilidades nesse aspecto. Busco sempre expandir meus conhecimentos, especialmente em projetos que envolvem banco de dados e desenvolvimento web.")
    st.write("Atualmente, estou concentrado em aprimorar minhas habilidades em Python, explorando diferentes bibliotecas e frameworks para criar soluções mais eficientes e impactantes.")
   # Adicione mais detalhes sobre sua jornada, projetos anteriores ou qualquer outra informação relevante.
   
elif choice == 'Projetos':
    st.header('Projetos')

    # Projeto 1
    st.subheader('Video downloader')
    st.write('Esse é um código em Python utilizando a biblioteca pytube para baixar vídeos do YouTube com uma interface gráfica básica usando o tkinter. Ele permite inserir a URL de um vídeo do YouTube e baixá-lo para o sistema local.')
    st.write('[Link para o Projeto](https://github.com/fred-borges/Video_Donloader/blob/caad4cea6b21624bdb6e5b4a30ea58b7115ef701/main.py)')

    # Projeto 2
    st.subheader('Visualização do perfil github')
    st.write('Um aplicativo Python utilizando Streamlit para buscar e exibir informações básicas de usuários do GitHub. Insira o nome de usuário para visualizar avatar, bio e um link direto para o perfil.')
    st.write('[Link para o Projeto](https://visualizador-de-perfil-do-app-uikrzndrtbb3xdu9ppig8g.streamlit.app)')

    # Projeto 3
    st.subheader('Interface gráfica para cadastro de usários')
    st.write('Este projeto consiste em um simples sistema de cadastro de usuários com uma interface gráfica desenvolvida em Python usando a biblioteca tkinter. O programa permite inserir informações básicas (nome, apelido e senha) e armazená-las em um banco de dados PostgreSQL.')
    st.write('[Link para o Projeto ](https://github.com/fred-borges/Cadastro_de_usuario/blob/1d2b2597b45a9e186b5be402df6b8637521cc65d/test.py)')


elif choice == 'Habilidades':
    st.header('Habilidades')

    st.subheader('Python e Desenvolvimento de Aplicações')
    st.write('Experiência sólida em Python para desenvolvimento de aplicativos e scripts. Habilidades na utilização de algumas bibliotecas.')

    st.subheader('Integração com APIs')
    st.write('Capacidade de integração com APIs externas, exemplificado no projeto de visualização do perfil do GitHub.')

    st.subheader('Banco de Dados e Armazenamento')
    st.write('Experiência em armazenamento de dados, incluindo a integração com bancos de dados PostgreSQL, como demonstrado no projeto de cadastro de usuários.')

    st.subheader('Desenvolvimento Web')
    st.write('Habilidades em desenvolvimento web, incluindo a criação de interfaces gráficas interativas para aplicativos e sistemas.')

elif choice == 'Contato':
    st.header('Contato')
    # Adicione formulário de contato ou informações de contato.

    contato = st.selectbox(
        'Como gostaria de ser contatado?',
        ('E-mail', 'Telefone', 'LinkedIn')
    )

    if contato == 'E-mail':
        st.write('ulissesborgess18@gmail.com')
    elif contato == 'Telefone':
        st.write('+351 969 330 246')
    elif contato == 'LinkedIn':
        st.write('https://www.linkedin.com/in/ulisses-borges-4a79b12a6')

# Footer
st.sidebar.markdown('---')
st.sidebar.text('Feito usando Streamlit')
