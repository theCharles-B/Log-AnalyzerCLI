# Log Inspector

Ferramenta simples em Python para analisar logs do Linux e identificar padrões de erro.

## Objetivo
Ajudar na identificação rápida de falhas recorrentes em arquivos de log.

## Funcionalidades (v0.1)
- Leitura de arquivos de log
- Contagem de ocorrências de error, warn e fail
- Relatório em CLI

## Uso
Execute o analisador passando o caminho do arquivo de log:

bash
python log_inspector/analyzer.py /caminho/para/arquivo.log

## Próximos passos
- Suporte a journalctl
- Exportação para JSON
- Classificação com IA
- Alertas automáticos
