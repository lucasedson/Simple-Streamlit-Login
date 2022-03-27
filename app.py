import streamlit as st
import streamlit_authenticator as stauth

with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



names = ['Lucas Edson']
usernames = ['lucas','rbriggs']
passwords = ['123']

def login():
    hashed_passwords = stauth.Hasher(passwords).generate()

    authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
        'some_cookie_name','some_signature_key',cookie_expiry_days=30)


    name, authentication_status, username = authenticator.login('Login','main')


    if authentication_status:
        st.write('Welcome *%s*' % (name))
        form()
        authenticator.logout('Logout', 'main')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

 

def form(): 
    col1, col2 = st.columns(2)
    with col1:   
        st.title('Vendas')
        nome_produto = st.text_input('Nome do produto:')
        preco_produto = st.number_input('Preço do produto:')
        quantidade_produto = st.number_input('Quantidade do produto:')
        st.write('Total: R$', preco_produto * quantidade_produto)
    with col2:
        st.title('Tabela de produtos')
        st.table(
            [
                ['Nome', 'Preço', 'Quantidade'],
                ['Celular', 'R$ 1.000,00', '1'],
                ['Notebook', 'R$ 2.000,00', '2'],
                ['Tablet', 'R$ 3.000,00', '3'],
                ['Mouse', 'R$ 1.000,00', '1'] ])


login()
#footer()        
st.markdown('<div class=footer><h5>&copy; SamaDev<h5></div>', unsafe_allow_html=True)