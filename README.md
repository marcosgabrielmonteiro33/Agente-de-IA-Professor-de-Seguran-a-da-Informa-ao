# Agente-de-IA-Professor-de-Seguran-a-da-Informa-ao
esse projeto foi feito com base no bootcamp de cybersecurity Santander + DIO

REPOSITORIO DO AGENTE ORIGINAL 

https://github.com/digitalinnovationone/dio-agent

1. A Especializacao do Agente e o Porquê

O agente foi especializado na area de Analise de Vulnerabilidades e Seguranca Defensiva (`vulnerability-analysis`).

Por que essa especializacao?
Foco no Raciocinio:


Profissionais iniciantes costumam pular direto para comandos de exploracao.
A especializacao treina o agente para agir como um mentor senior, investigando o contexto, explicando o impacto e ensinando o pensamento analitico.

Abordagem Defensiva:

Garante alinhamento etico e educacional, focando em mitigacao, modelagem de risco, principios de seguranca (Confidencialidade, Integridade e Disponibilidade) e blindagem de ambientes controlados de laboratorio.


2. Arquivos Criados ou Alterados

Para estruturar e persistir essa especializacao atraves de arquivos de configuracao e contexto, foram implementados:

1. skills/vulnerability-analysis/SKILL.md (Criado)
Define escopo, gatilhos de ativacao, processo passo a passo (Entender o cenario -> Explicar o conceito -> Analisar o risco -> Investigacao profissional -> Recomendacoes defensivas -> Verificacao de aprendizado) e diretrizes eticas.
2. knowledge/security-basics.md  (Criado)
Base de conhecimento fundamental abordando definicoes essenciais (Vulnerabilidade, Ameaça, Risco), a Triade CIA e boas praticas de blindagem.
3. persona.md (Alterado)
Incorporou a diretriz para assumir o papel de mentor em seguranca, priorizando o questionamento previo e a orientacao defensiva.
4. AGENTS.md (Alterado)
 Registrou a nova habilidade (`vulnerability-analysis`) na tabela de capacidades do agente.

3. Como Rodar o Agente no Harness e Melhorias

Como executar:
1. Certifique-se de estar no diretório raiz do projeto onde o harness e as configurações estão localizados.
2. Inicialize o ambiente de testes do laboratorio:
   python app.py

