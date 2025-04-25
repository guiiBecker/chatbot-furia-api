# 🎮 Oráculo da FURIA

Bot para Discord e Telegram que permite aos fãs da FURIA acompanharem todos os jogos da equipe em diferentes modalidades de e-sports.

## 🚀 Funcionalidades

- Ver próximos jogos da FURIA
- Acompanhar jogos ao vivo
- Ver resultados dos últimos jogos
- Suporte para múltiplos jogos (CS2, Valorant, Apex Legends, etc.)
- Integração com streams oficiais

## 📋 Pré-requisitos

- Python 3.8+
- Tokens de acesso para:
  - API do PandaScore
  - Bot do Discord
  - Bot do Telegram

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chatbot-furia.git
cd chatbot-furia
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```
Edite o arquivo `.env` com seus tokens e IDs dos times.

## 🎮 Uso

Para iniciar os bots:
```bash
python src/main.py
```

### Comandos disponíveis

#### Discord
- `/proximos_jogos [dias]` - Mostra os próximos jogos (padrão: 7 dias)
- `/ao_vivo` - Mostra jogos acontecendo agora
- `/ultimos_jogos [quantidade]` - Mostra os últimos jogos (padrão: 5 jogos)

#### Telegram
- `/start` - Inicia o bot e mostra mensagem de boas-vindas
- `/help` - Mostra ajuda com todos os comandos
- `/proximos_jogos [dias]` - Mostra os próximos jogos
- `/ao_vivo` - Mostra jogos acontecendo agora
- `/ultimos_jogos [quantidade]` - Mostra os últimos jogos

## 🤝 Contribuindo

Sinta-se à vontade para contribuir! Abra uma issue ou envie um pull request.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
