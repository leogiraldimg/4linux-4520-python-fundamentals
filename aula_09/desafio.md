# Desafio

Coletar os dados de 6 meses do historical data da B3:

- https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/historical-quote-data/
- Observar o layout do arquivo no seguinte link: https://www.b3.com.br/data/files/65/50/AD/26/29C8B51095EE46B5790D8AA8/HistoricalQuotations_B3.pdf

Os dados deverao ser armazenados no mongo atlas: https://atlas.mongodb.com

Cada documento do banco terao os seguintes campos:

- Data do pregao (DATA EXCHANGE)
- Codigo do papel (CODNEG)
- Nome reduzido (NOMERES)
- Preço de abertura (PREABE)
- Preço Maximo (PREMAX)
- Preço minimo (PREMIN)
- Preço Medio (PREMED)
- Ultimo preço (PREULT)

Desejaveis:
- Testes
- Modularizado -> OOP/FN
- Boas praticas -> PEP8
