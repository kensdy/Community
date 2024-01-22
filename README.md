# Community - Modelo de Fórum em Flask

![Visitas ao Repositório](https://img.shields.io/github/visits/kensdy/Community?style=flat-square&label=Visitas&color=blue)

O Community é um modelo de fórum desenvolvido em Flask, oferecendo uma estrutura simples e aberta para implementação de sistemas de discussão online. Este projeto é open source e pode ser facilmente personalizado para atender às necessidades específicas de diferentes comunidades online.

## Funcionalidades

- **Postagens e Comentários:** Os usuários podem criar postagens e interagir por meio de comentários, proporcionando uma experiência de discussão dinâmica.

- **Sem Sistema de Login:** O Community, por padrão, não possui um sistema de login. Isso simplifica o acesso, mas também significa que a identidade do usuário não é verificada.

- **Sem Banco de Dados:** Este modelo não utiliza um banco de dados para armazenar postagens ou comentários. Tenha em mente que, ao reiniciar o servidor, todas as postagens serão perdidas.

## Como Usar

1. **Pré-requisitos:**
   - Certifique-se de ter o Python instalado em sua máquina.

2. **Clonando o Repositório:**
   - Execute o seguinte comando para clonar o repositório:
     ```bash
     git clone https://github.com/kensdy/Community
     ```
3. **Executando o Aplicativo:**
   - Navegue para o diretório recém-clonado com `cd Community`.
   - Instale as dependências usando `pip install -r requirements.txt`.
   - Execute `python app.py` para iniciar o servidor local.
   - Acesse `http://localhost:5000` em seu navegador para interagir com o fórum.

4. **Personalização:**
   - Adapte o código-fonte para atender às suas necessidades específicas.
   - Considere implementar um sistema de login ou integração com um banco de dados, se necessário.

## Tutorial em Vídeo

Confira este vídeo tutorial que demonstra a instalação e apresenta uma visão geral do Community. O vídeo inclui:

- Instruções passo a passo para instalar o Community.
- Uma breve demonstração das funcionalidades principais.

[![Tutorial em Vídeo](https://img.youtube.com/vi/j09MK7o5NCU/0.jpg)](https://www.youtube.com/watch?v=j09MK7o5NCU)


## Contribuições

Contribuições são bem-vindas! Se você deseja melhorar o Community, sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE) - veja o arquivo LICENSE para mais detalhes.

## Agradecimentos

Agradecemos por utilizar o Community. Esperamos que seja útil como ponto de partida para suas implementações de fóruns online.
