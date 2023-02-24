# Weather2Telegram

Script para envio da previsão do tempo automaticamente usando GitHub Actions.

## Cidade

Encontre o código de sua cidade usando o link

```
http://servicos.cptec.inpe.br/XML/listaCidades?city=<cidade>
```

Para mais informações, visite [http://servicos.cptec.inpe.br/XML/#req-busca-localidade](http://servicos.cptec.inpe.br/XML/#req-busca-localidade)

## Ajustes

Nas configurações do repositório, vá em `Secrets and variables`, `Actions` e crie um segredo com o nome `BOT_TOKEN` tendo o token do bot como conteúdo.

Ainda em `Secrets and Variables`, clique em `Variables` e crie também as variáveis `DEST` e `CITY` com o destino da mensagem e o código da cidade respectivamente.

## Execução

A ação é executada automaticamente as 8:30 UTC +0, ou seja, 05:30 UTC -3.

Para iniciar a ação a qualquer momento, vá em `Actions`, `Cron Action`, `Run workflow` e clique em `Run workflow`.
