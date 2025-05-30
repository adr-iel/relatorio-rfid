
Processador de Relatórios RFID

Este script em Python foi desenvolvido devido a uma demanda interna e específica para Transmimo Ltda, uma empresa de transporte fretado, para atender o pedido de um de seus clientes que requisitava um relatório contendo as seguintes informações. Ele tem como objetivo processar um arquivo CSV contendo dados de entrada e saída de funcionários por meio de registros RFID. Ele organiza essas informações por funcionário e por dia do mês, calculando o tempo de permanência de cada um e gerando uma planilha de resultados no formato `.xlsx`.

Funcionalidades
- Carrega um arquivo CSV com registros de presença por RFID.
- Organiza os dados por funcionário e nome.
- Separa data e hora de cada registro.
- Calcula o tempo de permanência por dia.
- Filtra permanências superiores a 2 horas (para evitar duplicidade ou leituras inválidas).
- Gera uma planilha Excel com o total de horas/dia por funcionário no formato `hh:mm`.

Estrutura Esperada do CSV
O arquivo CSV deve conter pelo menos as seguintes colunas:
- `Código RFID` – Identificador único do crachá do funcionário.
- `Nome` – Nome do funcionário.
- `Data Hora` – Data e hora do registro (formato: `dd/mm/yyyy HH:MM:SS`).

Exemplo de dados:
```
Código RFID,Nome,Data Hora
12345678,João Silva,01/05/2024 07:45:00
12345678,João Silva,01/05/2024 09:30:00
...
```

Como Executar
1. Instale as dependências (caso ainda não tenha):
   ```bash
   pip install pandas openpyxl
   ```

2. Altere o caminho do arquivo CSV no início do script, se necessário:
   ```python
   df_original = pd.read_csv('C:/Users/seu_usuário/caminho/arquivo.csv')
   ```

3. Execute o script:
   ```bash
   python nome_do_script.py
   ```

4. O arquivo de resultado será gerado com o nome `Resultado.xlsx` no mesmo diretório do script (ou conforme o caminho configurado).

Resultado
O arquivo Excel de saída terá a seguinte estrutura:

| Código RFID | Nome        | Dia_1 | Dia_2 | ... | Dia_31 |
|-------------|-------------|-------|-------|-----|--------|
| 12345678    | João Silva  | 01:45 | 00:00 | ... | 00:00  |

- Cada coluna `Dia_X` representa o total de horas de permanência naquele dia.
- Os valores são formatados no padrão `hh:mm`.

Observações
- Registros com permanência superior a 2 horas são descartados.
- Certifique-se de que os dados estão no formato esperado para evitar erros de leitura ou conversão.
