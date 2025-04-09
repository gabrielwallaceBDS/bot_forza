# Bot de Automação de Leilões para Forza Horizon 5

Este projeto é um bot desenvolvido em Python para automatizar o processo de participação em leilões no jogo Forza Horizon 5. Utilizando a biblioteca PyAutoGUI, o bot interage com a interface do jogo, realizando buscas e efetuando compras de forma automatizada.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição do Projeto

O bot foi criado para facilitar a participação em leilões dentro do Forza Horizon 5, automatizando tarefas repetitivas e permitindo que o usuário economize tempo ao buscar e adquirir veículos no jogo.

## Funcionalidades

- **Ativação da Janela do Jogo**: O bot identifica e ativa a janela do Forza Horizon 5 para iniciar as interações.
- **Busca Automatizada**: Realiza buscas contínuas por leilões disponíveis.
- **Detecção de Leilões**: Verifica se há leilões disponíveis ou se a mensagem "Nenhum leilão para exibir" é apresentada.
- **Compra Automática**: Ao encontrar um leilão, o bot navega pelos menus e confirma a compra do veículo.
- **Logs em Tempo Real**: Exibe logs das ações realizadas para acompanhamento do usuário.
- **Interface Gráfica**: Fornece uma interface simples para iniciar e parar o bot, além de visualizar os logs.

## Requisitos

Antes de executar o bot, certifique-se de que os seguintes requisitos estão instalados:

- Python 3.x
- Bibliotecas Python:
  - `pyautogui`
  - `pygetwindow`
  - `pynput`
  - `tkinter` (geralmente incluído na instalação padrão do Python)

Além disso, o jogo Forza Horizon 5 deve estar instalado e devidamente configurado no seu computador.

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/bot-leilao-fh5.git
