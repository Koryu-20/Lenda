import streamlit as st

# Definindo o título do aplicativo
st.set_page_config(page_title="A Lenda de Metharion", page_icon="🌟")

# Incluindo o código HTML completo no Streamlit
st.markdown("""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> A Lenda de Metharion </title>
    <style>
        /* Reset de margens e padding */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Cor de fundo e fonte */
        body {
            font-family: 'Arial', sans-serif;
            background: url('https://i.gifer.com/MDg5.gif') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
            padding: 20px;
        }

        /* Cabeçalho */
        h1 {
            font-size: 3rem;
            font-weight: bold;
            margin-top: 30px;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        }

        /* Formulário de Cadastro */
        .form-container {
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            padding: 30px;
            max-width: 500px;
            margin: 40px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .form-container h2 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: #ffbf47;
        }

        input[type="text"] {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #ffbf47;
            border-radius: 5px;
            font-size: 1rem;
            background-color: rgba(0, 0, 0, 0.3);
            color: white;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: #ff9f00;
        }

        button {
            width: 100%;
            padding: 15px;
            background-color: #ffbf47;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #ff9f00;
        }

        /* Estilo para links de redes sociais */
        .social-links {
            margin-top: 30px;
        }

        .social-links a {
            color: #ffbf47;
            margin: 10px;
            font-size: 1.4rem;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: #ff9f00;
        }

        /* Novidades */
        .novidades {
            margin-top: 30px;
            font-size: 1.2rem;
            color: #ffbf47;
        }

        /* Mensagem de status */
        #mensagemStatus {
            font-size: 1.2rem;
            margin-top: 20px;
        }

        /* Responsividade */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }

            .form-container {
                padding: 20px;
                margin: 20px auto;
            }

            .social-links a {
                font-size: 1.2rem;
            }

            .novidades {
                font-size: 1.1rem;
            }
        }
    </style>
</head>
<body>
    <h1>🌟 A Lenda de Metharion 🌟</h1>

    <!-- Formulário de Cadastro -->
    <div class="form-container">
        <h2>Cadastre-se para receber novidades!</h2>
        <form id="formCadastro">
            <input type="text" id="nome" placeholder="Nome Completo" required>
            <input type="text" id="email" placeholder="E-mail" required>
            <input type="text" id="telefone" placeholder="Telefone" required>
            <button type="submit">Cadastrar</button>
        </form>
        <p id="mensagemStatus"></p>
    </div>

    <!-- Seção de redes sociais -->
    <div class="social-links">
        <h3>Siga-nos nas redes sociais:</h3>
        <a href="https://instagram.com" target="_blank">Instagram</a>
        <a href="https://facebook.com" target="_blank">Facebook</a>
        <a href="https://youtube.com" target="_blank">YouTube</a>
    </div>

    <!-- Seção de novidades -->
    <div class="novidades">
        <h3>Novidades:</h3>
        <p>Em breve, mais atualizações sobre a Lenda de Metharion. Fique ligado!</p>
    </div>

    <!-- Scripts -->
    <script>
        // Função para enviar e-mail (aqui está apenas como exemplo, o envio real deve ser feito via backend)
        function enviarEmail(nome, email, telefone) {
            // Simula o envio de e-mail
            alert(`📢 Novo cadastro de ${nome} com e-mail ${email} e telefone ${telefone}!`);
        }

        // Função para salvar dados (simula o comportamento do backend)
        function salvarDados(nome, email, telefone) {
            // Aqui, você pode salvar os dados em um banco de dados real
            console.log(`Cadastro de ${nome}, ${email}, ${telefone}`);
            return `Cadastro de ${nome} registrado com sucesso!`;
        }

        // Função chamada quando o formulário é enviado
        document.getElementById("formCadastro").addEventListener("submit", function(event) {
            event.preventDefault();

            const nome = document.getElementById("nome").value;
            const email = document.getElementById("email").value;
            const telefone = document.getElementById("telefone").value;

            if (nome && email && telefone) {
                // Salvar os dados (aqui é só simulação)
                const resultado = salvarDados(nome, email, telefone);

                // Enviar o e-mail (simulado)
                enviarEmail(nome, email, telefone);

                // Exibir a mensagem de sucesso
                document.getElementById("mensagemStatus").innerHTML = `✅ ${resultado} Você será notificado por e-mail sobre o novo cadastro.`;
                document.getElementById("mensagemStatus").style.color = "green";
            } else {
                document.getElementById("mensagemStatus").innerHTML = "❌ Por favor, preencha todos os campos!";
                document.getElementById("mensagemStatus").style.color = "red";
            }
        });
    </script>
</body>
</html>
""", unsafe_allow_html=True)
