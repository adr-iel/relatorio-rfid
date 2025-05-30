import pandas as pd

try:

    # Carregar o DataFrame do arquivo CSV
    df_original = pd.read_csv('caminho_arquivo_csv')

    # Organizar os dados na planilha Resultado
    df_resultado = df_original[['Código RFID', 'Nome']].drop_duplicates().sort_values(by='Nome')

    # Separar a coluna de Data e Hora
    df_original['Data'] = pd.to_datetime(df_original['Data Hora'], format='%d/%m/%Y %H:%M:%S')

    # Calcular a permanência dos funcionários
    df_original['Permanência'] = df_original.groupby(['Código RFID', df_original['Data'].dt.date])['Data'].diff()

    # Filtrar a permanência máxima
    df_original = df_original[df_original['Permanência'] <= pd.Timedelta(hours=2)]

    # Preencher a planilha "Resultado" com as colunas de cada dia
    dias_do_mes = range(1, 32)  
    for dia in dias_do_mes:
        df_dia = df_original[df_original['Data'].dt.day == dia]
        df_dia['Permanência'] = df_dia['Permanência'].dt.total_seconds() / 3600  # Converter para horas
        df_resultado[f'Dia_{dia}'] = df_resultado['Código RFID'].map(
            df_dia.groupby('Código RFID')['Permanência'].sum().fillna(0)
        )

    # Formatar as colunas dos dias como "hh:mm"
    for dia in dias_do_mes:
        df_resultado[f'Dia_{dia}'] = df_resultado[f'Dia_{dia}'].apply(lambda x: f"{int(x):02d}:{int((x % 1) * 60):02d}" if not pd.isna(x) else '0:00')

    # Salvar o DataFrame em um arquivo Excel
    df_resultado.to_excel('Resultado.xlsx', index=False)

    print("Finalizado")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

